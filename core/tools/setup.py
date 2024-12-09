# PyBeam QA
# Copyright (C) 2024 Kagiso Lebang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import (QWidget, QLabel, QDialog, QHBoxLayout, QFormLayout,
                               QLineEdit, QPushButton, QSizePolicy, QFileDialog, QGroupBox,
                               QVBoxLayout,)
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget, QGraphicsSvgItem

from ui import move_to_screen_center, resize_to_available_screen
from ui.util_widgets.wizard import WizardWindow, WizardPage
from ui.py_ui import icons_rc

from pathlib import Path
from core.configuration.config import WorkspaceConfig

import sys

workspace_config = WorkspaceConfig()
license_path = "core/about/license.rtf"

def init_setup_wizard() -> None:

    setup_info = {"accepted_terms": False,
                  "workspace_dir": None}

    setup_wizard = WizardWindow()
    resize_to_available_screen(setup_wizard, (0.6, 0.8))
    move_to_screen_center(setup_wizard)

    with open(license_path, mode='r') as license_file:
        license_text = license_file.read()

    # License page
    license_text_viewer = QLabel(license_text)
    license_page = WizardPage(license_text_viewer, "PyBeam QA License", 
                              "First Things First")
    setup_wizard.add_page(license_page)

    # Workspace page
    workspace_main = QWidget()
    workspace_main_layout = QVBoxLayout(workspace_main)
    workspace_main_layout.setSpacing(20)
    workspace_main.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    workspace_dir_grp = QGroupBox("Workspace Directory")
    workspace_dir_grp.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    institution_grp = QGroupBox("Institution Details")
    institution_grp.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    workspace_main_layout.addWidget(workspace_dir_grp)
    workspace_main_layout.addWidget(institution_grp)

    workspace_form_lay = QFormLayout(workspace_dir_grp)
    workspace_form_lay.setHorizontalSpacing(20)
    workspace_hbox_lay = QHBoxLayout()
    workspace_hbox_lay.setSpacing(6)
    folder_label = QLabel("Workspace path:")
    folder_field = QLineEdit()
    #folder_field.setMinimumWidth(300)
    folder_field.setReadOnly(True)
    select_button = QPushButton("Select Folder")
    select_button.clicked.connect(lambda: select_workspace_folder(folder_field))

    workspace_hbox_lay.addWidget(folder_field)
    workspace_hbox_lay.addWidget(select_button)
    workspace_form_lay.addRow(folder_label, workspace_hbox_lay)

    institution_form_lay = QFormLayout()
    institution_form_lay.setHorizontalSpacing(20)
    institution_label = QLabel("Institution:")
    institution_field = QLineEdit()
    department_label = QLabel("Department:")
    department_field = QLineEdit()
   
    institution_grp.setLayout(institution_form_lay)
    institution_form_lay.addRow(institution_label, institution_field)
    institution_form_lay.addRow(department_label, department_field)

    workspace_page = WizardPage(workspace_main, "Workspace Setup",
                                "Setup Your Workspace")
    workspace_page.register_field(folder_field)
    workspace_page.register_field(institution_field)
    workspace_page.register_field(department_field)
    setup_wizard.add_page(workspace_page)

    result = setup_wizard.exec()

    if result == QDialog.DialogCode.Accepted:
        config = workspace_config.getConfig()
        config["workspace_path"] = folder_field.text()
        config["institution_name"] = institution_field.text()
        config["department_name"] = department_field.text()

        workspace_config.saveConfig(config)

        Path(config["workspace_path"]).mkdir(exist_ok = True)
    else:
        sys.exit()

def select_workspace_folder(line_edit: QLineEdit):
        caption = "Select a Folder for the Workspace"
        folder = QFileDialog.getExistingDirectory(caption=caption)

        if folder and "PyBeamQA Workspace" not in folder:
            line_edit.setText(folder + "/PyBeamQA Workspace")

        else:
            line_edit.setText(folder)