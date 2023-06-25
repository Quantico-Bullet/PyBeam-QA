from PySide6.QtWidgets import (QWidget, QLabel, QProgressBar, QVBoxLayout, QFileDialog,
                               QListWidgetItem, QMenu, QSizePolicy, QMessageBox, 
                               QMainWindow, QFormLayout, QTabWidget, QFrame, QGridLayout,
                               QTableWidget, QSplitter, QTreeWidgetItem, QTreeWidget, QComboBox)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QEvent, QThread

from ui.py_ui import icons_rc
from ui.py_ui.picketFenceWorksheet_ui import Ui_QPicketFenceWorksheet
from core.analysis.picket_fence import QPicketFence, QPicketFenceWorker

import platform
import subprocess
import pyqtgraph as pg
from pathlib import Path
from pylinac.core.image import LinacDicomImage
from pylinac.picketfence import PicketFence, MLC

class QPicketFenceWorksheet(QWidget):

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
        self.ui.mlcTypeCB.addItems([mlc.value["name"] for mlc in MLC])

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
        self.ui.advancedViewBtn.clicked.connect(self.show_advanced_results_view)
        self.ui.imageListWidget.itemChanged.connect(self.update_marked_images)

        #-------- init defaults --------
        self.marked_images = []
        self.current_results = None
        self.imageView_windows = []
        self.advanced_results_view = None
        self.analysis_in_progress = False
        self.max_picket_error = None

        self.update_marked_images()
        self.set_analysis_outcome()
    
    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select DICOM Picket Fence Images",
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

        warning_icon = QPixmap(u":/colorIcons/icons/warning_48.png")
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

    def start_analysis(self):
        self.analysis_in_progress = True
        self.ui.advancedViewBtn.setEnabled(False)
        self.remove_list_checkmarks()

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

        if len(self.marked_images) < 2:
            qpf = QPicketFence(filename = self.marked_images[0],
                               use_filename = self.ui.useFilenameSCheckB.isChecked(),
                               mlc = self.ui.mlcTypeCB.currentText(),
                               crop_mm = self.ui.cropSB.value(),
                               tolerance = self.ui.toleranceDSB.value())
            
        else:
            qpf = QPicketFence(filename = self.marked_images,
                               use_filename = self.ui.useFilenameSCheckB.isChecked(),
                               mlc = self.ui.mlcTypeCB.currentText(),
                               crop_mm = self.ui.cropSB.value(),
                               tolerance = self.ui.toleranceDSB.value())
        
        self.analysis_worker = QPicketFenceWorker(qpf)

        self.qthread = QThread()
        self.analysis_worker.moveToThread(self.qthread)
        self.analysis_worker.thread_finished.connect(self.qthread.quit)
        self.analysis_worker.analysis_results_ready.connect(lambda results: self.show_analysis_results(results))
        self.qthread.started.connect(self.analysis_worker.analyze)
        self.qthread.finished.connect(self.qthread.deleteLater)

        self.qthread.start()

    def show_analysis_results(self, results: dict):
        self.current_results = results
        self.analysis_in_progress = False
        self.ui.advancedViewBtn.setEnabled(True)
        self.restore_list_checkmarks()

        # Analyze button is auto-enabled by update_marked_images() on item data change
        self.ui.analyzeBtn.setText(f"Analyze images")
        self.ui.addImgBtn.setEnabled(True)
        self.ui.genReportBtn.setEnabled(True)
    
        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        for summary_item in results["summary_text"]:
            self.form_layout.addRow(summary_item[0], QLabel(summary_item[1]))

        # Update the advanced view
        if self.advanced_results_view is not None:
            self.advanced_results_view.update_picket_fence(self.current_results["picket_fence_obj"])

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
            self.advanced_results_view.show()

        else: 
            self.advanced_results_view.show()
    
    def set_analysis_outcome(self):
        if self.max_picket_error is None:
            self.ui.outcomeLE.setStyleSheet(u"border-color: rgba(0, 0, 0,0);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(0, 0, 0, 0);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
            
        elif self.max_picket_error < self.ui.toleranceDSB.value():
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

        size_policy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        size_policy.setVerticalStretch(0)
        size_policy.setHorizontalStretch(0)
        self.central_widget.setSizePolicy(size_policy)
        self.tab_widget.setSizePolicy(size_policy)

        #-----  Setup stats tab content
        self.stats_qSplitter = QSplitter()
        self.stats_qSplitter.setContentsMargins(0, 10, 0, 0)
        self.stats_qSplitter.setSizePolicy(size_policy)

        self.stats_tree_widget = QTreeWidget(self.stats_qSplitter)
        self.stats_tree_widget.setColumnCount(3)
        self.stats_tree_widget.setHeaderLabels(["Parameter", "Value", "Comment"])
        self.stats_tree_widget.setColumnWidth(0, 300)
        self.stats_tree_widget.setSizePolicy(size_policy)

        self.stats_qSplitter.addWidget(self.stats_tree_widget)

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
        self.tab_widget.addTab(self.stats_qSplitter, "Statistics")

        self.top_layout.addWidget(self.tab_widget, 0, 0, 1, 1)

        self.curr_leaf_profile_widget = None

        if pf is not None:
            self.init_statistics()
            self.init_leaf_profiles()

        self.initComplete = True
    
    def update_picket_fence(self, pf: QPicketFence):
        self.pf = pf

        self.initComplete = False

        self.init_statistics()
        self.init_leaf_profiles()

        self.initComplete = True

    def init_statistics(self):
        self.stats_tree_widget.clear()

        statistics = [["Gantry angle", f"{self.pf.image.gantry_angle:2.2f}°", ""],
                      ["Collimator angle", f"{self.pf.image.collimator_angle:2.2f}°", ""],
                      ["Number of pickets found", f"{len(self.pf.pickets)}", ""],
                      ["Number of leaf pairs found", f"{int(len(self.pf.mlc_meas) / len(self.pf.pickets))}"],
                      ["Maximum error", f"{self.pf.max_error:2.3f} mm",
                       f"Max error at picket {self.pf.max_error_picket + 1} and leaf {self.pf.max_error_leaf + 1}"],
                      ["Percentage of passing leafs", f"{self.pf.percent_passing:2.0f}%", ""],
                      ["Number of failed leafs", f"{len(self.pf.failed_leaves())}", ""]]
        
        self.stats_tree_widget.addTopLevelItems([QTreeWidgetItem(stat) for stat in statistics])
    
    def init_leaf_profiles(self):
        self.pickets_cb.clear()
        self.leafs_cb.clear()

        if self.curr_leaf_profile_widget is not None:
            self.curr_leaf_profile_widget.deleteLater()

        self.curr_leaf_profile_widget = self.pf.profile_plot_widget
        self.leaf_profiles_qSplitter.addWidget(self.curr_leaf_profile_widget)

        self.pickets_cb.addItems([str(x) for x in range(1,self.pf.num_pickets+1)])
        self.leafs_cb.addItems([str(x) for x in sorted({mlc.leaf_num + 1 for mlc in self.pf.mlc_meas})])

        self.plot_leaf_profile(True)
        
    def plot_leaf_profile(self, force_plot: bool = False):

        if self.initComplete or force_plot:
            self.pf.qplot_leaf_profile(int(self.leafs_cb.currentText())-1,
                                       int(self.pickets_cb.currentText())-1)