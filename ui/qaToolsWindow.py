from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QToolButton, QMenu, QLabel, QDialog
from PySide6.QtCore import Qt, QObject, Signal, QDate, QPoint
from PySide6.QtGui import QAction, QCursor, QActionGroup, QCloseEvent, QPixmap

from ui.py_ui.qaMainWin_ui import Ui_MainWindow
from ui.about_dialog import AboutDialog
from ui.py_ui import icons_rc

class QAToolsWindow(QMainWindow):

    windowClosing = Signal()

    def __init__(self, initData: dict | None = None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worksheetType = None
        self.window_title = ""
        self.window_close_signalled = False

        self.untitled_counter = 0

        # Add app about
        self.ui.menuHelp.addAction("About PyBeam QA...", self.about_app)

        # setup basic window functionality
        self.ui.dockWidget.close()

        copyright_text = QLabel("PyBeam QA - v0.1.0 (Copyright © 2023 Kagiso Lebang)")
        copyright_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ui.statusbar.addPermanentWidget(
            copyright_text, 1)
        
        self.ui.tabWidget.currentChanged.connect(self.tab_window_changed)
        self.ui.tabWidget.tabCloseRequested.connect(self.ui.tabWidget.removeTab)

    def add_new_worksheet(self, worksheet, worksheet_name: str, enable_icon: bool = True):
        index = self.ui.tabWidget.addTab(worksheet, worksheet_name)

        if enable_icon:
            tab_icon = QPixmap(u":/colorIcons/icons/tools.png")
            tab_icon = tab_icon.scaled(16, 16, mode = Qt.TransformationMode.SmoothTransformation)

            self.ui.tabWidget.setCurrentIndex(index)
            self.ui.tabWidget.setTabIcon(index, tab_icon)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.windowClosing.emit()
        event.accept()    
    
    def tab_window_changed(self):
        if self.ui.tabWidget.count() > 0:
            title = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())
            self.setWindowTitle(title + "  |  " + self.window_title)

        elif self.ui.tabWidget.count() > 1:
            self.close()

    def about_app(self):
        about = AboutDialog()
        about.exec()

        del about