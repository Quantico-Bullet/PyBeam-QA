from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize

from ui.py_ui import icons_rc
from ui.py_ui.picketFenceWorksheet_ui import Ui_QPicketFenceWorksheet
from core.analysis.picket_fence import QPicketFence

import enum

from pylinac.picketfence import MLC

class QPicketFenceWorksheet(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_QPicketFenceWorksheet()
        self.ui.setupUi(self)

        self.image_icon = QIcon()
        self.image_icon.addFile(u":/colorIcons/icons/picture.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.mlcTypeCB.addItems([mlc.value["name"] for mlc in MLC])

        


