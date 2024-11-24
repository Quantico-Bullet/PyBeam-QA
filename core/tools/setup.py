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
                               QLineEdit, QPushButton, QSizePolicy, QFileDialog, QDialogButtonBox)
from PySide6.QtCore import Qt

from ui import move_to_screen_center, resize_to_available_screen
from ui.util_widgets.dialogs import MessageDialog
from ui.util_widgets.wizard import WizardWindow, WizardPage

import sys

license_path = "core/about/license.txt"
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
    workspace_widget = QWidget()

    workspace_form_lay = QFormLayout()
    workspace_hbox_lay = QHBoxLayout()
    folder_label = QLabel("Workspace Folder:")
    folder_field = QLineEdit()
    folder_field.setMinimumWidth(300)
    folder_field.setReadOnly(True)
    select_button = QPushButton("Select Folder")
    select_button.clicked.connect(lambda: select_workspace_folder(folder_field))

    workspace_widget.setLayout(workspace_form_lay)
    workspace_widget.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
    workspace_hbox_lay.addWidget(folder_field)
    workspace_hbox_lay.addWidget(select_button)
    workspace_form_lay.addRow(folder_label, workspace_hbox_lay)

    workspace_page = WizardPage(workspace_widget, "Workspace Setup",
                                "Setup Your Workspace")
    workspace_page.register_field(folder_field)
    setup_wizard.add_page(workspace_page)
    
    # Finalise setup page
    final_widget = QWidget()
    final_page = WizardPage(final_widget, "Finalising Setup",
                            "Let's Wrap It Up")
    setup_wizard.add_page(final_page)
    

    result = setup_wizard.exec()

    if result == QDialog.DialogCode.Accepted:
        setup_info["accepted_terms"] = True
        on_licence_accepted()
    else:
        sys.exit()

def select_workspace_folder(line_edit: QLineEdit):
        caption = "Select a Folder for the Workspace"
        folder = QFileDialog.getExistingDirectory(caption=caption)

        if folder:
            line_edit.setText(folder)

def on_licence_accepted() -> None:
    pass