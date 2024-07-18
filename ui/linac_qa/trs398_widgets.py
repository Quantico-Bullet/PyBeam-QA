from PySide6.QtWidgets import (QWidget, QFileDialog, QLineEdit,
                               QComboBox, QPlainTextEdit, QPushButton,
                               QHBoxLayout, QVBoxLayout, QCheckBox, QLabel,
                               QSizePolicy, QSpacerItem, QFormLayout, 
                               QDialogButtonBox, QDialog)
from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtGui import QPixmap, QIntValidator
from core.tools.devices import Linac

from ui.py_ui.photons_worksheet_ui import Ui_QPhotonsWorksheet
from ui.py_ui.electrons_worksheet_ui import Ui_QElectronsWorksheet
from ui.util_widgets import worksheet_save_report
from ui.util_widgets.validators import DoubleValidator
from ui.util_widgets.dialogs import MessageDialog
from core.tools.report import PhotonCalibrationReport, ElectronCalibrationReport
from core.calibration.trs398 import TRS398Photons, TRS398Electrons
from core.configuration.config import ChambersConfig, SettingsConfig
from ui.linac_qa.qa_tools_win import QAToolsWindow
from ui.preferences.prefs_main import Preferences

from pathlib import Path

from copy import copy
import json
import webbrowser

#TODO Move TRS398 Electrons here!

class BaseTRS398Window(QAToolsWindow):

    institution_changed = Signal(str)
    userName_changed = Signal(str)
    testDate_changed = Signal(QDate)
    tolerance_changed = Signal(float)
    setupType_changed = Signal(int)
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
        self.ui.menuFile.addAction("Save All Worksheets", lambda: self.save_worksheets_as(1), "Ctrl+S")
        self.ui.menuFile.addAction("Save Current Worksheet", lambda: self.save_worksheets_as(0), 
                                   "Ctrl+Shift+S")
        self.ui.menuFile.addSeparator()
        gen_report_menu = self.ui.menuFile.addMenu("Generate Report")
        gen_report_menu.hide()
        self.gen_rep_curr_action = gen_report_menu.addAction("Current Worksheet")
        self.gen_rep_curr_action.triggered.connect(lambda: self.save_worksheets_as(0,1))
        self.gen_rep_curr_action.setEnabled(False)
        self.gen_rep_all_action = gen_report_menu.addAction("All Complete Worksheets")
        self.gen_rep_all_action.triggered.connect(lambda: self.save_worksheets_as(1,1))
        self.gen_rep_all_action.setEnabled(True)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction("Preferences", self.show_preferences)

    def show_preferences(self):
        self.preferences = Preferences()
        self.preferences.exec()

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

            tab: QPhotonsWorksheet | QElectronsWorksheet = self.ui.tabWidget.widget(index)
            
            self.gen_rep_curr_action.setEnabled(
                tab.ui.gen_report_btn.isEnabled())

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

    def generate_report(self, calibration_info: dict):

        num_beams = self.ui.tabWidget.count()
        num = len(calibration_info["worksheets"])

        if num == 0: 
            no_reports_dialog = MessageDialog()
            no_reports_dialog.set_title("Info")
            no_reports_dialog.set_header_text("No complete calibration worksheets found!")
            no_reports_dialog.set_info_text("Please complete at least one calibration worksheet to " + 
                                            "generate a report")
            no_reports_dialog.set_icon(MessageDialog.INFO_ICON)

            no_reports_dialog.exec()

            return

        worksheet: QPhotonsWorksheet | QElectronsWorksheet = \
        self.ui.tabWidget.widget(0)

        physicist_name_le = QLineEdit()
        institution_name_le = QLineEdit()
        treatment_unit_le = QLineEdit()
        comments_te = QPlainTextEdit()
        physicist_name_le.setMaximumWidth(250)
        physicist_name_le.setMinimumWidth(250)
        institution_name_le.setMaximumWidth(350)
        institution_name_le.setMinimumWidth(350)
        treatment_unit_le.setMaximumWidth(250)
        treatment_unit_le.setMinimumWidth(250)

        # Set the fields from the first worksheet
        # TODO Put worksheet date on report 
        physicist_name_le.setText(worksheet.ui.userLE.text())
        institution_name_le.setText(worksheet.ui.institutionLE.text())
        treatment_unit_le.setText(worksheet.ui.linacNameLE.text())

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

        num_beams_reported =  QLabel()

        num_beams_reported.setText(f"{num} of {num_beams} " \
                "beam energies to be included in the report.")
        
        user_details_layout = QFormLayout()
        user_details_layout.addRow("Physicist:", physicist_name_le)
        user_details_layout.addRow("Treatment unit:", treatment_unit_le)
        user_details_layout.addRow("Institution:", institution_name_le)
        user_details_layout.addRow("Save location:", save_location_layout)
        user_details_layout.addRow("Comments:", comments_te)
        user_details_layout.addRow("", num_beams_reported)
        user_details_layout.addRow("", QLabel())
        user_details_layout.addRow("", show_report_layout)
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
        report_dialog.setWindowTitle("Generate Beam Calibration Report ‒ PyBeam QA")
        report_dialog.setLayout(layout)
        report_dialog.setMinimumSize(report_dialog.sizeHint())
        report_dialog.setMaximumSize(report_dialog.sizeHint())

        cancel_button.clicked.connect(report_dialog.reject)
        save_button.clicked.connect(report_dialog.accept)
        save_win_btn.clicked.connect(
            lambda: save_path_le.setText(worksheet_save_report(report_dialog)))

        result = report_dialog.exec()

        if result == QDialog.DialogCode.Accepted:

            calibration_info["comments"] = comments_te.toPlainText()

            if isinstance(worksheet, QPhotonsWorksheet):
                report = PhotonCalibrationReport(filename=save_path_le.text(),
                                                 calibration_info=calibration_info)
                report.save_report()
            
            else:
                report = ElectronCalibrationReport(filename=save_path_le.text(),
                                                 calibration_info=calibration_info)
                report.save_report()

            if show_report_checkbox.isChecked():
                webbrowser.open(save_path_le.text())

    def save_pybq_to(self) -> str | None:
        file_path = QFileDialog.getSaveFileName(caption="Save As...", 
                                                filter="PyBeam QA File (*.pybq)")
        
        if file_path[0] != "":
            path = file_path[0].split("/")
            
            if not path[-1].endswith(".pybq"):
                path[-1] = path[-1] + ".pybq"
            
            return "/".join(path)
        
        else:
            return None

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

            # Hide the volume averaging correction factor row
            worksheet.ui.corrFactorFL.setRowVisible(4, False)
            worksheet.ui.scrollArea.setMinimumSize(0, 340)

        # Send data changes to other worksheets
        worksheet.ui.institutionLE.textChanged.connect(self.institution_changed)
        worksheet.ui.userLE.textChanged.connect(self.userName_changed)
        worksheet.ui.dateDE.dateChanged.connect(self.testDate_changed)
        worksheet.ui.toleranceDSB.valueChanged.connect(self.tolerance_changed)
        worksheet.ui.calibSetupGroup.buttonClicked.connect(lambda button: 
            self.setupType_changed.emit(worksheet.ui.calibSetupGroup.id(button)))
        worksheet.ui.gen_report_btn.clicked.connect(lambda: self.save_worksheets_as(0,1))
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
        self.tolerance_changed.connect(worksheet.ui.toleranceDSB.setValue)
        self.setupType_changed.connect(lambda id: 
            worksheet.ui.ssdRadioButton.toggle() if id == -2 else 
            worksheet.ui.sadRadioButton.toggle())
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
                    
                    worksheet.ui.nomDoseRateLE.setText(worksheet_info["nominal_dose_rate"])
                    worksheet.ui.beamQualityLE.setText(worksheet_info["tpr_2010"])
                    worksheet.ui.refPhantomComboB.setCurrentText(worksheet_info["reference_phantom"])
                    worksheet.ui.reffieldSizeComboB.setCurrentText(worksheet_info["reference_field_size"])
                    worksheet.ui.refDistanceLE.setText(worksheet_info["reference_distance"])
                    worksheet.ui.refDepthComboB.setCurrentText(worksheet_info["reference_depth"])
                    worksheet.ui.rawDosReadLE.setText(worksheet_info["raw_dosimeter_reading_v1"])
                    worksheet.ui.corrLinacMULE.setText(worksheet_info["corresponding_linac_mu"])
                    worksheet.ui.userPressureLE.setText(worksheet_info["user_pressure"])
                    worksheet.ui.userTempLE.setText(worksheet_info["user_temperature"])
                    worksheet.ui.userHumidityLE.setText(worksheet_info["user_humidity"])
                    worksheet.ui.readMPosLE.setText(worksheet_info["m_positive_reading"])
                    worksheet.ui.readMNegLE.setText(worksheet_info["m_negative_reading"])
                    worksheet.ui.normVoltageLE.setText(worksheet_info["v1_voltage"])
                    worksheet.ui.redVoltageLE.setText(worksheet_info["v2_voltage"])
                    worksheet.ui.normReadLE.setText(worksheet_info["m1_reading"])
                    worksheet.ui.redReadLE.setText(worksheet_info["m2_reading"])
                    worksheet.ui.depthDMaxLE.setText(worksheet_info["depth_dmax"])
                    worksheet.ui.pddLE.setText(worksheet_info["pdd_zref"])
                    worksheet.ui.tmrLE.setText(worksheet_info["tmr_zref"])

                    (worksheet.ui.userPosPolarRadioButton.toggle() 
                     if worksheet_info["user_polarity"] == -2
                     else worksheet.ui.userNegPolarRadioButton.toggle())
                    
                    (worksheet.ui.pulsedRadioButton.toggle() if worksheet_info["beam_type"] == -2 
                     else worksheet.ui.pulsedScanRadioButton.toggle())
                    
                if file_info["worksheets"]:
                    worksheet_info = file_info["worksheets"][-1] # Use the last worksheet to set common info

                    worksheet.ui.userLE.setText(file_info["user"])
                    worksheet.ui.institutionLE.setText(file_info["institution"])
                    worksheet.ui.dateDE.setDate(QDate.fromString(file_info["date"], "dd MMM yyyy"))
                    worksheet.ui.toleranceDSB.valueFromText(file_info["tolerance"])

                    (worksheet.ui.ssdRadioButton.toggle() if 
                     file_info["setup_type"] == -2 else worksheet.ui.sadRadioButton.toggle())

                    worksheet.ui.IonChamberModelComboB.setCurrentText(
                        file_info["ion_chamber"]["model_name"])
                    worksheet.ui.chamberSerialNoLE.setText(
                        file_info["ion_chamber"]["serial_no"])
                    worksheet.ui.calibFactorLE.setText(
                        str(file_info["ion_chamber"]["calibration_coeff"]))
                    worksheet.ui.calibLabLE.setText(
                        str(file_info["ion_chamber"]["calibration_lab"]))
                    worksheet.ui.chamberCalibDE.setDate(
                        QDate.fromString(file_info["ion_chamber"]["calibration_date"], "dd MMM yyyy"))
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
                        file_info["electrometer"]["calibration_date"], "dd MMM yyyy"))
                    worksheet.ui.electRangeSettLE.setText(
                        file_info["electrometer"]["range_setting"])

                win.showMaximized()
                
    def save_worksheets_as(self, save_mode: int, save_format: int = 0):
        """
        Saves calibration worksheets to a PyBeam QA file or generate a PDF report.

        Parameters
        -----------
        save_mode: `int`
            - The mode for saving worksheets. 0 saves the current worksheet, 1 saves all worksheets.
            
        save_format: `int`
            - The save format. 0 generates a PyBeam QA file, 1 generates a PDF report.
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
        basic_info["tolerance"] = f"{worksheet.ui.toleranceDSB.value():2.2f}"
        basic_info["linac_name"] = worksheet.ui.linacNameLE.text()
        basic_info["setup_type"] = worksheet.ui.calibSetupGroup.checkedId() 

        ion_chamber_info["model_name"] = worksheet.ui.IonChamberModelComboB.currentText()
        ion_chamber_info["serial_no"] = worksheet.ui.chamberSerialNoLE.text()
        ion_chamber_info["calibration_coeff"] = worksheet.ui.calibFactorLE.text()
        ion_chamber_info["calibration_lab"] = worksheet.ui.calibLabLE.text()
        ion_chamber_info["calibration_date"] = worksheet.ui.chamberCalibDE.text()
        ion_chamber_info["water_proof_sleeve_mat"] = worksheet.ui.wSleeveMatlLE.text()
        ion_chamber_info["water_proof_sleeve_thick"] = worksheet.ui.wSleeveThickLE.text()
        ion_chamber_info["reference_pressure"] = worksheet.ui.refPressureLE.text()
        ion_chamber_info["reference_temperature"] = worksheet.ui.refTempLE.text()
        ion_chamber_info["reference_humidity"] = worksheet.ui.refHumidityLE.text()
        ion_chamber_info["polarizing_potential"] = worksheet.ui.polarPotV1LE.text()
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

        if save_format == 0:
            save_path = self.save_pybq_to()

            with open(save_path, 'w', encoding="utf-8") as file:
                for worksheet in file_info["photon_output_calibration"]["worksheets"]:
                    worksheet.pop("cal_summary", None)

                json.dump(file_info, file, ensure_ascii=False, indent=4)

        elif save_format == 1:
            cal_info = file_info["photon_output_calibration"]
            cal_info_new = copy(cal_info)

            # Delete the worksheets and add them again if completed
            del cal_info_new["worksheets"]
            cal_info_new["worksheets"] = []

            for worksheet in cal_info["worksheets"]:
                #TODO Replace this with signals
                if worksheet["cal_summary"]:
                    cal_info_new["worksheets"].append(worksheet)

            self.generate_report(cal_info_new)

class ElectronsMainWindow(BaseTRS398Window):
    
    def __init__(self, init_data: dict = None):
        super().__init__(init_data)

        self.window_title = "(TRS-398) Electron Output Calibration ‒ PyBeam QA"
        self.setWindowTitle(self.window_title)

        if init_data is not None:
            for beam in init_data["electron_beams"]:
                    self.setup_worksheets(init_data["linac"], beam)

            self.institution_changed.emit(init_data["institution"])
            self.userName_changed.emit(init_data["user"])

    def setup_worksheets(self, linac: str | Linac, beam_energy: int):
        worksheet = QElectronsWorksheet()
        worksheet.ui.nomAccPotLE.setText(f"{beam_energy}")
        worksheet.ui.nomAccPotLE.setReadOnly(True)

        self.ui.tabWidget.addTab(worksheet, f"{beam_energy} MeV beam")

        # Send data changes to other worksheets
        worksheet.ui.institutionLE.textChanged.connect(self.institution_changed)
        worksheet.ui.userLE.textChanged.connect(self.userName_changed)
        worksheet.ui.dateDE.dateChanged.connect(self.testDate_changed)
        worksheet.ui.toleranceDSB.valueChanged.connect(self.tolerance_changed)
        worksheet.ui.calibSetupGroup.buttonClicked.connect(lambda button: 
            self.setupType_changed.emit(worksheet.ui.calibSetupGroup.id(button)))
        worksheet.ui.gen_report_btn.clicked.connect(lambda: self.save_worksheets_as(0,1))
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
        self.tolerance_changed.connect(worksheet.ui.toleranceDSB.setValue)
        self.setupType_changed.connect(lambda id: 
            worksheet.ui.ssdRadioButton.toggle() if id == -2 else 
            worksheet.ui.sadRadioButton.toggle())
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

            if "electron_output_calibration" in pybq_file:
                #TODO Add error dialog for failed file parsing
                win = cls()

                file_info = pybq_file["electron_output_calibration"]
                for worksheet_info in file_info["worksheets"]:
                    worksheet = win.setup_worksheets(file_info["linac_name"],
                                                     worksheet_info["beam_energy"])
                    
                    worksheet.ui.nomDoseRateLE.setText(worksheet_info["nominal_dose_rate"])
                    worksheet.ui.measuredR50LE.setText(worksheet_info["r_50_ion"])
                    worksheet.ui.refPhantomComboB.setCurrentText(worksheet_info["reference_phantom"])
                    worksheet.ui.reffieldSizeComboB.setCurrentText(worksheet_info["reference_field_size"])
                    worksheet.ui.refDistanceLE.setText(worksheet_info["reference_distance"])
                    worksheet.ui.refDepthLE.setText(worksheet_info["reference_depth"])
                    worksheet.ui.rawDosReadLE.setText(worksheet_info["raw_dosimeter_reading_v1"])
                    worksheet.ui.corrLinacMULE.setText(worksheet_info["corresponding_linac_mu"])
                    worksheet.ui.userPressureLE.setText(worksheet_info["user_pressure"])
                    worksheet.ui.userTempLE.setText(worksheet_info["user_temperature"])
                    worksheet.ui.userHumidityLE.setText(worksheet_info["user_humidity"])
                    worksheet.ui.readMPosLE.setText(worksheet_info["m_positive_reading"])
                    worksheet.ui.readMNegLE.setText(worksheet_info["m_negative_reading"])
                    worksheet.ui.normVoltageLE.setText(worksheet_info["v1_voltage"])
                    worksheet.ui.redVoltageLE.setText(worksheet_info["v2_voltage"])
                    worksheet.ui.normReadLE.setText(worksheet_info["m1_reading"])
                    worksheet.ui.redReadLE.setText(worksheet_info["m2_reading"])
                    worksheet.ui.depthDMaxLE.setText(worksheet_info["depth_dmax"])
                    worksheet.ui.pddLE.setText(worksheet_info["pdd_zref"])

                    (worksheet.ui.userPosPolarRadioButton.toggle() 
                     if worksheet_info["user_polarity"] == -2
                     else worksheet.ui.userNegPolarRadioButton.toggle())
                    
                    (worksheet.ui.pulsedRadioButton.toggle() if worksheet_info["beam_type"] == -2 
                     else worksheet.ui.pulsedScanRadioButton.toggle())
                    
                if file_info["worksheets"]:
                    worksheet_info = file_info["worksheets"][-1] # Use the last worksheet to set common info

                    worksheet.ui.userLE.setText(file_info["user"])
                    worksheet.ui.institutionLE.setText(file_info["institution"])
                    worksheet.ui.dateDE.setDate(QDate.fromString(file_info["date"], "dd MMM yyyy"))
                    worksheet.ui.toleranceDSB.valueFromText(file_info["tolerance"])

                    worksheet.ui.IonChamberModelComboB.setCurrentText(
                        file_info["ion_chamber"]["model_name"])
                    worksheet.ui.chamberSerialNoLE.setText(
                        file_info["ion_chamber"]["serial_no"])
                    worksheet.ui.calibFactorLE.setText(
                        str(file_info["ion_chamber"]["calibration_coeff"]))
                    worksheet.ui.calibLabLE.setText(
                        str(file_info["ion_chamber"]["calibration_lab"]))
                    worksheet.ui.chamberCalibDE.setDate(
                        QDate.fromString(file_info["ion_chamber"]["calibration_date"], "dd MMM yyyy"))
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
                        file_info["electrometer"]["calibration_date"], "dd MMM yyyy"))
                    worksheet.ui.electRangeSettLE.setText(
                        file_info["electrometer"]["range_setting"])

                win.showMaximized()
                
    def save_worksheets_as(self, save_mode: int, save_format: int = 0):
        """
        Saves calibration worksheets to a PyBeam QA file or generate a PDF report.

        Parameters
        -----------
        save_mode: `int`
            - The mode for saving worksheets. 0 saves the current worksheet, 1 saves all worksheets.
            
        save_format: `int`
            - The save format. 0 generates a PyBeam QA file, 1 generates a PDF report.
        """
        worksheet_info = []

        if save_mode == 0:
            index = self.ui.tabWidget.currentIndex()
            worksheet: QElectronsWorksheet = self.ui.tabWidget.widget(index)
            worksheet_info.append(worksheet.save_worksheet_info())

        elif save_mode == 1:
            for index in range(self.ui.tabWidget.count()):
                worksheet: QElectronsWorksheet = self.ui.tabWidget.widget(index)
                worksheet_info.append(worksheet.save_worksheet_info())

        # Use the last worksheet to extract worksheet common information
        basic_info = {}
        ion_chamber_info = {}
        electrometer_info = {}

        basic_info["user"] = worksheet.ui.userLE.text()
        basic_info["institution"] = worksheet.ui.institutionLE.text()
        basic_info["date"] = worksheet.ui.dateDE.text()
        basic_info["tolerance"] = f"{worksheet.ui.toleranceDSB.value():2.2f}"
        basic_info["linac_name"] = worksheet.ui.linacNameLE.text()
        basic_info["setup_type"] = worksheet.ui.calibSetupGroup.checkedId() 

        ion_chamber_info["model_name"] = worksheet.ui.IonChamberModelComboB.currentText()
        ion_chamber_info["serial_no"] = worksheet.ui.chamberSerialNoLE.text()
        ion_chamber_info["calibration_coeff"] = worksheet.ui.calibFactorLE.text()
        ion_chamber_info["calibration_lab"] = worksheet.ui.calibLabLE.text()
        ion_chamber_info["calibration_date"] = worksheet.ui.chamberCalibDE.text()
        ion_chamber_info["water_proof_sleeve_mat"] = worksheet.ui.wSleeveMatlLE.text()
        ion_chamber_info["water_proof_sleeve_thick"] = worksheet.ui.wSleeveThickLE.text()
        ion_chamber_info["reference_pressure"] = worksheet.ui.refPressureLE.text()
        ion_chamber_info["reference_temperature"] = worksheet.ui.refTempLE.text()
        ion_chamber_info["reference_humidity"] = worksheet.ui.refHumidityLE.text()
        ion_chamber_info["polarizing_potential"] = worksheet.ui.polarPotV1LE.text()
        ion_chamber_info["calibration_quality"] = worksheet.ui.beamQualityGroup.checkedId()
        ion_chamber_info["calibration_polarity"] = worksheet.ui.calibPolarityGroup.checkedId()
        ion_chamber_info["polarity_effect_corrected"] = worksheet.ui.corrPolarEffCheckB.isChecked()

        electrometer_info["model_name"] = worksheet.ui.electModelLE.text()
        electrometer_info["serial_no"] = worksheet.ui.electSerialNoLE.text()
        electrometer_info["calibration_lab"] = worksheet.ui.electCalLabLE.text()
        electrometer_info["calibration_date"] = worksheet.ui.electCalDateDE.text()
        electrometer_info["range_setting"] = worksheet.ui.electRangeSettLE.text()

        file_info = {"electron_output_calibration": {}}
        file_info["electron_output_calibration"].update(basic_info)
        file_info["electron_output_calibration"].update({"ion_chamber": ion_chamber_info})
        file_info["electron_output_calibration"].update({"electrometer": electrometer_info})
        file_info["electron_output_calibration"].update({"worksheets": worksheet_info})

        if save_format == 0:
            save_path = self.save_pybq_to()

            with open(save_path, 'w', encoding="utf-8") as file:
                for worksheet in file_info["electron_output_calibration"]["worksheets"]:
                    worksheet.pop("cal_summary", None)

                json.dump(file_info, file, ensure_ascii=False, indent=4)

        elif save_format == 1:
            cal_info = file_info["electron_output_calibration"]
            cal_info_new = copy(cal_info)

            # Delete the worksheets and add them again if completed
            del cal_info_new["worksheets"]
            cal_info_new["worksheets"] = []

            for worksheet in cal_info["worksheets"]:
                #TODO Replace this with signals
                if worksheet["cal_summary"]:
                    cal_info_new["worksheets"].append(worksheet)

            self.generate_report(cal_info_new)

class QPhotonsWorksheet(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_QPhotonsWorksheet()
        self.ui.setupUi(self)

        self.trs398 = TRS398Photons()
        self.chambers_config = ChambersConfig()
        self.settings_config = SettingsConfig()

        self.hide_cal_outcome()

        # Load all ionization chambers
        self.all_chambers = []
        self.set_ion_chamber_list()

        #--- Set up basic functionality ---
        self.ui.dateDE.setDate(QDate.currentDate())
        self.ui.dateDE.setMaximumDate(QDate.currentDate())
        self.ui.chamberCalibDE.setMaximumDate(QDate.currentDate())
        self.ui.electCalDateDE.setMaximumDate(QDate.currentDate())
        self.ui.toleranceDSB.valueChanged.connect(self.set_zmax_depth_dose)

        self.ui.calibSetupGroup.buttonToggled.connect(self.cal_setup_changed)
        self.ui.calibSeparateGroup.idToggled.connect(self.same_calib) # use idToggled to allow other tab signals to enable fields
        self.ui.beamQualityLE.textChanged.connect(self.tpr2010_changed)
        self.ui.calibLabLE.textChanged.connect(self.same_calib)
        self.ui.chamberCalibDE.dateChanged.connect(self.same_calib)
        self.ui.IonChamberModelComboB.currentIndexChanged.connect(self.chamber_model_changed)
        self.ui.calibSetupGroup.buttonClicked.connect(self.set_zmax_depth_dose)
        self.ui.IonChamberModelComboB.currentIndexChanged.connect(self.calc_kq)
        self.ui.beamQualityLE.textChanged.connect(self.calc_kq)
        self.ui.refDepthComboB.currentTextChanged.connect(self.calc_kq)
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
        self.ui.nomDoseRateLE.setValidator(DoubleValidator.from_args(1.0, 1000, 4))
        self.ui.beamQualityLE.setValidator(DoubleValidator.from_args(0.5, 0.84, 4))
        self.ui.refDistanceLE.setValidator(DoubleValidator.from_args(50.0, 120, 2))
        dVal = DoubleValidator()
        dVal.setDecimals(4)
        self.ui.calibFactorLE.setValidator(dVal)
        self.ui.wSleeveThickLE.setValidator(dVal)
        self.ui.pWinThickLE.setValidator(dVal)
        self.ui.refPressureLE.setValidator(DoubleValidator.from_args(50.0, 115, 3))
        self.ui.refTempLE.setValidator(DoubleValidator.from_args(10, 50, 3))
        self.ui.refHumidityLE.setValidator(DoubleValidator.from_args(0,100,3))
        self.ui.polarPotV1LE.setValidator(QIntValidator())
        self.ui.rawDosReadLE.setValidator(dVal)
        self.ui.corrLinacMULE.setValidator(dVal)
        self.ui.userPressureLE.setValidator(DoubleValidator.from_args(50.0, 115, 3))
        self.ui.userTempLE.setValidator(DoubleValidator.from_args(10, 50, 3))
        self.ui.userHumidityLE.setValidator(DoubleValidator.from_args(0,100,3))
        self.ui.readMPosLE.setValidator(dVal)
        self.ui.readMNegLE.setValidator(dVal)
        self.ui.normVoltageLE.setValidator(dVal)
        self.ui.redVoltageLE.setValidator(dVal)
        self.ui.normReadLE.setValidator(dVal)
        self.ui.redReadLE.setValidator(dVal)
        self.ui.depthDMaxLE.setValidator(dVal)
        self.ui.pddLE.setValidator(DoubleValidator.from_args(0.0, 100.0, 2))
        self.ui.tmrLE.setValidator(dVal)

        # set reference condition values
        self.ui.refTempLE.setText(f"{self.trs398.refTemp}")
        self.ui.refPressureLE.setText(f"{self.trs398.refPress}")

        self.cal_setup_changed()
        self.same_calib()
        self.chamber_model_changed()

    def set_ion_chamber_list(self):
        self.chambers = self.chambers_config.getConfig()
        self.all_chambers.extend(self.chambers["cylindrical"])

        self.all_chambers.sort()   
        self.ui.IonChamberModelComboB.addItems(self.all_chambers)

    def tpr2010_changed(self):
        self.ui.refDepthComboB.clear()
        if self.ui.beamQualityLE.hasAcceptableInput():
            if float(self.ui.beamQualityLE.text()) >= 0.70:
                self.ui.refDepthComboB.addItems(["10.0"])
            else:
                self.ui.refDepthComboB.addItems(["5.0", "10.0"])

            self.ui.refDepthComboB.setCurrentIndex(0)

        else:
            self.ui.refDepthComboB.setPlaceholderText("N/A")

    def chamber_model_changed(self):
        curr_chamber = self.ui.IonChamberModelComboB.currentText()

        for type in self.chambers:
            if curr_chamber in self.chambers[type]:
                self.ui.cWallMatLE.setText(self.chambers[type][curr_chamber]["wall_material"])
                self.ui.cWallThickLE.setText(str(self.chambers[type][curr_chamber]["wall_thickness"]))

    def cal_setup_changed(self):
        if self.ui.calibSetupGroup.checkedButton() == self.ui.ssdRadioButton:
            self.ui.setupSW.setCurrentIndex(0)
        else: self.ui.setupSW.setCurrentIndex(1)

    def same_calib(self):
        if self.ui.calibSeparateGroup.checkedButton() == self.ui.calibSepNoRadioButton:
            self.ui.electCalDateDE.setDate(self.ui.chamberCalibDE.date())
            self.ui.electCalLabLE.setText(self.ui.calibLabLE.text())
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
        """
        Calculate the beam quality correction factor and the volume averaging correction 
        factor
        """
        curr_chamber = self.ui.IonChamberModelComboB.currentText()
        tpr_value = self.ui.beamQualityLE.text()

        chambers = self.chambers_config.getConfig()

        if tpr_value != "":
            for chamberType in chambers:
                if curr_chamber in chambers[chamberType]:
                    tpr_value = float(tpr_value)
                    tpr_kQ: dict = chambers[chamberType][curr_chamber]["tpr_kQ"]
                    kQ = self.trs398.tpr2010_to_kQ(tpr_value, tpr_kQ)

                    self.ui.kQLE.setText("%.3f" % kQ)

                    if "(FFF" in self.ui.nomAccPotUnit.text():
                        if self.ui.refDepthComboB.currentText() != "":
                            depth = float(self.ui.refDepthComboB.currentText())
                            sdd = 100. + depth
                            cavity_len = chambers[chamberType][curr_chamber]["cavity_length"] / 10 #to cm
                            kVol = self.trs398.kVol_corr(tpr_value, cavity_len, sdd)
                            self.ui.kVolLE.setText("%.3f" % kVol)

        else:
            self.ui.kQLE.clear()
            self.ui.kVolLE.clear()

    def calc_ktp(self):
        user_temp = self.ui.userTempLE.text()
        user_press = self.ui.userPressureLE.text()
        user_humid = self.ui.userHumidityLE.text()

        if user_temp != "" and user_press != "" and user_humid != "":
            kTP = self.trs398.kTP_corr(float(user_temp), float(user_press))
            self.ui.kTPLE.setText("%.3f" % kTP)
        else:
            self.ui.kTPLE.clear()

    def cal_kpol(self):
        m_pos = self.ui.readMPosLE.text()
        m_neg = self.ui.readMNegLE.text()

        if m_pos != "" and m_neg != "":
            if self.ui.userPolarityGroup.checkedButton() == self.ui.userPosPolarRadioButton:
                isPosPref = True
            else:
                isPosPref = False

            kPol = self.trs398.kPol_corr(float(m_pos), float(m_neg), isPosPref)
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
            v_norm = float(self.ui.normVoltageLE.text())
            v_red = float(self.ui.redVoltageLE.text())
            m_norm = float(self.ui.normReadLE.text())
            m_red = float(self.ui.redReadLE.text())

            if self.ui.beamTypeGroup.checkedButton() == self.ui.pulsedScanRadioButton:
                is_pulsed_scanned = True
            else:
                is_pulsed_scanned = False
            
            kS = self.trs398.kS_corr(v_norm, v_red, m_norm, m_red, is_pulsed_scanned)
            self.ui.kSLE.setText("%.3f" % kS)
        else:
            self.ui.kSLE.clear()

    def check_ks_value(self):
        if self.ui.kSLE.text() != "":
            kS = float(self.ui.kSLE.text())
            v_norm = float(self.ui.normVoltageLE.text())
            v_red = float(self.ui.redVoltageLE.text())
            m_norm = float(self.ui.normReadLE.text())
            m_red = float(self.ui.redReadLE.text())

            kS = kS - 1.0
            kS_test = ((m_norm/m_red) - 1.0) / ((v_norm/v_red) - 1.0)

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
            raw_read = float(self.ui.rawDosReadLE.text())
            linac_MU = float(self.ui.corrLinacMULE.text())

            self.trs398.mRaw = raw_read
            self.trs398.linac_mu = linac_MU
            self.ui.ratioReadMULE.setText("%.5f" % (raw_read / linac_MU))
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
        ratio_read = self.ui.ratioReadMULE.text()
        nDw = self.ui.calibFactorLE.text()

        all_valid = (kTP != "" and kS != "" and kElec != "" and kPol != "" and kQ != "" and ratio_read != ""
            and nDw != "")

        if all_valid:
            self.ui.zrefDoseLE.setText(("%.3f" % (self.trs398.get_DwQ_zref()*100.0)) + " cGy/MU")
        else:
            self.ui.zrefDoseLE.clear()

    def set_zmax_depth_dose(self):
        if self.ui.calibSetupGroup.checkedButton() == self.ui.ssdRadioButton:
            z_ref_dd = self.ui.zrefDoseLE.text()
            pdd_z_ref = self.ui.pddLE.text()

            if z_ref_dd != "" and pdd_z_ref != "":
                d_max = self.trs398.get_DwQ_zmax_ssdSetup(float(pdd_z_ref))*100.0
                self.ui.zmaxDoseLE.setText("%.3f" % d_max + " cGy/MU")
                self.set_outcome(d_max)
            else:
                self.ui.zmaxDoseLE.clear()
                self.ui.outcomeLE.clear()
                self.hide_cal_outcome()
        else:
            z_ref_dd = self.ui.zrefDoseLE.text()
            tmr_ref = self.ui.tmrLE.text()

            if z_ref_dd != "" and tmr_ref != "":
                d_max = self.trs398.get_DwQ_zmax_tmrSetup(float(tmr_ref))*100.0
                self.ui.zmaxDoseLE.setText("%.3f" % d_max + " cGy/MU")
                self.set_outcome(d_max)
            else:
                self.ui.zmaxDoseLE.clear()
                self.ui.outcomeLE.clear()
                self.hide_cal_outcome()

    def set_outcome(self, d_max: float):
        tol = self.ui.toleranceDSB.value()
        diff = abs(d_max - 1.00) # Reference is 1.00 cGy/MU

        if diff*100.0 <= tol:
            self.ui.outcomeLE.setText(
            f"PASS -- with a {diff*100.0:2.2f}% deviation from 1.00 cGy/MU")

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
            f"FAIL -- with a {diff*100.0:2.2f}% deviation from 1.00 cGy/MU")

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
    
    def toggle_simple_view(self):
        #Check QT form structure before editing row numbers to hide

        #hide section one fields
        rows_to_hide = [2]
        for row in rows_to_hide:
            self.ui.sectionOneFL.setRowVisible(row, False)

        #hide section two fields
        rows_to_hide = [1, 3, 4, 5, 6, 7, 10, 16, 17, 18, 19, 20]
        for row in rows_to_hide:
            self.ui.sectionTwoFL.setRowVisible(row, False)

        #hide section four fields
        rows_to_hide = [0, 1]
        for row in rows_to_hide:
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
        worksheet_info["beam_energy"] = self.ui.nomAccPotLE.text()
        worksheet_info["is_fff"] = True if "(FFF" in self.ui.nomAccPotUnit.text() else False
        worksheet_info["nominal_dose_rate"] = self.ui.nomDoseRateLE.text()
        worksheet_info["tpr_2010"] = self.ui.beamQualityLE.text() 
        worksheet_info["reference_phantom"] = self.ui.refPhantomComboB.currentText()
        worksheet_info["reference_field_size"] = self.ui.reffieldSizeComboB.currentText()
        worksheet_info["reference_distance"] = self.ui.refDistanceLE.text()
        worksheet_info["reference_depth"] = self.ui.refDepthComboB.currentText()
        worksheet_info["user_polarity"] = self.ui.userPolarityGroup.checkedId()
        worksheet_info["raw_dosimeter_reading_v1"] = self.ui.rawDosReadLE.text()
        worksheet_info["corresponding_linac_mu"] = self.ui.corrLinacMULE.text()
        worksheet_info["user_pressure"] = self.ui.userPressureLE.text()
        worksheet_info["user_temperature"] = self.ui.userTempLE.text()
        worksheet_info["user_humidity"] = self.ui.userHumidityLE.text()
        worksheet_info["m_positive_reading"] = self.ui.readMPosLE.text()
        worksheet_info["m_negative_reading"] = self.ui.readMNegLE.text()
        worksheet_info["v1_voltage"] = self.ui.normVoltageLE.text()
        worksheet_info["v2_voltage"] = self.ui.redVoltageLE.text()
        worksheet_info["m1_reading"] = self.ui.normReadLE.text()
        worksheet_info["m2_reading"] = self.ui.redReadLE.text()
        worksheet_info["beam_type"] = self.ui.beamTypeGroup.checkedId()
        worksheet_info["depth_dmax"] = self.ui.depthDMaxLE.text()
        worksheet_info["pdd_zref"] = self.ui.pddLE.text()
        worksheet_info["tmr_zref"] = self.ui.tmrLE.text()

        if self.ui.outcomeLE.text() != "":
            cal_summary = {}
            cal_summary["kQQo"] = self.ui.kQLE.text()
            cal_summary["kElec"] = self.ui.kElecLE.text()
            cal_summary["kTP"] = self.ui.kTPLE.text()
            cal_summary["kPol"] = self.ui.kPolLE.text()
            cal_summary["kS"] = self.ui.kSLE.text()
            cal_summary["corr_dos_reading"] = f"{self.trs398.get_Mcorrected():2.2f}"
            cal_summary["dw_zref"] = self.ui.zrefDoseLE.text().split(" ")[0]
            cal_summary["dw_zmax"] = self.ui.zmaxDoseLE.text().split(" ")[0]
            cal_summary["test_outcome"] = self.ui.outcomeLE.text().split(" ")[0]
            worksheet_info["cal_summary"] = cal_summary

        else:
            worksheet_info["cal_summary"] = None

        return worksheet_info

class QElectronsWorksheet(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_QElectronsWorksheet()
        self.ui.setupUi(self)

        self.trs398 = TRS398Electrons()
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
        self.ui.toleranceDSB.valueChanged.connect(self.set_zmax_depth_dose)

        self.ui.calibSetupGroup.buttonToggled.connect(self.cal_setup_changed)
        
        self.ui.calibSeparateGroup.idToggled.connect(self.same_calib) # use idToggled to allow other tab signals to enable fields
        self.ui.r50SourceGroup.idToggled.connect(self.measured_r50_changed)
        
        self.ui.measuredR50LE.textChanged.connect(self.measured_r50_changed)
        self.ui.calibLabLE.textChanged.connect(self.same_calib)
        self.ui.chamberCalibDE.dateChanged.connect(self.same_calib)
        self.ui.IonChamberModelComboB.currentIndexChanged.connect(self.chamber_model_changed)
        self.ui.calibSetupGroup.buttonClicked.connect(self.set_zmax_depth_dose)
        self.ui.IonChamberModelComboB.currentIndexChanged.connect(self.measured_r50_changed)
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
        self.ui.nomDoseRateLE.setValidator(DoubleValidator.from_args(1.0, 1000, 4))
        self.ui.measuredR50LE.setValidator(DoubleValidator.from_args(1.0, 20.0, 4))
        self.ui.refDistanceLE.setValidator(DoubleValidator.from_args(50.0, 120, 2))
        dVal = DoubleValidator()
        dVal.setDecimals(4)
        self.ui.calibFactorLE.setValidator(dVal)
        self.ui.wSleeveThickLE.setValidator(dVal)
        self.ui.pWinThickLE.setValidator(dVal)
        self.ui.refPressureLE.setValidator(DoubleValidator.from_args(50.0, 115, 3))
        self.ui.refTempLE.setValidator(DoubleValidator.from_args(10, 50, 3))
        self.ui.refHumidityLE.setValidator(DoubleValidator.from_args(0,100,3))
        self.ui.polarPotV1LE.setValidator(QIntValidator())
        self.ui.rawDosReadLE.setValidator(dVal)
        self.ui.corrLinacMULE.setValidator(dVal)
        self.ui.userPressureLE.setValidator(DoubleValidator.from_args(50.0, 115, 3))
        self.ui.userTempLE.setValidator(DoubleValidator.from_args(10, 50, 3))
        self.ui.userHumidityLE.setValidator(DoubleValidator.from_args(0,100,3))
        self.ui.readMPosLE.setValidator(dVal)
        self.ui.readMNegLE.setValidator(dVal)
        self.ui.normVoltageLE.setValidator(dVal)
        self.ui.redVoltageLE.setValidator(dVal)
        self.ui.normReadLE.setValidator(dVal)
        self.ui.redReadLE.setValidator(dVal)
        self.ui.depthDMaxLE.setValidator(dVal)
        self.ui.pddLE.setValidator(DoubleValidator.from_args(0.0, 100.0, 2))
        self.ui.tmrLE.setValidator(dVal)

        # set reference condition values
        self.ui.refTempLE.setText(f"{self.trs398.refTemp}")
        self.ui.refPressureLE.setText(f"{self.trs398.refPress}")

        self.cal_setup_changed()
        self.same_calib()
        self.chamber_model_changed()

    def set_ion_chamber_list(self):
        self.chambers = self.chambersConfig.getConfig()
        chambersAllowed = self.settingsConfig.getConfig()
        chambersAllowed = chambersAllowed["trs398"]["electron_calibration"]
        chambersAllowed = chambersAllowed["allowed_chambers"]

        self.allChambers.extend(self.chambers["cylindrical"])
        self.allChambers.extend(self.chambers["plane_parallel"])

        self.allChambers = list(set(self.allChambers).intersection(
            set(chambersAllowed)))

        self.allChambers.sort()   
        self.ui.IonChamberModelComboB.addItems(self.allChambers)

    def measured_r50_changed(self):
        if self.ui.measuredR50LE.hasAcceptableInput():
            r50ion_source = ("ion_curves" if self.ui.r50SourceGroup.checkedId() == -2 
                             else "dose_curves")
            r50ion = float(self.ui.measuredR50LE.text())

            """
            Determine R50 from the set R50ion value, if obtained from dose curves
            then R50 = R50ion
            """
            r50 = self.trs398.r50ion_to_r50(r50ion, r50ion_source)
            self.ui.beamQualityLE.setText(f"{r50:2.3f}")
            # Set the reference depth
            self.ui.refDepthLE.setText(f"{self.trs398.ref_depth:2.3f}")

            # Set the beam quality correction factor
            chambers = self.chambersConfig.getConfig()
            currChamber = self.ui.IonChamberModelComboB.currentText()

            for chamberType in chambers:
                if currChamber in chambers[chamberType]:
                    r50_kQ: dict = chambers[chamberType][currChamber]["r50_kQ"]

                    try:
                        kQ = self.trs398.r50_to_kQ(r50_kQ)
                        self.ui.kQLE.setText(f"{kQ:2.3f}")
                    except ValueError as err:
                        self.ui.kQLE.setText("Out of range")

        else:
            self.ui.refDepthLE.clear()
            self.ui.kQLE.clear()

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
            self.ui.electCalLabLE.setText(self.ui.calibLabLE.text())
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

    def calc_ktp(self):
        userTemp = self.ui.userTempLE.text()
        userPress = self.ui.userPressureLE.text()
        userHumid = self.ui.userHumidityLE.text()

        if userTemp != "" and userPress != "" and userHumid != "":
            kTP = self.trs398.kTP_corr(float(userTemp), float(userPress))
            self.ui.kTPLE.setText(f"{kTP:2.3f}")
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

            self.trs398.mRaw = rawRead
            self.trs398.linac_mu = linacMU
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
                self.set_outcome(dMax)
            else:
                self.ui.zmaxDoseLE.clear()
                self.ui.outcomeLE.clear()
                self.hide_cal_outcome()
        else:
            zRefDD = self.ui.zrefDoseLE.text()
            tmrRef = self.ui.tmrLE.text()

            if zRefDD != "" and tmrRef != "":
                dMax = self.trs398.get_DwQ_zmax_tmrSetup(float(tmrRef))*100.0
                self.ui.zmaxDoseLE.setText("%.3f" % dMax + " cGy/MU")
                self.set_outcome(dMax)
            else:
                self.ui.zmaxDoseLE.clear()
                self.ui.outcomeLE.clear()
                self.hide_cal_outcome()

    def set_outcome(self, dMax: float):
        tol = self.ui.toleranceDSB.value()
        diff = abs(dMax - 1.00) # Reference is 1.00 cGy/MU

        if diff*100.0 <= tol:
            self.ui.outcomeLE.setText(
            f"PASS -- with a {diff*100.0:2.2f}% deviation from 1.00 cGy/MU")

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
            f"FAIL -- with a {diff*100.0:2.2f}% deviation from 1.00 cGy/MU")

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
        worksheet_info["beam_energy"] = self.ui.nomAccPotLE.text()
        worksheet_info["nominal_dose_rate"] = self.ui.nomDoseRateLE.text()
        worksheet_info["r_50_ion"] = self.ui.measuredR50LE.text()
        worksheet_info["r_50"] = self.ui.beamQualityLE.text() 
        worksheet_info["reference_phantom"] = self.ui.refPhantomComboB.currentText()
        worksheet_info["reference_field_size"] = self.ui.reffieldSizeComboB.currentText()
        worksheet_info["reference_distance"] = self.ui.refDistanceLE.text()
        worksheet_info["reference_depth"] = self.ui.refDepthLE.text()
        worksheet_info["user_polarity"] = self.ui.userPolarityGroup.checkedId()
        worksheet_info["raw_dosimeter_reading_v1"] = self.ui.rawDosReadLE.text()
        worksheet_info["corresponding_linac_mu"] = self.ui.corrLinacMULE.text()
        worksheet_info["user_pressure"] = self.ui.userPressureLE.text()
        worksheet_info["user_temperature"] = self.ui.userTempLE.text()
        worksheet_info["user_humidity"] = self.ui.userHumidityLE.text()
        worksheet_info["m_positive_reading"] = self.ui.readMPosLE.text()
        worksheet_info["m_negative_reading"] = self.ui.readMNegLE.text()
        worksheet_info["v1_voltage"] = self.ui.normVoltageLE.text()
        worksheet_info["v2_voltage"] = self.ui.redVoltageLE.text()
        worksheet_info["m1_reading"] = self.ui.normReadLE.text()
        worksheet_info["m2_reading"] = self.ui.redReadLE.text()
        worksheet_info["depth_dmax"] = self.ui.depthDMaxLE.text()
        worksheet_info["pdd_zref"] = self.ui.pddLE.text()

        if self.ui.outcomeLE.text() != "":
            cal_summary = {}
            cal_summary["kQQo"] = self.ui.kQLE.text()
            cal_summary["kElec"] = self.ui.kElecLE.text()
            cal_summary["kTP"] = self.ui.kTPLE.text()
            cal_summary["kPol"] = self.ui.kPolLE.text()
            cal_summary["kS"] = self.ui.kSLE.text()
            cal_summary["corr_dos_reading"] = f"{self.trs398.get_Mcorrected():2.2f}"
            cal_summary["dw_zref"] = self.ui.zrefDoseLE.text().split(" ")[0]
            cal_summary["dw_zmax"] = self.ui.zmaxDoseLE.text().split(" ")[0]
            cal_summary["test_outcome"] = self.ui.outcomeLE.text().split(" ")[0]
            worksheet_info["cal_summary"] = cal_summary

        else:
            worksheet_info["cal_summary"] = None

        return worksheet_info