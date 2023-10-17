from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (QDialog, QWidget, QDialogButtonBox, QFileDialog,
                               QLineEdit)

from ui.py_ui.starshot_test_dialog_ui import Ui_StarshotTestDialog

class StarshotTestDialog(QDialog):

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.ui = Ui_StarshotTestDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Starshot Benchmark Testing")
        self.setFixedSize(self.size())

        self.apply_btn = self.ui.button_box.button(QDialogButtonBox.StandardButton.Apply)
        self.apply_btn.clicked.connect(self.accept)
        self.apply_btn.setEnabled(False)
        self.ui.sim_image_cb.addItems(["AS500", "AS1000", "AS1200"])

        self.ui.select_file_btn.clicked.connect(lambda: self.save_file_to(self.ui.out_file_le))
        self.ui.test_name_le.textChanged.connect(self.validate_info)
        self.ui.out_file_le.textChanged.connect(self.validate_info)

    def save_file_to(self, line_edit: QLineEdit):
        file_path = QFileDialog.getSaveFileName(caption="Save As...", filter="DICOM (*.dcm)")
        
        if file_path[0] != "":
            path = file_path[0].split("/")
            
            if not path[-1].endswith(".dcm"):
                path[-1] = path[-1] + ".dcm"
            
            line_edit.setText("/".join(path))

    def validate_info(self):
        if self.ui.test_name_le.text() != "" and self.ui.out_file_le.text() != "":
            self.apply_btn.setEnabled(True)

        else: self.apply_btn.setEnabled(False)


