from PySide6.QtWidgets import (QWidget, QHBoxLayout, QLabel)
from PySide6.QtGui import Qt, QPixmap

from ui.py_ui import icons_rc

class AnalysisInfoLabel(QWidget):

    IDLE = -1
    IN_PROGRESS = 0
    COMPLETE = 1
    FAILED = 2

    def __init__(self) -> None:
        super().__init__()
        self.setContentsMargins(0,0,0,0)

        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        self.label = QLabel()
        self.icon = QLabel()
        
        layout.addWidget(self.icon)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def set_message(self, state: int = IDLE, message: str | None = None):
        if state == self.IDLE:
            self.label.clear()
            self.icon.clear()

        elif state == self.IN_PROGRESS:
            base_text = "Analysis in progress..."
            self.label.setText(base_text + f" ({message}%)" if message else base_text)

            icon_pixmap = QPixmap(u":/colorIcons/icons/in_progress.png")
            icon_pixmap = icon_pixmap.scaled(16, 16, mode = Qt.TransformationMode.SmoothTransformation)
            self.icon.setPixmap(icon_pixmap)

        elif state == self.COMPLETE:
            base_text = "Analysis completed"
            alt_text = "Analysis completed in "
            self.label.setText(alt_text + message if message else base_text)

            icon_pixmap = QPixmap(u":/colorIcons/icons/correct.png")
            icon_pixmap = icon_pixmap.scaled(16, 16, mode = Qt.TransformationMode.SmoothTransformation)
            self.icon.setPixmap(icon_pixmap)

        elif state == self.FAILED:
            self.label.setText("Analysis failed (see error message...)")

            icon_pixmap = QPixmap(u":/colorIcons/icons/error_round.png")
            icon_pixmap = icon_pixmap.scaled(16, 16, mode = Qt.TransformationMode.SmoothTransformation)
            self.icon.setPixmap(icon_pixmap)

        else:
            raise ValueError("Unknown message state passed in")