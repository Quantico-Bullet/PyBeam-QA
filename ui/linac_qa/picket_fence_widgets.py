from PySide6.QtWidgets import (QWidget, QLabel, QProgressBar, QVBoxLayout, QFileDialog,
                               QListWidgetItem, QMenu, QSizePolicy, QMessageBox, 
                               QMainWindow, QFormLayout, QTabWidget, QFrame, QGridLayout,
                               QSplitter, QTreeWidgetItem, QTreeWidget, QComboBox,
                               QDialog, QDialogButtonBox, QLineEdit, QSpacerItem,
                               QPushButton, QCheckBox, QHBoxLayout, QPlainTextEdit,
                               QDateEdit)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QEvent, QThread, Signal, QDate

from ui.util_widgets import worksheet_save_report
from ui.util_widgets.dialogs import MessageDialog
from ui.util_widgets.statusbar import AnalysisInfoLabel
from ui.linac_qa.picket_fence_test_dialog import PFTestDialog
from ui.linac_qa.qa_tools_win import QAToolsWindow
from ui.py_ui import icons_rc
from ui.py_ui.picket_fence_worksheet_ui import Ui_QPicketFenceWorksheet
from core.analysis.picket_fence import (QPicketFence,
                                        QPicketFenceWorker,
                                        generate_picket_fence)
from core.tools.report import PicketFenceReport
from core.tools.devices import DeviceManager

import traceback
import platform
import webbrowser
import subprocess
import pyqtgraph as pg
from pathlib import Path

from pylinac.core.image_generator import (GaussianFilterLayer,
                                          PerfectFieldLayer,
                                          AS500Image,
                                          AS1000Image,
                                          AS1200Image)
from pylinac.core.image import LinacDicomImage
from pylinac.picketfence import MLC, Orientation

class PicketFenceMainWindow(QAToolsWindow):
    
    def __init__(self, initData: dict = None):
        super().__init__(initData)

        self.window_title = "Picket Fence ‒ PyBeam QA"
        self.setWindowTitle(self.window_title)

        self.add_new_worksheet()

        self.ui.menuFile.addAction("Add Image(s)", self.ui.tabWidget.currentWidget().add_files)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction("Add New Worksheet", self.add_new_worksheet)
        self.ui.menuTools.addAction("Benchmark Test", self.init_test_dialog, "Ctrl+T")
        self.ui.menuTools.addAction("Compare Profiles", self.compare_profiles, "Ctrl+Shift+P")

    def add_new_worksheet(self, worksheet_name: str = None, enable_icon: bool = True):
        if worksheet_name is None:
            self.untitled_counter = self.untitled_counter + 1
            worksheet_name = f"Picket Fence (Untitled-{self.untitled_counter})"

        return super().add_new_worksheet(QPicketFenceWorksheet(), worksheet_name, enable_icon)
    
    def init_test_dialog(self):
        dialog = PFTestDialog()
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            sim_image = dialog.ui.sim_image_cb.currentText()
            img_orientation = dialog.ui.image_orientation_cb.currentText()

            # Set simulation image
            if sim_image == "AS500":
                sim_image = AS500Image
            
            elif sim_image == "AS1000":
                sim_image = AS1000Image
            
            else: sim_image = AS1200Image

            # Set image orientation
            if img_orientation == "Up-Down":
                img_orientation = Orientation.UP_DOWN
            
            else: img_orientation = Orientation.LEFT_RIGHT

            picket_offset_errs = dialog.picket_offset_errors if \
            dialog.picket_offset_errors else None

            generate_picket_fence(
                simulator = sim_image(dialog.ui.sid_sb.value()),
                field_layer = PerfectFieldLayer,
                file_out = dialog.ui.out_file_le.text(),
                final_layers = [
                    GaussianFilterLayer(sigma_mm = 0.1),
                ],
                pickets = dialog.ui.num_pickets_sb.value(),
                picket_spacing_mm = dialog.ui.picket_spacing_sb.value(),
                picket_width_mm = dialog.ui.picket_width_sb.value(),
                picket_offset_error = picket_offset_errs,
                orientation = img_orientation,
                image_rotation = dialog.ui.image_rotation_dsb.value()
            )

            self.add_new_worksheet(dialog.ui.test_name_le.text() + " (Test)")
            self.ui.tabWidget.currentWidget().add_files([dialog.ui.out_file_le.text()])

    def compare_profiles(self):
        comp_profile_dialog = QDialog()
        comp_profile_dialog.setWindowTitle("Compare Picket Fence Profiles")

        layout = QVBoxLayout()
        widget_layout = QFormLayout()

        profiles_list_0_cb = QComboBox()
        profiles_list_1_cb = QComboBox()
        profiles_list_0_cb.setFixedWidth(200)
        profiles_list_1_cb.setFixedWidth(200)

        widget_layout.addRow("Profile 1:", profiles_list_0_cb)
        widget_layout.addRow("Profile 2:", profiles_list_1_cb)

        dialog_buttons = QDialogButtonBox()
        apply_button = dialog_buttons.addButton(QDialogButtonBox.StandardButton(
            QDialogButtonBox.StandardButton.Apply), )
        apply_button.setEnabled(False)
        cancel_button = dialog_buttons.addButton(QDialogButtonBox.StandardButton(
            QDialogButtonBox.StandardButton.Cancel), )

        for index in range(self.ui.tabWidget.count()):
            widget: QPicketFenceWorksheet = self.ui.tabWidget.widget(index)

            if widget.has_analysis:
                apply_button.setEnabled(True)
                profiles_list_0_cb.addItem(self.ui.tabWidget.tabText(index))
                profiles_list_1_cb.addItem(self.ui.tabWidget.tabText(index))

        layout.addLayout(widget_layout)
        comp_profile_dialog.setLayout(layout)

        cancel_button.clicked.connect(comp_profile_dialog.reject)
        apply_button.clicked.connect(comp_profile_dialog.accept)

        layout.addWidget(dialog_buttons)
        comp_profile_dialog.setFixedSize(comp_profile_dialog.sizeHint())
        comp_profile_dialog.exec()

class QPicketFenceWorksheet(QWidget):

    analysis_info_signal = Signal(dict)
    save_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()

        self.ui = Ui_QPicketFenceWorksheet()
        self.ui.setupUi(self)

        self.image_icon = QIcon()
        self.image_icon.addFile(u":/colorIcons/icons/picture.png", QSize(), QIcon.Normal, QIcon.Off)

        self.form_layout = QFormLayout()
        self.form_layout.setHorizontalSpacing(40)
        self.ui.analysisInfoVL.addLayout(self.form_layout)

        self.ui.analyzeBtn.setText("Analyze image(s)")
        self.ui.advancedViewBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)

        #--------  add widgets --------
        self.progress_vl = QVBoxLayout()
        self.progress_vl.setSpacing(10)

        self.ui.analysisInfoVL.addLayout(self.progress_vl)

        # setup context menu for image list widget
        self.img_list_contextmenu = QMenu()
        self.img_list_contextmenu.addAction("View Original Image", self.view_dicom_image, "Ctrl+I")
        self.img_list_contextmenu.addAction("Show Containing Folder", self.open_file_folder)
        self.remove_file_action = self.img_list_contextmenu.addAction("Remove from List", self.remove_file)
        self.delete_file_action = self.img_list_contextmenu.addAction("Delete", self.delete_file)
        self.img_list_contextmenu.addAction("Properties")
        self.img_list_contextmenu.addSeparator()
        self.select_all_action = self.img_list_contextmenu.addAction("Select All", lambda: self.perform_selection("selectAll"), "Ctrl+A")
        self.unselect_all_action = self.img_list_contextmenu.addAction("Unselect All", lambda: self.perform_selection("unselectAll"),
                                                                        "Ctrl+Shift+A")
        self.invert_select_action = self.img_list_contextmenu.addAction("Invert Selection", lambda: self.perform_selection("invertSelection"))
        self.img_list_contextmenu.addSeparator()
        self.remove_selected_files_action = self.img_list_contextmenu.addAction("Remove Selected Files", self.remove_selected_files)
        self.remove_all_files_action = self.img_list_contextmenu.addAction("Remove All Files", self.remove_all_files)
        self.ui.imageListWidget.installEventFilter(self)

        #Add all context menu actions to this widget to use shortcuts
        self.addActions(self.img_list_contextmenu.actions())

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
        self.ui.toleranceDSB.valueChanged.connect(self.set_analysis_outcome)

        #-------- init defaults --------
        self.marked_images = []
        self.current_results: dict = None
        self.imageView_windows = []
        self.advanced_results_view = None
        self.analysis_in_progress = False
        self.has_analysis = False

        self.setup_config()
        self.update_marked_images()
        self.set_analysis_outcome()

        #Set analysis state and message for status bar
        self.analysis_message = None
        self.analysis_state = AnalysisInfoLabel.IDLE

        # Set initial session save info
        self.report_author = ""
        self.report_institution = ""
        self.report_date = QDate.currentDate()
        self.save_path = ""
        self.save_comment = ""

    def setup_config(self):
        self.ui.mlcTypeCB.addItems([mlc.value["name"] for mlc in MLC])
        self.ui.numPicketsCB.addItems(["Auto detect", "Specify"])

        self.ui.numPicketsCB.currentIndexChanged.connect(self.on_config_change)

        self.on_config_change()
        self.set_default_values()
    
    def set_default_values(self):
        self.ui.mlcTypeCB.setCurrentIndex(0)
        self.ui.numPicketsCB.setCurrentIndex(0)
        self.ui.numPicketsSB.setValue(5)
        self.ui.cropDSB.setValue(3.0)
        self.ui.nominalGapDSB.setValue(3.0)
        self.ui.combLeafAnalysisCheckB.setChecked(True)
        self.ui.useFilenameSCheckB.setChecked(False)
        self.ui.invertImageCheckB.setChecked(False)

    def on_config_change(self):
        if self.ui.numPicketsCB.currentText() == "Auto detect":
            self.ui.configFormLayout.setRowVisible(3, False)
        else:
            self.ui.configFormLayout.setRowVisible(3, True)
    
    def add_files(self, files: tuple | list | None = None):
        if not files:
            files, _ = QFileDialog.getOpenFileNames(
                self,
                "Select Picket Fence Images",
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
        image = LinacDicomImage(image_path)

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

        warning_dialog = MessageDialog()
        warning_dialog.set_icon(MessageDialog.WARNING_ICON)
        warning_dialog.set_title("Delete File")
        warning_dialog.set_header_text(f"Are you sure you want to permanently delete {listWidgetItem.text()} ?")
        warning_dialog.set_info_text("This action is irreversible!")
        warning_dialog.set_standard_buttons(QDialogButtonBox.StandardButton.Yes | 
                                            QDialogButtonBox.StandardButton.Cancel)

        ret = warning_dialog.exec()

        if ret == QDialogButtonBox.StandardButton.Yes:
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

    def on_analysis_failed(self,
                           title_text: str = "Oops! An error was encountered",
                           error_message: str = "Unknown Error"):
        self.analysis_info_signal.emit({"state": AnalysisInfoLabel.FAILED,
                                        "message": None})
        self.analysis_state =  AnalysisInfoLabel.FAILED
        self.analysis_message = None

        self.analysis_in_progress = False
        self.restore_list_checkmarks()

        self.ui.analyzeBtn.setText(f"Analyze images")
        self.ui.addImgBtn.setEnabled(True)
    
        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        self.error_dialog = MessageDialog()
        self.error_dialog.set_icon(MessageDialog.CRITICAL_ICON)
        self.error_dialog.set_title("Analysis Error")
        self.error_dialog.set_header_text("Oops! An error was encountered")
        self.error_dialog.set_info_text(error_message)
        self.error_dialog.set_standard_buttons(QDialogButtonBox.StandardButton.Ok)
        
        self.error_dialog.exec()

    def start_analysis(self):
        self.analysis_info_signal.emit({"state": AnalysisInfoLabel.IN_PROGRESS,
                                        "message": None})
        self.analysis_state =  AnalysisInfoLabel.IN_PROGRESS
        self.analysis_message = None

        self.analysis_in_progress = True
        self.ui.advancedViewBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.remove_list_checkmarks()
        self.set_analysis_outcome()

        if self.current_results is not None:
            self.clear_analysis_data()

        row_count = self.form_layout.rowCount()
        for i in range(row_count):
            self.form_layout.removeRow(row_count - (i+1))

        self.ui.addImgBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.ui.analyzeBtn.setEnabled(False)
        self.ui.analyzeBtn.setText("Analysis in progress...")
        self.analysis_message_label.setText("Analysis in progress")
        self.analysis_progress_bar.show()
        self.analysis_message_label.show()

        if len(self.marked_images) > 0:
            images = self.marked_images[0]
            
            try:

                num_pickets = (None if self.ui.numPicketsCB.currentText() == "Auto detect" 
                               else self.ui.numPicketsSB.value())

                self.worker = QPicketFenceWorker(filename = images,
                                use_filename = self.ui.useFilenameSCheckB.isChecked(),
                                mlc = self.ui.mlcTypeCB.currentText(),
                                crop_mm = self.ui.cropDSB.value(),
                                invert = self.ui.invertImageCheckB.isChecked(),
                                tolerance = self.ui.toleranceDSB.value(),
                                num_pickets = num_pickets,
                                nominal_gap = self.ui.nominalGapDSB.value(),
                                separate_leaves = not self.ui.combLeafAnalysisCheckB.isChecked())
        
                self.qthread = QThread()
                self.worker.moveToThread(self.qthread)
                self.worker.analysis_failed.connect(self.qthread.quit)
                self.worker.analysis_failed.connect(lambda x: self.on_analysis_failed(error_message = x))
                self.worker.thread_finished.connect(self.qthread.quit)
                self.worker.thread_finished.connect(self.worker.deleteLater)
                self.worker.analysis_results_ready.connect(lambda results: self.show_analysis_results(results))
                self.qthread.started.connect(self.worker.analyze)
                self.qthread.finished.connect(self.qthread.deleteLater)

                self.qthread.start()

            except Exception as err:
                self.on_analysis_failed(error_message = traceback.format_exception_only(err)[-1])

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
    
        # Update status bar message
        self.analysis_info_signal.emit({"state": AnalysisInfoLabel.COMPLETE,
                                        "message": None})
        self.analysis_state =  AnalysisInfoLabel.COMPLETE
        self.analysis_message = None

        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        for summary_item in results["summary_text"]:
            self.form_layout.addRow(summary_item[0], QLabel(summary_item[1]))

        #set outcome
        self.set_analysis_outcome()
        
        # Update the advanced view
        if self.advanced_results_view is not None:
            self.advanced_results_view.update_picket_fence(results["picket_fence_obj"])

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
            self.advanced_results_view = AdvancedPFView(pf = self.current_results["picket_fence_obj"])
            self.advanced_results_view.showMaximized()

        else: 
            self.advanced_results_view.showMaximized()
    
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
            
        elif self.current_results["picket_fence_obj"].max_error < self.ui.toleranceDSB.value():
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
        analysis_date = QDateEdit()
        comments_te = QPlainTextEdit()
        treatment_unit_le.setEditable(True)
        physicist_name_le.setMaximumWidth(250)
        physicist_name_le.setMinimumWidth(250)
        institution_name_le.setMaximumWidth(350)
        institution_name_le.setMinimumWidth(350)
        treatment_unit_le.setMaximumWidth(250)
        treatment_unit_le.setMinimumWidth(250)
        analysis_date.setMaximumWidth(120)
        analysis_date.setCalendarPopup(True)
        analysis_date.setDisplayFormat("dd MMMM yyyy")
        analysis_date.setMaximumDate(QDate.currentDate())

        # restore current save info
        physicist_name_le.setText(self.report_author)
        institution_name_le.setText(self.report_institution)
        analysis_date.setDate(self.report_date)
        comments_te.setPlainText(self.save_comment)

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
        user_details_layout.addRow("Analysis date:", analysis_date)
        user_details_layout.addRow("Comments:", comments_te)
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
        report_dialog.setWindowTitle("Generate Picket Fence Report ‒ PyBeam QA")
        report_dialog.setLayout(layout)
        report_dialog.setMinimumSize(report_dialog.sizeHint())
        report_dialog.setMaximumSize(report_dialog.sizeHint())


        cancel_button.clicked.connect(report_dialog.reject)
        save_button.clicked.connect(report_dialog.accept)
        save_win_btn.clicked.connect(lambda: save_path_le.setText(worksheet_save_report(self)))

        result = report_dialog.exec()

        if result == QDialog.DialogCode.Accepted:

            # Amend save info
            self.report_author = physicist_name_le.text()
            self.report_institution = institution_name_le.text()
            self.save_comment = comments_te.toPlainText()
            self.report_date = analysis_date.date()

            physicist_name = "N/A" if physicist_name_le.text() == "" else physicist_name_le.text()
            institution_name = "N/A" if institution_name_le.text() == "" else institution_name_le.text()
            treatment_unit = "N/A" if treatment_unit_le.currentText() == "" else treatment_unit_le.currentText()

            pf = self.current_results["picket_fence_obj"]

            summary_text = {"Gantry angle": f"{pf.image.gantry_angle:2.2f}°",
                            "Collimator angle": f"{pf.image.collimator_angle:2.2f}°",
                            "Number of leaves failing": str(len(pf.failed_leaves())),
                            "Absolute median error": f"{pf.abs_median_error:2.2f} mm",
                            "Mean picket spacing": f"{pf.mean_picket_spacing:2.2f} mm"}
            
            if pf.separate_leaves:
                leaf_name = pf.max_error_leaf[0] + f"-{(int(pf.max_error_leaf[1:]) + 1)}"
                summary_text["Max Error"] = [f"{pf.max_error:2.3f} mm",
                                             f"At picket: {pf.max_error_picket + 1}, leaf: {leaf_name}"]

            else:
                summary_text["Max Error"] = [f"{pf.max_error:2.3f} mm",
                                             f"At picket: {pf.max_error_picket + 1}, leaf: {pf.max_error_leaf + 1}"] 

            report = PicketFenceReport(save_path_le.text(),
                                   author = physicist_name,
                                   institution = institution_name,
                                   treatment_unit_name = treatment_unit,
                                   mlc_type = pf.mlc_type,
                                   analysis_date = self.report_date.toString("dd MMMM yyyy"),
                                   analysis_summary = summary_text,
                                   report_status = self.ui.outcomeLE.text(),
                                   max_error = pf.max_error,
                                   tolerance = self.ui.toleranceDSB.value(),
                                   summary_plot = pf.get_publishable_plot(),
                                   comments = comments_te.toPlainText()
                                   )
        
            report.save_report()

            if show_report_checkbox.isChecked():
                webbrowser.open(save_path_le.text())

    def clear_analysis_data(self):
        del self.current_results
        self.current_results = None

        # Run the garbage collector now to free resources
        #gc.collect()
            
class AdvancedPFView(QMainWindow):

    def __init__(self, parent: QWidget | None = None, pf: QPicketFence = None):
        super().__init__(parent = parent)

        self.pf = pf

        self.initComplete = False

        self.setWindowTitle("Picket Fence Analysis (Advanced Results) ‒ PyBeam QA")
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

        #-----  Setup details tab content
        self.details_qSplitter = QSplitter()
        self.details_qSplitter.setContentsMargins(0, 10, 0, 0)
        self.details_qSplitter.setSizePolicy(size_policy)

        self.details_tree_widget = QTreeWidget(self.details_qSplitter)
        self.details_tree_widget.setColumnCount(3)
        self.details_tree_widget.setHeaderLabels(["Parameter", "Value", "Comment"])
        self.details_tree_widget.setColumnWidth(0, 300)
        self.details_tree_widget.setSizePolicy(size_policy)

        self.details_qSplitter.addWidget(self.details_tree_widget)

        #----- Setup analyzed image tab content
        self.analyzed_img_qSplitter = QSplitter()
        self.analyzed_img_qSplitter.setSizePolicy(size_policy)

        #----- Setup leaf profile tab content
        self.leaf_profiles_qSplitter = QSplitter()
        self.leaf_profiles_qSplitter.setSizePolicy(size_policy)

        self.leaf_profiles_frame = QFrame()
        self.leaf_profiles_fl = QFormLayout()
        self.leaf_profiles_frame.setLayout(self.leaf_profiles_fl)
        self.leafs_cb = QComboBox()
        self.leafs_cb.currentIndexChanged.connect(lambda: self.plot_leaf_profile())
        self.pickets_cb = QComboBox()
        self.pickets_cb.currentIndexChanged.connect(lambda: self.plot_leaf_profile())

        self.leaf_profiles_fl.addRow("Picket number:", self.pickets_cb)
        self.leaf_profiles_fl.addRow("Leaf number:", self.leafs_cb)

        self.leaf_profiles_qSplitter.addWidget(self.leaf_profiles_frame)

        self.tab_widget.addTab(self.analyzed_img_qSplitter, "Analyzed Image")
        self.tab_widget.addTab(self.leaf_profiles_qSplitter, "Leaf Profiles")
        self.tab_widget.addTab(self.details_qSplitter, "Details")

        self.top_layout.addWidget(self.tab_widget, 0, 0, 1, 1)

        self.curr_leaf_profile_widget = None
        self.curr_analyzed_image_widget = None

        if pf is not None:
            self.init_details()
            self.init_leaf_profiles()
            self.init_analyzed_image()

        self.initComplete = True
    
    def update_picket_fence(self, pf: QPicketFence):
        self.pf = pf

        self.initComplete = False

        self.init_details()
        self.init_leaf_profiles()
        self.init_analyzed_image()

        self.initComplete = True

    def init_details(self):
        self.details_tree_widget.clear()

        details = [["Gantry angle", f"{self.pf.image.gantry_angle:2.2f}°", ""],
                      ["Collimator angle", f"{self.pf.image.collimator_angle:2.2f}°", ""],
                      ["Number of pickets found", f"{len(self.pf.pickets)}", ""],
                      ["Number of leaf pairs found", f"{int(len(self.pf.mlc_meas) / len(self.pf.pickets))}"]]
        
        if self.pf.separate_leaves:
            leaf_name = self.pf.max_error_leaf[0] + f"-{(int(self.pf.max_error_leaf[1:]) + 1)}"
            details.append(["Maximum error", f"{self.pf.max_error:2.3f} mm " \
                            f"(Picket: {self.pf.max_error_picket + 1}, Leaf: {leaf_name})"])

        else:
            details.append(["Maximum error", f"{self.pf.max_error:2.3f} mm " \
                            f"(Picket: {self.pf.max_error_picket + 1}, Leaf: {self.pf.max_error_leaf + 1})"])

        details.extend([["Percentage of passing leafs", f"{self.pf.percent_passing:2.0f}%", ""],
                       ["Number of failed leafs", f"{len(self.pf.failed_leaves())}", ""],
                       ["", "", ""]])
                               
        self.details_tree_widget.addTopLevelItems([QTreeWidgetItem(detail) for detail in details])
        
        picket_offsets_item = QTreeWidgetItem(["Picket to CAX offset", "", ""])
        picket_offsets_item.setExpanded(True)

        for i in range(len(self.pf.pickets)):
            offset = self.pf.pickets[i].dist2cax
            picket_offsets_item.addChild(QTreeWidgetItem([f"Picket {i + 1}", f"{offset:3.1f} mm", ""]))

        picket_offsets_item.addChildren([QTreeWidgetItem(["", "", ""]),
                                         QTreeWidgetItem(["Mean picket spacing", f"{self.pf.mean_picket_spacing:3.1f} mm", ""])])

        self.details_tree_widget.addTopLevelItem(picket_offsets_item)
    
    def init_leaf_profiles(self):
        self.pickets_cb.clear()
        self.leafs_cb.clear()
        self.pf.init_profile_plot()

        if self.curr_leaf_profile_widget is not None:
            self.curr_leaf_profile_widget.deleteLater()
            self.curr_leaf_profile_widget = self.pf.profile_plot_widget
            self.leaf_profiles_qSplitter.replaceWidget(1,self.curr_leaf_profile_widget)

        else:
            self.curr_leaf_profile_widget = self.pf.profile_plot_widget
            self.leaf_profiles_qSplitter.addWidget(self.curr_leaf_profile_widget)

        self.pickets_cb.addItems([str(x) for x in range(1,self.pf.num_pickets+1)])

        if not self.pf.separate_leaves:
            self.leafs_cb.addItems([str(x) for x in sorted({mlc.leaf_num + 1 for mlc in self.pf.mlc_meas})])
        
        else:
            leaf_items = []
            [leaf_items.extend([f"A{x}", f"B{x}"]) for x in sorted({mlc.leaf_num for mlc in self.pf.mlc_meas})]
            self.leafs_cb.addItems(leaf_items)

        self.plot_leaf_profile(True)
        
    def plot_leaf_profile(self, force_plot: bool = False):
        if self.initComplete or force_plot:
            if not self.pf.separate_leaves:
                self.pf.qplot_leaf_profile(int(self.leafs_cb.currentText())-1,
                                           int(self.pickets_cb.currentText())-1)
                
            else:
                self.pf.qplot_leaf_profile(self.leafs_cb.currentText(),
                                           int(self.pickets_cb.currentText())-1)
            
    def init_analyzed_image(self):
        if self.curr_analyzed_image_widget is not None:
            self.curr_analyzed_image_widget.deleteLater()
            self.curr_analyzed_image_widget = self.pf.analyzed_image_plot_widget
            self.analyzed_img_qSplitter.replaceWidget(0,self.curr_analyzed_image_widget)

        else:
            self.curr_analyzed_image_widget = self.pf.analyzed_image_plot_widget
            self.analyzed_img_qSplitter.addWidget(self.curr_analyzed_image_widget)

        self.pf.qplot_analyzed_image()