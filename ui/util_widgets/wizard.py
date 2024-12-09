from PySide6.QtCore import Qt, Signal, QObject, QEvent
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtWidgets import (QDialog, QWidget, QGridLayout, QDialogButtonBox,
                               QLabel, QStackedWidget, QSizePolicy, QFrame, QScrollArea,
                               QHBoxLayout, QVBoxLayout, QLineEdit, QTextEdit,
                               QCheckBox, QComboBox)

from ui.py_ui import icons_rc

class SectionItem(QFrame):

    item_clicked_signal = Signal(QObject)

    def __init__(self, title_text: str = ""):
        super().__init__(None)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.title = QLabel(title_text)
        self.status_icon = QLabel()
        self.status_icon.setFixedSize(32, 32)
        self.status_icon.setScaledContents(True)
        self.status_icon.setSizePolicy(QSizePolicy.Policy.Fixed,
                                       QSizePolicy.Policy.Fixed)
        self.main_layout = QHBoxLayout()

        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.status_icon)
        self.main_layout.addWidget(self.title)

        self.set_active(False)
        self.set_status(0)
        
        self.setMinimumWidth(250)

    def set_text(self, title_text: str = "") -> None:
        self.title.setText(title_text)

    def set_status(self, status: int) -> None:
        if status == WizardPage.LOCKED:
            self.status_icon.setPixmap(QPixmap(u":/colorIcons/icons/not_started.png"))

        elif status == WizardPage.IN_PROGRESS:
            self.status_icon.setPixmap(QPixmap(u":/colorIcons/icons/in_progress.png"))

        elif status == WizardPage.COMPLETED:
            self.status_icon.setPixmap(QPixmap(u":/colorIcons/icons/correct.png"))

        else:
            self.status_icon.clear()

    def set_active(self, active: bool) -> None:
        if active:
            self.setStyleSheet("SectionItem {" \
                               "background-color: rgba(82, 142, 122, 0.30);" \
                               "border-radius: 15px;}" \
                               "QLabel {" \
                               "font-weight: bold}")
        else:
            self.setStyleSheet("SectionItem {" \
                               "font-weight: 400;" \
                               "background-color: rgba(0, 0, 0, 0.0);" \
                               "border-radius: 15px;}")
            
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.item_clicked_signal.emit(self)

        return super().mousePressEvent(event)

class WizardPage(QScrollArea):

    LOCKED = 0
    IN_PROGRESS = 1
    COMPLETED = 2

    page_status_changed = Signal(int)

    def __init__(self, widget, 
                 title: str = "", summary: str = "") -> None:
        super().__init__(None)

        widget.setContentsMargins(10, 0, 10, 0)

        self.status = self.LOCKED
        self.summary_title = summary
        self.title = title
        self.section_item = SectionItem(self.title)
        self.section_item.setEnabled(False)
        self.page_status_changed.connect(self.section_item.set_status)
        self.setWidget(widget)
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.Shape.NoFrame)
        
        self.mandatory_fields: list[QWidget] = []

    def register_field(self, widget: QWidget) -> None:
        if isinstance(widget, (QLineEdit, QTextEdit)):
            widget.textChanged.connect(self.validate_page)
            widget.textChanged.connect(self.page_status_changed.emit)

        elif isinstance(widget, QCheckBox):
            widget.toggled.connect(self.validate_page)
            widget.toggled.connect(self.page_status_changed.emit)

        elif isinstance(widget, QComboBox):
            widget.currentTextChanged.connect(self.validate_page)
            widget.currentTextChanged.connect(self.page_status_changed.emit)

        self.mandatory_fields.append(widget)

    def validate_page(self) -> bool:
        page_is_valid = True 

        if self.status == WizardPage.LOCKED:
            return False

        for widget in self.mandatory_fields:
            if isinstance(widget, (QLineEdit, QTextEdit)):
                if widget.text() == "":
                    page_is_valid = False
                    break
            
            elif isinstance(widget, QCheckBox):
                if not widget.isChecked():
                    page_is_valid = False
                    break

        if page_is_valid:
            self.set_status(WizardPage.COMPLETED, broadcast = False)
        else:
            self.set_status(WizardPage.IN_PROGRESS, broadcast = False)

        return page_is_valid

    def set_active(self, active: bool) -> None:
        self.section_item.set_active(active)

    def set_status(self, status: int, broadcast: bool = True) -> None:
        self.section_item.set_status(status)
        self.status = status

        if self.status == WizardPage.LOCKED:
            self.setEnabled(False)
            self.section_item.setEnabled(False)
        else:
            self.setEnabled(True)
            self.section_item.setEnabled(True)
        
        if broadcast: self.page_status_changed.emit(self.status)

class WizardWindow(QDialog):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setModal(True)
        self.setWindowTitle("Setup ‒ PyBeam QA")
        self.setMinimumSize(900, 280)  # For testing purposes
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.description_label = QLabel()
        self.description_label.setContentsMargins(0,10,0,20)
        self.description_label.setStyleSheet("font-size: 16pt;")
        self.description_label.setTextFormat(Qt.TextFormat.RichText)
        
        self.section_items: list[SectionItem] = []

        self.wizard_button_box = QDialogButtonBox(self)
        self.wizard_button_box.accepted.connect(self.accept)
        self.wizard_button_box.rejected.connect(self.reject)
        self.wizard_button_box.setContentsMargins(0, 10, 0, 0)
        self.previous_button = self.wizard_button_box.addButton("<< Previous",
                                                QDialogButtonBox.ButtonRole.ActionRole)
        self.previous_button.clicked.connect(self.to_prev_page)
        self.previous_button.setDisabled(True)
        self.next_button = self.wizard_button_box.addButton("Next >>", 
                                                QDialogButtonBox.ButtonRole.ActionRole)
        self.next_button.clicked.connect(self.to_next_page)
        #self.next_button.setDisabled(True)
        self.finish_button = self.wizard_button_box.addButton("Finish",
                                                QDialogButtonBox.ButtonRole.AcceptRole)
        self.finish_button.setEnabled(False)
        self.cancel_button = self.wizard_button_box.addButton(
                                                QDialogButtonBox.StandardButton.Cancel)

        self.page_list_scroller = QScrollArea()
        self.page_list_scroller.setFrameShape(QFrame.Shape.NoFrame)
        self.page_list_scroller.setFixedSize(280, 400)

        self.page_list = QWidget()
        self.page_list.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, 
                                     QSizePolicy.Policy.MinimumExpanding)
        self.page_list_layout = QVBoxLayout(self.page_list)
        self.page_list_layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetMinAndMaxSize)

        self.page_list_scroller.setWidget(self.page_list)

        self.pages_widget = QStackedWidget()
        self.pages_widget.currentChanged.connect(self.on_page_changed)
        self.pages_widget.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, 
                                        QSizePolicy.Policy.MinimumExpanding)
        
        splitter_line = QFrame()
        splitter_line.setFrameShape(QFrame.Shape.VLine)
        splitter_line.setLineWidth(2)
        splitter_line.setStyleSheet("color: rgba(0, 0, 0, 0.1);")

        self.main_layout.addWidget(self.page_list_scroller, 1, 0, 1, 1,
                                   Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(splitter_line, 1, 1)
        self.main_layout.addWidget(self.description_label, 0, 2, Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.pages_widget, 1, 2)
        self.main_layout.addWidget(self.wizard_button_box, 2, 0, 1, 3,
                                   Qt.AlignmentFlag.AlignRight)
    
    def add_page(self, wizard_page: WizardPage) -> None:
        self.pages_widget.addWidget(wizard_page)

        self.section_items.append(wizard_page.section_item)
        self.page_list_layout.addWidget(wizard_page.section_item)

        wizard_page.section_item.set_text(
            f"{len(self.section_items)}. {wizard_page.title}"
        )

        if self.pages_widget.count() == 1:
            wizard_page.set_active(True)
            wizard_page.set_status(WizardPage.IN_PROGRESS)

        wizard_page.validate_page()
        # Register this current page
        wizard_page.section_item.item_clicked_signal.connect(self.section_item_clicked)
        wizard_page.page_status_changed.connect(self.toggle_buttons)

    def toggle_buttons(self) -> None:
        if self.pages_widget.currentIndex() > 0:
            self.previous_button.setEnabled(True)

            if self.pages_widget.currentIndex() == (self.pages_widget.count() - 1):
                self.next_button.setEnabled(False)

                if self.pages_widget.currentWidget().validate_page():
                    self.finish_button.setEnabled(True)
                else:
                    self.finish_button.setEnabled(False)
            else:
                if self.pages_widget.currentWidget().validate_page():
                    self.next_button.setEnabled(True)
                else:
                    self.next_button.setEnabled(False)
        else:
            self.previous_button.setEnabled(False)

            if self.pages_widget.currentWidget().validate_page():
                self.next_button.setEnabled(True)
            else:
                self.next_button.setEnabled(False)
            
    def section_item_clicked(self, section_item):
        for item in self.section_items:
            if item == section_item:
                self.go_to_page(self.section_items.index(item))

    def to_prev_page(self) -> None:
        self.go_to_page(self.pages_widget.currentIndex() - 1)

    def to_next_page(self) -> None:
        self.go_to_page(self.pages_widget.currentIndex() + 1)

    def go_to_page(self, index: int) -> None:
        if not index == self.pages_widget.currentIndex():
            current_page: WizardPage = self.pages_widget.currentWidget()
            current_page.set_active(False)
            self.pages_widget.setCurrentIndex(index)

    def on_page_changed(self) -> None:
        current_page: WizardPage = self.pages_widget.currentWidget()
        current_page.set_active(True)
        current_page.set_status(WizardPage.IN_PROGRESS)

        self.description_label.setText(current_page.summary_title)
