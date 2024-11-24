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
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from PySide6.QtWidgets import QDialog, QWidget, QDialogButtonBox, QFileDialog, QLineEdit

from ui.py_ui.picket_fence_test_dialog_ui import Ui_PFTestDialog

import ast

class PFTestDialog(QDialog):
    
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.ui = Ui_PFTestDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Picket Fence Benchmark Testing")

        self.apply_btn = self.ui.button_box.button(QDialogButtonBox.StandardButton.Apply)
        self.apply_btn.clicked.connect(self.accept)

        self.ui.picket_offsets_le.textChanged.connect(self.validate_info)
        self.ui.num_pickets_sb.valueChanged.connect(self.validate_info)
        self.ui.test_name_le.textChanged.connect(self.validate_info)
        self.ui.out_file_le.textChanged.connect(self.validate_info)
        self.ui.select_file_btn.clicked.connect(lambda: self.save_file_to(self.ui.out_file_le))

        self.ui.sim_image_cb.addItems(["AS500", "AS1000", "AS1200"])
        self.ui.image_orientation_cb.addItems(["Up-Down", "Left-Right"])

        self.apply_btn.setEnabled(False)

        self.picket_offset_errors = []

    def save_file_to(self, line_edit: QLineEdit):
        file_path = QFileDialog.getSaveFileName(caption="Save As...", filter="DICOM (*.dcm)")
        
        if file_path[0] != "":
            path = file_path[0].split("/")
            
            if not path[-1].endswith(".dcm"):
                path[-1] = path[-1] + ".dcm"
            
            line_edit.setText("/".join(path))

    def validate_info(self):
        pf_offset_errors = self.ui.picket_offsets_le.text()
        self.picket_offset_errors.clear()

        if pf_offset_errors != "":
            offset_error_list = pf_offset_errors.split("; ")

            if len(offset_error_list) == self.ui.num_pickets_sb.value():
                for err_value in offset_error_list:
                    try:
                        err_value = ast.literal_eval(err_value)

                        if isinstance(err_value, (float, int)):
                            self.picket_offset_errors.append(err_value)
                        
                        else: return self.apply_btn.setEnabled(False)

                    except Exception as err:
                        return self.apply_btn.setEnabled(False)
                    
            else: return self.apply_btn.setEnabled(False)

        elif pf_offset_errors == "":
            self.apply_btn.setEnabled(True)
        
        else: return self.apply_btn.setEnabled(False)
            
        if self.ui.test_name_le.text() != "" and self.ui.out_file_le.text() != "":
            self.apply_btn.setEnabled(True)

        else: self.apply_btn.setEnabled(False)
