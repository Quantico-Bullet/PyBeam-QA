from PySide6.QtWidgets import (QWidget, QMainWindow, QCheckBox)
from PySide6.QtCore import QObject, QEvent

from ui.py_ui.appMainWin_ui import Ui_MainWindow as Ui_AppMainWin
from ui.qaMainWin import QAToolsWin
from core.tools.devices import DeviceManager, Linac

class AppMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_AppMainWin()
        self.__ui.setupUi(self)

        self.initSetupComplete = False

        self.setWindowTitle("PyBeam QA")
        self.setupPages()

        self.initSetupComplete = True

    def setupPages(self):
        # setup main page
        self.__ui.navTabBtnGroup.buttonClicked.connect(self.changeNavPage)
        self.__ui.photonCalib.installEventFilter(self)
        self.__ui.electronCalib.installEventFilter(self)
        self.__ui.winstonLutzAnalysis.installEventFilter(self)
        self.__ui.planarImagingAnalysis.installEventFilter(self)
        self.__ui.fieldAnalysis.installEventFilter(self)
        self.__ui.starshotAnalysis.installEventFilter(self)
        self.__ui.picketFence.installEventFilter(self)

        # setup defaults, useful to avoid defaults set by Qt designer
        self.__ui.mainStackWidget.setCurrentIndex(0)
        self.__ui.navigationStackedWidget.setCurrentIndex(0)

        self.winston_lutz_win = None
        self.picket_fence_win = None
        self.starshot_win = None

    def setupCalibrationPage(self, calibType: str):
        self.currLinac = None
        self.beamCheckBoxList = []

        # setup daily/monthly photons page functionality
        self.__ui.calibStartBtn.clicked.connect(lambda: "fake slot") # use fake slots so that we can disconnect past slots without errors
        self.__ui.backBtn.clicked.connect(lambda: "fake slot")
        self.__ui.linacNameCB.currentTextChanged.connect(lambda x: "fake slot")
        self.__ui.backBtn.clicked.disconnect()
        self.__ui.backBtn.clicked.connect(lambda: self.changeMainPage(self.__ui.linacQAPage))
        self.__ui.calibStartBtn.clicked.disconnect()
        self.__ui.linacNameCB.currentTextChanged.disconnect()
        self.__ui.institutionLE.clear()
        self.__ui.userLE.clear()
        self.__ui.linacNameCB.clear()

        if calibType == "photons":
            self.__ui.calibPageTitle.setText("Photon Output Calibration")
            self.__ui.calibStartBtn.clicked.connect(lambda: self.initPhotonsCalibQA())
            self.__ui.linacNameCB.currentTextChanged.connect(lambda x: self.setLinacDetails(calibType, x))   

        elif calibType == "electrons":
            self.__ui.calibPageTitle.setText("Electron Output Calibration")
            self.__ui.calibStartBtn.clicked.connect(lambda: self.openElectronsCalibQA())
            self.__ui.linacNameCB.currentTextChanged.connect(lambda x: self.setLinacDetails(calibType, x))
        
        # Add all available linacs
        for linac in DeviceManager.device_list["linacs"]:
            self.__ui.linacNameCB.addItem(linac.name)

    def setLinacDetails(self, calibType: str, linacName: str):
        for linac in DeviceManager.device_list["linacs"]:
            if linacName == linac.name:
                self.currLinac = linac
        
        # check if there are beams added prior and remove them
        self.beamCheckBoxList.clear()
        addedPrior = self.__ui.linacBeamsField.count()
                
        for i in range(addedPrior):
            layout = self.__ui.linacBeamsField.takeAt(0)
            widget = layout.widget()
            widget.deleteLater()

        # TODO check if these fields exist/make sure they exist but are empty
        self.__ui.linacSerialNumField.setText(self.currLinac.serial_num)
        self.__ui.linacModelField.setText(self.currLinac.model_name)
        self.__ui.linacManufacField.setText(self.currLinac.manufacturer)

        # add new beams
        if calibType == "photons":
            for i,beam in enumerate(self.currLinac.beams["photons"]):
                checkBox = QCheckBox(f"{beam} MV")
                self.__ui.linacBeamsField.addWidget(checkBox,i,0,1,1)
                self.beamCheckBoxList.append(checkBox)

            for i,beam in enumerate(self.currLinac.beams["photonsFFF"]):
                checkBox = QCheckBox(f"{beam} MV FFF")
                self.__ui.linacBeamsField.addWidget(checkBox,i,1,1,1)
                self.beamCheckBoxList.append(checkBox)

        elif calibType == "electrons":
            for i,beam in enumerate(self.currLinac.beams["electrons"]):
                checkBox = QCheckBox(f"{beam} MeV")
                self.__ui.linacBeamsField.addWidget(checkBox,i,0,1,1)
                self.beamCheckBoxList.append(checkBox)

            for i,beam in enumerate(self.currLinac.beams["electronsFFF"]):
                checkBox = QCheckBox(f"{beam} MeV FFF")
                self.__ui.linacBeamsField.addWidget(checkBox,i,1,1,1)
                self.beamCheckBoxList.append(checkBox)

    def changeMainPage(self, currWidget: QWidget):
        self.__ui.mainStackWidget.setCurrentWidget(currWidget)

    def changeNavPage(self):
        if self.__ui.navTabBtnGroup.checkedButton() == self.__ui.qaToolsBtn:
            self.__ui.currentPageTitle.setText("QA Tools")
            self.__ui.navigationStackedWidget.setCurrentIndex(0)
        elif self.__ui.navTabBtnGroup.checkedButton() == self.__ui.qaReportsBtn:
            self.__ui.currentPageTitle.setText("Reports")
            self.__ui.navigationStackedWidget.setCurrentIndex(1)
        else:
            self.__ui.currentPageTitle.setText("Devices")
            self.__ui.navigationStackedWidget.setCurrentIndex(2)
    
    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        # Catch all sub-navigation component clicks here
        if event.type() == QEvent.Type.MouseButtonPress and source is self.__ui.photonCalib:
            self.setupCalibrationPage("photons")
            self.changeMainPage(self.__ui.initCalibPage)

        elif event.type() == QEvent.Type.MouseButtonPress and source is self.__ui.electronCalib:
            self.setupCalibrationPage("electrons")
            self.changeMainPage(self.__ui.initCalibPage)

        elif event.type() == QEvent.Type.MouseButtonPress and source is self.__ui.winstonLutzAnalysis:
            if self.winston_lutz_win is None:
                initData = {"toolType": "winston_lutz"}

                self.winston_lutz_win = QAToolsWin(initData = initData)
                self.winston_lutz_win.showMaximized()
            else:
                self.winston_lutz_win.addNewWorksheet()
        
        elif event.type() == QEvent.Type.MouseButtonPress and source is self.__ui.picketFence:
            if self.picket_fence_win is None:
                initData = {"toolType": "picket_fence"}

                self.picket_fence_win = QAToolsWin(initData = initData)
                self.picket_fence_win.showMaximized()
            else:
                self.picket_fence_win.addNewWorksheet()

        elif event.type() == QEvent.Type.MouseButtonPress and source is self.__ui.starshotAnalysis:
            if self.starshot_win is None:
                initData = {"toolType": "starshot"}

                self.starshot_win = QAToolsWin(initData = initData)
                self.starshot_win.showMaximized()
            else:
                self.starshot_win.addNewWorksheet()
            
        return super().eventFilter(source, event)
    
    def initPhotonsCalibQA(self):
        initData = {"toolType": "photon_calibration",
                    "institution": None,
                    "user": None,
                    "photonBeams": [],
                    "photonFFFBeams": [],
                    "linac": self.currLinac}
        
        # get CheckBoxes and select the checked ones
        for beamCheckBox in self.beamCheckBoxList:
            if beamCheckBox.isChecked():
                if "FFF" in str(beamCheckBox.text()):
                    initData["photonFFFBeams"].append(int(str(beamCheckBox.text())
                                    .split(" ")[0]))
                else:
                    initData["photonBeams"].append(int(str(beamCheckBox.text())
                                    .split(" ")[0]))
                    
        initData["institution"] = self.__ui.institutionLE.text()
        initData["user"] = self.__ui.userLE.text()
        self.photonCalWin = QAToolsWin(initData = initData)
        self.photonCalWin.showMaximized()

    def initElectronsCalibQA(self):
        initData = {"toolType": "electron_calibration",
                    "institution": None,
                    "user": None,
                    "electronBeams": [],
                    "electronFFFBeams": [],
                    "linac": self.currLinac}
        
        # retrieve checkboxes and select the checked ones
        for beamCheckBox in self.beamCheckBoxList:
            if beamCheckBox.isChecked():
                if "FFF" in str(beamCheckBox.text()):
                    initData["electronFFFBeams"].append(int(str(beamCheckBox.text())
                                    .split(" ")[0]))
                else:
                    initData["electronBeams"].append(int(str(beamCheckBox.text())
                                    .split(" ")[0]))
                    
        initData["institution"] = self.__ui.institutionLE.text()
        initData["user"] = self.__ui.userLE.text()
        self.photonCalWin = QAToolsWin(initData = initData)
        self.photonCalWin.showMaximized()