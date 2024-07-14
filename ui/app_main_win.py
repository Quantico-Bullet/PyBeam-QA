from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import (QWidget, QMainWindow, QCheckBox)

from ui.py_ui.app_main_win_ui import Ui_MainWindow as Ui_AppMainWin
from ui.linac_qa.qa_tools_win import QAToolsWindow
from ui.linac_qa.trs398_widgets import PhotonsMainWindow, ElectronsMainWindow
from ui.linac_qa.starshot_widgets import StarshotMainWindow
from ui.linac_qa.winston_lutz_widgets import WinstonLutzMainWindow
from ui.linac_qa.picket_fence_widgets import PicketFenceMainWindow
from ui.linac_qa.field_analysis_widgets import FieldAnalysisMainWindow
from ui.linac_qa.planar_imaging_widgets import PlanarImagingMainWindow

from core import __app_name__
from core.tools.devices import DeviceManager

class AppMainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self._ui = Ui_AppMainWin()
        self._ui.setupUi(self)

        self.initSetupComplete = False

        self.setWindowTitle(__app_name__)
        self.setup_pages()

        self.initSetupComplete = True

    def setup_pages(self):
        # setup main page
        self._ui.navTabBtnGroup.buttonClicked.connect(self.change_nav_page)
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

    def setup_calibration_page(self, calibType: str):
        self.curr_linac = None
        self.beam_checkbox_list = []

        # setup daily/monthly photons page functionality
        self._ui.calibStartBtn.clicked.connect(lambda: "fake slot") # use fake slots so that we can disconnect past slots without errors
        self._ui.loadQABtn.clicked.connect(lambda: "fake slot")
        self._ui.backBtn.clicked.connect(lambda: "fake slot")
        self._ui.linacNameCB.currentTextChanged.connect(lambda x: "fake slot")
        self._ui.backBtn.clicked.disconnect()
        self._ui.backBtn.clicked.connect(lambda: self.change_main_page(self._ui.linacQAPage))
        self._ui.calibStartBtn.clicked.disconnect()
        self._ui.loadQABtn.clicked.disconnect()
        self._ui.linacNameCB.currentTextChanged.disconnect()
        self._ui.institutionLE.clear()
        self._ui.userLE.clear()
        self._ui.linacNameCB.clear()

        if calibType == "photons":
            self._ui.calibPageTitle.setText("Photon Output Calibration")
            self._ui.calibStartBtn.clicked.connect(lambda: self.init_photons_calib_qa())
            self._ui.loadQABtn.clicked.connect(lambda: PhotonsMainWindow.load_from_file(None))
            self._ui.linacNameCB.currentTextChanged.connect(lambda x: self.set_linac_details(calibType, x))   

        elif calibType == "electrons":
            self._ui.calibPageTitle.setText("Electron Output Calibration")
            self._ui.calibStartBtn.clicked.connect(lambda: self.init_electrons_calib_qa())
            self._ui.loadQABtn.clicked.connect(lambda: ElectronsMainWindow.load_from_file(None))
            self._ui.linacNameCB.currentTextChanged.connect(lambda x: self.set_linac_details(calibType, x))
        
        # Add all available linacs
        for linac in DeviceManager.device_list["linacs"]:
            self._ui.linacNameCB.addItem(linac.name)

    def set_linac_details(self, calibType: str, linacName: str):
        for linac in DeviceManager.device_list["linacs"]:
            if linacName == linac.name:
                self.curr_linac = linac
        
        # check if there are beams added prior and remove them
        self.beam_checkbox_list.clear()
        added_prior = self._ui.linacBeamsField.count()
                
        for i in range(added_prior):
            layout = self._ui.linacBeamsField.takeAt(0)
            widget = layout.widget()
            widget.deleteLater()

        # TODO check if these fields exist/make sure they exist but are empty
        self._ui.linacSerialNumField.setText(self.curr_linac.serial_num)
        self._ui.linacModelField.setText(self.curr_linac.model_name)
        self._ui.linacManufacField.setText(self.curr_linac.manufacturer)

        # add new beams
        if calibType == "photons":
            for i, beam in enumerate(self.curr_linac.beams["photons"]):
                check_box = QCheckBox(f"{beam} MV")
                self._ui.linacBeamsField.addWidget(check_box,i,0,1,1)
                self.beam_checkbox_list.append(check_box)

            for i,beam in enumerate(self.curr_linac.beams["photonsFFF"]):
                check_box = QCheckBox(f"{beam} MV FFF")
                self._ui.linacBeamsField.addWidget(check_box,i,1,1,1)
                self.beam_checkbox_list.append(check_box)

        elif calibType == "electrons":
            for i,beam in enumerate(self.curr_linac.beams["electrons"]):
                check_box = QCheckBox(f"{beam} MeV")
                self._ui.linacBeamsField.addWidget(check_box,i,0,1,1)
                self.beam_checkbox_list.append(check_box)

    def change_main_page(self, currWidget: QWidget):
        self._ui.mainStackWidget.setCurrentWidget(currWidget)

    def change_nav_page(self):
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
            self.setup_calibration_page("photons")
            self.change_main_page(self._ui.initCalibPage)

        elif event.type() == QEvent.Type.MouseButtonPress and source is self._ui.electronCalib:
            self.setup_calibration_page("electrons")
            self.change_main_page(self._ui.initCalibPage)

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
    
    def init_photons_calib_qa(self):
        init_data = {"institution": None,
                    "user": None,
                    "photon_beams": [],
                    "photon_fff_beams": [],
                    "linac": self.curr_linac}
        
        # get CheckBoxes and select the checked ones
        for beam_checkbox in self.beam_checkbox_list:
            if beam_checkbox.isChecked():
                if "FFF" in str(beam_checkbox.text()):
                    init_data["photon_fff_beams"].append(int(str(beam_checkbox.text())
                                    .split(" ")[0]))
                else:
                    init_data["photon_beams"].append(int(str(beam_checkbox.text())
                                    .split(" ")[0]))
                    
        init_data["institution"] = self._ui.institutionLE.text()
        init_data["user"] = self._ui.userLE.text()
        
        self.open_window("photon_cal", PhotonsMainWindow, init_data)

    def init_electrons_calib_qa(self):
        init_data = {"institution": None,
                    "user": None,
                    "electron_beams": [],
                    "linac": self.curr_linac}
        
        # retrieve checkboxes and select the checked ones
        for beam_checkbox in self.beam_checkbox_list:
            if beam_checkbox.isChecked():
                init_data["electron_beams"].append(int(str(beam_checkbox.text()).split(" ")[0]))
                    
        init_data["institution"] = self._ui.institutionLE.text()
        init_data["user"] = self._ui.userLE.text()
        
        self.open_window("electron_cal", ElectronsMainWindow, init_data)