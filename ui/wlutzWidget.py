from PySide6.QtWidgets import (QWidget, QListWidgetItem, QMenu, QFileDialog, QFormLayout,
                               QVBoxLayout, QLabel, QProgressBar, QMessageBox, QErrorMessage,
                               QSizePolicy, QMainWindow)
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QEvent, QThread

from ui.py_ui.wlutzWorksheet_ui import Ui_QWLutzWorksheet
from ui.py_ui import icons_rc
from core.analysis.wlutz import QWinstonLutzWorker

from pylinac.core.image import LinacDicomImage
from pathlib import Path
import pyqtgraph as pg
import platform
import subprocess

pg.setConfigOptions(antialias=True, imageAxisOrder='row-major')

class QWLutzWorksheet(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_QWLutzWorksheet()
        self.ui.setupUi(self)

        self.image_icon = QIcon()
        self.image_icon.addFile(u":/colorIcons/icons/picture.png", QSize(), QIcon.Normal, QIcon.Off)

        self.form_layout = QFormLayout()
        self.form_layout.setHorizontalSpacing(30)
        self.ui.analysisInfoVL.addLayout(self.form_layout)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.shiftInfoBtn.setEnabled(False)

        # setup context menu for image list widget
        self.img_list_contextmenu = QMenu()
        self.img_list_contextmenu.addAction("View Original Image", self.view_dicom_image)
        self.view_analyzed_img_action = self.img_list_contextmenu.addAction("View Analyzed Image", self.viewAnalyzedImage)
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

        self.ui.addImgBtn.clicked.connect(self.add_files)
        self.ui.importImgBtn.clicked.connect(self.add_files)
        self.ui.analyzeBtn.clicked.connect(self.start_analysis)
        self.ui.shiftInfoBtn.clicked.connect(self.showShiftInfo)
        self.ui.imageListWidget.itemChanged.connect(lambda x: self.update_marked_images())

        self.marked_images = []
        self.imageView_windows = []
        self.analysis_in_progress = False

        self.params = {
            "pylinac_version": "PyLinac version",
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

    def add_files(self):
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
    
    def start_analysis(self):
        self.analysis_in_progress = True
        self.remove_list_checkmarks()

        self.analysis_progress_bar.show()
        self.analysis_message_label.show()

        row_count = self.form_layout.rowCount()
        for i in range(row_count):
            self.form_layout.removeRow(row_count - (i+1))

        self.ui.analyzeBtn.setEnabled(False)
        self.ui.analyzeBtn.setText("Analysis in progress...")

        self.analysis_worker = QWinstonLutzWorker(self.marked_images)
    
        self.thread = QThread()
        self.analysis_worker.moveToThread(self.thread)
        self.thread.started.connect(self.analysis_worker.analyze)
        self.thread.finished.connect(self.thread.deleteLater)
        self.analysis_worker.images_analyzed.connect(self.analysis_progress_bar.setValue)
        self.analysis_worker.images_analyzed.connect(lambda num:
                            self.analysis_message_label.setText(f"Analyzing images ({num} of {len(self.marked_images)} complete)"))
        self.analysis_worker.analysis_results_changed.connect(self.show_analysis_results)
        self.analysis_worker.bb_shift_info_changed.connect(self.update_bb_shift)
        self.analysis_worker.thread_finished.connect(self.thread.quit)
        self.analysis_worker.thread_finished.connect(self.analysis_worker.deleteLater)

        self.analysis_progress_bar.setRange(0, len(self.marked_images))
        self.analysis_progress_bar.setValue(0)
        self.analysis_message_label.setText("Starting analysis...")

        self.thread.start()

    def show_analysis_results(self, results):
        self.analysis_in_progress = False
        self.restore_list_checkmarks()

        # NB: Data change of list widgets items will auto enable analyzeBtn
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

        for key in self.params:
            if "_mm" in key:
                self.form_layout.addRow(f"{self.params[key]}:", QLabel(f"{round(float(results[key]),2)} mm"))
            else:
                self.form_layout.addRow(f"{self.params[key]}:", QLabel(str(results[key])))

        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

    def update_bb_shift(self, bb_shift_info: str):
        self.shift_info = bb_shift_info
        self.ui.shiftInfoBtn.setEnabled(True)

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

    def viewAnalyzedImage(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()
        image_short_name = listWidgetItem.text()
        image_path = listWidgetItem.data(Qt.UserRole)["file_path"]
        image_data = listWidgetItem.data(Qt.UserRole)["analysis_data"]
        image = LinacDicomImage(image_path)

        plotView = pg.PlotWidget()
        plotView.setAspectLocked(True)
        plotItem = plotView.getPlotItem()
        plotItem.invertY(False)
        
        #This makes the image appear correctly somehow!
        image.flipud()
        imageItem = pg.ImageItem(image=image.array)

        bbX = image_data["bb_location"]["x"]
        bbY = image_data["bb_location"]["y"]
        caxX = image_data["field_cax"]["x"]
        caxY = image_data["field_cax"]["y"]
        epidX = image_data["epid"]["x"]
        epidY = image_data["epid"]["y"]

        bb_plotItem = pg.ScatterPlotItem()
        cax_plotItem = pg.ScatterPlotItem()
        bb_plotItem.addPoints(pos=[(bbX, bbY)], pen=None, size=10, brush=(255, 0, 0, 255), name="BB")
        cax_plotItem.addPoints(pos=[(caxX, caxY)], pen=None, size=10, brush=(0, 0, 255, 255),
                                symbol="s", name="CAX")
        
        epidX_plotItem = pg.InfiniteLine(movable=False, angle=90, pen = (0,255,0), name="EPID X line",
                                        label="EPID x = {value:0.2f}", labelOpts={'position': 0.1,
                                        'color': (200,200,100), 'fill': (0,200,0,50), 'movable': False})
        
        epidY_plotItem = pg.InfiniteLine(movable=False, angle=0, pen = (0,255,0), name="EPID Y line", 
                                         label="EPID y = {value:0.2f}", labelOpts={'position': 0.1, 
                                        'color': (200,200,100), 'fill': (0,200,0,50), 'movable': False})
        
        epidX_plotItem.setPos([epidX,0])
        epidY_plotItem.setPos([0,epidY])
        plotItem.addItem(imageItem)
        plotItem.addColorBar(imageItem, colorMap="viridis")
        plotItem.addItem(bb_plotItem)
        plotItem.addItem(cax_plotItem)
        plotItem.addItem(epidX_plotItem)
        plotItem.addItem(epidY_plotItem)

        legend = pg.LegendItem((50,50), offset=(50,50))
        legend.setParentItem(plotItem)
        legend.addItem(bb_plotItem, "BB")
        legend.addItem(cax_plotItem, "Field CAX")
        legend.addItem(epidX_plotItem, "EPID-x line")
        legend.addItem(epidY_plotItem, "EPID-y line")

        new_win = QMainWindow()
        new_win.setWindowTitle(image_short_name + " (Analyzed)")
        new_win.setCentralWidget(plotView)
        new_win.setMinimumSize(600, 500)
        
        self.imageView_windows.append(new_win)
        new_win.show()
        new_win.setMinimumSize(0, 0)

    def showShiftInfo(self):
        self.shift_dialog = QMessageBox()
        self.shift_dialog.setWindowTitle("BB Shift Instructions")
        self.shift_dialog.setText("<p><span style=\" font-weight:700; font-size: 11pt;\">" \
                                 "To minimize the mean positioning error shift the ball-bearing as follows: </span></p>")
        self.shift_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.shift_dialog.setTextFormat(Qt.TextFormat.RichText)

        shifts = self.shift_info.split("; ")
        self.shift_dialog.setInformativeText(f'{shifts[0].split(" ")[0]}: {shifts[0].split(" ")[1].replace("mm", " mm")}\n' \
                                            f'{shifts[1].split(" ")[0]}: {shifts[1].split(" ")[1].replace("mm", " mm")}\n' \
                                            f'{shifts[2].split(" ")[0]}: {shifts[2].split(" ")[1].replace("mm", " mm")}')

        shift_icon = QPixmap(u":/colorIcons/icons/bb_shift.png")
        self.shift_dialog.setIconPixmap(shift_icon)

        self.shift_dialog.exec()

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