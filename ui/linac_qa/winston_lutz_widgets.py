from PySide6.QtWidgets import (QWidget, QListWidgetItem, QMenu, QFileDialog, QDialog, 
                               QFormLayout, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar, 
                               QMessageBox, QSizePolicy, QMainWindow, QGroupBox, 
                               QLineEdit, QComboBox, QDialogButtonBox, QPushButton, QSpacerItem,
                               QCheckBox, QGridLayout, QTabWidget, QSplitter, QTableWidget,
                               QHeaderView, QTableWidgetItem, QPlainTextEdit, QDateEdit)
from PySide6.QtGui import QIcon, QPixmap, QColor, QAction, QTransform
from PySide6.QtCore import Qt, QSize, QEvent, QThread, Signal, QDate

from ui.py_ui import icons_rc
from ui.linac_qa.qa_tools_win import QAToolsWindow
from ui.py_ui.winston_lutz_worksheet_ui import Ui_QWLutzWorksheet
from ui.util_widgets.statusbar import AnalysisInfoLabel
from ui.util_widgets import worksheet_save_report
from ui.util_widgets.dialogs import MessageDialog
from ui.linac_qa.winston_lutz_test_dialog import WLTestDialog

from core.analysis.wlutz import QWinstonLutzWorker, generate_winstonlutz
from core.tools.report import WinstonLutzReport
from core.tools.devices import DeviceManager

from pylinac.core.image_generator import (FilteredFieldLayer,
                                          FilterFreeConeLayer,
                                          FilterFreeFieldLayer,
                                          GaussianFilterLayer,
                                          PerfectConeLayer,
                                          PerfectFieldLayer,
                                          AS500Image,
                                          AS1000Image,
                                          AS1200Image,
                                          generate_winstonlutz_cone)
from pylinac.core.image import LinacDicomImage
from pylinac.metrics.image import (GlobalSizedDiskLocator)

from pathlib import Path
import pyqtgraph as pg
import platform        
import subprocess
import webbrowser
import numpy as np

pg.setConfigOptions(antialias=True, imageAxisOrder='row-major')

class WinstonLutzMainWindow(QAToolsWindow):
    
    def __init__(self, initData: dict = None):
        super().__init__(initData)

        self.tests_counter = 0

        self.window_title = "Winston Lutz ‒ PyBeam QA"
        self.setWindowTitle(self.window_title)

        self.add_new_worksheet()

        self.ui.menuFile.addAction("Add Image(s)", self.ui.tabWidget.currentWidget().add_files)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction("Add New Worksheet", self.add_new_worksheet)
        self.ui.menuTools.addAction("Benchmark Test", self.init_test_dialog, "Ctrl+T")
        self.ui.menubar.setEnabled(True)

    def add_new_worksheet(self, worksheet_name: str = None, enable_icon: bool = True):
        if worksheet_name is None:
            self.untitled_counter = self.untitled_counter + 1
            worksheet_name = f"Winston Lutz (Untitled-{self.untitled_counter})"

        return super().add_new_worksheet(QWLutzWorksheet(), worksheet_name, enable_icon)

    def init_test_dialog(self):
        dialog = WLTestDialog()
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            self.tests_counter = self.tests_counter + 1

            field_layer = dialog.ui.field_layer_cb.currentText()

            # Set the field layer
            if field_layer == "Filtered field":
                field_layer = FilteredFieldLayer

            elif field_layer == "Filter free field":
                field_layer = FilterFreeFieldLayer

            elif field_layer == "Perfect field":
                field_layer = PerfectFieldLayer

            elif field_layer == "Filter free cone":
                field_layer = FilterFreeConeLayer

            else: field_layer = PerfectConeLayer

            # Set the simulation image
            sim_image = dialog.ui.sim_image_cb.currentText()
            
            if sim_image == "AS500":
                sim_image = AS500Image()
            
            elif sim_image == "AS1000":
                sim_image = AS1000Image()
            
            else: sim_image = AS1200Image()

            # Get the field size
            if dialog.ui.field_type_cb.currentText() == "Rectangle":
                field_size = (dialog.ui.rec_field_width_dsb.value(),
                              dialog.ui.rec_field_height_dsb.value())
                
                images = generate_winstonlutz(
                    simulator = sim_image,
                    field_layer = field_layer,
                    dir_out = dialog.ui.out_dir_le.text(),
                    field_size_mm = field_size,
                    final_layers = [GaussianFilterLayer()],
                    bb_size_mm = dialog.ui.bb_size_dsb.value(),
                    offset_mm_left = dialog.ui.left_offset_dsb.value(),
                    offset_mm_up = dialog.ui.up_offset_dsb.value(),
                    offset_mm_in = dialog.ui.in_offset_dsb.value(),
                    image_axes = dialog.image_axes,
                    gantry_tilt = dialog.ui.gantry_tilt_dsb.value(),
                    gantry_sag = dialog.ui.gantry_sag_dsb.value(),
                    clean_dir = False
                )

            else:
                field_size = dialog.ui.cone_field_size_dsb.value()

                images = generate_winstonlutz_cone(
                    simulator = sim_image,
                    cone_layer = field_layer,
                    dir_out = dialog.ui.out_dir_le.text(),
                    cone_size_mm = field_size,
                    final_layers = [GaussianFilterLayer()],
                    bb_size_mm = dialog.ui.bb_size_dsb.value(),
                    offset_mm_left = dialog.ui.left_offset_dsb.value(),
                    offset_mm_up = dialog.ui.up_offset_dsb.value(),
                    offset_mm_in = dialog.ui.in_offset_dsb.value(),
                    image_axes = dialog.image_axes,
                    gantry_tilt = dialog.ui.gantry_tilt_dsb.value(),
                    gantry_sag = dialog.ui.gantry_sag_dsb.value(),
                    clean_dir = False
                )

            images = [dialog.ui.out_dir_le.text() + "/" + image for image in images]

            self.add_new_worksheet(dialog.ui.test_name_le.text() + " (Test)")
            self.ui.tabWidget.currentWidget().add_files(images)

class QWLutzWorksheet(QWidget):

    analysis_info_signal = Signal(dict)

    COORD_SYS = ["IEC 61217", "Varian IEC", "Varian Standard"]

    ANALYSIS_METRICS = {
            "num_gantry_images": "Number of gantry images",
            "num_gantry_coll_images": "Number of gantry + collimator images",
            "num_coll_images": "Number of collimator images",
            "num_couch_images": "Number of couch images",
            "num_total_images": "Total number of images",
            "max_2d_cax_to_bb_mm": "Maximum 2D distance (CAX to BB)",
            "median_2d_cax_to_bb_mm": "Median 2D distance (CAX to BB)",
            "mean_2d_cax_to_bb_mm": "Mean 2D distance (CAX to BB)",
            "max_2d_cax_to_epid_mm": "Maximum 2D distance (CAX to EPID)",
            "median_2d_cax_to_epid_mm": "Median 2D distance (CAX to EPID)",
            "mean_2d_cax_to_epid_mm": "Mean 2D distance (CAX to EPID)",
            "gantry_3d_iso_diameter_mm": "Gantry 3D isocenter diameter",
            "max_gantry_rms_deviation_mm": "Maximum gantry RMS deviation",
            "max_epid_rms_deviation_mm": "Maximum EPID RMS deviation",
            "gantry_coll_3d_iso_diameter_mm": "Gantry + Collimator 3D isocenter diameter",
            "coll_2d_iso_diameter_mm": "Collimator 2D isocenter diameter",
            "max_coll_rms_deviation_mm": "Maximum collimator RMS deviation",
            "couch_2d_iso_diameter_mm": "Couch 2D isocenter diameter",
            "max_couch_rms_deviation_mm": "Maximum couch RMS deviation"
        }

    def __init__(self):
        super().__init__()
        self.ui = Ui_QWLutzWorksheet()
        self.ui.setupUi(self)

        self.image_icon = QIcon()
        self.image_icon.addFile(u":/colorIcons/icons/picture.png", QSize(), QIcon.Normal, QIcon.Off)

        self.form_layout = QFormLayout()
        self.form_layout.setHorizontalSpacing(40)
        self.ui.analysisInfoVL.addLayout(self.form_layout)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.shiftInfoBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.ui.advancedViewBtn.setEnabled(False)
        self.ui.coordSysCB.setEnabled(False)
        self.ui.coordSysCB.addItems(self.COORD_SYS)

        # setup context menu for image list widget
        self.img_list_contextmenu = QMenu()
        self.img_list_contextmenu.addAction("View Original Image", self.view_dicom_image, "Ctrl+I")
        self.view_analyzed_img_action = self.img_list_contextmenu.addAction("View Analyzed Image", self.view_analyzed_image, "Ctrl+Shift+I")
        self.view_analyzed_img_action.setEnabled(False)
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

        #Add widgets
        self.progress_vl = QVBoxLayout()
        self.progress_vl.setSpacing(10)

        self.analysis_progress_bar = QProgressBar()
        self.analysis_progress_bar.setRange(0,0)
        self.analysis_progress_bar.setTextVisible(False)
        self.analysis_progress_bar.setMaximumSize(300, 10)
        self.analysis_progress_bar.setMinimumSize(300, 10)
        self.analysis_progress_bar.hide()

        self.analysis_message_label = QLabel()
        self.analysis_message_label.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred))
        self.analysis_message_label.hide()

        self.progress_vl.addWidget(self.analysis_progress_bar, 0, Qt.AlignHCenter)
        self.progress_vl.addWidget(self.analysis_message_label, 0, Qt.AlignHCenter)

        self.ui.analysisInfoVL.addLayout(self.progress_vl)

        # connect slots
        self.ui.addImgBtn.clicked.connect(self.add_files)
        self.ui.importImgBtn.clicked.connect(self.add_files)
        self.ui.analyzeBtn.clicked.connect(self.start_analysis)
        self.ui.shiftInfoBtn.clicked.connect(self.show_shift_info)
        self.ui.advancedViewBtn.clicked.connect(self.show_advanced_results_view)
        self.ui.genReportBtn.clicked.connect(self.generate_report)
        self.ui.imageListWidget.itemChanged.connect(self.update_marked_images)
        self.ui.toleranceDSB.valueChanged.connect(self.set_analysis_outcome)
        self.ui.toleranceDSB.valueChanged.connect(lambda: self.show_advanced_results_view(True))

        self.marked_images = []
        self.imageView_windows = []
        self.analysis_in_progress = False
        self.maxLocError = None
        self.current_results = None
        self.advanced_results_view = None

        self.analysis_summary = {}
        self.set_analysis_outcome()

        # Set analysis state and message for status bar
        self.analysis_message = None
        self.analysis_state = AnalysisInfoLabel.IDLE

        # Set initial session save info
        self.report_author = ""
        self.report_institution = ""
        self.report_date = QDate.currentDate()
        self.save_path = ""
        self.save_comment = ""

    def add_files(self, files: tuple | list | None = None):
        if not files:
            files, _ = QFileDialog.getOpenFileNames(
                self,
                "Select DICOM WL Images",
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
            
            if self.ui.stackedWidget.currentIndex() == 0:
                self.ui.stackedWidget.setCurrentIndex(1)

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
    
    def update_marked_images(self):
        self.marked_images.clear()

        for index in range(self.ui.imageListWidget.count()):
            if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                self.marked_images.append(self.ui.imageListWidget.item(index).data(Qt.UserRole)["file_path"])
        
        if len(self.marked_images) > 1:
            self.ui.analyzeBtn.setText(f"Analyze {len(self.marked_images)} images")
            self.ui.analyzeBtn.setEnabled(True)

        else:
            self.ui.analyzeBtn.setText(f"Analyze images")
            self.ui.analyzeBtn.setEnabled(False)

    def on_analysis_failed(self, error_message: str = "Unknown Error"):
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

        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle("Analysis Error")
        self.error_dialog.setText("<p><span style=\" font-weight:700; font-size: 12pt;\">" \
                                  "Oops! An error was encountered</span></p>")
        self.error_dialog.setInformativeText(error_message)
        self.error_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.error_dialog.setTextFormat(Qt.TextFormat.RichText)

        error_icon = QPixmap(u":/colorIcons/icons/error_round.png")
        error_icon = error_icon.scaled(QSize(48, 48), mode = Qt.TransformationMode.SmoothTransformation)
        self.error_dialog.setIconPixmap(error_icon)

        self.error_dialog.exec()
    
    def start_analysis(self):
        self.analysis_info_signal.emit({"state": AnalysisInfoLabel.IN_PROGRESS,
                                        "message": None})
        self.analysis_state =  AnalysisInfoLabel.IN_PROGRESS
        self.analysis_message = None
        self.analysis_in_progress = True
        self.remove_list_checkmarks()

        self.analysis_progress_bar.show()
        self.analysis_message_label.show()

        row_count = self.form_layout.rowCount()
        for i in range(row_count):
            self.form_layout.removeRow(row_count - (i+1))

        self.ui.addImgBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.ui.advancedViewBtn.setEnabled(False)
        self.ui.shiftInfoBtn.setEnabled(False)
        self.ui.analyzeBtn.setEnabled(False)
        self.ui.analyzeBtn.setText("Analysis in progress...")

        self.worker = QWinstonLutzWorker(self.marked_images,
                                         self.ui.bb_size_dsb.value(),
                                         self.ui.useFilenameSCheckBox.isChecked())
    
        self.qthread = QThread()
        self.worker.moveToThread(self.qthread)
        self.worker.analysis_failed.connect(self.qthread.quit)
        self.worker.analysis_failed.connect(self.on_analysis_failed)
        self.worker.images_analyzed.connect(self.analysis_progress_bar.setValue)
        self.worker.images_analyzed.connect(lambda counter: self.analysis_message_label.setText(
            f"Analyzing images ({counter} of {len(self.marked_images)} complete)"))
        self.worker.analysis_results_changed.connect(self.show_analysis_results)
        self.worker.bb_shift_info_changed.connect(self.update_bb_shift)
        self.worker.thread_finished.connect(self.qthread.quit)
        self.worker.thread_finished.connect(self.worker.deleteLater)
        self.qthread.started.connect(self.worker.analyze)
        self.qthread.finished.connect(self.qthread.deleteLater)

        self.analysis_progress_bar.setRange(0, len(self.marked_images))
        self.analysis_progress_bar.setValue(0)
        self.analysis_message_label.setText("Starting analysis...")

        self.qthread.start()

    def show_analysis_results(self, results: dict):
        self.current_results = results
        self.analysis_in_progress = False
        self.restore_list_checkmarks()
        self.analysis_summary = {}
        self.maxLocError = results["max_2d_cax_to_bb_mm"]

        # Update status bar message
        self.analysis_info_signal.emit({"state": AnalysisInfoLabel.COMPLETE,
                                        "message": None})
        self.analysis_state =  AnalysisInfoLabel.COMPLETE
        self.analysis_message = None

        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        # Analyze button is auto-enabled by update_marked_images() on item data change
        self.ui.addImgBtn.setEnabled(True)
        self.ui.genReportBtn.setEnabled(True)
        self.ui.advancedViewBtn.setEnabled(True)
        self.ui.shiftInfoBtn.setEnabled(True)

        for index in range(self.ui.imageListWidget.count()):
            listItemWidget = self.ui.imageListWidget.item(index)
            item_data = listItemWidget.data(Qt.UserRole)

            for image_details in results["image_details"]:
                if item_data["file_path"] == image_details["file_path"]:
                    item_data["analysis_data"] = image_details
                    break
                else:
                    item_data["analysis_data"] = None

            listItemWidget.setData(Qt.UserRole, item_data)

        for key in self.ANALYSIS_METRICS:
            param = self.ANALYSIS_METRICS[key]
            if "_mm" in key:
                value = f"{float(results[key]):2.2f} mm"
                self.form_layout.addRow(f"{param}:", QLabel(value))
                self.analysis_summary[param] = value
            else:
                self.form_layout.addRow(f"{param}:", QLabel(str(results[key])))

        self.show_advanced_results_view(True)
        self.set_analysis_outcome()

    def show_advanced_results_view(self, only_update: bool = False):
        if self.current_results is not None:
            if self.advanced_results_view is None:
                self.advanced_results_view = AdvancedWLView(results = self.current_results["image_details"],
                                                            tolerance = self.ui.toleranceDSB.value())
                if not only_update:
                    self.advanced_results_view.showMaximized()

            else:
                self.advanced_results_view.update_analysis_data(self.current_results["image_details"],
                                                                self.ui.toleranceDSB.value())

                if not only_update: 
                    self.advanced_results_view.show()

    def set_analysis_outcome(self):
        if self.maxLocError is None:
            self.ui.outcomeLE.setStyleSheet(u"border-color: rgba(0, 0, 0,0);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(0, 0, 0, 0);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
            
        elif self.maxLocError < self.ui.toleranceDSB.value():
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

    def update_bb_shift(self, bb_shift_info: str):
        self.shift_info = bb_shift_info
        self.ui.shiftInfoBtn.setEnabled(True)

    def view_dicom_image(self):
        if len(self.ui.imageListWidget.selectedItems()) > 0:
            image_short_name = self.ui.imageListWidget.currentItem().text()
            image_path = self.ui.imageListWidget.selectedItems()[0].data(Qt.UserRole)["file_path"]
            image = LinacDicomImage(image_path)

            imgView = pg.ImageView()
            imgView.setImage(image.array)
            imgView.setPredefinedGradient("grey")

            new_win = QMainWindow(self)
            new_win.setWindowTitle(image_short_name)
            new_win.setCentralWidget(imgView)
            new_win.setMinimumSize(600, 500)
            new_win.show()

    def view_analyzed_image(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()
        analysed_image_viewer = AnalysedImageViewer(list_item=listWidgetItem, 
                                                    tolerance=self.ui.toleranceDSB.value(),
                                                    parent=self)

        analysed_image_viewer.show()

    def show_shift_info(self):
        self.shift_dialog = MessageDialog()
        self.shift_dialog.set_title("BB Shift Instructions")
        self.shift_dialog.set_header_text("To minimize the mean positioning error, shift the ball-bearing as follows:")
        self.shift_dialog.set_standard_buttons(QDialogButtonBox.StandardButton.Ok)

        shifts = self.shift_info.split("; ")
        self.shift_dialog.set_info_text(f'{shifts[0].split(" ")[0]}: {shifts[0].split(" ")[1].replace("mm", " mm")}\n' 
                                        f'{shifts[1].split(" ")[0]}: {shifts[1].split(" ")[1].replace("mm", " mm")}\n' \
                                        f'{shifts[2].split(" ")[0]}: {shifts[2].split(" ")[1].replace("mm", " mm")}')

        shift_icon = QPixmap(u":/colorIcons/icons/bb_shift.png")
        self.shift_dialog.set_icon(shift_icon)

        self.shift_dialog.exec()

    def delete_file(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()

        self.delete_dialog = MessageDialog()
        self.delete_dialog.set_title("Delete File")
        self.delete_dialog.set_icon(MessageDialog.WARNING_ICON)
        self.delete_dialog.set_header_text(f"Are you sure you want to permanently delete {listWidgetItem.text()}?")
        self.delete_dialog.set_info_text("This action is irreversible!")
        self.delete_dialog.set_standard_buttons(QDialogButtonBox.StandardButton.Yes | 
                                             QDialogButtonBox.StandardButton.Cancel)

        ret = self.delete_dialog.exec()

        if ret == QDialogButtonBox.StandardButton.Yes:
            path = Path(listWidgetItem.data(Qt.UserRole)["file_path"])
            path.unlink(missing_ok=True)
            self.ui.imageListWidget.takeItem(self.ui.imageListWidget.currentRow())
            del listWidgetItem

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
        
        patient_name_le = QLineEdit()
        patient_id_le = QLineEdit()
        patient_name_le.setMaximumWidth(250)
        patient_name_le.setMinimumWidth(250)
        patient_id_le.setMaximumWidth(250)
        patient_id_le.setMinimumWidth(250)
        
        self.patient_info_toggled = False
        patient_info_group = QGroupBox("Patient Information")
        patient_info_group.hide()
        patient_info_layout = QFormLayout()
        patient_info_layout.addRow("Patient name:", patient_name_le)
        patient_info_layout.addRow("Patient id:", patient_id_le)
        patient_info_group.setLayout(patient_info_layout)

        layout = QVBoxLayout()
        layout.addLayout(user_details_layout)
        layout.addWidget(patient_info_group)

        dialog_buttons = QDialogButtonBox()
        save_button = dialog_buttons.addButton(QDialogButtonBox.StandardButton(
            QDialogButtonBox.StandardButton.Save), )
        save_button.setEnabled(False)
        cancel_button = dialog_buttons.addButton(QDialogButtonBox.StandardButton(
            QDialogButtonBox.StandardButton.Cancel))
        patient_info_button = dialog_buttons.addButton("Add Patient Info", 
                                QDialogButtonBox.ButtonRole.ActionRole)
        
        # enable the save button once we have a path to save the report to
        save_path_le.textChanged.connect(lambda: save_button.setEnabled(True))
        
        layout.addWidget(dialog_buttons)

        report_dialog = QDialog()
        report_dialog.setWindowTitle("Generate WL Report ‒ PyBeam QA")
        report_dialog.setLayout(layout)
        report_dialog.setMinimumSize(report_dialog.sizeHint())
        report_dialog.setMaximumSize(report_dialog.sizeHint())

        patient_info_button.clicked.connect(lambda: self.toggle_patient_info(
            patient_info_button, patient_info_group, report_dialog))
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

            if self.patient_info_toggled:
                patient_info = {"patient_name": patient_name_le.text(),
                                "patient_id": patient_id_le.text()}
            else:
                patient_info = None

            report = WinstonLutzReport(save_path_le.text(),
                                   author = physicist_name,
                                   institution = institution_name,
                                   treatment_unit_name = treatment_unit,
                                   analysis_date = self.report_date.toString("dd MMMM yyyy"),
                                   summary_plot = self.current_results["summary_plot"],
                                   analysis_summary = self.analysis_summary,
                                   report_status = self.ui.outcomeLE.text(),
                                   patient_info = patient_info,
                                   tolerance = self.ui.toleranceDSB.value(),
                                   comments = comments_te.toPlainText()
                                   )
        
            report.save_report()

            if show_report_checkbox.isChecked():
                webbrowser.open(save_path_le.text())

    def toggle_patient_info(self, button: QPushButton, layout_group: QGroupBox, dialog: QDialog):
        if self.patient_info_toggled:
            button.setText("Add Patient Info")
            layout_group.hide()
            self.patient_info_toggled = False
            dialog.setMinimumSize(dialog.sizeHint())
            dialog.setMaximumSize(dialog.sizeHint())

        else:
            button.setText("Remove Patient Info")
            layout_group.show()
            self.patient_info_toggled = True
            dialog.setMinimumSize(dialog.sizeHint())
            dialog.setMaximumSize(dialog.sizeHint())

class AdvancedWLView(QMainWindow):

    def __init__(self, parent: QWidget | None = None,
                 results: list | None = None,
                 tolerance: float = 1.00) -> None:
        super().__init__(parent)

        self.initComplete = False

        self.setWindowTitle("Winston Lutz Analysis (Advanced Results) ‒ PyBeam QA")
        self.resize(720, 480)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.top_layout = QGridLayout(self.central_widget)
        self.top_layout.setContentsMargins(0, 0, 0, 0)

        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setTabsClosable(False)

        size_policy = QSizePolicy(QSizePolicy.Expanding,
                                  QSizePolicy.Expanding)
        size_policy.setVerticalStretch(0)
        size_policy.setHorizontalStretch(0)
        self.central_widget.setSizePolicy(size_policy)
        self.tab_widget.setSizePolicy(size_policy)

        #----- Setup table content
        self.analyzed_img_qSplitter = QSplitter()
        self.analyzed_img_qSplitter.setSizePolicy(size_policy)

        self.tab_widget.addTab(self.analyzed_img_qSplitter, "Advanced analysis data")

        self.top_layout.addWidget(self.tab_widget, 0, 0, 1, 1)

        self.table_widget = QTableWidget(self.analyzed_img_qSplitter)
        size_policy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                                  QSizePolicy.Policy.MinimumExpanding)
        self.table_widget.setSizePolicy(size_policy)

        self.update_analysis_data(results, tolerance)
        
    def update_analysis_data(self, results: list, tolerance: float):
        self.table_widget.clear()

        # Disable sorting before data population to avoid weird behaviour when sorting later
        self.table_widget.setSortingEnabled(False)

        headers = ["Filename", "Gantry angle (°)", "Collimator angle (°)",
                   "Couch angle (°)", "CAX to EPID distance (mm)", "𝚫u (mm)",
                   "𝚫v (mm)", "CAX to BB distance (mm)", "Outcome (Pass/Fail)"]
        
        self.table_widget.setColumnCount(len(headers))
        self.table_widget.setRowCount(len(results))
        self.table_widget.setHorizontalHeaderLabels(headers)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)

        for row, result in enumerate(results):

            filename_item = QTableWidgetItem(result["filename"])
            gantry_angle_item = QTableWidgetItem(result["gantry_angle"])
            coll_angle_item = QTableWidgetItem(result["collimator_angle"])
            couch_angle_item = QTableWidgetItem(result["couch_angle"])
            cax_2_epid_item = QTableWidgetItem(f"{result['cax_to_epid_dist']:2.2f}")
            delta_u_item = QTableWidgetItem(result["delta_u"])
            delta_v_item = QTableWidgetItem(result["delta_v"])
            cax_2_bb_item = QTableWidgetItem(f"{result['cax_to_bb_dist']:2.2f}")

            if result["cax_to_bb_dist"] < tolerance:
                outcome_item = QTableWidgetItem("PASS")
                outcome_item.setBackground(QColor(95, 200, 26))

            else:
                outcome_item = QTableWidgetItem("FAIL")
                outcome_item.setBackground(QColor(231, 29, 14))

            filename_item.setFlags(filename_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            gantry_angle_item.setFlags(gantry_angle_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            coll_angle_item.setFlags(coll_angle_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            couch_angle_item.setFlags(couch_angle_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            cax_2_epid_item.setFlags(cax_2_epid_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            delta_u_item.setFlags(delta_u_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            delta_v_item.setFlags(delta_v_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            cax_2_bb_item.setFlags(cax_2_bb_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            outcome_item.setFlags(outcome_item.flags() ^ Qt.ItemFlag.ItemIsEditable)

            gantry_angle_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            coll_angle_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            couch_angle_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            cax_2_epid_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            delta_u_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            delta_v_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            cax_2_bb_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            outcome_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.table_widget.setItem(row, 0, filename_item)
            self.table_widget.setItem(row, 1, gantry_angle_item)
            self.table_widget.setItem(row, 2, coll_angle_item)
            self.table_widget.setItem(row, 3, couch_angle_item)
            self.table_widget.setItem(row, 4, cax_2_epid_item)
            self.table_widget.setItem(row, 5, delta_u_item)
            self.table_widget.setItem(row, 6, delta_v_item)
            self.table_widget.setItem(row, 7, cax_2_bb_item)
            self.table_widget.setItem(row, 8, outcome_item)
    
        self.table_widget.setSortingEnabled(True)

class AnalysedImageViewer(QMainWindow):

    def __init__(self, list_item: QListWidgetItem,
                 tolerance: float = 1.0,
                 parent: QWidget = None) -> None:
        super().__init__(parent)

        self.setWindowTitle(list_item.text() + " (Analyzed Image)")

        self.list_item = list_item
        self.tolerance = tolerance

        # plot config values
        self.show_analysis_info = True
        self.show_epid_coord_sys = True
        self.use_mm_units = False

        # Initialise the plot item
        central_win = QWidget()
        #central_win.setStyleSheet('background-color: black')
        self.main_layout = QGridLayout()
        self.main_layout.setHorizontalSpacing(50)
        self.plot_widget = pg.PlotWidget()
        self.plot_info = QLabel()
        self.plot_info.setTextFormat(Qt.TextFormat.RichText)
        self.plot_item = self.plot_widget.getPlotItem()
        self.plot_item.setAspectLocked(True)

        self.main_layout.addWidget(self.plot_info, 0, 0)
        self.main_layout.addWidget(self.plot_widget, 0, 1)

        # Modify plot context menu
        context_menu = self.plot_item.getViewBox().menu
        context_menu.addSeparator()

        self.show_analysis_summary = QAction("Show analysis summary")
        self.show_analysis_summary.setEnabled(True)
        self.show_analysis_summary.setCheckable(True)
        self.show_analysis_summary.triggered.connect(self.toggleAnalysisInfo)
        context_menu.addAction(self.show_analysis_summary)

        self.show_epid_coords_action = QAction("Show EPID coordinate system")
        self.show_epid_coords_action.setEnabled(False)
        self.show_epid_coords_action.setCheckable(True)
        context_menu.addAction(self.show_epid_coords_action)

        self.chg_axes_units = context_menu.addAction("Change axes units to mm or pixels")
        self.chg_axes_units.triggered.connect(lambda: 
                                    self.set_axes_units(not self.use_mm_units))

        central_win.setLayout(self.main_layout)
        self.setCentralWidget(central_win)
        self.setStyleSheet('background-color: black')
        self.setMinimumSize(600, 500)
        
        self.setPlotInfo()
        # draw the plot
        self.draw_plots()

    def setPlotInfo(self):
        image_data = self.list_item.data(Qt.UserRole)["analysis_data"]

        if image_data["cax_to_bb_dist"] < self.tolerance:
            color = "green"
            status = "Pass"
        else:
            color = "red"
            status = "Fail"

        # Set plot info
        self.plot_info.setText(f"<p><b>Outcome:<span style='color:{color}'> {status}</span></b></p>"\
                                "<span style='white-space: pre-line'></span>" \
                                f"<p><b>Gantry ∡:</b> {image_data['gantry_angle']}°</p>" \
                                f"<p><b>Collimator ∡:</b> {image_data['collimator_angle']}°</p>" \
                                f"<p><b>Couch ∡:</b> {image_data['couch_angle']}°</p>" \
                                "<span style='white-space: pre-line'></span>" \
                                f"<p><b>Field CAX to EPID CAX:</b> {image_data['cax_to_epid_dist']:3.2f} mm</p>"\
                                f"<p><b>Field CAX to BB CAX:</b> {image_data['cax_to_bb_dist']:3.2f} mm</p>"\
                                f"<p><b>𝚫u:</b> {image_data['delta_u']} mm</p>" \
                                f"<p><b>𝚫v:</b> {image_data['delta_v']} mm</p>"
                                )

    def draw_plots(self):
        self.plot_item.clear()

        image_path = self.list_item.data(Qt.UserRole)["file_path"]
        image_data = self.list_item.data(Qt.UserRole)["analysis_data"]
        image = LinacDicomImage(image_path)

        self.image_dim = image.array.shape
        self.mm_per_dot = 1/image.dpmm

        image_item = pg.ImageItem(image=image.array)

        self.plot_item.setLabel('left', '<b>Y (px)</b>') # in pixels
        self.plot_item.setLabel('bottom', '<b>X (px)</b>')
        plot_legend = self.plot_item.addLegend(size = (50,50), offset=(30,20), 
                                               labelTextColor=(255,255,255),
                                               brush=pg.mkBrush((27, 38, 59, 200)))

        bbX = image_data["bb_location"]["x"]
        bbY = image_data["bb_location"]["y"]
        caxX = image_data["field_cax"]["x"]
        caxY = image_data["field_cax"]["y"]
        epidX = image_data["epid"]["x"]
        epidY = image_data["epid"]["y"]

        bb_plotItem = pg.ScatterPlotItem()
        cax_plotItem = pg.ScatterPlotItem()
        bb_plotItem.addPoints(pos=[(bbX, bbY)], pen=None, size=10, brush=(255,0,0,255), name="BB center")
        cax_plotItem.addPoints(pos=[(caxX, caxY)], pen=None, size=10, brush=(255,165,0,255),
                                symbol="s", name="Field CAX")
        
        epidX_plot = pg.InfiniteLine(pos=[epidX,0],movable=False, angle=90, pen = (0,255,0), name="EPID-x line",
                                        label="EPID x = {value:3.2f}", labelOpts={'position': 0.1,
                                        'color': (255,255,255), 'fill': (0,200,0,200), 'movable': True})
        setattr(epidX_plot, 'id', "EPID-x line")
        
        epidY_plot = pg.InfiniteLine(pos=[0,epidY], movable=False, angle=0, pen = (0,255,0), name="EPID-y line", 
                                         label="EPID y = {value:3.2f}", labelOpts={'position': 0.1, 
                                        'color': (255,255,255), 'fill': (0,200,0,200), 'movable': True})
        setattr(epidY_plot, 'id', "EPID-y line")

        plot_legend.addItem(epidX_plot, "EPID-x line")
        plot_legend.addItem(epidY_plot, "EPID-y line")
        
        epidX_plot.opts = {"pen": epidX_plot.pen}
        epidY_plot.opts = {"pen": epidY_plot.pen}
        
        self.plot_item.addItem(image_item)
        self.plot_item.addColorBar(image_item, colorMap=pg.colormap.getFromMatplotlib('gray'))
        self.plot_item.addItem(bb_plotItem)
        self.plot_item.addItem(cax_plotItem)
        self.plot_item.addItem(epidX_plot)
        self.plot_item.addItem(epidY_plot)
        self.plot_item.autoRange()
        self.set_axis_ranges()

    def set_axis_ranges(self):
        if self.use_mm_units:
            xMin = -self.mm_per_dot * (0.5*self.image_dim[1]+150)
            xMax = self.mm_per_dot * (0.5*self.image_dim[1]+150)
            yMin = -self.mm_per_dot * (0.5*self.image_dim[0]+150)
            yMax = self.mm_per_dot * (0.5*self.image_dim[0]+150)
            xRange = (xMin + 50 * self.mm_per_dot, xMax - 50 * self.mm_per_dot)
            yRange = (yMin + 50 * self.mm_per_dot, yMax - 50 * self.mm_per_dot)

        else:
            xMin, yMin = -150, -150
            xMax, yMax= self.image_dim[1]+150, self.image_dim[0]+150
            xRange = (xMin + 50, xMax - 50)
            yRange = (yMin + 50, yMax - 50)

        self.plot_item.setRange(xRange=xRange, yRange=yRange)
        self.plot_item.setLimits(xMin=xMin, xMax=xMax, yMin=yMin, yMax=yMax)
        self.plot_item.autoRange()

    def set_axes_units(self, use_mm_units: bool):
        image_data = self.list_item.data(Qt.UserRole)["analysis_data"]

        if use_mm_units:
            transform = QTransform() # The transformation to use
            transform.scale(self.mm_per_dot, self.mm_per_dot)
            transform.translate(-0.5*self.image_dim[1], -0.5*self.image_dim[0])

            for item in self.plot_item.items:
                if hasattr(item, "id"):
                    if item.id == "EPID-x line":
                        item.setPos([0,0])

                    elif item.id == "EPID-y line":
                        item.setPos([0,0])
                else:
                    item.setTransform(transform)

            self.plot_item.setLabel('left', '<b>EPID Y offset, v  (mm)</b>')
            self.plot_item.setLabel('bottom', '<b>EPID X offset, u (mm)</b>')
        else:
            for item in self.plot_item.items:
                if hasattr(item, "id"):
                    if item.id == "EPID-x line":
                        item.setPos(image_data["epid"]["x"])

                    elif item.id == "EPID-y line":
                        item.setPos(image_data["epid"]["y"])
                
                else:
                    item.resetTransform()

            self.plot_item.setLabel('left', '<b>Y (px)</b>')
            self.plot_item.setLabel('bottom', '<b>X (px)</b>')

        self.use_mm_units = use_mm_units
        self.set_axis_ranges()

    def toggleAnalysisInfo(self): 
        if self.show_analysis_info:
            self.show_analysis_info = False
            self.plot_info.hide()
        else:
            self.show_analysis_info = True
            self.plot_info.show()

        self.show_analysis_summary.setChecked(self.show_analysis_info)
        
