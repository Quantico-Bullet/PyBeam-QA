from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtGui import QDesktopServices, QPixmap, QImage, QPainter, QColor
from PySide6.QtSvg import QSvgRenderer

from ui.py_ui.about_dialog_ui import Ui_AboutDialog
from ui.py_ui import icons_rc

from pylinac import __version__ as pylinac_version
from pdfrw import __version__ as pdfrw_version
from PySide6 import __version__ as pyside6_version
from pyqtgraph import __version__ as pyqtgraph_version

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

        self.ui.open_source_te.setText(f"⊹ PySide6 ({pyside6_version})\n" \
                                       f"⊹ Pylinac ({pylinac_version})\n" \
                                       f"⊹ Pyqtgraph ({pyqtgraph_version})\n" \
                                       f"⊹ Pdfrw ({pdfrw_version})") 

        self.setFixedSize(self.size())

    def open_github(self):
        QDesktopServices.openUrl("https://github.com/Quantico-Bullet/PyBeam-QA/")

