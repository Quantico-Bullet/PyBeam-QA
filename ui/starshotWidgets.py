from PySide6.QtWidgets import (QWidget, QLabel, QProgressBar, QVBoxLayout, QFileDialog,
                               QListWidgetItem, QMenu, QSizePolicy, QMessageBox, 
                               QMainWindow, QFormLayout, QComboBox,
                               QDialog, QDialogButtonBox, QLineEdit, QSpacerItem,
                               QPushButton, QCheckBox, QHBoxLayout)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QEvent, QThread

from ui.qaToolsWindow import QAToolsWindow
from ui.py_ui import icons_rc
from ui.py_ui.starshotWorksheet_ui import Ui_QStarshotWorksheet
from core.analysis.starshot import QStarshotWorker

from scipy import ndimage
from core.tools.report import StarshotReport
from core.tools.devices import DeviceManager

import traceback
import platform
import webbrowser
import subprocess
import pyqtgraph as pg
from pathlib import Path

from pylinac.core.image import load
from pylinac.core.image_generator import (GaussianFilterLayer,
                                          FilteredFieldLayer,
                                          AS500Image,
                                          AS1000Image,
                                          AS1200Image)

from ui.starshot_test_dialog import StarshotTestDialog

class StarshotMainWindow(QAToolsWindow):
    
    def __init__(self, initData: dict = None):
        super().__init__(initData)

        self.window_title = "Starshot Analysis ‒ PyBeam QA"
        self.setWindowTitle(self.window_title)

        self.add_new_worksheet()

        self.ui.menuFile.addAction("Add Images(s)", self.ui.tabWidget.currentWidget().add_files)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction("Add New Worksheet", self.add_new_worksheet)
        self.ui.menuTools.addAction("Benchmark Test", self.init_test_dialog, "Ctrl+T")

    def init_test_dialog(self):
        dialog = StarshotTestDialog()
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            sim_image = dialog.ui.sim_image_cb.currentText()
            
            if sim_image == "AS500":
                sim_image = AS500Image()
            
            elif sim_image == "AS1000":
                sim_image = AS1000Image()
            
            else: sim_image = AS1200Image()

            num_spokes = dialog.ui.num_spokes_sb.value()
            cax_offset = dialog.ui.cax_offset_dsb.value()

            for _ in range(num_spokes):
                sim_image.add_layer(FilteredFieldLayer((200, 5),
                                    alpha=0.5,
                                    cax_offset_mm = (cax_offset, cax_offset)))
                
                sim_image.image = ndimage.rotate(sim_image.image,
                                                 360 / num_spokes,
                                                 reshape = False,
                                                 mode = 'nearest')
                
            sim_image.add_layer(GaussianFilterLayer(sigma_mm = 3))
            sim_image.generate_dicom(dialog.ui.out_file_le.text())

            self.add_new_worksheet(dialog.ui.test_name_le.text() + " (Test)")
            self.ui.tabWidget.currentWidget().add_files([dialog.ui.out_file_le.text()])

    def add_new_worksheet(self, worksheet_name: str = None, enable_icon: bool = True):
        if worksheet_name is None:
            self.untitled_counter = self.untitled_counter + 1
            worksheet_name = f"Starshot (Untitled-{self.untitled_counter})"

        return super().add_new_worksheet(QStarshotWorksheet(), worksheet_name, enable_icon)

class QStarshotWorksheet(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_QStarshotWorksheet()
        self.ui.setupUi(self)

        self.image_icon = QIcon()
        self.image_icon.addFile(u":/colorIcons/icons/picture.png", QSize(), QIcon.Normal, QIcon.Off)

        self.form_layout = QFormLayout()
        self.form_layout.setHorizontalSpacing(40)
        self.ui.analysisInfoVL.addLayout(self.form_layout)

        self.ui.analyzeBtn.setText("Analyze image(s)")
        self.ui.genReportBtn.setEnabled(False)

        #--------  add widgets --------
        self.progress_vl = QVBoxLayout()
        self.progress_vl.setSpacing(10)

        self.ui.analysisInfoVL.addLayout(self.progress_vl)

        # setup context menu for image list widget
        self.img_list_contextmenu = QMenu()
        self.img_list_contextmenu.addAction("View Original Image", self.view_dicom_image)
        self.view_analyzed_img_action = self.img_list_contextmenu.addAction("View Analyzed Image")
        self.view_analyzed_img_action.setEnabled(False)
        self.img_list_contextmenu.addAction("Show Containing Folder", self.open_file_folder)
        self.remove_file_action = self.img_list_contextmenu.addAction("Remove from List", self.remove_file)
        self.delete_file_action = self.img_list_contextmenu.addAction("Delete", self.delete_file)
        self.img_list_contextmenu.addAction("Properties")
        self.img_list_contextmenu.addSeparator()
        self.select_all_action = self.img_list_contextmenu.addAction("Select All", lambda: self.perform_selection("selectAll"))
        self.unselect_all_action = self.img_list_contextmenu.addAction("Unselect All", lambda: self.perform_selection("unselectAll"))
        self.invert_select_action = self.img_list_contextmenu.addAction("Invert Selection", lambda: self.perform_selection("invertSelection"))
        self.img_list_contextmenu.addSeparator()
        self.remove_selected_files_action = self.img_list_contextmenu.addAction("Remove Selected Files", self.remove_selected_files)
        self.remove_all_files_action = self.img_list_contextmenu.addAction("Remove All Files", self.remove_all_files)
        self.ui.imageListWidget.installEventFilter(self)

        self.analysis_progress_bar = QProgressBar()
        self.analysis_progress_bar.setRange(0,0)
        self.analysis_progress_bar.setTextVisible(False)
        self.analysis_progress_bar.setMaximumSize(300, 10)
        self.analysis_progress_bar.setMinimumSize(300, 10)
        self.analysis_progress_bar.hide()

        self.analysis_message_label = QLabel("Analysis in progress")
        self.analysis_message_label.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred))
        self.analysis_message_label.hide()

        self.progress_vl.addWidget(self.analysis_progress_bar, 0, Qt.AlignHCenter)
        self.progress_vl.addWidget(self.analysis_message_label, 0, Qt.AlignHCenter)

        #--------  connect slots -------- 
        self.ui.addImgBtn.clicked.connect(self.add_files)
        self.ui.analyzeBtn.clicked.connect(self.start_analysis)
        self.ui.genReportBtn.clicked.connect(self.generate_report)
        self.ui.imageListWidget.itemChanged.connect(self.update_marked_images)
        self.ui.toleranceDSB.valueChanged.connect(self.set_analysis_outcome)

        #-------- init defaults --------
        self.marked_images = []
        self.current_plot = None
        self.current_results = None
        self.imageView_windows = []
        self.advanced_results_view = None
        self.analysis_in_progress = False
        self.has_analysis = False

        self.setup_config()
        self.update_marked_images()
        self.set_analysis_outcome()

    def setup_config(self):
        self.ui.SIDInputCB.addItems(["Auto", "Manual"])
        self.ui.DPIInputCB.addItems(["Auto", "Manual"])
        self.ui.DPIInputCB.currentIndexChanged.connect(self.on_config_change)
        self.ui.SIDInputCB.currentIndexChanged.connect(self.on_config_change)

        # call this one time to ensure correct config display
        self.on_config_change()

    def on_config_change(self):
        if self.ui.SIDInputCB.currentText() == "Manual":
            self.ui.configFormLayout.setRowVisible(4, True)
        else:
            self.ui.configFormLayout.setRowVisible(4, False)

        if self.ui.DPIInputCB.currentText() == "Manual":
            self.ui.configFormLayout.setRowVisible(6, True)
        else:
            self.ui.configFormLayout.setRowVisible(6, False)
     
    def add_files(self, files: tuple | list | None = None):

        if not files:
            files, _ = QFileDialog.getOpenFileNames(
                self,
                "Select Starshot Images",
                "",
                "DICOM Images (*.dcm);; TIFF Images (*.tiff *.tif);; PNG Image (*.png)",
                )

        if files:
            for file in files:
                path = Path(file)

                itemData = {"file_path": str(path),
                            "analysis_data": None}
                
                listItemWidget = QListWidgetItem(self.ui.imageListWidget)
                listItemWidget.setText(path.name)
                listItemWidget.setIcon(self.image_icon)
                listItemWidget.setCheckState(Qt.Unchecked)
                listItemWidget.setData(Qt.UserRole, itemData)

    def remove_selected_files(self):
        index = 0
        while index < self.ui.imageListWidget.count():
            if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                listItemWidget = self.ui.imageListWidget.takeItem(index)
                del listItemWidget
            else:
                index += 1

        self.update_marked_images()

    def remove_all_files(self):
        item_count = self.ui.imageListWidget.count()
        for index in range(item_count):
            listItemWidget = self.ui.imageListWidget.takeItem(item_count-(index+1))
            del listItemWidget
        
        self.update_marked_images()

    def remove_file(self):
        listItemWidget = self.ui.imageListWidget.takeItem(self.ui.imageListWidget.currentRow())
        del listItemWidget

        self.update_marked_images()

    def open_file_folder(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()
        file_path = str(Path(listWidgetItem.data(Qt.UserRole)["file_path"]).parent.resolve())
        
        if platform.system() == "Windows":
            subprocess.Popen(["explorer", file_path])
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", file_path])
        else:
            subprocess.Popen(["xdg-open", file_path])

    def perform_selection(self, selection_type: str):

        if selection_type == "selectAll":
            for index in range(self.ui.imageListWidget.count()):
                self.ui.imageListWidget.item(index).setCheckState(Qt.CheckState.Checked)
        
        elif selection_type == "unselectAll":
            for index in range(self.ui.imageListWidget.count()):
                self.ui.imageListWidget.item(index).setCheckState(Qt.CheckState.Unchecked)
        
        elif selection_type == "invertSelection":
            for index in range(self.ui.imageListWidget.count()):
                if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                    self.ui.imageListWidget.item(index).setCheckState(Qt.CheckState.Unchecked)
                elif self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Unchecked:
                    self.ui.imageListWidget.item(index).setCheckState(Qt.CheckState.Checked)

        self.update_marked_images()

    def update_marked_images(self):
        self.marked_images.clear()

        for index in range(self.ui.imageListWidget.count()):
            if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                self.marked_images.append(self.ui.imageListWidget.item(index).data(Qt.UserRole)["file_path"])
        
        if len(self.marked_images) > 0:
            self.ui.analyzeBtn.setEnabled(True)

            if len(self.marked_images) > 1:
                self.analysis_message_label.setText(f"{len(self.marked_images)} images will be merged and analyzed")
                self.analysis_message_label.show()

            else:
                self.analysis_message_label.hide()

        else:
            self.ui.analyzeBtn.setEnabled(False)
            self.analysis_message_label.hide()

    def view_dicom_image(self):
        image_short_name = self.ui.imageListWidget.currentItem().text()
        image_path = self.ui.imageListWidget.selectedItems()[0].data(Qt.UserRole)["file_path"]
        image = load(image_path)

        imgView = pg.ImageView()
        imgView.setImage(image.array)
        imgView.setPredefinedGradient("grey")

        new_win = QMainWindow()
        new_win.setWindowTitle(image_short_name)
        new_win.setCentralWidget(imgView)
        new_win.setMinimumSize(600, 500)
        
        self.imageView_windows.append(new_win)
        new_win.show()
        new_win.setMinimumSize(0, 0)

    def delete_file(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()

        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle("Delete File")
        self.error_dialog.setText("<p><span style=\" font-weight:700; font-size: 11pt;\">" \
                                  f"Are you sure you want to permanently delete \'{listWidgetItem.text()}\' ? </span></p>")
        self.error_dialog.setInformativeText("This action is irreversible!")
        self.error_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | 
                                             QMessageBox.StandardButton.Cancel)
        self.error_dialog.setTextFormat(Qt.TextFormat.RichText)

        warning_icon = QPixmap(u":/colorIcons/icons/warning.png")
        warning_icon = warning_icon.scaled(QSize(48, 48), mode = Qt.TransformationMode.SmoothTransformation)
        self.error_dialog.setIconPixmap(warning_icon)

        ret = self.error_dialog.exec()

        if ret == QMessageBox.StandardButton.Yes:
            path = Path(listWidgetItem.data(Qt.UserRole)["file_path"])
            path.unlink(missing_ok=True)
            self.ui.imageListWidget.takeItem(self.ui.imageListWidget.currentRow())
            del listWidgetItem

    def eventFilter(self, source, event: QEvent):
        if (event.type() == QEvent.ContextMenu and source is self.ui.imageListWidget):
            pos = self.ui.imageListWidget.mapFromGlobal(event.globalPos())

            if type(self.ui.imageListWidget.itemAt(pos)) == QListWidgetItem:
                # Show context menu
                if not self.analysis_in_progress:
                    if self.ui.imageListWidget.itemAt(pos).data(Qt.UserRole)["analysis_data"]:
                        self.view_analyzed_img_action.setEnabled(True)
                    else:
                        self.view_analyzed_img_action.setEnabled(False)

                    if len(self.marked_images) > 0:
                        self.invert_select_action.setEnabled(True)
                        self.unselect_all_action.setEnabled(True)
                        self.remove_selected_files_action.setEnabled(True)
                    else:
                        self.invert_select_action.setEnabled(False)
                        self.unselect_all_action.setEnabled(False)
                        self.remove_selected_files_action.setEnabled(False)

                    if len(self.marked_images) == self.ui.imageListWidget.count():
                        self.select_all_action.setEnabled(False)
                    else:
                        self.select_all_action.setEnabled(True)
                    
                    self.remove_file_action.setEnabled(True)
                    self.delete_file_action.setEnabled(True)
                    self.remove_all_files_action.setEnabled(True)
                    self.select_all_action.setEnabled(True)
                
                else:
                    self.remove_file_action.setEnabled(False)
                    self.delete_file_action.setEnabled(False)
                    self.remove_selected_files_action.setEnabled(False)
                    self.remove_all_files_action.setEnabled(False)
                    self.select_all_action.setEnabled(False)
                    self.view_analyzed_img_action.setEnabled(False)

                self.img_list_contextmenu.exec(event.globalPos())

        return super().eventFilter(source, event)
    
    def on_analysis_failed(self, error_message: str = "Unknown Error"):
        self.analysis_in_progress = False
        self.restore_list_checkmarks()

        self.ui.analyzeBtn.setText(f"Analyze images")
        self.ui.addImgBtn.setEnabled(True)
    
        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle("Analysis Error")
        self.error_dialog.setText("<p><span style=\" font-weight:700; font-size: 12pt;\">" \
                                  "Oops! An error was encountered </span></p>")
        self.error_dialog.setInformativeText(error_message)
        self.error_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.error_dialog.setTextFormat(Qt.TextFormat.RichText)

        error_icon = QPixmap(u":/colorIcons/icons/error_round.png")
        error_icon = error_icon.scaled(QSize(48, 48), mode = Qt.TransformationMode.SmoothTransformation)
        self.error_dialog.setIconPixmap(error_icon)

        self.error_dialog.exec()

    def start_analysis(self):
        self.analysis_in_progress = True
        self.ui.genReportBtn.setEnabled(False)
        self.remove_list_checkmarks()
        self.set_analysis_outcome()

        row_count = self.form_layout.rowCount()
        for i in range(row_count):
            self.form_layout.removeRow(row_count - (i+1))

        if self.current_plot is not None:
            self.current_plot.deleteLater()
            self.current_plot = None

        self.ui.addImgBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.ui.analyzeBtn.setEnabled(False)
        self.ui.analyzeBtn.setText("Analysis in progress...")
        self.analysis_message_label.setText("Analysis in progress")
        self.analysis_progress_bar.show()
        self.analysis_message_label.show()

        if len(self.marked_images) < 2:
            images = self.marked_images[0]
            
        else:
            images = self.marked_images

        params = {}

        if self.ui.SIDInputCB.currentText() == "Manual":
            params["sid"] = self.ui.sIDDSB.value()

        if self.ui.DPIInputCB.currentText() == "Manual":
            params["dpi"] = self.ui.dPIDSB.value()

        # Top level try clause catches file IO errors
        try:
            self.worker = QStarshotWorker(filepath = images,
                                          radius = self.ui.radiusSB.value(),
                                          min_peak_height = self.ui.miniPeakHeightDSB.value(),
                                          tolerance = self.ui.toleranceDSB.value(),
                                          fwhm = self.ui.useFWHMCB.isChecked(),
                                          recursive = self.ui.recursiveSearchCB.isChecked(),
                                          invert = self.ui.forceInvertCB.isChecked(),
                                          **params
                                          )
            self.qthread = QThread()
            self.worker.moveToThread(self.qthread)
            self.worker.analysis_failed.connect(self.qthread.quit)
            self.worker.analysis_failed.connect(self.on_analysis_failed)
            self.worker.thread_finished.connect(self.qthread.quit)
            self.worker.thread_finished.connect(self.worker.deleteLater)
            self.worker.analysis_results_ready.connect(lambda results: self.show_analysis_results(results))
            self.qthread.started.connect(self.worker.analyze)
            self.qthread.finished.connect(self.qthread.deleteLater)

            self.qthread.start()

        except Exception as err:
            self.on_analysis_failed(traceback.format_exception_only(err)[-1])

    def show_analysis_results(self, results: dict):
        self.has_analysis = True
        self.current_results = results
        self.analysis_in_progress = False
        self.ui.genReportBtn.setEnabled(True)
        self.restore_list_checkmarks()

        # Analyze button is auto-enabled by update_marked_images() on item data change
        self.ui.analyzeBtn.setText(f"Analyze images")
        self.ui.addImgBtn.setEnabled(True)
        self.ui.genReportBtn.setEnabled(True)
    
        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        for summary_item in results["summary_text"]:
            self.form_layout.addRow(summary_item[0], QLabel(summary_item[1]))

        #set outcome
        self.set_analysis_outcome()

        # Update the plot
        starshot = results["starshot_obj"]
        starshot.plotImage()
        self.current_plot = starshot.imagePlotWidget
        self.ui.analysisInfoVL.addWidget(self.current_plot)

        #Update the summary
        self.analysis_summary = [["Wobble (circle) diameter", f"{starshot.wobble.radius_mm*2.0:2.3f} mm"],
                                 ["Number of spokes detected", f"{len(starshot.lines)}"]]

    def remove_list_checkmarks(self):
        for index in range(self.ui.imageListWidget.count()):
            listItemWidget = self.ui.imageListWidget.item(index)
            listItemWidget.setFlags(Qt.ItemFlag.ItemIsEnabled)

    def restore_list_checkmarks(self):
        for index in range(self.ui.imageListWidget.count()):
            listItemWidget = self.ui.imageListWidget.item(index)
            listItemWidget.setFlags(Qt.ItemFlag.ItemIsEnabled |
                                    Qt.ItemFlag.ItemIsUserCheckable |
                                    Qt.ItemFlag.ItemIsDragEnabled |
                                    Qt.ItemFlag.ItemIsSelectable)
            
            if listItemWidget.data(Qt.ItemDataRole.UserRole)["file_path"] in self.marked_images:
                listItemWidget.setCheckState(Qt.CheckState.Checked)

    def set_analysis_outcome(self):
        if not self.has_analysis or self.analysis_in_progress:
            self.ui.outcomeLE.clear()
            self.ui.outcomeLE.setStyleSheet(u"border-color: rgba(0, 0, 0,0);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(0, 0, 0, 0);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
            
        elif self.current_results["starshot_obj"].wobble.radius_mm * 2.0 < self.ui.toleranceDSB.value():
            self.ui.outcomeLE.setText("PASS")
            self.ui.outcomeLE.setStyleSheet(u"border-color: rgb(95, 200, 26);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(95, 200, 26, 150);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
            
        else:
            self.ui.outcomeLE.setText("FAIL")
            self.ui.outcomeLE.setStyleSheet(u"border-color: rgb(231, 29, 14);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(231, 29, 14, 150);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
    
    def generate_report(self):
        physicist_name_le = QLineEdit()
        institution_name_le = QLineEdit()
        treatment_unit_le = QComboBox()
        treatment_unit_le.setEditable(True)
        physicist_name_le.setMaximumWidth(250)
        physicist_name_le.setMinimumWidth(250)
        institution_name_le.setMaximumWidth(350)
        institution_name_le.setMinimumWidth(350)
        treatment_unit_le.setMaximumWidth(250)
        treatment_unit_le.setMinimumWidth(250)

        save_path_le = QLineEdit()
        save_win_btn = QPushButton("Save to...")
        save_path_le.setReadOnly(True)
        save_location_layout = QHBoxLayout()
        save_location_layout.addWidget(save_path_le)
        save_location_layout.addWidget(save_win_btn)

        show_report_checkbox = QCheckBox()
        show_report_label = QLabel("Open report:")
        show_report_checkbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        show_report_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        show_report_layout = QHBoxLayout()
        show_report_layout.addWidget(show_report_label)
        show_report_layout.addWidget(show_report_checkbox)

        # get linac devices
        linac_devices = DeviceManager.device_list["linacs"]
        treatment_unit_le.addItems([linac.name for linac in linac_devices])

        user_details_layout = QFormLayout()
        user_details_layout.addRow("Physicist:", physicist_name_le)
        user_details_layout.addRow("Treatment unit:", treatment_unit_le)
        user_details_layout.addRow("Institution:", institution_name_le)
        user_details_layout.addRow("Save location:", save_location_layout)
        user_details_layout.addRow("",show_report_layout)
        user_details_layout.addItem(QSpacerItem(1,10, QSizePolicy.Policy.Minimum,
                                                QSizePolicy.Policy.Minimum))
        
        layout = QVBoxLayout()
        layout.addLayout(user_details_layout)

        dialog_buttons = QDialogButtonBox()
        save_button = dialog_buttons.addButton(QDialogButtonBox.StandardButton(
            QDialogButtonBox.StandardButton.Save), )
        save_button.setEnabled(False)
        cancel_button = dialog_buttons.addButton(QDialogButtonBox.StandardButton(
            QDialogButtonBox.StandardButton.Cancel))
        
        # enable the save button once we have a path to save the report to
        save_path_le.textChanged.connect(lambda: save_button.setEnabled(True))
        
        layout.addWidget(dialog_buttons)

        report_dialog = QDialog()
        report_dialog.setWindowTitle("Generate Starshot Report ‒ PyBeam QA")
        report_dialog.setLayout(layout)
        report_dialog.setMinimumSize(report_dialog.sizeHint())
        report_dialog.setMaximumSize(report_dialog.sizeHint())

        cancel_button.clicked.connect(report_dialog.reject)
        save_button.clicked.connect(report_dialog.accept)
        save_win_btn.clicked.connect(lambda: self.save_report_to(save_path_le))

        result = report_dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            physicist_name = "N/A" if physicist_name_le.text() == "" else physicist_name_le.text()
            institution_name = "N/A" if institution_name_le.text() == "" else institution_name_le.text()
            treatment_unit = "N/A" if treatment_unit_le.currentText() == "" else treatment_unit_le.currentText()
        
            starshot = self.current_results["starshot_obj"]

            report = StarshotReport(filename = save_path_le.text(),
                                    author = physicist_name,
                                    institution = institution_name,
                                    treatment_unit_name = treatment_unit,
                                    analysis_summary = self.analysis_summary,
                                    summary_plots = starshot.get_publishable_plots(),
                                    wobble_diameter = starshot.wobble.radius_mm * 2.0,
                                    tolerance = self.ui.toleranceDSB.value(),
                                    report_status = self.ui.outcomeLE.text())
            report.saveReport()

            if show_report_checkbox.isChecked():
                webbrowser.open(save_path_le.text())

    def save_report_to(self, line_edit: QLineEdit):
        file_path = QFileDialog.getSaveFileName(caption="Save To File...", filter="PDF (*.pdf)")
        
        if file_path[0] != "":
            path = file_path[0].split("/")
            
            if not path[-1].endswith(".pdf"):
                path[-1] = path[-1] + ".pdf"
            
            line_edit.setText("/".join(path))
            