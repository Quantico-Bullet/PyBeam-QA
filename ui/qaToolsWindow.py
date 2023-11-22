from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QDesktopServices

from ui.utilsWidgets.statusbar_widgets import AnalysisInfoLabel
from ui.py_ui.qaMainWin_ui import Ui_MainWindow
from ui.about_dialog import AboutDialog
from ui.py_ui import icons_rc

class QAToolsWindow(QMainWindow):

    windowClosing = Signal()

    def __init__(self, initData: dict | None = None):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worksheetType = None
        self.window_title = ""
        self.window_close_signalled = False

        self.untitled_counter = 0

        #self.ui.menuHelp.addAction("Contents", lambda: print(1), "F1")
        self.ui.menuHelp.addSeparator()
        self.ui.menuHelp.addAction("Report Issue", lambda: QDesktopServices.openUrl(
            "https://github.com/Quantico-Bullet/PyBeam-QA/issues"))
        self.ui.menuHelp.addAction("Request Feature", lambda: QDesktopServices.openUrl(
            "https://github.com/Quantico-Bullet/PyBeam-QA/issues"))
        self.ui.menuHelp.addSeparator()

        # Add app about
        self.ui.menuHelp.addAction("About PyBeam QA...", self.about_app)

        full_screen_action = self.ui.menuView.addAction("Full Screen")
        full_screen_action.setEnabled(False)
        full_screen_action.setShortcut("F11")
        full_screen_action.setCheckable(True)
        #full_screen_action.toggled.connect(self.set_window_state)

        # setup basic window functionality
        self.ui.dockWidget.close()

        #copyright_text = QLabel("PyBeam QA - v0.1.0 (Copyright © 2023 Kagiso Lebang)")
        #copyright_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #self.ui.statusbar.addPermanentWidget(
        #    copyright_text, 1)
        
        #Add analysis message to status bar
        self.analysis_info_label = AnalysisInfoLabel()
        self.ui.statusbar.addWidget(self.analysis_info_label)

        self.curr_anal_message = None
        self.curr_anal_state = AnalysisInfoLabel.IDLE
        
        self.ui.tabWidget.currentChanged.connect(self.tab_window_changed)
        self.ui.tabWidget.tabCloseRequested.connect(self.ui.tabWidget.removeTab)

        self.current_tab_index = 0
        self.current_window_state = self.isMaximized()

    def add_new_worksheet(self, worksheet, worksheet_name: str, enable_icon: bool = True):
        index = self.ui.tabWidget.addTab(worksheet, worksheet_name)

        if enable_icon:
            tab_icon = QPixmap(u":/colorIcons/icons/tools.png")
            tab_icon = tab_icon.scaled(16, 16, mode = Qt.TransformationMode.SmoothTransformation)

            self.ui.tabWidget.setCurrentIndex(index)
            self.ui.tabWidget.setTabIcon(index, tab_icon) 
    
    def tab_window_changed(self, index: int):
        if self.ui.tabWidget.count() > 0:
            title = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())
            self.setWindowTitle(title + "  |  " + self.window_title)
            
            self.analysis_worksheet = self.ui.tabWidget.widget(index)
            analysis_state = self.analysis_worksheet.analysis_state
            analysis_message = self.analysis_worksheet.analysis_message

            self.analysis_info_label.set_message(analysis_state, analysis_message)
            self.analysis_worksheet.analysis_info_signal.connect(lambda: "dummy disconnect")
            self.analysis_worksheet.analysis_info_signal.disconnect()
            self.analysis_worksheet.analysis_info_signal.connect(lambda x: 
                    self.analysis_info_label.set_message(x["state"], x["message"]))

        elif self.ui.tabWidget.count() == 0:
            self.close()

    def about_app(self):
        about = AboutDialog()
        about.exec()

        del about