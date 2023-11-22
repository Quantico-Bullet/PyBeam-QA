from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtGui import QPixmap, QIntValidator, QDoubleValidator
from core.tools.devices import Linac

from ui.py_ui.photonsWorksheet_ui import Ui_QPhotonsWorksheet
from ui.utilsWidgets.validators import DoubleValidator
from core.calibration.trs398 import TRS398Photons
from core.configuration.config import ChambersConfig, SettingsConfig
from ui.qaToolsWindow import QAToolsWindow

from pathlib import Path

import json

#TODO Move TRS398 Electrons here!

class BaseTRS398Window(QAToolsWindow):

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
    refPressure_changed = Signal(str)
    refTemperature_changed = Signal(str)
    refHumidity_changed = Signal(str)
    polarityEffectCorrected_changed = Signal(bool)
    calibrationPolarity_changed = Signal(int)
    calPolPotent_changed = Signal(str)
    electroMModel_changed = Signal(str)
    electroMSerial_changed = Signal(str)
    electroMCalLab_changed = Signal(str)
    electroMCalDate_changed = Signal(QDate)
    rangeSett_changed = Signal(str)
    calSeparate_changed = Signal(int)
    
    def __init__(self, initData: dict = None):
        super().__init__(initData)

        self.ui.menuFile.addAction("Open File", lambda: self.load_from_file(self), "Ctrl+O")
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction("Save Current Worksheet", lambda: self.save_worksheets(0), "Ctrl+S")
        self.ui.menuFile.addAction("Save All Worksheets", lambda: self.save_worksheets(1), 
                                   "Ctrl+Shift+S")

    def add_new_worksheet(self, worksheet, worksheet_name: str, enable_icon: bool = True):
        index = self.ui.tabWidget.addTab(worksheet, worksheet_name)

        if enable_icon:
            tab_icon = QPixmap(u":/colorIcons/icons/tools.png")
            tab_icon = tab_icon.scaled(16, 16, mode = Qt.TransformationMode.SmoothTransformation)

            self.ui.tabWidget.setCurrentIndex(index)
            self.ui.tabWidget.setTabIcon(index, tab_icon)

    def tab_window_changed(self, index: int):
        if self.ui.tabWidget.count() > 0:
            title = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())
            self.setWindowTitle(title + "  |  " + self.window_title)

        elif self.ui.tabWidget.count() == 0:
            self.close()

    @staticmethod
    def load_from_file(parent: QWidget) -> str | None:
        file, _ = QFileDialog.getOpenFileName(
            parent,
            "Open File",
            "",
            "PyBeam QA File (*.pybq)",
            ) 
        
        return file

class PhotonsMainWindow(BaseTRS398Window):
    
    def __init__(self, init_data: dict = None):
        super().__init__(init_data)

        self.window_title = "(TRS-398) Photon Output Calibration ‒ PyBeam QA"
        self.setWindowTitle(self.window_title)

        if init_data is not None:
            for beam in init_data["photon_beams"]:
                    self.setup_worksheets(init_data["linac"], beam, False)

            for beam in init_data["photon_fff_beams"]:
                self.setup_worksheets(init_data["linac"], beam, True)

            self.institution_changed.emit(init_data["institution"])
            self.userName_changed.emit(init_data["user"])

    def setup_worksheets(self, linac: str | Linac, beam_energy: int, isFFF: bool):
        worksheet = QPhotonsWorksheet()
        worksheet.ui.nomAccPotLE.setText(f"{beam_energy}")
        worksheet.ui.nomAccPotLE.setReadOnly(True)

        if isFFF:
            self.ui.tabWidget.addTab(worksheet, f"{beam_energy} MV FFF beam")
            worksheet.ui.nomAccPotUnit.setText("MV (FFF beam)")
        else:
            self.ui.tabWidget.addTab(worksheet, f"{beam_energy} MV beam")

        # Send data changes to other worksheets
        worksheet.ui.institutionLE.textChanged.connect(self.institution_changed)
        worksheet.ui.userLE.textChanged.connect(self.userName_changed)
        worksheet.ui.dateDE.dateChanged.connect(self.testDate_changed)
        worksheet.ui.nomDoseRateLE.textChanged.connect(self.nomDoseRate_changed)
        worksheet.ui.IonChamberModelComboB.currentIndexChanged.connect(self.ionChamber_changed)
        worksheet.ui.calibFactorLE.textChanged.connect(self.chamberCalFactor_changed)
        worksheet.ui.chamberSerialNoLE.textChanged.connect(self.chamberSerial_changed)
        worksheet.ui.calibLabLE.textChanged.connect(self.chamberCalLab_changed)
        worksheet.ui.chamberCalibDE.dateChanged.connect(self.chamberCalDate_changed)
        worksheet.ui.beamQualityGroup.buttonClicked.connect(lambda button:
            self.chamberCalQual_changed.emit(worksheet.ui.beamQualityGroup.id(button)))
        worksheet.ui.calibPolarityGroup.buttonClicked.connect(lambda button:
            self.calibrationPolarity_changed.emit(worksheet.ui.calibPolarityGroup.id(button)))
        worksheet.ui.refPressureLE.textChanged.connect(self.refPressure_changed)
        worksheet.ui.refTempLE.textChanged.connect(self.refTemperature_changed)
        worksheet.ui.refHumidityLE.textChanged.connect(self.refHumidity_changed)
        worksheet.ui.corrPolarEffCheckB.stateChanged.connect(lambda:
                self.polarityEffectCorrected_changed.emit(worksheet.ui.corrPolarEffCheckB.isChecked()))
        worksheet.ui.polarPotV1LE.textChanged.connect(self.calPolPotent_changed)
        worksheet.ui.electModelLE.textChanged.connect(self.electroMModel_changed)
        worksheet.ui.electSerialNoLE.textChanged.connect(self.electroMSerial_changed)
        worksheet.ui.electCalLabLE.textChanged.connect(self.electroMCalLab_changed)
        worksheet.ui.electCalDateDE.dateChanged.connect(self.electroMCalDate_changed)
        worksheet.ui.electRangeSettLE.textChanged.connect(self.rangeSett_changed)
        worksheet.ui.calibSeparateGroup.buttonClicked.connect(lambda button:
            self.calSeparate_changed.emit(worksheet.ui.calibSeparateGroup.id(button)))

        # Receive data changes from other worksheets
        self.institution_changed.connect(worksheet.ui.institutionLE.setText)
        self.userName_changed.connect(worksheet.ui.userLE.setText)
        self.testDate_changed.connect(worksheet.ui.dateDE.setDate)
        self.nomDoseRate_changed.connect(worksheet.ui.nomDoseRateLE.setText)
        self.ionChamber_changed.connect(worksheet.ui.IonChamberModelComboB.setCurrentIndex)
        self.chamberCalFactor_changed.connect(worksheet.ui.calibFactorLE.setText)
        self.chamberSerial_changed.connect(worksheet.ui.chamberSerialNoLE.setText)
        self.chamberCalLab_changed.connect(worksheet.ui.calibLabLE.setText)
        self.chamberCalDate_changed.connect(worksheet.ui.chamberCalibDE.setDate)
        self.chamberCalQual_changed.connect(lambda id: 
            worksheet.ui.cobaltRadioButton.toggle() if id == -2 else 
            worksheet.ui.photonBeamRadioButton.toggle())
        self.calibrationPolarity_changed.connect(lambda id: 
            worksheet.ui.calPosPolarRadioButton.toggle() if id == -2 else 
            worksheet.ui.calNegPolarRadioButton.toggle())
        self.refPressure_changed.connect(worksheet.ui.refPressureLE.setText)
        self.refTemperature_changed.connect(worksheet.ui.refTempLE.setText)
        self.refHumidity_changed.connect(worksheet.ui.refHumidityLE.setText)
        self.polarityEffectCorrected_changed.connect(lambda x: worksheet.ui.corrPolarEffCheckB.setChecked(x))
        self.calPolPotent_changed.connect(worksheet.ui.polarPotV1LE.setText)
        self.electroMModel_changed.connect(worksheet.ui.electModelLE.setText)
        self.electroMSerial_changed.connect(worksheet.ui.electSerialNoLE.setText)
        self.electroMCalLab_changed.connect(worksheet.ui.electCalLabLE.setText)
        self.electroMCalDate_changed.connect(worksheet.ui.electCalDateDE.setDate)
        self.rangeSett_changed.connect(worksheet.ui.electRangeSettLE.setText)
        self.calSeparate_changed.connect(lambda id: 
            worksheet.ui.calibSepYesRadioButton.toggle() if id == -2 else 
            worksheet.ui.calibSepNoRadioButton.toggle())
        
        if linac is not None:
            if isinstance(linac, Linac):
                worksheet.ui.linacNameLE.setText(f"{linac.name} ({linac.manufacturer} " +
                                        f"{linac.model_name})")
            else:
                worksheet.ui.linacNameLE.setText(linac)

            worksheet.ui.linacNameLE.setReadOnly(True)
            worksheet.ui.linacNameLE.setClearButtonEnabled(False)

        return worksheet

    @classmethod
    def load_from_file(cls, parent: QWidget):
        """
        Loads saved beam calibration worksheets from a PyBeam QA file
        """
        file_path = BaseTRS398Window.load_from_file(parent)

        if file_path:
            file_path = str(Path(file_path))

            with open(file_path, 'r', encoding="utf-8") as file:
                pybq_file = json.load(file)

            if "photon_output_calibration" in pybq_file:
                #TODO Add error dialog for failed file parsing
                win = cls()

                file_info = pybq_file["photon_output_calibration"]
                for worksheet_info in file_info["worksheets"]:
                    worksheet = win.setup_worksheets(file_info["linac_name"],
                                                     worksheet_info["beam_energy"],
                                                     worksheet_info["is_fff"])
                    
                    worksheet.ui.nomDoseRateLE.setText(str(worksheet_info["nominal_dose_rate"]))
                    worksheet.ui.beamQualityLE.setText(str(worksheet_info["nominal_dose_rate"]))
                    worksheet.ui.refPhantomComboB.setCurrentText(worksheet_info["reference_phantom"])
                    worksheet.ui.reffieldSizeComboB.setCurrentText(worksheet_info["reference_field_size"])
                    worksheet.ui.refDistanceLE.setText(str(worksheet_info["reference_distance"]))
                    worksheet.ui.refDepthLE.setText(str(worksheet_info["reference_depth"]))
                    worksheet.ui.rawDosReadLE.setText(str(worksheet_info["raw_dosimeter_reading_v1"]))
                    worksheet.ui.corrLinacMULE.setText(str(worksheet_info["corresponding_linac_mu"]))
                    worksheet.ui.userPressureLE.setText(str(worksheet_info["user_pressure"]))
                    worksheet.ui.userTempLE.setText(str(worksheet_info["user_temperature"]))
                    worksheet.ui.userHumidityLE.setText(str(worksheet_info["user_humidity"]))
                    worksheet.ui.readMPosLE.setText(str(worksheet_info["m_positive_reading"]))
                    worksheet.ui.readMNegLE.setText(str(worksheet_info["m_negative_reading"]))
                    worksheet.ui.normVoltageLE.setText(str(worksheet_info["v1_voltage"]))
                    worksheet.ui.redVoltageLE.setText(str(worksheet_info["v2_voltage"]))
                    worksheet.ui.normReadLE.setText(str(worksheet_info["m1_reading"]))
                    worksheet.ui.redReadLE.setText(str(worksheet_info["m2_reading"]))
                    worksheet.ui.depthDMaxLE.setText(str(worksheet_info["depth_dmax"]))
                    worksheet.ui.pddLE.setText(str(worksheet_info["pdd_zref"]))

                    (worksheet.ui.userPosPolarRadioButton.toggle() if worksheet_info["user_polarity"] == -2
                     else worksheet.ui.userNegPolarRadioButton.toggle())
                    
                    (worksheet.ui.pulsedRadioButton.toggle() if worksheet_info["beam_type"] == -2 
                     else worksheet.ui.pulsedScanRadioButton.toggle())
                    
                if file_info["worksheets"]:
                    worksheet_info = file_info["worksheets"][-1] # Use the last worksheet to get common info

                    worksheet.ui.userLE.setText(file_info["user"])
                    worksheet.ui.institutionLE.setText(file_info["institution"])
                    worksheet.ui.dateDE.setDate(QDate.fromString(file_info["date"], "dd/MM/yyyy"))

                    worksheet.ui.IonChamberModelComboB.setCurrentText(
                        file_info["ion_chamber"]["model_name"])
                    worksheet.ui.chamberSerialNoLE.setText(
                        file_info["ion_chamber"]["serial_no"])
                    worksheet.ui.calibFactorLE.setText(
                        str(file_info["ion_chamber"]["calibration_factor"]))
                    worksheet.ui.calibLabLE.setText(
                        str(file_info["ion_chamber"]["calibration_lab"]))
                    worksheet.ui.chamberCalibDE.setDate(
                        QDate.fromString(file_info["ion_chamber"]["calibration_date"], "dd/MM/yyyy"))
                    worksheet.ui.wSleeveMatlLE.setText(
                        file_info["ion_chamber"]["water_proof_sleeve_mat"])
                    worksheet.ui.wSleeveThickLE.setText(
                        str(file_info["ion_chamber"]["water_proof_sleeve_thick"]))
                    worksheet.ui.refPressureLE.setText(
                        str(file_info["ion_chamber"]["reference_pressure"]))
                    worksheet.ui.refTempLE.setText(
                        str(file_info["ion_chamber"]["reference_temperature"]))
                    worksheet.ui.refHumidityLE.setText(
                        str(file_info["ion_chamber"]["reference_humidity"]))
                    worksheet.ui.polarPotV1LE.setText(
                        str(file_info["ion_chamber"]["polarizing_potential"]))
                    
                    (worksheet.ui.cobaltRadioButton.toggle() if 
                    file_info["ion_chamber"]["calibration_quality"] == -2 else
                      worksheet.ui.photonBeamRadioButton.toggle())
                    worksheet.ui.corrPolarEffCheckB.setChecked(
                        file_info["ion_chamber"]["polarity_effect_corrected"])

                    worksheet.ui.electModelLE.setText(
                        file_info["electrometer"]["model_name"])
                    worksheet.ui.electSerialNoLE.setText(
                        file_info["electrometer"]["serial_no"])
                    worksheet.ui.electCalLabLE.setText(
                        file_info["electrometer"]["calibration_lab"])
                    worksheet.ui.electCalDateDE.setDate(QDate.fromString(
                        file_info["electrometer"]["calibration_date"], "dd/MM/yyyy"))
                    worksheet.ui.electRangeSettLE.setText(
                        file_info["electrometer"]["range_setting"])

                win.showMaximized()
                
    def save_worksheets(self, save_mode: int):
        """
        Saves calibration worksheets to a PyBeam QA file

        Parameters
        -----------
        save_mode: `int`
            - The mode for saving worksheets. 0 saves the current worksheet, 1 saves all worksheets
        """
        worksheet_info = []

        if save_mode == 0:
            index = self.ui.tabWidget.currentIndex()
            worksheet: QPhotonsWorksheet = self.ui.tabWidget.widget(index)
            worksheet_info.append(worksheet.save_worksheet_info())

        elif save_mode == 1:
            for index in range(self.ui.tabWidget.count()):
                worksheet: QPhotonsWorksheet = self.ui.tabWidget.widget(index)
                worksheet_info.append(worksheet.save_worksheet_info())

        # Use the last worksheet to extract worksheet common information
        basic_info = {}
        ion_chamber_info = {}
        electrometer_info = {}

        basic_info["user"] = worksheet.ui.userLE.text()
        basic_info["institution"] = worksheet.ui.institutionLE.text()
        basic_info["date"] = worksheet.ui.dateDE.text()
        basic_info["linac_name"] = worksheet.ui.linacNameLE.text()

        ion_chamber_info["model_name"] = worksheet.ui.IonChamberModelComboB.currentText()
        ion_chamber_info["serial_no"] = worksheet.ui.chamberSerialNoLE.text()
        ion_chamber_info["calibration_factor"] = type_convert(float, worksheet.ui.calibFactorLE.text())
        ion_chamber_info["calibration_lab"] = worksheet.ui.calibLabLE.text()
        ion_chamber_info["calibration_date"] = worksheet.ui.chamberCalibDE.text()
        ion_chamber_info["water_proof_sleeve_mat"] = worksheet.ui.wSleeveMatlLE.text()
        ion_chamber_info["water_proof_sleeve_thick"] = type_convert(float, worksheet.ui.wSleeveThickLE.text())
        ion_chamber_info["reference_pressure"] = type_convert(float, worksheet.ui.refPressureLE.text())
        ion_chamber_info["reference_temperature"] = type_convert(float, worksheet.ui.refTempLE.text())
        ion_chamber_info["reference_humidity"] = type_convert(float, worksheet.ui.refHumidityLE.text())
        ion_chamber_info["polarizing_potential"] = type_convert(int, worksheet.ui.polarPotV1LE.text())
        ion_chamber_info["calibration_quality"] = worksheet.ui.beamQualityGroup.checkedId()
        ion_chamber_info["calibration_polarity"] = worksheet.ui.calibPolarityGroup.checkedId()
        ion_chamber_info["polarity_effect_corrected"] = worksheet.ui.corrPolarEffCheckB.isChecked()

        electrometer_info["model_name"] = worksheet.ui.electModelLE.text()
        electrometer_info["serial_no"] = worksheet.ui.electSerialNoLE.text()
        electrometer_info["calibration_lab"] = worksheet.ui.electCalLabLE.text()
        electrometer_info["calibration_date"] = worksheet.ui.electCalDateDE.text()
        electrometer_info["range_setting"] = worksheet.ui.electRangeSettLE.text()

        file_info = {"photon_output_calibration": {}}
        file_info["photon_output_calibration"].update(basic_info)
        file_info["photon_output_calibration"].update({"ion_chamber": ion_chamber_info})
        file_info["photon_output_calibration"].update({"electrometer": electrometer_info})
        file_info["photon_output_calibration"].update({"worksheets": worksheet_info})

        save_path = self.save_worksheets_to()

        if save_path:
            with open(save_path, 'w', encoding="utf-8") as file:
                json.dump(file_info, file, ensure_ascii=False, indent=4)

    def save_worksheets_to(self) -> str | None:
        file_path = QFileDialog.getSaveFileName(caption="Save As...", filter="PyBeam QA File (*.pybq)")
        
        if file_path[0] != "":
            path = file_path[0].split("/")
            
            if not path[-1].endswith(".pybq"):
                path[-1] = path[-1] + ".pybq"
            
            return "/".join(path)
        
        else:
            return None

class QPhotonsWorksheet(QWidget):

    beam_type = 0 # 0 for a flattened beam and 1 for FFF

    def __init__(self):
        super().__init__()
        self.ui = Ui_QPhotonsWorksheet()
        self.ui.setupUi(self)

        self.initSetupComplete = False
        self.trs398 = TRS398Photons()
        self.chambersConfig = ChambersConfig()
        self.settingsConfig = SettingsConfig()

        self.hide_cal_outcome()

        # Load all ionization chambers
        self.allChambers = []
        self.set_ion_chamber_list()

        #--- Set up basic functionality ---
        self.ui.dateDE.setDate(QDate.currentDate())
        self.ui.dateDE.setMaximumDate(QDate.currentDate())
        self.ui.chamberCalibDE.setMaximumDate(QDate.currentDate())
        self.ui.electCalDateDE.setMaximumDate(QDate.currentDate())

        self.ui.calibSetupGroup.buttonClicked.connect(self.cal_setup_changed)
        self.cal_setup_changed()
        self.ui.calibSeparateGroup.idToggled.connect(self.same_calib) # use idToggled to allow other tab signals to enable fields
        self.same_calib()
        self.ui.IonChamberModelComboB.currentIndexChanged.connect(self.chamber_model_changed)
        self.chamber_model_changed()
        self.ui.calibSetupGroup.buttonClicked.connect(self.set_zmax_depth_dose)
        self.ui.IonChamberModelComboB.currentIndexChanged.connect(self.calc_kq)
        self.ui.beamQualityLE.textChanged.connect(self.calc_kq)
        self.ui.refPressureLE.textChanged.connect(self.calc_ktp)
        self.ui.refTempLE.textChanged.connect(self.calc_ktp)
        self.ui.refHumidityLE.textChanged.connect(self.calc_ktp)
        self.ui.userPressureLE.textChanged.connect(self.calc_ktp)
        self.ui.userTempLE.textChanged.connect(self.calc_ktp)
        self.ui.userHumidityLE.textChanged.connect(self.calc_ktp)
        self.ui.kElecLE_2.textChanged.connect(self.set_kelec)
        self.ui.kElecLE_2.textChanged.connect(self.set_ref_depth_dose)
        self.ui.userPolarityGroup.buttonClicked.connect(self.cal_kpol)
        self.ui.readMPosLE.textChanged.connect(self.cal_kpol)
        self.ui.readMNegLE.textChanged.connect(self.cal_kpol)
        self.ui.beamTypeGroup.buttonClicked.connect(self.calc_ks)
        self.ui.normReadLE.textChanged.connect(self.calc_ks)
        self.ui.redReadLE.textChanged.connect(self.calc_ks)
        self.ui.normVoltageLE.textChanged.connect(self.calc_ks)
        self.ui.redVoltageLE.textChanged.connect(self.calc_ks)
        self.ui.rawDosReadLE.textChanged.connect(self.set_ratio_read_mu)
        self.ui.corrLinacMULE.textChanged.connect(self.set_ratio_read_mu)
        self.ui.ratioReadMULE.setReadOnly(True)
        self.ui.ratioReadMULE.textChanged.connect(self.set_ref_depth_dose)
        self.ui.calibFactorLE.textChanged.connect(self.set_ndw)
        self.ui.calibFactorLE.textChanged.connect(self.set_ref_depth_dose)
        self.ui.kQLE.textChanged.connect(self.set_ref_depth_dose)
        self.ui.kSLE.textChanged.connect(self.set_ref_depth_dose)
        self.ui.kSLE.textChanged.connect(self.check_ks_value)
        self.ui.kTPLE.textChanged.connect(self.set_ref_depth_dose)
        self.ui.kElecLE.textChanged.connect(self.set_ref_depth_dose)
        self.ui.kPolLE.textChanged.connect(self.set_ref_depth_dose)
        self.ui.zrefDoseLE.textChanged.connect(self.set_zmax_depth_dose)
        self.ui.pddLE.textChanged.connect(self.set_zmax_depth_dose)

        # Add validators to text fields (QLineEdit)
        self.ui.nomDoseRateLE.setValidator(DoubleValidator(1.0, 1000, 4))
        self.ui.beamQualityLE.setValidator(DoubleValidator(0.5, 0.84, 4))
        self.ui.refDistanceLE.setValidator(DoubleValidator(50.0, 120, 2))
        self.ui.refDepthLE.setValidator(DoubleValidator(5.0,10.0, 1))
        dVal = QDoubleValidator()
        dVal.setDecimals(4)
        self.ui.calibFactorLE.setValidator(dVal)
        self.ui.wSleeveThickLE.setValidator(dVal)
        self.ui.pWinThickLE.setValidator(dVal)
        self.ui.refPressureLE.setValidator(DoubleValidator(50.0, 115, 3))
        self.ui.refTempLE.setValidator(DoubleValidator(10, 50, 3))
        self.ui.refHumidityLE.setValidator(DoubleValidator(0,100,3))
        self.ui.polarPotV1LE.setValidator(QIntValidator())
        self.ui.rawDosReadLE.setValidator(dVal)
        self.ui.corrLinacMULE.setValidator(dVal)
        self.ui.userPressureLE.setValidator(DoubleValidator(50.0, 115, 3))
        self.ui.userTempLE.setValidator(DoubleValidator(10, 50, 3))
        self.ui.userHumidityLE.setValidator(DoubleValidator(0,100,3))
        self.ui.readMPosLE.setValidator(dVal)
        self.ui.readMNegLE.setValidator(dVal)
        self.ui.normVoltageLE.setValidator(dVal)
        self.ui.redVoltageLE.setValidator(dVal)
        self.ui.normReadLE.setValidator(dVal)
        self.ui.redReadLE.setValidator(dVal)
        self.ui.depthDMaxLE.setValidator(dVal)
        self.ui.pddLE.setValidator(DoubleValidator(0.0, 100.0, 2))
        self.ui.tmrLE.setValidator(dVal)

        # set reference condition values
        self.ui.refTempLE.setText(f"{self.trs398.refTemp}")
        self.ui.refPressureLE.setText(f"{self.trs398.refPress}")

        self.initSetupComplete = True
        self.calibStatus = None

    def set_ion_chamber_list(self):
        self.chambers = self.chambersConfig.getConfig()
        self.allChambers.extend(self.chambers["cylindrical"])

        self.allChambers.sort()   
        self.ui.IonChamberModelComboB.addItems(self.allChambers)

    def chamber_model_changed(self):
        currentChamber = self.ui.IonChamberModelComboB.currentText()

        for type in self.chambers:
            if currentChamber in self.chambers[type]:
                self.ui.cWallMatLE.setText(self.chambers[type][currentChamber]["wall_material"])
                self.ui.cWallThickLE.setText(str(self.chambers[type][currentChamber]["wall_thickness"]))

    def cal_setup_changed(self):
        if self.ui.calibSetupGroup.checkedButton() == self.ui.ssdRadioButton:
            self.ui.setupSW.setCurrentIndex(0)
        else: self.ui.setupSW.setCurrentIndex(1)

    def same_calib(self):
        if self.ui.calibSeparateGroup.checkedButton() == self.ui.calibSepNoRadioButton:
            self.ui.electCalDateDE.setDate(self.ui.chamberCalibDE.date())
            self.ui.electCalDateDE.setEnabled(False)
            self.ui.electCalLabLE.setEnabled(False)
            self.ui.electmeterCorrSpacer.hide()
            self.ui.electmeterCorrLabel.hide()
            self.ui.kElecLabel_2.hide()
            self.ui.kElecLE_2.hide()
            self.ui.kElecLE_2.clear()
            self.ui.kElecLE.setText("1.000")
            self.trs398.kElec_corr(1.000)

        else:
            self.ui.electCalLabLE.clear()
            self.ui.electCalDateDE.setEnabled(True)
            self.ui.electCalLabLE.setEnabled(True)
            self.ui.electmeterCorrSpacer.show()
            self.ui.electmeterCorrLabel.show()
            self.ui.kElecLabel_2.show()
            self.ui.kElecLE_2.show()
            self.ui.kElecLE.clear() # kElec will still be 1.00 in TRS class until set

    def calc_kq(self):
        currChamber = self.ui.IonChamberModelComboB.currentText()
        tprValue = self.ui.beamQualityLE.text()

        chambers = self.chambersConfig.getConfig()

        if tprValue != "":
            for chamberType in chambers:
                if currChamber in chambers[chamberType]:
                    tpr_kQ: dict = chambers[chamberType][currChamber]["tpr_kQ"]
                    kQ = self.trs398.tpr2010_to_kQ(float(tprValue), tpr_kQ)
                    self.ui.kQLE.setText("%.3f" % kQ)
        else:
            self.ui.kQLE.clear()

    def calc_ktp(self):
        userTemp = self.ui.userTempLE.text()
        userPress = self.ui.userPressureLE.text()
        userHumid = self.ui.userHumidityLE.text()

        if userTemp != "" and userPress != "" and userHumid != "":
            kTP = self.trs398.kTP_corr(float(userTemp), float(userPress))
            self.ui.kTPLE.setText("%.3f" % kTP)
        else:
            self.ui.kTPLE.clear()

    def cal_kpol(self):
        mPos = self.ui.readMPosLE.text()
        mNeg = self.ui.readMNegLE.text()

        if mPos != "" and mNeg != "":
            if self.ui.userPolarityGroup.checkedButton() == self.ui.userPosPolarRadioButton:
                isPosPref = True
            else:
                isPosPref = False

            kPol = self.trs398.kPol_corr(float(mPos), float(mNeg), isPosPref)
            self.ui.kPolLE.setText("%.3f" % kPol)
        else:
            self.ui.kPolLE.clear()

    def calc_ks(self):

        correct_input = (self.ui.normVoltageLE.hasAcceptableInput() and
                         self.ui.redVoltageLE.hasAcceptableInput() and
                         self.ui.normReadLE.hasAcceptableInput() and
                         self.ui.redReadLE.hasAcceptableInput()
        )

        if correct_input:
            vNorm = float(self.ui.normVoltageLE.text())
            vRed = float(self.ui.redVoltageLE.text())
            mNorm = float(self.ui.normReadLE.text())
            mRed = float(self.ui.redReadLE.text())

            if self.ui.beamTypeGroup.checkedButton() == self.ui.pulsedScanRadioButton:
                isPulsedScanned = True
            else:
                isPulsedScanned = False
            
            kS = self.trs398.kS_corr(vNorm, vRed, mNorm, mRed, isPulsedScanned)
            self.ui.kSLE.setText("%.3f" % kS)
        else:
            self.ui.kSLE.clear()

    def check_ks_value(self):
        if self.ui.kSLE.text() != "":
            kS = float(self.ui.kSLE.text())
            vNorm = float(self.ui.normVoltageLE.text())
            vRed = float(self.ui.redVoltageLE.text())
            mNorm = float(self.ui.normReadLE.text())
            mRed = float(self.ui.redReadLE.text())

            kS = kS - 1.0
            kS_test = ((mNorm/mRed) - 1.0) / ((vNorm/vRed) - 1.0)

            if abs(kS - kS_test) <= 0.01:
                pixmap = QPixmap(u":/colorIcons/icons/correct.png")
                pixmap = pixmap.scaled(24, 24, mode = Qt.TransformationMode.SmoothTransformation)
                self.ui.ks_status_icon.setPixmap(pixmap)

            else:
                pixmap = QPixmap(u":/colorIcons/icons/warning.png")
                pixmap = pixmap.scaled(24, 24, mode = Qt.TransformationMode.SmoothTransformation)
                self.ui.ks_status_icon.setPixmap(pixmap)

            self.ui.ks_status_icon.show()

        else:
            self.ui.ks_status_icon.hide()
    
    def set_kelec(self):
        kElec = self.ui.kElecLE_2.text()

        if kElec != "":
            self.ui.kElecLE.setText("%.3f" % self.trs398.kElec_corr(float(kElec)))
        else:
            self.ui.kElecLE.clear()

    def set_ratio_read_mu(self):
        correct_input = (self.ui.rawDosReadLE.hasAcceptableInput() and 
                         self.ui.corrLinacMULE.hasAcceptableInput())

        if correct_input:
            rawRead = float(self.ui.rawDosReadLE.text())
            linacMU = float(self.ui.corrLinacMULE.text())

            self.trs398.mRaw = rawRead / linacMU
            self.ui.ratioReadMULE.setText("%.5f" % (rawRead / linacMU))
        else:
            self.ui.ratioReadMULE.clear()

    def set_ndw(self):
        if self.ui.calibFactorLE.hasAcceptableInput:
            self.trs398.nDW = float(self.ui.calibFactorLE.text())

    def set_ref_depth_dose(self):
        kTP = self.ui.kTPLE.text()
        kS = self.ui.kSLE.text()
        kElec = self.ui.kElecLE.text()
        kPol = self.ui.kPolLE.text()
        kQ = self.ui.kQLE.text()
        ratioRead = self.ui.ratioReadMULE.text()
        nDw = self.ui.calibFactorLE.text()

        areAllValid = (kTP != "" and kS != "" and kElec != "" and kPol != "" and kQ != "" and ratioRead != ""
            and nDw != "")

        if areAllValid:
            self.ui.zrefDoseLE.setText(("%.3f" % (self.trs398.get_DwQ_zref()*100.0)) + " cGy/MU")
        else:
            self.ui.zrefDoseLE.clear()

    def set_zmax_depth_dose(self):
        if self.ui.calibSetupGroup.checkedButton() == self.ui.ssdRadioButton:
            zRefDD = self.ui.zrefDoseLE.text()
            pddzRef = self.ui.pddLE.text()

            if zRefDD != "" and pddzRef != "":
                dMax = self.trs398.get_DwQ_zmax_ssdSetup(float(pddzRef))*100.0
                self.ui.zmaxDoseLE.setText("%.3f" % dMax + " cGy/MU")
                self.setOutcome(dMax)
            else:
                self.ui.zmaxDoseLE.clear()
                self.ui.outcomeLE.clear()
                self.hide_cal_outcome()
        else:
            zRefDD = self.ui.zrefDoseLE.text()
            tmrRef = self.ui.tmrLE.text()

            if zRefDD != "" and pddzRef != "":
                dMax = self.trs398.get_DwQ_zmax_tmrSetup(float(tmrRef))*100.0
                self.ui.zmaxDoseLE.setText("%.3f" % dMax + " cGy/MU")
                self.setOutcome(dMax)
            else:
                self.ui.zmaxDoseLE.clear()
                self.ui.outcomeLE.clear()
                self.hide_cal_outcome()

    def setOutcome(self, dMax: float):
        tol = self.settingsConfig.getConfig()["trs398"]["tolerance"]
        diff = abs(dMax - 1.00)

        if  diff <= tol:
            self.ui.outcomeLE.setText(
            "PASS -- with a deviation of {}%".format("%.2f" % (diff*100.0)))

            self.ui.outcomeLE.setStyleSheet(u"border-color: rgb(95, 200, 26);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(95, 200, 26, 150);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
        else:
            self.ui.outcomeLE.setText(
            "FAIL -- with a deviation of {}%".format("%.2f" % (diff*100.0)))

            self.ui.outcomeLE.setStyleSheet(u"border-color: rgb(231, 29, 14);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(231, 29, 14, 150);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")

        self.ui.gen_report_btn.setEnabled(True)
        
    def hide_cal_outcome(self):
        self.ui.outcomeLE.setStyleSheet(u"border-color: rgba(0, 0, 0,0);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(0, 0, 0, 0);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
        
        self.ui.gen_report_btn.setEnabled(False)
    
    def toggleSimpleView(self):
        #Check QT form structure before editing row numbers to hide

        #hide section one fields
        rowsToHide = [2]
        for row in rowsToHide:
            self.ui.sectionOneFL.setRowVisible(row, False)

        #hide section two fields
        rowsToHide = [1, 3, 4, 5, 6, 7, 10, 16, 17, 18, 19, 20]
        for row in rowsToHide:
            self.ui.sectionTwoFL.setRowVisible(row, False)

        #hide section four fields
        rowsToHide = [0, 1]
        for row in rowsToHide:
            self.ui.depthDMaxFL.setRowVisible(row, False)

    def toggle_detailed_view(self):
        #show section one fields
        for row in range(self.ui.sectionOneFL.rowCount()):
            self.ui.sectionOneFL.setRowVisible(row, True)

        #show section two fields
        for row in range(self.ui.sectionTwoFL.rowCount()):
            self.ui.sectionTwoFL.setRowVisible(row, True)

        #show section four fields
        for row in range(self.ui.depthDMaxFL.rowCount()):
            self.ui.depthDMaxFL.setRowVisible(row, True)

    def save_worksheet_info(self) -> dict:
        worksheet_info = {}

        #TODO replace use of type conversion with QtValidators
        worksheet_info["beam_energy"] = type_convert(int, self.ui.nomAccPotLE.text())
        worksheet_info["is_fff"] = True if "(FFF" in self.ui.nomAccPotUnit.text() else False
        worksheet_info["nominal_dose_rate"] = type_convert(float, self.ui.nomDoseRateLE.text())
        worksheet_info["setup_type"] = self.ui.calibSetupGroup.checkedId()  
        worksheet_info["reference_phantom"] = self.ui.refPhantomComboB.currentText()
        worksheet_info["reference_field_size"] = self.ui.reffieldSizeComboB.currentText()
        worksheet_info["reference_distance"] = type_convert(float, self.ui.refDistanceLE.text())
        worksheet_info["reference_depth"] = type_convert(float, self.ui.refDepthLE.text())
        worksheet_info["user_polarity"] = self.ui.userPolarityGroup.checkedId()
        worksheet_info["raw_dosimeter_reading_v1"] = type_convert(float, self.ui.rawDosReadLE.text())
        worksheet_info["corresponding_linac_mu"] = type_convert(float, self.ui.corrLinacMULE.text())
        worksheet_info["user_pressure"] = type_convert(float, self.ui.userPressureLE.text())
        worksheet_info["user_temperature"] = type_convert(float, self.ui.userTempLE.text())
        worksheet_info["user_humidity"] = type_convert(float, self.ui.userHumidityLE.text())
        worksheet_info["m_positive_reading"] = type_convert(float, self.ui.readMPosLE.text())
        worksheet_info["m_negative_reading"] = type_convert(float, self.ui.readMNegLE.text())
        worksheet_info["v1_voltage"] = type_convert(int, self.ui.normVoltageLE.text())
        worksheet_info["v2_voltage"] = type_convert(int, self.ui.redVoltageLE.text())
        worksheet_info["m1_reading"] = type_convert(float, self.ui.normReadLE.text())
        worksheet_info["m2_reading"] = type_convert(float, self.ui.redReadLE.text())
        worksheet_info["beam_type"] = self.ui.beamTypeGroup.checkedId()
        worksheet_info["depth_dmax"] = type_convert(float, self.ui.depthDMaxLE.text())
        worksheet_info["pdd_zref"] = type_convert(float, self.ui.pddLE.text())
        worksheet_info["tmr_zref"] = type_convert(float, self.ui.tmrLE.text())

        return worksheet_info

def type_convert(conversion_type, arg):
    try:
        return conversion_type(arg)
    except ValueError:
        return ""