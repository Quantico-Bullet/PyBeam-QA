from PySide6.QtWidgets import (QWidget, QMainWindow, QCheckBox)
from PySide6.QtCore import QObject, QEvent

from core.tools.devices import DeviceManager

from ui.py_ui.appMainWin_ui import Ui_MainWindow as Ui_AppMainWin
from ui.qaToolsWindow import QAToolsWindow
from ui.trs398Widgets import PhotonsMainWindow, ElectronsMainWindow
from ui.starshotWidgets import StarshotMainWindow
from ui.wlutzWidgets import WinstonLutzMainWindow
from ui.fieldAnalysisWidgets import FieldAnalysisMainWindow
from ui.picketFenceWidgets import PicketFenceMainWindow
from ui.planarImagingWidgets import PlanarImagingMainWindow

class AppMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_AppMainWin()
        self._ui.setupUi(self)

        self.initSetupComplete = False

        self.setWindowTitle("PyBeam QA")
        self.setupPages()

        self.initSetupComplete = True

    def setupPages(self):
        # setup main page
        self._ui.navTabBtnGroup.buttonClicked.connect(self.changeNavPage)
        self._ui.photonCalib.installEventFilter(self)
        self._ui.electronCalib.installEventFilter(self)
        self._ui.winstonLutzAnalysis.installEventFilter(self)
        self._ui.planarImagingAnalysis.installEventFilter(self)
        self._ui.fieldAnalysis.installEventFilter(self)
        self._ui.starshotAnalysis.installEventFilter(self)
        self._ui.picketFence.installEventFilter(self)

        # setup defaults, useful to avoid defaults set by Qt designer
        self._ui.mainStackWidget.setCurrentIndex(0)
        self._ui.navigationStackedWidget.setCurrentIndex(0)

        self.qa_windows = {"photon_cal": None,
                      "electron_cal": None,
                      "picket_fence": None,
                      "starshot": None,
                      "winston_lutz": None,
                      "field_analysis": None,
                      "planar_imaging_analysis": None}

    def setupCalibrationPage(self, calibType: str):
        self.currLinac = None
        self.beamCheckBoxList = []

        # setup daily/monthly photons page functionality
        self._ui.calibStartBtn.clicked.connect(lambda: "fake slot") # use fake slots so that we can disconnect past slots without errors
        self._ui.loadQABtn.clicked.connect(lambda: "fake slot")
        self._ui.backBtn.clicked.connect(lambda: "fake slot")
        self._ui.linacNameCB.currentTextChanged.connect(lambda x: "fake slot")
        self._ui.backBtn.clicked.disconnect()
        self._ui.backBtn.clicked.connect(lambda: self.changeMainPage(self._ui.linacQAPage))
        self._ui.calibStartBtn.clicked.disconnect()
        self._ui.loadQABtn.clicked.disconnect()
        self._ui.linacNameCB.currentTextChanged.disconnect()
        self._ui.institutionLE.clear()
        self._ui.userLE.clear()
        self._ui.linacNameCB.clear()

        if calibType == "photons":
            self._ui.calibPageTitle.setText("Photon Output Calibration")
            self._ui.calibStartBtn.clicked.connect(lambda: self.initPhotonsCalibQA())
            self._ui.loadQABtn.clicked.connect(lambda: PhotonsMainWindow.load_from_file(None))
            self._ui.linacNameCB.currentTextChanged.connect(lambda x: self.setLinacDetails(calibType, x))   

        elif calibType == "electrons":
            self._ui.calibPageTitle.setText("Electron Output Calibration")
            self._ui.calibStartBtn.clicked.connect(lambda: self.initElectronsCalibQA())
            self._ui.loadQABtn.clicked.connect(lambda: ElectronsMainWindow.load_from_file(None))
            self._ui.linacNameCB.currentTextChanged.connect(lambda x: self.setLinacDetails(calibType, x))
        
        # Add all available linacs
        for linac in DeviceManager.device_list["linacs"]:
            self._ui.linacNameCB.addItem(linac.name)

    def setLinacDetails(self, calibType: str, linacName: str):
        for linac in DeviceManager.device_list["linacs"]:
            if linacName == linac.name:
                self.currLinac = linac
        
        # check if there are beams added prior and remove them
        self.beamCheckBoxList.clear()
        addedPrior = self._ui.linacBeamsField.count()
                
        for i in range(addedPrior):
            layout = self._ui.linacBeamsField.takeAt(0)
            widget = layout.widget()
            widget.deleteLater()

        # TODO check if these fields exist/make sure they exist but are empty
        self._ui.linacSerialNumField.setText(self.currLinac.serial_num)
        self._ui.linacModelField.setText(self.currLinac.model_name)
        self._ui.linacManufacField.setText(self.currLinac.manufacturer)

        # add new beams
        if calibType == "photons":
            for i,beam in enumerate(self.currLinac.beams["photons"]):
                checkBox = QCheckBox(f"{beam} MV")
                self._ui.linacBeamsField.addWidget(checkBox,i,0,1,1)
                self.beamCheckBoxList.append(checkBox)

            for i,beam in enumerate(self.currLinac.beams["photonsFFF"]):
                checkBox = QCheckBox(f"{beam} MV FFF")
                self._ui.linacBeamsField.addWidget(checkBox,i,1,1,1)
                self.beamCheckBoxList.append(checkBox)

        elif calibType == "electrons":
            for i,beam in enumerate(self.currLinac.beams["electrons"]):
                checkBox = QCheckBox(f"{beam} MeV")
                self._ui.linacBeamsField.addWidget(checkBox,i,0,1,1)
                self.beamCheckBoxList.append(checkBox)

    def changeMainPage(self, currWidget: QWidget):
        self._ui.mainStackWidget.setCurrentWidget(currWidget)

    def changeNavPage(self):
        if self._ui.navTabBtnGroup.checkedButton() == self._ui.qaToolsBtn:
            self._ui.currentPageTitle.setText("QA Tools")
            self._ui.navigationStackedWidget.setCurrentIndex(0)
        elif self._ui.navTabBtnGroup.checkedButton() == self._ui.qaReportsBtn:
            self._ui.currentPageTitle.setText("Reports")
            self._ui.navigationStackedWidget.setCurrentIndex(1)
        else:
            self._ui.currentPageTitle.setText("Devices")
            self._ui.navigationStackedWidget.setCurrentIndex(2)
    
    def eventFilter(self, source: QObject, event: QEvent) -> bool:
        # Catch all sub-navigation component clicks here
        # TODO remove too many if else checks
        if event.type() == QEvent.Type.MouseButtonPress and source is self._ui.photonCalib:
            self.setupCalibrationPage("photons")
            self.changeMainPage(self._ui.initCalibPage)

        elif event.type() == QEvent.Type.MouseButtonPress and source is self._ui.electronCalib:
            self.setupCalibrationPage("electrons")
            self.changeMainPage(self._ui.initCalibPage)

        elif event.type() == QEvent.Type.MouseButtonPress and source is self._ui.winstonLutzAnalysis:
            self.open_window("winston_lutz", WinstonLutzMainWindow)
        
        elif event.type() == QEvent.Type.MouseButtonPress and source is self._ui.picketFence:
            self.open_window("picket_fence", PicketFenceMainWindow)

        elif event.type() == QEvent.Type.MouseButtonPress and source is self._ui.starshotAnalysis:
            self.open_window("starshot", StarshotMainWindow)

        elif event.type() == QEvent.Type.MouseButtonPress and source is self._ui.fieldAnalysis:
            self.open_window("field_analysis", FieldAnalysisMainWindow)

        elif event.type() == QEvent.Type.MouseButtonPress and source is self._ui.planarImagingAnalysis:
            self.open_window("planar_imaging_analysis", PlanarImagingMainWindow)
            
        return super().eventFilter(source, event)
    
    def open_window(self, window_type: str, window: QAToolsWindow, data: dict | None = None):
        if self.qa_windows[window_type] is None:

            if window_type != 'photon_cal' and window_type != 'electron_cal':
                self.qa_windows[window_type] = window(data)
                self.qa_windows[window_type].showMaximized()
                
                self.qa_windows[window_type].destroyed.connect(
                    lambda: self.window_closed(window_type))
                
            else:
                window(data).showMaximized()
              
        else:
            self.qa_windows[window_type].add_new_worksheet()
            self.qa_windows[window_type].activateWindow()
    
    def window_closed(self, winType: str):
        self.qa_windows[winType] = None
    
    def initPhotonsCalibQA(self):
        initData = {"institution": None,
                    "user": None,
                    "photon_beams": [],
                    "photon_fff_beams": [],
                    "linac": self.currLinac}
        
        # get CheckBoxes and select the checked ones
        for beamCheckBox in self.beamCheckBoxList:
            if beamCheckBox.isChecked():
                if "FFF" in str(beamCheckBox.text()):
                    initData["photon_fff_beams"].append(int(str(beamCheckBox.text())
                                    .split(" ")[0]))
                else:
                    initData["photon_beams"].append(int(str(beamCheckBox.text())
                                    .split(" ")[0]))
                    
        initData["institution"] = self._ui.institutionLE.text()
        initData["user"] = self._ui.userLE.text()
        
        self.open_window("photon_cal", PhotonsMainWindow, initData)

    def initElectronsCalibQA(self):
        initData = {"institution": None,
                    "user": None,
                    "electron_beams": [],
                    "linac": self.currLinac}
        
        # retrieve checkboxes and select the checked ones
        for beamCheckBox in self.beamCheckBoxList:
            if beamCheckBox.isChecked():
                initData["electron_beams"].append(int(str(beamCheckBox.text()).split(" ")[0]))
                    
        initData["institution"] = self._ui.institutionLE.text()
        initData["user"] = self._ui.userLE.text()
        
        self.open_window("electron_cal", ElectronsMainWindow, initData)