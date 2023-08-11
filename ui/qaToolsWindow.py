from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QToolButton, QMenu, QLabel
from PySide6.QtCore import Qt, QObject, Signal, QDate, QPoint
from PySide6.QtGui import QAction, QCursor, QActionGroup, QCloseEvent, QPixmap

from ui.py_ui.photonsMainWin_ui import Ui_MainWindow
from ui.py_ui import icons_rc

class QAToolsWindow(QMainWindow):

    windowClosing = Signal()

    def __init__(self, initData: dict | None = None):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self.worksheetType = None
        self.window_title = ""

        self.untitled_counter = 0

        # disable the menu bar for now
        self._ui.menubar.setEnabled(False)

        # setup basic window functionality
        self._ui.dockWidget.close()

        copyright_text = QLabel("PyBeam QA - v0.1.0 (Copyright © 2023 Kagiso Lebang)")
        copyright_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._ui.statusbar.addPermanentWidget(
            copyright_text, 1)
        
        self._ui.tabWidget.currentChanged.connect(self.tab_window_title)
        """
        self.sheetsCurrentViewButton = QPushButton()
        self.__ui.statusbar.addPermanentWidget(self.sheetsCurrentViewButton)
        
        self.__ui.actionDetailedView.toggled.connect(lambda detailedMode: self.toggleViewMode(detailedMode))
        self.__ui.actionDetailedView.setChecked(True)

        self.viewModeMenu = QMenu()
        self.actionGroup = QActionGroup(None)
        self.simpleViewAction = QAction("Simple view")
        self.detailedViewAction = QAction("Detailed view")
        self.viewModeMenu.addAction(self.simpleViewAction)
        self.viewModeMenu.addAction(self.detailedViewAction)
        self.actionGroup.addAction(self.simpleViewAction)
        self.actionGroup.addAction(self.detailedViewAction)
        
        self.sheetsCurrentViewButton.clicked.connect(lambda: self.viewModeMenu.popup(QCursor.pos()))"""

    def toggleViewMode(self, detailedMode: bool):
        if detailedMode:
            for worksheet in self.worksheetList:
                worksheet.toggleDetailedView()
                self.sheetsCurrentViewButton.setText("Detailed View On")

        else:
            for worksheet in self.worksheetList:
                worksheet.toggleSimpleView()
                self.sheetsCurrentViewButton.setText("Simple View On")

    def add_new_worksheet(self, worksheet, worksheet_name: str, enable_icon: bool = True):
        index = self._ui.tabWidget.addTab(worksheet, worksheet_name)

        if enable_icon:
            tab_icon = QPixmap(u":/colorIcons/icons/tools.png")
            tab_icon = tab_icon.scaled(16, 16, mode = Qt.TransformationMode.SmoothTransformation)

            self._ui.tabWidget.setCurrentIndex(index)
            self._ui.tabWidget.setTabIcon(index, tab_icon)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.windowClosing.emit()
        return super().closeEvent(event)
    
    def tab_window_title(self):
        title = self._ui.tabWidget.tabText(self._ui.tabWidget.currentIndex())
        self.setWindowTitle(title + "  |  " + self.window_title)