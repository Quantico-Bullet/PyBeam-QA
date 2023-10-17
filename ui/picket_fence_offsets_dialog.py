from PySide6.QtWidgets import QDialog, QWidget, QDialogButtonBox, QFileDialog, QLineEdit

from ui.py_ui.pf_offsets_dialog_ui import Ui_PFOffsetDialog

class PFTestDialog(QDialog):
    
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.ui = Ui_PFOffsetDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Set leaf-pair offsets")        