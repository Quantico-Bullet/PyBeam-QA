from PySide6.QtWidgets import (QWidget, QLabel, QProgressBar, QVBoxLayout, QFileDialog,
                               QListWidgetItem, QMenu, QSizePolicy, QMessageBox, 
                               QMainWindow, QFormLayout, QTabWidget, QFrame, QGridLayout,
                               QSplitter, QTreeWidgetItem, QTreeWidget, QComboBox,
                               QDialog, QDialogButtonBox, QLineEdit, QSpacerItem,
                               QPushButton, QCheckBox, QHBoxLayout)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QEvent, QThread

from ui.py_ui import icons_rc
from ui.py_ui.fieldAnalysisWorksheet_ui import Ui_QFieldAnalysisWorksheet
from core.analysis.field_analysis import QFieldAnalysis, QFieldAnalysisWorker
from core.tools.report import FieldAnalysisReport
from core.tools.devices import DeviceManager

import platform
import webbrowser
import subprocess
import pyqtgraph as pg
from pathlib import Path
from pylinac.core.image import LinacDicomImage
from pylinac.field_analysis import Protocol, Centering, Interpolation, Normalization, Edge

class QFieldAnalysisWorksheet(QWidget):

    DEFAULT_PROTOCOLS = {"Varian": Protocol.VARIAN,
                         "Elekta": Protocol.ELEKTA,
                         "Siemens": Protocol.SIEMENS}
    
    CENTERING = {"Beam center": Centering.BEAM_CENTER,
                 "Geometric center": Centering.GEOMETRIC_CENTER,
                 "Manual": Centering.MANUAL}
    
    INTERPOLATION = {"Linear": Interpolation.LINEAR,
                     "Spline": Interpolation.SPLINE}
    
    EDGE_DETECTION = {"FWHM": Edge.FWHM,
                      "Inflection Derivative": Edge.INFLECTION_DERIVATIVE,
                      "Inflection Hill": Edge.INFLECTION_HILL}
    
    NORMALIZATION = {"Beam center": Normalization.BEAM_CENTER,
                     "Geometric center": Normalization.GEOMETRIC_CENTER,
                     "Max": Normalization.MAX}

    def __init__(self):
        super().__init__()

        self.ui = Ui_QFieldAnalysisWorksheet()
        self.ui.setupUi(self)

        self.image_icon = QIcon()
        self.image_icon.addFile(u":/colorIcons/icons/picture.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.analyzeBtn.setText("Analyze image(s)")
        self.ui.advancedViewBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.ui.summaryTE.setReadOnly(True)

        #--------  add widgets --------
        self.progress_vl = QVBoxLayout()
        self.progress_vl.setSpacing(10)
        self.ui.analysisOutcomeFrame.hide()

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
        self.ui.advancedViewBtn.clicked.connect(self.show_advanced_results_view)
        self.ui.genReportBtn.clicked.connect(self.generate_report)
        self.ui.imageListWidget.itemChanged.connect(self.update_marked_images)

        #-------- init defaults --------
        self.marked_images = []
        self.current_results = None
        self.imageView_windows = []
        self.advanced_results_view = None
        self.analysis_in_progress = False
        self.has_analysis = False

        self.setup_config()
        self.update_marked_images()

    def setup_config(self):
        """
        Setup field analysis configuration options and values.
        """
        self.ui.protocolCB.clear()
        self.ui.centeringCB.clear()
        self.ui.interpolationCB.clear()

        self.ui.protocolCB.addItems([key for key in self.DEFAULT_PROTOCOLS.keys()])
        self.ui.centeringCB.addItems([key for key in self.CENTERING.keys()])
        self.ui.interpolationCB.addItems([key for key in self.INTERPOLATION.keys()])
        self.ui.edgeDetCB.addItems([key for key in self.EDGE_DETECTION.keys()])
        self.ui.normalizationCB.addItems([key for key in self.NORMALIZATION.keys()])

        self.ui.centeringCB.currentIndexChanged.connect(self.on_config_change)
        self.ui.interpolationCB.currentIndexChanged.connect(self.on_config_change)
        self.ui.edgeDetCB.currentIndexChanged.connect(self.on_config_change)
        self.ui.normalizationCB.currentIndexChanged.connect(self.on_config_change)
        self.ui.fffBeamCheckB.stateChanged.connect(self.on_config_change)

        # call this manually the first time to display correct config options
        self.on_config_change()

        self.set_default_values()

    def set_default_values(self):
        """
        Set default values for configuration fields, useful for restoring defaults.
        """
        self.ui.centeringCB.setCurrentIndex(0)

        self.ui.vertPosDSB.setValue(0.50)
        self.ui.horPosDSB.setValue(0.50)
        self.ui.edgeSmoothDSB.setValue(0.003)
        self.ui.hillWinRatioDSB.setValue(0.15)
        self.ui.interpolationResDSB.setValue(0.10)
        self.ui.inFieldRatioDSB.setValue(0.80)
        self.ui.slopeExclRatioDSB.setValue(0.20)

        self.ui.groundCheckB.setChecked(True)
        self.ui.invertImageCheckB.setChecked(False)
        self.ui.fffBeamCheckB.setChecked(False)

    def on_config_change(self):
        """
        Checks the current config values and adjusts fields and displays warnings if any issues
        are encountered
        """

        if self.ui.centeringCB.currentText() == "Manual":
            self.ui.configFormLayout.setRowVisible(2, True)
        else:
            self.ui.configFormLayout.setRowVisible(2, False)

        if self.ui.edgeDetCB.currentText() == "Inflection Hill":
            self.ui.hillWinRatioLabel.show()
            self.ui.hillWinRatioDSB.show()
        else:
            self.ui.hillWinRatioLabel.hide()
            self.ui.hillWinRatioDSB.hide()

            if self.ui.edgeDetCB.currentText() == "FWHM" and self.ui.fffBeamCheckB.isChecked():
               self.show_warning("Oh-oh! Becareful with your parameters",
                                 "Using FWHM as an edge detection method for a FFF beam is not advised. "
                                 "Consider using 'Inflection Derivative' or 'Inflection Hill'")

        if self.ui.interpolationCB.currentText() == "None":
            self.ui.configFormLayout.setRowVisible(7, False)
        else:
            self.ui.configFormLayout.setRowVisible(7, True)

    def show_warning(self, title_text:str, message: str):
        self.warning_dialog = QMessageBox()
        self.warning_dialog.resize(400,0)
        self.warning_dialog.setWindowTitle("Warning")
        self.warning_dialog.setText("<p><span style=\" font-weight:700; font-size: 12pt;\">" \
                                  f"{title_text}</span></p>")
        self.warning_dialog.setInformativeText(message)
        self.warning_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.warning_dialog.setTextFormat(Qt.TextFormat.RichText)

        error_icon = QPixmap(u":/colorIcons/icons/error_round.png")
        error_icon = error_icon.scaled(QSize(48, 48), mode = Qt.TransformationMode.SmoothTransformation)
        self.warning_dialog.setIconPixmap(error_icon)

        self.warning_dialog.exec()

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select DICOM Field Analysis Images",
            "",
            "DICOM Images (*.dcm)",
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

        else:
            self.ui.analyzeBtn.setEnabled(False)
            self.analysis_message_label.hide()

    def view_dicom_image(self):
        image_short_name = self.ui.imageListWidget.currentItem().text()
        image_path = self.ui.imageListWidget.selectedItems()[0].data(Qt.UserRole)["file_path"]
        image = LinacDicomImage(image_path)

        imgView = pg.ImageView()
        imgView.setImage(image.array)
        imgView.setPredefinedGradient("viridis")

        new_win = QMainWindow()
        new_win.setWindowTitle(image_short_name)
        new_win.setCentralWidget(imgView)
        new_win.setMinimumSize(600, 500)
        
        self.imageView_windows.append(new_win)
        new_win.show()
        new_win.setMinimumSize(0, 0)

    def delete_file(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()

        self.delete_dialog = QMessageBox()
        self.delete_dialog.setWindowTitle("Delete File")
        self.delete_dialog.setText("<p><span style=\" font-weight:700; font-size: 11pt;\">" \
                                  f"Are you sure you want to permanently delete \'{listWidgetItem.text()}\' ? </span></p>")
        self.delete_dialog.setInformativeText("This action is irreversible!")
        self.delete_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | 
                                             QMessageBox.StandardButton.Cancel)
        self.delete_dialog.setTextFormat(Qt.TextFormat.RichText)

        warning_icon = QPixmap(u":/colorIcons/icons/warning.png")
        warning_icon = warning_icon.scaled(QSize(48, 48), mode = Qt.TransformationMode.SmoothTransformation)
        self.delete_dialog.setIconPixmap(warning_icon)

        ret = self.delete_dialog.exec()

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

        self.warning_dialog = QMessageBox()
        self.warning_dialog.setWindowTitle("Analysis Error")
        self.warning_dialog.setText("<p><span style=\" font-weight:700; font-size: 12pt;\">" \
                                  "Oops! An error was encountered</span></p>")
        self.warning_dialog.setInformativeText(error_message)
        self.warning_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.warning_dialog.setTextFormat(Qt.TextFormat.RichText)

        error_icon = QPixmap(u":/colorIcons/icons/error_round.png")
        error_icon = error_icon.scaled(QSize(48, 48), mode = Qt.TransformationMode.SmoothTransformation)
        self.warning_dialog.setIconPixmap(error_icon)

        self.warning_dialog.exec()

    def start_analysis(self):
        self.analysis_in_progress = True
        self.ui.advancedViewBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.remove_list_checkmarks()

        self.ui.summaryTE.hide()
        self.ui.summaryTE.clear()

        self.ui.addImgBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.ui.analyzeBtn.setEnabled(False)
        self.ui.analyzeBtn.setText("Analysis in progress...")
        self.analysis_message_label.setText("Analysis in progress")
        self.analysis_progress_bar.show()
        self.analysis_message_label.show()
            
        self.worker = QFieldAnalysisWorker(path = self.marked_images[0],
                                           protocol = self.DEFAULT_PROTOCOLS[self.ui.protocolCB.currentText()],
                                           centering = self.ui.centeringCB.currentText(),
                                           vert_position = self.ui.vertPosDSB.value(),
                                           horiz_position = self.ui.horPosDSB.value(),
                                           normalization_method = self.ui.normalizationCB.currentText(),
                                           edge_detection_method = self.ui.edgeDetCB.currentText(),
                                           edge_smoothing_ratio = self.ui.edgeSmoothDSB.value(),
                                           hill_window_ratio = self.ui.hillWinRatioDSB.value(),
                                           interpolation = self.ui.interpolationCB.currentText(),
                                           in_field_ratio = self.ui.inFieldRatioDSB.value(),
                                           slope_exclusion_ratio = self.ui.slopeExclRatioDSB.value(),
                                           is_FFF = self.ui.fffBeamCheckB.isChecked(),
                                           invert = self.ui.invertImageCheckB.isChecked(),
                                           ground = self.ui.groundCheckB.isChecked()
                                           )
        
        self.qthread = QThread()
        self.worker.moveToThread(self.qthread)
        self.worker.analysis_failed.connect(self.qthread.quit)
        self.worker.analysis_failed.connect(self.on_analysis_failed)
        self.worker.thread_finished.connect(self.qthread.quit)
        self.worker.analysis_results_ready.connect(lambda results: self.show_analysis_results(results))
        self.qthread.started.connect(self.worker.analyze)
        self.qthread.finished.connect(self.qthread.deleteLater)

        self.qthread.start()

    def show_analysis_results(self, results: dict):
        self.has_analysis = True
        self.current_results = results
        self.analysis_in_progress = False
        self.ui.advancedViewBtn.setEnabled(True)
        self.ui.genReportBtn.setEnabled(True)
        self.restore_list_checkmarks()

        # Analyze button is auto-enabled by update_marked_images() on item data change
        self.ui.analyzeBtn.setText(f"Analyze images")
        self.ui.addImgBtn.setEnabled(True)
        self.ui.genReportBtn.setEnabled(True)
    
        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        # Update the report summary
        pf = results["field_analysis_obj"]

        self.ui.summaryTE.setText(results["summary_text"])
        self.ui.summaryTE.show()

        # Update the advanced view
        if self.advanced_results_view is not None:
            self.advanced_results_view.update_picket_fence(pf)

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

    def show_advanced_results_view(self):
        if self.advanced_results_view is None:
            self.advanced_results_view = AdvancedFAView(fa = self.current_results["field_analysis_obj"])
            self.advanced_results_view.show()

        else: 
            self.advanced_results_view.show()
    
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
        report_dialog.setWindowTitle("Generate Field Analysis Report ‒ PyBeam QA")
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

            fa = self.current_results["field_analysis_obj"]

            report = FieldAnalysisReport(save_path_le.text(),
                                   author = physicist_name,
                                   institution = institution_name,
                                   treatment_unit_name = treatment_unit,
                                   protocol = "Varian",
                                   analysis_summary = fa.get_publishable_results(),
                                   summary_plots = fa.get_publishable_plots(),
            )
        
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
            
class AdvancedFAView(QMainWindow):

    def __init__(self, parent: QWidget | None = None, fa: QFieldAnalysis = None):
        super().__init__(parent = parent)

        self.fa = fa
 
        self.initComplete = False

        self.setWindowTitle("Field Analysis (Advanced Results) ‒ PyBeam QA")
        self.resize(720, 480)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.top_layout = QGridLayout(self.central_widget)
        self.top_layout.setContentsMargins(0, 0, 0, 0)

        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setTabsClosable(False)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        size_policy.setVerticalStretch(0)
        size_policy.setHorizontalStretch(0)
        self.central_widget.setSizePolicy(size_policy)
        self.tab_widget.setSizePolicy(size_policy)

        #----- Setup analyzed image tab content
        self.analyzed_img_qSplitter = QSplitter()
        self.analyzed_img_qSplitter.setSizePolicy(size_policy)

        self.tab_widget.addTab(self.analyzed_img_qSplitter, "Analyzed Image")

        self.top_layout.addWidget(self.tab_widget, 0, 0, 1, 1)

        self.curr_analyzed_image_widget = None

        if fa is not None:
            self.init_analyzed_image()

        self.initComplete = True
    
    def update_picket_fence(self, fa: QFieldAnalysis):
        self.fa = fa

        self.initComplete = False

        self.init_analyzed_image()

        self.initComplete = True
            
    def init_analyzed_image(self):
        if self.curr_analyzed_image_widget is not None:
            self.curr_analyzed_image_widget.deleteLater()

        self.curr_analyzed_image_widget = self.fa.analyzed_image_plot_widget
        self.analyzed_img_qSplitter.addWidget(self.curr_analyzed_image_widget)

        self.fa.qplot_analyzed_image()