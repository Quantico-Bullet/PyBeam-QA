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

from PySide6.QtGui import (QPixmap, QImage, QDesktopServices, QPixmap, QImage, QPainter, 
                           QColor)
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QWidget, QDialogButtonBox, QGridLayout,
                               QSizePolicy, QDialog, QLabel,
                               QVBoxLayout)
from PySide6.QtGui import QGuiApplication

from core import __version__ as pybeamqa_version
from pdfrw import __version__ as pdfrw_version
from pylinac import __version__ as pylinac_version
from PySide6 import __version__ as pyside6_version
from pyqtgraph import __version__ as pyqtgraph_version

from ui.py_ui import icons_rc
from ui.py_ui.about_dialog_ui import Ui_AboutDialog

class MessageDialog(QDialog):

    NO_ICON = 0
    INFO_ICON = 1
    WARNING_ICON = 2
    CRITICAL_ICON = 3
    QUESTION_ICON = 4

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.header_text = QLabel()
        self.message_text = QLabel()
        self.header_text.setWordWrap(True)
        self.message_text.setWordWrap(True)
        self.header_text.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.message_text.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        self.icon = QLabel()
        self.icon.setFixedSize(QSize(48, 48))
        self.icon.setScaledContents(True)
        self.icon.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        self.button_box = QDialogButtonBox()

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        base_layout = QVBoxLayout()
        layout = QGridLayout()
        layout.setHorizontalSpacing(10)
        layout.addWidget(self.icon, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.header_text, 0, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.message_text, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        base_layout.addLayout(layout)
        base_layout.addWidget(self.button_box)
        self.setLayout(base_layout)

        primary_screen = QGuiApplication.primaryScreen()

        self.setFixedWidth(primary_screen.availableSize().toTuple()[0] * 0.35)

        #set default button
        self.set_standard_buttons()

    def set_standard_buttons(self, buttons = QDialogButtonBox.StandardButton.Ok):
        self.button_box.clear()
        self.button_box.setStandardButtons(buttons)

    def set_title(self, title):
        return super().setWindowTitle(title)

    def set_header_text(self, text: str) -> None:
        text = "<p><span style=\" font-weight:700; font-size: 12pt;\">" \
                f"{text}</span></p>"
        
        self.header_text.setText(text)
    
    def set_info_text(self, text: str) -> None:
        self.message_text.setText(text)
    
    def set_icon(self, pixmap: QPixmap | QImage | str | int, smooth_image: bool = True) -> None:
        if isinstance(pixmap, (QPixmap, QImage)) and smooth_image:
            pixmap = pixmap

        elif isinstance(pixmap, int):
            if pixmap == self.INFO_ICON:
                pixmap = QPixmap(u":/colorIcons/icons/info.png")

            elif pixmap == self.WARNING_ICON:
                pixmap = QPixmap(u":/colorIcons/icons/warning.png")

            elif pixmap == self.CRITICAL_ICON:
                pixmap = QPixmap(u":/colorIcons/icons/error_round.png")

            elif pixmap == self.QUESTION_ICON:
                pixmap = QPixmap(u":/colorIcons/icons/question.png")

            else:
                return
            
        self.icon.setPixmap(pixmap)

class AboutDialog(QDialog):

    app_svg = QSvgRenderer(u":/misc_icons/icons/ic_app.svg")
    app_img = QImage(256, 256, QImage.Format.Format_ARGB32)
    app_img.fill(QColor(255, 255, 255, 0))
    qpainter = QPainter(app_img)
    app_svg.render(qpainter)
    qpainter.end()
    
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.setWindowTitle("About PyBeam QA")

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        self.ui.github_btn.clicked.connect(self.open_github)
        
        self.app_icon = QPixmap.fromImage(self.app_img)
        self.app_icon = self.app_icon.scaled(QSize(128, 128),
                               mode = Qt.TransformationMode.SmoothTransformation)
        self.ui.app_icon.setPixmap(self.app_icon) 

        self.ui.app_version_label.setText(f"version {pybeamqa_version}")
        self.ui.open_source_te.setText(f"⊹ PySide6 ({pyside6_version})\n" \
                                       f"⊹ Pylinac ({pylinac_version})\n" \
                                       f"⊹ Pyqtgraph ({pyqtgraph_version})\n" \
                                       f"⊹ Pdfrw ({pdfrw_version})") 

        self.setFixedSize(self.size())

    def open_github(self):
        QDesktopServices.openUrl("https://github.com/Quantico-Bullet/PyBeam-QA/")