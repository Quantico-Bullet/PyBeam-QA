# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 515)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setStyleSheet(u"QPushButton:!checked{\n"
"	background-color: rgba(82, 142, 122,20);\n"
"    min-width: 140px;\n"
"	min-height:25px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-top-left-radius: 15px;\n"
"	border-top-right-radius: 0px ;\n"
"	border-bottom-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px ;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(52, 91, 78);\n"
"	color: white;\n"
"	font: bold;\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 300, 436))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nav_top_spacer = QSpacerItem(20, 132, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.nav_top_spacer)

        self.general_btn = QPushButton(self.scrollAreaWidgetContents)
        self.general_btn.setObjectName(u"general_btn")
        self.general_btn.setCheckable(True)
        self.general_btn.setChecked(True)

        self.verticalLayout.addWidget(self.general_btn)

        self.devices_btn = QPushButton(self.scrollAreaWidgetContents)
        self.devices_btn.setObjectName(u"devices_btn")
        self.devices_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.devices_btn)

        self.reporting_btn = QPushButton(self.scrollAreaWidgetContents)
        self.reporting_btn.setObjectName(u"reporting_btn")
        self.reporting_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.reporting_btn)

        self.analysis_config_btn = QPushButton(self.scrollAreaWidgetContents)
        self.analysis_config_btn.setObjectName(u"analysis_config_btn")
        self.analysis_config_btn.setEnabled(True)
        self.analysis_config_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.analysis_config_btn)

        self.nav_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.nav_bottom_spacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.page_title_label = QLabel(self.centralwidget)
        self.page_title_label.setObjectName(u"page_title_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.page_title_label.sizePolicy().hasHeightForWidth())
        self.page_title_label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(16)
        self.page_title_label.setFont(font)

        self.gridLayout.addWidget(self.page_title_label, 0, 2, 1, 1, Qt.AlignHCenter)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.general_page = QWidget()
        self.general_page.setObjectName(u"general_page")
        self.stackedWidget.addWidget(self.general_page)
        self.devices_page = QWidget()
        self.devices_page.setObjectName(u"devices_page")
        self.verticalLayout_2 = QVBoxLayout(self.devices_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.devices_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.linac_tab = QWidget()
        self.linac_tab.setObjectName(u"linac_tab")
        self.verticalLayout_3 = QVBoxLayout(self.linac_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.linac_scroll_area = QScrollArea(self.linac_tab)
        self.linac_scroll_area.setObjectName(u"linac_scroll_area")
        self.linac_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 443, 370))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.linac_label = QLabel(self.scrollAreaWidgetContents_2)
        self.linac_label.setObjectName(u"linac_label")
        sizePolicy.setHeightForWidth(self.linac_label.sizePolicy().hasHeightForWidth())
        self.linac_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.linac_label)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.lina_info_group_box = QGroupBox(self.scrollAreaWidgetContents_2)
        self.lina_info_group_box.setObjectName(u"lina_info_group_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lina_info_group_box.sizePolicy().hasHeightForWidth())
        self.lina_info_group_box.setSizePolicy(sizePolicy3)
        self.verticalLayout_4 = QVBoxLayout(self.lina_info_group_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.linac_info_fl = QFormLayout()
        self.linac_info_fl.setObjectName(u"linac_info_fl")
        self.linac_name_label = QLabel(self.lina_info_group_box)
        self.linac_name_label.setObjectName(u"linac_name_label")

        self.linac_info_fl.setWidget(0, QFormLayout.LabelRole, self.linac_name_label)

        self.linac_name_field = QLabel(self.lina_info_group_box)
        self.linac_name_field.setObjectName(u"linac_name_field")

        self.linac_info_fl.setWidget(0, QFormLayout.FieldRole, self.linac_name_field)

        self.linac_model_label = QLabel(self.lina_info_group_box)
        self.linac_model_label.setObjectName(u"linac_model_label")

        self.linac_info_fl.setWidget(1, QFormLayout.LabelRole, self.linac_model_label)

        self.linac_model_field = QLabel(self.lina_info_group_box)
        self.linac_model_field.setObjectName(u"linac_model_field")

        self.linac_info_fl.setWidget(1, QFormLayout.FieldRole, self.linac_model_field)

        self.serial_num_label = QLabel(self.lina_info_group_box)
        self.serial_num_label.setObjectName(u"serial_num_label")

        self.linac_info_fl.setWidget(2, QFormLayout.LabelRole, self.serial_num_label)

        self.serial_num_field = QLabel(self.lina_info_group_box)
        self.serial_num_field.setObjectName(u"serial_num_field")

        self.linac_info_fl.setWidget(2, QFormLayout.FieldRole, self.serial_num_field)

        self.linac_state_label = QLabel(self.lina_info_group_box)
        self.linac_state_label.setObjectName(u"linac_state_label")

        self.linac_info_fl.setWidget(3, QFormLayout.LabelRole, self.linac_state_label)

        self.linac_state_field = QLabel(self.lina_info_group_box)
        self.linac_state_field.setObjectName(u"linac_state_field")

        self.linac_info_fl.setWidget(3, QFormLayout.FieldRole, self.linac_state_field)


        self.verticalLayout_4.addLayout(self.linac_info_fl)


        self.verticalLayout_5.addWidget(self.lina_info_group_box)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 9)
        self.beam_energies_fl = QFormLayout()
        self.beam_energies_fl.setObjectName(u"beam_energies_fl")
        self.photon_beam_label = QLabel(self.groupBox)
        self.photon_beam_label.setObjectName(u"photon_beam_label")

        self.beam_energies_fl.setWidget(0, QFormLayout.LabelRole, self.photon_beam_label)

        self.photon_beam_field = QLabel(self.groupBox)
        self.photon_beam_field.setObjectName(u"photon_beam_field")

        self.beam_energies_fl.setWidget(0, QFormLayout.FieldRole, self.photon_beam_field)

        self.electron_beam_label = QLabel(self.groupBox)
        self.electron_beam_label.setObjectName(u"electron_beam_label")

        self.beam_energies_fl.setWidget(1, QFormLayout.LabelRole, self.electron_beam_label)

        self.electron_beam_field = QLabel(self.groupBox)
        self.electron_beam_field.setObjectName(u"electron_beam_field")

        self.beam_energies_fl.setWidget(1, QFormLayout.FieldRole, self.electron_beam_field)


        self.verticalLayout_7.addLayout(self.beam_energies_fl)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.edit_linac_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.edit_linac_btn.setObjectName(u"edit_linac_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.edit_linac_btn.sizePolicy().hasHeightForWidth())
        self.edit_linac_btn.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.edit_linac_btn, 0, Qt.AlignTop)

        self.delete_linac_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.delete_linac_btn.setObjectName(u"delete_linac_btn")
        sizePolicy4.setHeightForWidth(self.delete_linac_btn.sizePolicy().hasHeightForWidth())
        self.delete_linac_btn.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.delete_linac_btn)

        self.add_linac_btn = QPushButton(self.scrollAreaWidgetContents_2)
        self.add_linac_btn.setObjectName(u"add_linac_btn")
        sizePolicy4.setHeightForWidth(self.add_linac_btn.sizePolicy().hasHeightForWidth())
        self.add_linac_btn.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.add_linac_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 1, 1, 1)

        self.linac_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.linac_scroll_area)

        self.tabWidget.addTab(self.linac_tab, "")
        self.chambers_tab = QWidget()
        self.chambers_tab.setObjectName(u"chambers_tab")
        self.tabWidget.addTab(self.chambers_tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.devices_page)
        self.reporting_page = QWidget()
        self.reporting_page.setObjectName(u"reporting_page")
        self.stackedWidget.addWidget(self.reporting_page)
        self.analysis_config_page = QWidget()
        self.analysis_config_page.setObjectName(u"analysis_config_page")
        self.stackedWidget.addWidget(self.analysis_config_page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)

        self.dialog_buttons = QDialogButtonBox(self.centralwidget)
        self.dialog_buttons.setObjectName(u"dialog_buttons")
        self.dialog_buttons.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.dialog_buttons, 2, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.general_btn.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.devices_btn.setText(QCoreApplication.translate("MainWindow", u"Devices", None))
        self.reporting_btn.setText(QCoreApplication.translate("MainWindow", u"Reporting", None))
        self.analysis_config_btn.setText(QCoreApplication.translate("MainWindow", u"Analysis Config.", None))
        self.page_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Page Title</span></p></body></html>", None))
        self.linac_label.setText(QCoreApplication.translate("MainWindow", u"Linac:", None))
        self.lina_info_group_box.setTitle(QCoreApplication.translate("MainWindow", u"General Info", None))
        self.linac_name_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.linac_name_field.setText("")
        self.linac_model_label.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.linac_model_field.setText("")
        self.serial_num_label.setText(QCoreApplication.translate("MainWindow", u"Serial No:", None))
        self.serial_num_field.setText("")
        self.linac_state_label.setText(QCoreApplication.translate("MainWindow", u"State:", None))
        self.linac_state_field.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Beam Energies", None))
        self.photon_beam_label.setText(QCoreApplication.translate("MainWindow", u"Photon beams (MV):", None))
        self.photon_beam_field.setText("")
        self.electron_beam_label.setText(QCoreApplication.translate("MainWindow", u"Electron beams (MeV):", None))
        self.electron_beam_field.setText("")
        self.edit_linac_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_linac_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.add_linac_btn.setText(QCoreApplication.translate("MainWindow", u"Add...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.linac_tab), QCoreApplication.translate("MainWindow", u"Linear Accelerators", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chambers_tab), QCoreApplication.translate("MainWindow", u"Ionization Chambers", None))
    # retranslateUi

