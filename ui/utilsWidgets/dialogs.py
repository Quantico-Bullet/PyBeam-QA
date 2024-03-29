from PySide6.QtWidgets import (QWidget, QDialogButtonBox, QSpacerItem, QGridLayout,
                               QSizePolicy, QDialog, QLabel,
                               QVBoxLayout, QMessageBox)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QSize

from enum import Flag

from ui.py_ui import icons_rc

class MessageDialog(QDialog):

    NO_ICON = 0
    INFO_ICON = 1
    WARNING_ICON = 2
    CRITICAL_ICON = 3
    QUESTION_ICON = 4

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.header_text = QLabel()
        self.header_text.setWordWrap(True)
        self.header_text.setMinimumWidth(400)
        self.icon = QLabel()
        self.icon.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.message_text = QLabel()
        self.message_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        self.button_box = QDialogButtonBox()

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        hor_spacer = QSpacerItem(350, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        base_layout = QVBoxLayout()
        layout = QGridLayout()
        layout.setHorizontalSpacing(10)
        layout.addWidget(self.icon, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.header_text, 0, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.message_text, 1, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)
        layout.addItem(hor_spacer, 2, 0, 1, 2, Qt.AlignmentFlag.AlignLeft)

        base_layout.addLayout(layout)
        base_layout.addWidget(self.button_box)
        self.setLayout(base_layout)

        self.setMaximumWidth(450)

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
            pixmap = pixmap.scaled(QSize(48, 48), mode = Qt.TransformationMode.SmoothTransformation)

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
            
            pixmap = pixmap.scaled(QSize(48, 48), mode = Qt.TransformationMode.SmoothTransformation)

        self.icon.setPixmap(pixmap)


    