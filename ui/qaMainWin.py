from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QToolButton, QMenu
from PySide6.QtCore import QObject, Signal, QDate, QPoint
from PySide6.QtGui import QAction, QCursor, QActionGroup

from ui.py_ui.photonsMainWin_ui import Ui_MainWindow as Ui_PhotonsMainWin
from ui.photonsWidget import QPhotonsWorksheet
from ui.wlutzWidget import QWLutzWorksheet
from core.tools.devices import Linac

class QAToolsWin(QMainWindow):
    def __init__(self, initData: dict = None):
        super().__init__()
        self.__ui = Ui_PhotonsMainWin()
        self.__ui.setupUi(self)
        self.worksheetType = None

        # disable the menu bar for now
        self.__ui.menubar.setEnabled(False)

        if initData is not None:
            if initData["toolType"] == "photon_calibration":
                self.setWindowTitle("(TRS-398) Photon Output Calibration ‒ PyBeam QA")

                # setup, add, and link photon calibration worksheets
                self.worksheetList = []
                self.dataModel = PhotonsCalModel()

                for beam in initData["photonBeams"]:
                    self.setupWorksheet(initData["linac"], beam, False)

                for beam in initData["photonFFFBeams"]:
                    self.setupWorksheet(initData["linac"], beam, True)

                self.dataModel.institution_changed.emit(initData["institution"])
                self.dataModel.userName_changed.emit(initData["user"])

            elif initData["toolType"] == "winston_lutz":
                self.worksheetType = "WL_WORKSHEET"

                self.setWindowTitle("Winston Lutz Analysis ‒ PyBeam QA")
                self.addNewWorksheet()

        # setup basic window functionality
        self.__ui.dockWidget.close()
        """
        self.sheetsCurrentViewButton = QPushButton()
        self.__ui.statusbar.addPermanentWidget(self.sheetsCurrentViewButton)
        
        self.__ui.actionDetailedView.toggled.connect(lambda detailedMode: self.toggleViewMode(detailedMode))
        self.__ui.actionDetailedView.setChecked(True)

        self.viewModeMenu = QMenu()
        self.actionGroup = QActionGroup(None)
        self.simpleViewAction = QAction("Simple view")
        self.detailedViewAction = QAction("Detailed view")
        self.viewModeMenu.addAction(self.simpleViewAction)
        self.viewModeMenu.addAction(self.detailedViewAction)
        self.actionGroup.addAction(self.simpleViewAction)
        self.actionGroup.addAction(self.detailedViewAction)
        
        self.sheetsCurrentViewButton.clicked.connect(lambda: self.viewModeMenu.popup(QCursor.pos()))"""

    def toggleViewMode(self, detailedMode: bool):
        if detailedMode:
            for worksheet in self.worksheetList:
                worksheet.toggleDetailedView()
                self.sheetsCurrentViewButton.setText("Detailed View On")

        else:
            for worksheet in self.worksheetList:
                worksheet.toggleSimpleView()
                self.sheetsCurrentViewButton.setText("Simple View On")

    def setupWorksheet(self, linac: Linac, beam: int, isFFF: bool):
        worksheet = QPhotonsWorksheet()
        worksheet.ui.nomAccPotLE.setText(f"{beam}")
        worksheet.ui.nomAccPotLE.setReadOnly(True)

        if isFFF:
            self.__ui.tabWidget.addTab(worksheet, f"{beam} MV FFF Beam")
            worksheet.ui.nomAccPotUnit.setText("MV (Flattening filter-free)")
        else:
            self.__ui.tabWidget.addTab(worksheet, f"{beam} MV Beam")

        #set ids for button group buttons
        worksheet.ui.beamQualityGroup.setId(worksheet.ui.cobaltRadioButton, 0)
        worksheet.ui.beamQualityGroup.setId(worksheet.ui.photonBeamRadioButton, 1)
        worksheet.ui.calibSeparateGroup.setId(worksheet.ui.calibSepYesRadioButton, 0)
        worksheet.ui.calibSeparateGroup.setId(worksheet.ui.calibSepNoRadioButton, 1)

        #send data changes to model
        worksheet.ui.institutionLE.textChanged.connect(self.dataModel.institution_changed)
        worksheet.ui.userLE.textChanged.connect(self.dataModel.userName_changed)
        worksheet.ui.dateDE.dateChanged.connect(self.dataModel.testDate_changed)
        worksheet.ui.nomDoseRateLE.textChanged.connect(self.dataModel.nomDoseRate_changed)
        worksheet.ui.IonChamberModelComboB.currentIndexChanged.connect(self.dataModel.ionChamber_changed)
        worksheet.ui.calibFactorLE.textChanged.connect(self.dataModel.chamberCalFactor_changed)
        worksheet.ui.chamberSerialNoLE.textChanged.connect(self.dataModel.chamberSerial_changed)
        worksheet.ui.calibLabLE.textChanged.connect(self.dataModel.chamberCalLab_changed)
        worksheet.ui.chamberCalibDE.dateChanged.connect(self.dataModel.chamberCalDate_changed)
        worksheet.ui.beamQualityGroup.buttonClicked.connect(lambda button:
            self.dataModel.chamberCalQual_changed.emit(worksheet.ui.beamQualityGroup.id(button)))
        worksheet.ui.polarPotV1LE.textChanged.connect(self.dataModel.calPolPotent_changed)
        worksheet.ui.electModelLE.textChanged.connect(self.dataModel.electroMModel_changed)
        worksheet.ui.electSerialNoLE.textChanged.connect(self.dataModel.electroMSerial_changed)
        worksheet.ui.electCalLabLE.textChanged.connect(self.dataModel.electroMCalLab_changed)
        worksheet.ui.electCalDateDE.dateChanged.connect(self.dataModel.electroMCalDate_changed)
        worksheet.ui.electRangeSettLE.textChanged.connect(self.dataModel.rangeSett_changed)
        worksheet.ui.calibSeparateGroup.buttonClicked.connect(lambda button:
            self.dataModel.calSeparate_changed.emit(worksheet.ui.calibSeparateGroup.id(button)))

        #receive data changes from model
        self.dataModel.institution_changed.connect(worksheet.ui.institutionLE.setText)
        self.dataModel.userName_changed.connect(worksheet.ui.userLE.setText)
        self.dataModel.testDate_changed.connect(worksheet.ui.dateDE.setDate)
        self.dataModel.nomDoseRate_changed.connect(worksheet.ui.nomDoseRateLE.setText)
        self.dataModel.ionChamber_changed.connect(worksheet.ui.IonChamberModelComboB.setCurrentIndex)
        self.dataModel.chamberCalFactor_changed.connect(worksheet.ui.calibFactorLE.setText)
        self.dataModel.chamberSerial_changed.connect(worksheet.ui.chamberSerialNoLE.setText)
        self.dataModel.chamberCalLab_changed.connect(worksheet.ui.calibLabLE.setText)
        self.dataModel.chamberCalDate_changed.connect(worksheet.ui.chamberCalibDE.setDate)
        self.dataModel.chamberCalQual_changed.connect(lambda id: 
            worksheet.ui.cobaltRadioButton.toggle() if id == 0 else 
            worksheet.ui.photonBeamRadioButton.toggle())
        self.dataModel.calPolPotent_changed.connect(worksheet.ui.polarPotV1LE.setText)
        self.dataModel.electroMModel_changed.connect(worksheet.ui.electModelLE.setText)
        self.dataModel.electroMSerial_changed.connect(worksheet.ui.electSerialNoLE.setText)
        self.dataModel.electroMCalLab_changed.connect(worksheet.ui.electCalLabLE.setText)
        self.dataModel.electroMCalDate_changed.connect(worksheet.ui.electCalDateDE.setDate)
        self.dataModel.rangeSett_changed.connect(worksheet.ui.electRangeSettLE.setText)
        self.dataModel.calSeparate_changed.connect(lambda id: 
            worksheet.ui.calibSepYesRadioButton.toggle() if id == 0 else 
            worksheet.ui.calibSepNoRadioButton.toggle())

        if linac is not None:
            worksheet.ui.linacNameLE.setText(f"{linac.name} ({linac.manufacturer} " +
                                        f"{linac.model_name})")
            worksheet.ui.linacNameLE.setReadOnly(True)
            worksheet.ui.linacNameLE.setClearButtonEnabled(False)
    
        self.worksheetList.append(worksheet)

    def addNewWorksheet(self):
        if self.worksheetType == "WL_WORKSHEET":
            worksheet = QWLutzWorksheet()
            self.__ui.tabWidget.addTab(worksheet, u"WL Analysis (Untitled)")

class PhotonsCalModel(QObject):
    institution_changed = Signal(str)
    userName_changed = Signal(str)
    testDate_changed = Signal(QDate)
    nomDoseRate_changed = Signal(str)
    ionChamber_changed = Signal(int)
    chamberCalFactor_changed = Signal(str)
    chamberSerial_changed = Signal(str)
    chamberCalLab_changed = Signal(str)
    chamberCalDate_changed = Signal(QDate)
    chamberCalQual_changed = Signal(int)
    calPolPotent_changed = Signal(str)
    electroMModel_changed = Signal(str)
    electroMSerial_changed = Signal(str)
    electroMCalLab_changed = Signal(str)
    electroMCalDate_changed = Signal(QDate)
    rangeSett_changed = Signal(str)
    calSeparate_changed = Signal(int)

    def __init__(self):
        super().__init__() 