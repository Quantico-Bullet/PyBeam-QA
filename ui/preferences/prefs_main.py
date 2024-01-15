from PySide6.QtWidgets import (QFormLayout, QDialog, QFileDialog,
                               QLineEdit, QComboBox, QDialogButtonBox,
                               QHBoxLayout, QPushButton, QSpacerItem, 
                               QSizePolicy)

from PySide6.QtCore import Qt
from ui.py_ui.preferences_ui import Ui_PreferencesDialog

class Preferences(QDialog):

    GENERAL_PAGE = 0
    DEVICES_PAGE = 1
    REPORTING_PAGE = 2
    ANALYSIS_TOOLS_PAGE = 3

    def __init__(self, nav_index: tuple = (GENERAL_PAGE, 0)):
        super().__init__()
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Preferences ‒ PyBeam QA")

        # Add slots
        self.ui.nav_button_group.buttonClicked.connect(
            self.change_preferences_page
        )

        #init pages
        self.gen_prefs = GeneralPreferences(self.ui)
        self.devices_pref = DevicesPreferences(self.ui)

        # Set default views
        self.change_preferences_page()

        # Navigate to the initial set index
        self.ui.nav_stacked_widget.setCurrentIndex(nav_index[0])

    def change_preferences_page(self):
        checked_button = self.ui.nav_button_group.checkedButton()

        if checked_button == self.ui.general_btn:
            self.ui.nav_stacked_widget.setCurrentIndex(self.GENERAL_PAGE)
            self.ui.page_title_label.setText(self.ui.general_btn.text())

        elif checked_button == self.ui.devices_btn:
            self.ui.nav_stacked_widget.setCurrentIndex(self.DEVICES_PAGE)
            self.ui.page_title_label.setText(self.ui.devices_btn.text())

        elif checked_button == self.ui.reporting_btn:
            self.ui.nav_stacked_widget.setCurrentIndex(self.REPORTING_PAGE)
            self.ui.page_title_label.setText(self.ui.reporting_btn.text())

        elif checked_button == self.ui.analysis_tools_btn:
            self.ui.nav_stacked_widget.setCurrentIndex(self.ANALYSIS_TOOLS_PAGE)
            self.ui.page_title_label.setText(self.ui.analysis_tools_btn.text())

class GeneralPreferences:

    def __init__(self, ui: Ui_PreferencesDialog):

        self.ui = ui
        self.ui.workspace_browse_btn.clicked.connect(self.select_workspace_folder)

    def select_workspace_folder(self):
        caption = "Select a Folder for the Workspace"
        folder = QFileDialog.getExistingDirectory(caption=caption)

        if folder:
            self.ui.workspace_loc_le.setText(folder)

class DevicesPreferences:

    def __init__(self, ui: Ui_PreferencesDialog):
        self.ui = ui

        self.ui.linac_comboB.currentIndexChanged.connect(self.linac_view_changed)
        self.ui.add_linac_btn.clicked.connect(self.add_new_linac)

    def add_new_linac(self):
        linac_name_le = QLineEdit()
        linac_manufacturer_comboB = QComboBox()
        linac_model_comboB = QComboBox()
        linac_serial_num_le = QLineEdit()
        linac_serial_num_le.setFixedWidth(200)
        photon_beams_le = QLineEdit("2, 4, 6, 8, 10 FFF, 12 FFF")
        photon_beams_le.setReadOnly(True)
        photon_beams_le.setFixedWidth(200)
        photon_beams_le.setClearButtonEnabled(True)
        add_photon_beam_btn = QPushButton("Add")
        electron_beams_le = QLineEdit("1, 3, 5, 7")
        electron_beams_le.setReadOnly(True)
        electron_beams_le.setFixedWidth(200)
        electron_beams_le.setClearButtonEnabled(True)
        add_electron_beam_btn = QPushButton("Add")
        
        linac_manufacturer_comboB.currentTextChanged.connect(lambda x:
            self.add_linac_manufacturer_changed(x, linac_model_comboB))
        linac_manufacturer_comboB.addItems(["Elekta", "Varian"])

        layout = QFormLayout()
        layout.addRow("Linac name:", linac_name_le)
        layout.addRow("Manufacturer:", linac_manufacturer_comboB)
        layout.addRow("Model:", linac_model_comboB)
        layout.addRow("Serial No:", linac_serial_num_le)

        photon_beams_layout = QHBoxLayout()
        electron_beams_layout = QHBoxLayout()
        photon_beams_layout.addWidget(photon_beams_le)
        photon_beams_layout.addWidget(add_photon_beam_btn)
        electron_beams_layout.addWidget(electron_beams_le)
        electron_beams_layout.addWidget(add_electron_beam_btn)

        layout.addRow("Photon beams (MV):", photon_beams_layout)
        layout.addRow("Electron beams (MeV):", electron_beams_layout)
        layout.addItem(QSpacerItem(0, 10, QSizePolicy.Policy.Fixed, 
                                   QSizePolicy.Policy.Fixed))

        dialog_buttons = QDialogButtonBox()
        apply_btn = dialog_buttons.addButton(QDialogButtonBox.StandardButton.Apply)
        cancel_btn = dialog_buttons.addButton(QDialogButtonBox.StandardButton.Cancel)

        layout.addWidget(dialog_buttons)
        
        add_dialog = QDialog()
        add_dialog.setWindowTitle("Add New Linac")
        add_dialog.setModal(True)
        add_dialog.setLayout(layout)
        add_dialog.setMinimumSize(add_dialog.sizeHint())
        add_dialog.setMaximumSize(add_dialog.sizeHint())
        apply_btn.clicked.connect(add_dialog.accept)
        cancel_btn.clicked.connect(add_dialog.reject)

        result_code = add_dialog.exec()

        if result_code == QDialog.DialogCode.Accepted:

            data = {"linac_name": linac_name_le.text(),
                    "linac_manufacturer": linac_manufacturer_comboB.currentText(),
                    "linac_model": linac_model_comboB.currentText(),
                    "linac_serial_num": linac_serial_num_le.text(),
                    "beams": {}}
            
            photon_beams_data = photon_beams_le.text()
            electron_beams_data = electron_beams_le.text()

            data["beams"]["photons"] = []
            data["beams"]["photons_fff"] = []
            data["beams"]["electrons"] = []

            if photon_beams_data:
                photon_beams_data = photon_beams_data.split(", ")

                for beam in photon_beams_data:
                    if "FFF" in beam:
                        data["beams"]["photons_fff"].append(
                            int(beam.split(" ")[0]))

                    else:
                        data["beams"]["photons"].append(int(beam))

            if electron_beams_data:
                electron_beams_data = electron_beams_data.split(", ")

                for beam in electron_beams_data:
                    data["beams"]["electrons"].append(int(beam))

            self.ui.linac_comboB.addItem(data["linac_name"], data)
            self.ui.linac_comboB.setCurrentText(data["linac_name"])

    def add_linac_manufacturer_changed(self,
                                       manufacturer: str,
                                       linac_model_comboB: QComboBox):
        linac_model_comboB.clear()

        if manufacturer == "Varian":
            linac_model_comboB.addItems(["Halycon", "TrueBeam", "VitalBeam"])

        else:
            linac_model_comboB.addItems(["Harmony", "Versa HD", "Synergy", "Infinity"])
        
    def linac_view_changed(self, index: int):
        item_data = self.ui.linac_comboB.itemData(index,
                                                  Qt.ItemDataRole.UserRole)
        
        self.ui.linac_name_field.setText(item_data["linac_name"])
        self.ui.linac_model_field.setText(item_data["linac_model"])
        self.ui.linac_serial_num_field.setText(item_data["linac_serial_num"])

        self.ui.photon_beam_field.setText(" ".join(
            [str(x) for x in item_data["beams"]["photons"]]))
        
        self.ui.photon_fff_beam_field.setText(" ".join(
            [str(x) for x in item_data["beams"]["photons_fff"]]))
        
        self.ui.electron_beam_field.setText(" ".join(
            [str(x) for x in item_data["beams"]["electrons"]]))