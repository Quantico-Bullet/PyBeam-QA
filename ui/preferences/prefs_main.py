from PySide6.QtWidgets import QDialog

from ui.py_ui.preferences_ui import Ui_PreferencesDialog

class Preferences(QDialog):

    GENERAL_PAGE = 0
    DEVICES_PAGE = 1
    REPORTING_PAGE = 2
    ANALYSIS_TOOLS_PAGE = 3

    def __init__(self, nav_index: int = GENERAL_PAGE):
        super().__init__()
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Preferences ‒ PyBeam QA")

        # Add slots
        self.ui.nav_button_group.buttonClicked.connect(
            self.change_preferences_page
        )

        # Set default views
        self.change_preferences_page()

        self.ui.nav_stacked_widget.setCurrentIndex(nav_index)

    def change_preferences_page(self):
        checked_button = self.ui.nav_button_group.checkedButton()

        if checked_button == self.ui.general_btn:
            self.ui.nav_stacked_widget.setCurrentIndex(self.GENERAL_PAGE)
            self.ui.page_title_label.setText(self.ui.general_btn.text())

        elif checked_button == self.ui.devices_btn:
            self.ui.nav_stacked_widget.setCurrentIndex(self.DEVICES_PAGE)
            self.ui.page_title_label.setText(self.ui.devices_btn.text())

        elif checked_button == self.ui.reporting_btn:
            self.ui.nav_stacked_widget.setCurrentIndex(self.REPORTING_PAGE)
            self.ui.page_title_label.setText(self.ui.reporting_btn.text())

        elif checked_button == self.ui.analysis_tools_btn:
            self.ui.nav_stacked_widget.setCurrentIndex(self.ANALYSIS_TOOLS_PAGE)
            self.ui.page_title_label.setText(self.ui.analysis_tools_btn.text())



        

