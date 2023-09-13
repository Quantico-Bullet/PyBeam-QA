from PySide6.QtWidgets import (QWidget, QMessageBox, QSpacerItem, QGridLayout,
                               QSizePolicy, QLineEdit, QFileDialog)
from PySide6.QtGui import QPixmap, QImage, QResizeEvent
from PySide6.QtCore import Qt, QSize

from ui.py_ui import icons_rc

class MessageDialog(QMessageBox):

    NO_ICON = 0
    INFO_ICON = 1
    WARNING_ICON = 2
    CRITICAL_ICON = 3
    QUESTION_ICON = 4

    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        hor_spacer = QSpacerItem(800, 0,
                                 QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout: QGridLayout = self.layout()
        layout.addItem(hor_spacer, layout.rowCount(), 0, 1, layout.columnCount())
        self.setTextFormat(Qt.TextFormat.RichText)

        self.setStyleSheet("QSpacerItem{min-width: 600px;}")

    def set_title(self, title):
        return super().setWindowTitle(title)

    def set_text(self, text: str) -> None:
        text = "<p><span style=\" font-weight:700; font-size: 12pt;\">" \
                f"{text}</span></p>"
        return super().setText(text)
    
    def set_info_text(self, text: str) -> None:
        return super().setInformativeText(text)
    
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

        return super().setIconPixmap(pixmap)