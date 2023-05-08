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

        self.imageIcon = QIcon()
        self.imageIcon.addFile(u":/colorIcons/icons/picture.png", QSize(), QIcon.Normal, QIcon.Off)

        self.formLayout = QFormLayout()
        self.formLayout.setHorizontalSpacing(30)
        self.ui.analysisInfoVL.addLayout(self.formLayout)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.shiftInfoBtn.setEnabled(False)

        # setup context menu for image list widget
        self.imgListContextMenu = QMenu()
        self.imgListContextMenu.addAction("View Original Image", self.viewDicomImage)
        self.viewAnalyzedImgAction = self.imgListContextMenu.addAction("View Analyzed Image", self.viewAnalyzedImage)
        self.viewAnalyzedImgAction.setEnabled(False)
        self.imgListContextMenu.addAction("Show Containing Folder", self.openFileFolder)
        self.removeFileAction = self.imgListContextMenu.addAction("Remove from List", self.removeFile)
        self.deleteFileAction = self.imgListContextMenu.addAction("Delete", self.deleteFile)
        self.imgListContextMenu.addAction("Properties")
        self.imgListContextMenu.addSeparator()
        self.selectAllAction = self.imgListContextMenu.addAction("Select All", lambda: self.performSelection("selectAll"))
        self.unselectAllAction = self.imgListContextMenu.addAction("Unselect All", lambda: self.performSelection("unselectAll"))
        self.invertSelectAction = self.imgListContextMenu.addAction("Invert Selection", lambda: self.performSelection("invertSelection"))
        self.imgListContextMenu.addSeparator()
        self.removeSelectedFilesAction = self.imgListContextMenu.addAction("Remove Selected Files", self.removeSelectedFiles)
        self.removeAllFilesAction = self.imgListContextMenu.addAction("Remove All Files", self.removeAllFiles)
        self.ui.imageListWidget.installEventFilter(self)

        #Add widgets
        self.progressVL = QVBoxLayout()
        self.progressVL.setSpacing(10)

        self.analysisProgressBar = QProgressBar()
        self.analysisProgressBar.setRange(0,0)
        self.analysisProgressBar.setTextVisible(False)
        self.analysisProgressBar.setMaximumSize(300, 10)
        self.analysisProgressBar.setMinimumSize(300, 10)
        self.analysisProgressBar.hide()

        self.analysisMessage = QLabel()
        self.analysisMessage.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred))
        self.analysisMessage.hide()

        self.progressVL.addWidget(self.analysisProgressBar, 0, Qt.AlignHCenter)
        self.progressVL.addWidget(self.analysisMessage, 0, Qt.AlignHCenter)

        self.ui.analysisInfoVL.addLayout(self.progressVL)

        self.ui.addImgBtn.clicked.connect(self.addFiles)
        self.ui.importImgBtn.clicked.connect(self.addFiles)
        self.ui.analyzeBtn.clicked.connect(self.startAnalysis)
        self.ui.shiftInfoBtn.clicked.connect(self.showShiftInfo)
        self.ui.imageListWidget.itemChanged.connect(lambda x: self.updateMarkedImages())

        self.markedImages = []
        self.imageViewWindows = []
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

    def addFiles(self):
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
                listItemWidget.setIcon(self.imageIcon)
                listItemWidget.setCheckState(Qt.Unchecked)
                listItemWidget.setData(Qt.UserRole, itemData)
            
            if self.ui.stackedWidget.currentIndex() == 0:
                self.ui.stackedWidget.setCurrentIndex(1)

    def removeSelectedFiles(self):
        index = 0
        while index < self.ui.imageListWidget.count():
            if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                listItemWidget = self.ui.imageListWidget.takeItem(index)
                del listItemWidget
            else:
                index += 1

        self.updateMarkedImages()

    def removeAllFiles(self):
        itemCount = self.ui.imageListWidget.count()
        for index in range(itemCount):
            listItemWidget = self.ui.imageListWidget.takeItem(itemCount-(index+1))
            del listItemWidget
        
        self.updateMarkedImages()

    def removeFile(self):
        listItemWidget = self.ui.imageListWidget.takeItem(self.ui.imageListWidget.currentRow())
        del listItemWidget

        self.updateMarkedImages()

    def openFileFolder(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()
        filePath = str(Path(listWidgetItem.data(Qt.UserRole)["file_path"]).parent.resolve())
        
        if platform.system() == "Windows":
            subprocess.Popen(["explorer", filePath])
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", filePath])
        else:
            subprocess.Popen(["xdg-open", filePath])

    def performSelection(self, selection_type: str):

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

        self.updateMarkedImages()


    def eventFilter(self, source, event: QEvent):
        if (event.type() == QEvent.ContextMenu and source is self.ui.imageListWidget):
            pos = self.ui.imageListWidget.mapFromGlobal(event.globalPos())

            if type(self.ui.imageListWidget.itemAt(pos)) == QListWidgetItem:
                # Show context menu
                if not self.analysis_in_progress:
                    if self.ui.imageListWidget.itemAt(pos).data(Qt.UserRole)["analysis_data"]:
                        self.viewAnalyzedImgAction.setEnabled(True)
                    else:
                        self.viewAnalyzedImgAction.setEnabled(False)

                    if len(self.markedImages) > 0:
                        self.invertSelectAction.setEnabled(True)
                        self.unselectAllAction.setEnabled(True)
                        self.removeSelectedFilesAction.setEnabled(True)
                    else:
                        self.invertSelectAction.setEnabled(False)
                        self.unselectAllAction.setEnabled(False)
                        self.removeSelectedFilesAction.setEnabled(False)

                    if len(self.markedImages) == self.ui.imageListWidget.count():
                        self.selectAllAction.setEnabled(False)
                    else:
                        self.selectAllAction.setEnabled(True)
                    
                    self.removeFileAction.setEnabled(True)
                    self.deleteFileAction.setEnabled(True)
                    self.removeAllFilesAction.setEnabled(True)
                    self.selectAllAction.setEnabled(True)
                
                else:
                    self.removeFileAction.setEnabled(False)
                    self.deleteFileAction.setEnabled(False)
                    self.removeSelectedFilesAction.setEnabled(False)
                    self.removeAllFilesAction.setEnabled(False)
                    self.selectAllAction.setEnabled(False)
                    self.viewAnalyzedImgAction.setEnabled(False)

                self.imgListContextMenu.exec(event.globalPos())
    
        return super().eventFilter(source, event)
    
    def updateMarkedImages(self):
        self.markedImages.clear()

        for index in range(self.ui.imageListWidget.count()):
            if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                self.markedImages.append(self.ui.imageListWidget.item(index).data(Qt.UserRole)["file_path"])
        
        if len(self.markedImages) > 1:
            self.ui.analyzeBtn.setText(f"Analyze {len(self.markedImages)} images")
            self.ui.analyzeBtn.setEnabled(True)

        else:
            self.ui.analyzeBtn.setText(f"Analyze images")
            self.ui.analyzeBtn.setEnabled(False)
    
    def startAnalysis(self):
        self.analysis_in_progress = True
        self.removeListCheckmarks()

        self.analysisProgressBar.show()
        self.analysisMessage.show()

        rowCount = self.formLayout.rowCount()
        for i in range(rowCount):
            self.formLayout.removeRow(rowCount - (i+1))

        self.ui.analyzeBtn.setEnabled(False)
        self.ui.analyzeBtn.setText("Analysis in progress...")

        self.analysisWorker = QWinstonLutzWorker(self.markedImages)
    
        self.thread = QThread()
        self.analysisWorker.moveToThread(self.thread)
        self.thread.started.connect(self.analysisWorker.analyze)
        self.thread.finished.connect(self.thread.deleteLater)
        self.analysisWorker.imagesAnalyzed.connect(self.analysisProgressBar.setValue)
        self.analysisWorker.imagesAnalyzed.connect(lambda num:
                            self.analysisMessage.setText(f"Analyzing images ({num} of {len(self.markedImages)} complete)"))
        self.analysisWorker.analysisResultsChanged.connect(self.showAnalysisResults)
        self.analysisWorker.bbShiftInfoChanged.connect(self.updateBBShift)
        self.analysisWorker.threadFinished.connect(self.thread.quit)
        self.analysisWorker.threadFinished.connect(self.analysisWorker.deleteLater)

        self.analysisProgressBar.setRange(0, len(self.markedImages))
        self.analysisProgressBar.setValue(0)
        self.analysisMessage.setText("Starting analysis...")

        self.thread.start()

    def showAnalysisResults(self, results):
        self.analysis_in_progress = False
        self.restoreListCheckmarks()

        # NB: Data change of list widgets items will auto enable analyzeBtn
        for index in range(self.ui.imageListWidget.count()):
            listItemWidget = self.ui.imageListWidget.item(index)
            itemData = listItemWidget.data(Qt.UserRole)

            for imageDetails in results["image_details"]:
                if itemData["file_path"] == imageDetails["file_path"]:
                    itemData["analysis_data"] = imageDetails
                    break
                else:
                    itemData["analysis_data"] = None

            listItemWidget.setData(Qt.UserRole, itemData)

        for key in self.params:
            if "_mm" in key:
                self.formLayout.addRow(f"{self.params[key]}:", QLabel(f"{round(float(results[key]),2)} mm"))
            else:
                self.formLayout.addRow(f"{self.params[key]}:", QLabel(str(results[key])))

        self.analysisProgressBar.hide()
        self.analysisMessage.hide()

    def updateBBShift(self, bbShiftInfo: str):
        self.shiftInfo = bbShiftInfo
        self.ui.shiftInfoBtn.setEnabled(True)

    def viewDicomImage(self):
        imageShortName = self.ui.imageListWidget.currentItem().text()
        imagePath = self.ui.imageListWidget.selectedItems()[0].data(Qt.UserRole)["file_path"]
        image = LinacDicomImage(imagePath)

        imgView = pg.ImageView()
        imgView.setImage(image.array)
        imgView.setPredefinedGradient("viridis")

        newWin = QMainWindow()
        newWin.setWindowTitle(imageShortName)
        newWin.setCentralWidget(imgView)
        newWin.setMinimumSize(600, 500)
        
        self.imageViewWindows.append(newWin)
        newWin.show()
        newWin.setMinimumSize(0, 0)

    def viewAnalyzedImage(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()
        imageShortName = listWidgetItem.text()
        imagePath = listWidgetItem.data(Qt.UserRole)["file_path"]
        imageData = listWidgetItem.data(Qt.UserRole)["analysis_data"]
        image = LinacDicomImage(imagePath)

        plotView = pg.PlotWidget()
        plotItem = plotView.getPlotItem()
        plotItem.invertY(False)
        
        #This makes the image appear correctly somehow!
        image.flipud()
        imageItem = pg.ImageItem(image=image.array)

        bbX = imageData["bb_location"]["x"]
        bbY = imageData["bb_location"]["y"]
        caxX = imageData["field_cax"]["x"]
        caxY = imageData["field_cax"]["y"]
        epidX = imageData["epid"]["x"]
        epidY = imageData["epid"]["y"]

        bbCaxPlotItem = pg.ScatterPlotItem()
        bbCaxPlotItem.addPoints(pos=[(bbX, bbY)], pen=None, size=10, brush=(255, 0, 0, 255))
        bbCaxPlotItem.addPoints(pos=[(caxX, caxY)], pen=None, size=10, brush=(0, 0, 255, 255),
                                symbol="s")
        
        epidXPlotItem = pg.InfiniteLine(movable=False, angle=90, pen = (0,255,0), label="EPID x = {value:0.2f}",
                       labelOpts={'position': 0.1, 'color': (200,200,100), 'fill': (0,200,0,50), 'movable': False})
        
        epidYPlotItem = pg.InfiniteLine(movable=False, angle=0, pen = (0,255,0), label="EPID y = {value:0.2f}",
                       labelOpts={'position': 0.1, 'color': (200,200,100), 'fill': (0,200,0,50), 'movable': False})
        
        epidXPlotItem.setPos([epidX,0])
        epidYPlotItem.setPos([0,epidY])
        plotItem.addItem(imageItem)
        plotItem.addItem(bbCaxPlotItem)
        plotItem.addItem(epidXPlotItem)
        plotItem.addItem(epidYPlotItem)

        newWin = QMainWindow()
        newWin.setWindowTitle(imageShortName + " (Analyzed)")
        newWin.setCentralWidget(plotView)
        newWin.setMinimumSize(600, 500)
        
        self.imageViewWindows.append(newWin)
        newWin.show()
        newWin.setMinimumSize(0, 0)

    def showShiftInfo(self):
        self.shiftDialog = QMessageBox()
        self.shiftDialog.setWindowTitle("BB Shift Instructions")
        self.shiftDialog.setText("<p><span style=\" font-weight:700; font-size: 11pt;\">" \
                                 "To minimize the mean positioning error shift the ball-bearing as follows: </span></p>")
        self.shiftDialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.shiftDialog.setTextFormat(Qt.TextFormat.RichText)

        shifts = self.shiftInfo.split("; ")
        self.shiftDialog.setInformativeText(f'{shifts[0].split(" ")[0]}: {shifts[0].split(" ")[1].replace("mm", " mm")}\n' \
                                            f'{shifts[1].split(" ")[0]}: {shifts[1].split(" ")[1].replace("mm", " mm")}\n' \
                                            f'{shifts[2].split(" ")[0]}: {shifts[2].split(" ")[1].replace("mm", " mm")}')

        shiftIcon = QPixmap(u":/colorIcons/icons/bb_shift.png")
        self.shiftDialog.setIconPixmap(shiftIcon)

        self.shiftDialog.exec()

    def deleteFile(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()

        self.deleteDialog = QMessageBox()
        self.deleteDialog.setWindowTitle("Delete File")
        self.deleteDialog.setText("<p><span style=\" font-weight:700; font-size: 11pt;\">" \
                                  f"Are you sure you want to permanently delete \'{listWidgetItem.text()}\' ? </span></p>")
        self.deleteDialog.setInformativeText("This action is irreversible!")
        self.deleteDialog.setStandardButtons(QMessageBox.StandardButton.Yes | 
                                             QMessageBox.StandardButton.Cancel)
        self.deleteDialog.setTextFormat(Qt.TextFormat.RichText)

        warningIcon = QPixmap(u":/colorIcons/icons/warning_48.png")
        self.deleteDialog.setIconPixmap(warningIcon)

        ret = self.deleteDialog.exec()

        if ret == QMessageBox.StandardButton.Yes:
            path = Path(listWidgetItem.data(Qt.UserRole)["file_path"])
            path.unlink(missing_ok=True)
            self.ui.imageListWidget.takeItem(self.ui.imageListWidget.currentRow())
            del listWidgetItem


    def removeListCheckmarks(self):
        for index in range(self.ui.imageListWidget.count()):
            listItemWidget = self.ui.imageListWidget.item(index)
            listItemWidget.setFlags(Qt.ItemFlag.ItemIsEnabled)

    def restoreListCheckmarks(self):
        for index in range(self.ui.imageListWidget.count()):
            listItemWidget = self.ui.imageListWidget.item(index)
            listItemWidget.setFlags(Qt.ItemFlag.ItemIsEnabled |
                                    Qt.ItemFlag.ItemIsUserCheckable |
                                    Qt.ItemFlag.ItemIsDragEnabled |
                                    Qt.ItemFlag.ItemIsSelectable)
            
            if listItemWidget.data(Qt.ItemDataRole.UserRole)["file_path"] in self.markedImages:
                listItemWidget.setCheckState(Qt.CheckState.Checked)