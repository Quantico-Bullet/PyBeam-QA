# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")
        PreferencesDialog.resize(860, 540)
        self.gridLayout = QGridLayout(PreferencesDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.page_title_label = QLabel(PreferencesDialog)
        self.page_title_label.setObjectName(u"page_title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_title_label.sizePolicy().hasHeightForWidth())
        self.page_title_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.page_title_label.setFont(font)

        self.gridLayout.addWidget(self.page_title_label, 0, 2, 1, 1, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(PreferencesDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMaximumSize(QSize(250, 16777215))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 250, 461))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nav_top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.nav_top_spacer)

        self.general_btn = QPushButton(self.scrollAreaWidgetContents)
        self.nav_button_group = QButtonGroup(PreferencesDialog)
        self.nav_button_group.setObjectName(u"nav_button_group")
        self.nav_button_group.addButton(self.general_btn)
        self.general_btn.setObjectName(u"general_btn")
        self.general_btn.setCheckable(True)
        self.general_btn.setChecked(True)

        self.verticalLayout.addWidget(self.general_btn)

        self.devices_btn = QPushButton(self.scrollAreaWidgetContents)
        self.nav_button_group.addButton(self.devices_btn)
        self.devices_btn.setObjectName(u"devices_btn")
        self.devices_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.devices_btn)

        self.reporting_btn = QPushButton(self.scrollAreaWidgetContents)
        self.nav_button_group.addButton(self.reporting_btn)
        self.reporting_btn.setObjectName(u"reporting_btn")
        self.reporting_btn.setEnabled(False)
        self.reporting_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.reporting_btn)

        self.analysis_tools_btn = QPushButton(self.scrollAreaWidgetContents)
        self.nav_button_group.addButton(self.analysis_tools_btn)
        self.analysis_tools_btn.setObjectName(u"analysis_tools_btn")
        self.analysis_tools_btn.setEnabled(False)
        self.analysis_tools_btn.setCheckable(True)

        self.verticalLayout.addWidget(self.analysis_tools_btn)

        self.nav_bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.nav_bottom_spacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.nav_line_separator = QFrame(PreferencesDialog)
        self.nav_line_separator.setObjectName(u"nav_line_separator")
        self.nav_line_separator.setMaximumSize(QSize(1, 16777215))
        self.nav_line_separator.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.nav_line_separator.setFrameShape(QFrame.VLine)
        self.nav_line_separator.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.nav_line_separator, 1, 1, 1, 1)

        self.nav_stacked_widget = QStackedWidget(PreferencesDialog)
        self.nav_stacked_widget.setObjectName(u"nav_stacked_widget")
        self.general_page = QWidget()
        self.general_page.setObjectName(u"general_page")
        self.verticalLayout_3 = QVBoxLayout(self.general_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.general_tab_widget = QTabWidget(self.general_page)
        self.general_tab_widget.setObjectName(u"general_tab_widget")
        self.workspace_tab = QWidget()
        self.workspace_tab.setObjectName(u"workspace_tab")
        self.verticalLayout_9 = QVBoxLayout(self.workspace_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.workspace_scroll_area = QScrollArea(self.workspace_tab)
        self.workspace_scroll_area.setObjectName(u"workspace_scroll_area")
        self.workspace_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 129, 49))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.config_group_box = QGroupBox(self.scrollAreaWidgetContents_4)
        self.config_group_box.setObjectName(u"config_group_box")
        self.horizontalLayoutWidget_2 = QWidget(self.config_group_box)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 30, 501, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.workspace_loc_label = QLabel(self.horizontalLayoutWidget_2)
        self.workspace_loc_label.setObjectName(u"workspace_loc_label")

        self.horizontalLayout_5.addWidget(self.workspace_loc_label)

        self.workspace_loc_le = QLineEdit(self.horizontalLayoutWidget_2)
        self.workspace_loc_le.setObjectName(u"workspace_loc_le")
        self.workspace_loc_le.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.workspace_loc_le)

        self.workspace_browse_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.workspace_browse_btn.setObjectName(u"workspace_browse_btn")

        self.horizontalLayout_5.addWidget(self.workspace_browse_btn)


        self.gridLayout_4.addWidget(self.config_group_box, 0, 0, 1, 1)

        self.workspace_scroll_area.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_9.addWidget(self.workspace_scroll_area)

        self.general_tab_widget.addTab(self.workspace_tab, "")

        self.verticalLayout_3.addWidget(self.general_tab_widget)

        self.nav_stacked_widget.addWidget(self.general_page)
        self.devices_page = QWidget()
        self.devices_page.setObjectName(u"devices_page")
        self.verticalLayout_2 = QVBoxLayout(self.devices_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.devices_tab_widget = QTabWidget(self.devices_page)
        self.devices_tab_widget.setObjectName(u"devices_tab_widget")
        self.linac_tab = QWidget()
        self.linac_tab.setObjectName(u"linac_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.linac_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.linac_scroll_area = QScrollArea(self.linac_tab)
        self.linac_scroll_area.setObjectName(u"linac_scroll_area")
        self.linac_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 449, 395))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.linac_label = QLabel(self.scrollAreaWidgetContents_2)
        self.linac_label.setObjectName(u"linac_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.linac_label.sizePolicy().hasHeightForWidth())
        self.linac_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.linac_label)

        self.linac_comboB = QComboBox(self.scrollAreaWidgetContents_2)
        self.linac_comboB.setObjectName(u"linac_comboB")

        self.horizontalLayout.addWidget(self.linac_comboB)


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

        self.linac_serial_num_label = QLabel(self.lina_info_group_box)
        self.linac_serial_num_label.setObjectName(u"linac_serial_num_label")

        self.linac_info_fl.setWidget(2, QFormLayout.LabelRole, self.linac_serial_num_label)

        self.linac_serial_num_field = QLabel(self.lina_info_group_box)
        self.linac_serial_num_field.setObjectName(u"linac_serial_num_field")

        self.linac_info_fl.setWidget(2, QFormLayout.FieldRole, self.linac_serial_num_field)

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

        self.beam_energies_fl.setWidget(2, QFormLayout.LabelRole, self.electron_beam_label)

        self.electron_beam_field = QLabel(self.groupBox)
        self.electron_beam_field.setObjectName(u"electron_beam_field")

        self.beam_energies_fl.setWidget(2, QFormLayout.FieldRole, self.electron_beam_field)

        self.photon_fff_beam_label = QLabel(self.groupBox)
        self.photon_fff_beam_label.setObjectName(u"photon_fff_beam_label")

        self.beam_energies_fl.setWidget(1, QFormLayout.LabelRole, self.photon_fff_beam_label)

        self.photon_fff_beam_field = QLabel(self.groupBox)
        self.photon_fff_beam_field.setObjectName(u"photon_fff_beam_field")

        self.beam_energies_fl.setWidget(1, QFormLayout.FieldRole, self.photon_fff_beam_field)


        self.verticalLayout_7.addLayout(self.beam_energies_fl)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.linac_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_4.addWidget(self.linac_scroll_area)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 9, -1, 9)
        self.edit_linac_btn = QPushButton(self.linac_tab)
        self.edit_linac_btn.setObjectName(u"edit_linac_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.edit_linac_btn.sizePolicy().hasHeightForWidth())
        self.edit_linac_btn.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.edit_linac_btn, 0, Qt.AlignTop)

        self.add_linac_btn = QPushButton(self.linac_tab)
        self.add_linac_btn.setObjectName(u"add_linac_btn")
        sizePolicy4.setHeightForWidth(self.add_linac_btn.sizePolicy().hasHeightForWidth())
        self.add_linac_btn.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.add_linac_btn)

        self.delete_linac_btn = QPushButton(self.linac_tab)
        self.delete_linac_btn.setObjectName(u"delete_linac_btn")
        sizePolicy4.setHeightForWidth(self.delete_linac_btn.sizePolicy().hasHeightForWidth())
        self.delete_linac_btn.setSizePolicy(sizePolicy4)

        self.verticalLayout_6.addWidget(self.delete_linac_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.devices_tab_widget.addTab(self.linac_tab, "")
        self.chambers_tab = QWidget()
        self.chambers_tab.setObjectName(u"chambers_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.chambers_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.chambers_scroll_area = QScrollArea(self.chambers_tab)
        self.chambers_scroll_area.setObjectName(u"chambers_scroll_area")
        self.chambers_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 449, 395))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ion_chamber_label = QLabel(self.scrollAreaWidgetContents_3)
        self.ion_chamber_label.setObjectName(u"ion_chamber_label")
        sizePolicy2.setHeightForWidth(self.ion_chamber_label.sizePolicy().hasHeightForWidth())
        self.ion_chamber_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.ion_chamber_label)

        self.ion_chamber_comboB = QComboBox(self.scrollAreaWidgetContents_3)
        self.ion_chamber_comboB.setObjectName(u"ion_chamber_comboB")

        self.horizontalLayout_2.addWidget(self.ion_chamber_comboB)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.chamber_info_fl = QFormLayout()
        self.chamber_info_fl.setObjectName(u"chamber_info_fl")
        self.chamber_name_label = QLabel(self.groupBox_2)
        self.chamber_name_label.setObjectName(u"chamber_name_label")

        self.chamber_info_fl.setWidget(0, QFormLayout.LabelRole, self.chamber_name_label)

        self.chamber_name_field = QLabel(self.groupBox_2)
        self.chamber_name_field.setObjectName(u"chamber_name_field")

        self.chamber_info_fl.setWidget(0, QFormLayout.FieldRole, self.chamber_name_field)

        self.chamber_model_label = QLabel(self.groupBox_2)
        self.chamber_model_label.setObjectName(u"chamber_model_label")

        self.chamber_info_fl.setWidget(1, QFormLayout.LabelRole, self.chamber_model_label)

        self.chamber_model_field = QLabel(self.groupBox_2)
        self.chamber_model_field.setObjectName(u"chamber_model_field")

        self.chamber_info_fl.setWidget(1, QFormLayout.FieldRole, self.chamber_model_field)

        self.chamber_serial_num_label = QLabel(self.groupBox_2)
        self.chamber_serial_num_label.setObjectName(u"chamber_serial_num_label")

        self.chamber_info_fl.setWidget(2, QFormLayout.LabelRole, self.chamber_serial_num_label)

        self.chamber_serial_num_field = QLabel(self.groupBox_2)
        self.chamber_serial_num_field.setObjectName(u"chamber_serial_num_field")

        self.chamber_info_fl.setWidget(2, QFormLayout.FieldRole, self.chamber_serial_num_field)

        self.chamber_type_label = QLabel(self.groupBox_2)
        self.chamber_type_label.setObjectName(u"chamber_type_label")

        self.chamber_info_fl.setWidget(3, QFormLayout.LabelRole, self.chamber_type_label)

        self.chamber_type_field = QLabel(self.groupBox_2)
        self.chamber_type_field.setObjectName(u"chamber_type_field")

        self.chamber_info_fl.setWidget(3, QFormLayout.FieldRole, self.chamber_type_field)


        self.verticalLayout_11.addLayout(self.chamber_info_fl)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.chamber_cal_info_fl = QFormLayout()
        self.chamber_cal_info_fl.setObjectName(u"chamber_cal_info_fl")
        self.chamber_cal_lab_label = QLabel(self.groupBox_3)
        self.chamber_cal_lab_label.setObjectName(u"chamber_cal_lab_label")

        self.chamber_cal_info_fl.setWidget(0, QFormLayout.LabelRole, self.chamber_cal_lab_label)

        self.chamber_cal_lab_field = QLabel(self.groupBox_3)
        self.chamber_cal_lab_field.setObjectName(u"chamber_cal_lab_field")

        self.chamber_cal_info_fl.setWidget(0, QFormLayout.FieldRole, self.chamber_cal_lab_field)

        self.chamber_cal_date_label = QLabel(self.groupBox_3)
        self.chamber_cal_date_label.setObjectName(u"chamber_cal_date_label")

        self.chamber_cal_info_fl.setWidget(1, QFormLayout.LabelRole, self.chamber_cal_date_label)

        self.chamber_cal_date_field = QLabel(self.groupBox_3)
        self.chamber_cal_date_field.setObjectName(u"chamber_cal_date_field")

        self.chamber_cal_info_fl.setWidget(1, QFormLayout.FieldRole, self.chamber_cal_date_field)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.chamber_cal_info_fl.setWidget(2, QFormLayout.LabelRole, self.label)


        self.verticalLayout_12.addLayout(self.chamber_cal_info_fl)


        self.verticalLayout_10.addWidget(self.groupBox_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.gridLayout_3.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.chambers_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_3.addWidget(self.chambers_scroll_area)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 9, -1, 9)
        self.pushButton_3 = QPushButton(self.chambers_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_8.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.chambers_tab)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.chambers_tab)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_8.addWidget(self.pushButton_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.devices_tab_widget.addTab(self.chambers_tab, "")

        self.verticalLayout_2.addWidget(self.devices_tab_widget)

        self.nav_stacked_widget.addWidget(self.devices_page)
        self.reporting_page = QWidget()
        self.reporting_page.setObjectName(u"reporting_page")
        self.nav_stacked_widget.addWidget(self.reporting_page)
        self.analysis_tools_page = QWidget()
        self.analysis_tools_page.setObjectName(u"analysis_tools_page")
        self.nav_stacked_widget.addWidget(self.analysis_tools_page)

        self.gridLayout.addWidget(self.nav_stacked_widget, 1, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 3)


        self.retranslateUi(PreferencesDialog)
        self.buttonBox.accepted.connect(PreferencesDialog.accept)
        self.buttonBox.rejected.connect(PreferencesDialog.reject)

        self.nav_stacked_widget.setCurrentIndex(1)
        self.general_tab_widget.setCurrentIndex(0)
        self.devices_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PreferencesDialog)
    # setupUi

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QCoreApplication.translate("PreferencesDialog", u"Dialog", None))
        self.page_title_label.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Page Title</span></p></body></html>", None))
        self.general_btn.setText(QCoreApplication.translate("PreferencesDialog", u"General", None))
        self.devices_btn.setText(QCoreApplication.translate("PreferencesDialog", u"Devices", None))
        self.reporting_btn.setText(QCoreApplication.translate("PreferencesDialog", u"Reporting", None))
        self.analysis_tools_btn.setText(QCoreApplication.translate("PreferencesDialog", u"Analysis Tools", None))
        self.config_group_box.setTitle(QCoreApplication.translate("PreferencesDialog", u"Configuration", None))
        self.workspace_loc_label.setText(QCoreApplication.translate("PreferencesDialog", u"Workspace location:", None))
        self.workspace_browse_btn.setText(QCoreApplication.translate("PreferencesDialog", u"Browse...", None))
        self.general_tab_widget.setTabText(self.general_tab_widget.indexOf(self.workspace_tab), QCoreApplication.translate("PreferencesDialog", u"Workspace", None))
        self.linac_label.setText(QCoreApplication.translate("PreferencesDialog", u"Linac:", None))
        self.lina_info_group_box.setTitle(QCoreApplication.translate("PreferencesDialog", u"General Info", None))
        self.linac_name_label.setText(QCoreApplication.translate("PreferencesDialog", u"Name:", None))
        self.linac_name_field.setText("")
        self.linac_model_label.setText(QCoreApplication.translate("PreferencesDialog", u"Model:", None))
        self.linac_model_field.setText("")
        self.linac_serial_num_label.setText(QCoreApplication.translate("PreferencesDialog", u"Serial No:", None))
        self.linac_serial_num_field.setText("")
        self.linac_state_label.setText(QCoreApplication.translate("PreferencesDialog", u"State:", None))
        self.linac_state_field.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("PreferencesDialog", u"Beam Energies", None))
        self.photon_beam_label.setText(QCoreApplication.translate("PreferencesDialog", u"Photon beams (MV):", None))
        self.photon_beam_field.setText("")
        self.electron_beam_label.setText(QCoreApplication.translate("PreferencesDialog", u"Electron beams (MeV):", None))
        self.electron_beam_field.setText("")
        self.photon_fff_beam_label.setText(QCoreApplication.translate("PreferencesDialog", u"Photon FFF beams (MV):", None))
        self.photon_fff_beam_field.setText("")
        self.edit_linac_btn.setText(QCoreApplication.translate("PreferencesDialog", u"Edit", None))
        self.add_linac_btn.setText(QCoreApplication.translate("PreferencesDialog", u"Add...", None))
        self.delete_linac_btn.setText(QCoreApplication.translate("PreferencesDialog", u"Delete", None))
        self.devices_tab_widget.setTabText(self.devices_tab_widget.indexOf(self.linac_tab), QCoreApplication.translate("PreferencesDialog", u"Linear Accelerators", None))
        self.ion_chamber_label.setText(QCoreApplication.translate("PreferencesDialog", u"Ion. Chamber:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PreferencesDialog", u"General Info", None))
        self.chamber_name_label.setText(QCoreApplication.translate("PreferencesDialog", u"Name:", None))
        self.chamber_name_field.setText("")
        self.chamber_model_label.setText(QCoreApplication.translate("PreferencesDialog", u"Model:", None))
        self.chamber_model_field.setText("")
        self.chamber_serial_num_label.setText(QCoreApplication.translate("PreferencesDialog", u"Serial No:", None))
        self.chamber_serial_num_field.setText("")
        self.chamber_type_label.setText(QCoreApplication.translate("PreferencesDialog", u"Type:", None))
        self.chamber_type_field.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("PreferencesDialog", u"Calibration Info", None))
        self.chamber_cal_lab_label.setText(QCoreApplication.translate("PreferencesDialog", u"Calibration laboratory:", None))
        self.chamber_cal_lab_field.setText("")
        self.chamber_cal_date_label.setText(QCoreApplication.translate("PreferencesDialog", u"Calibration date:", None))
        self.chamber_cal_date_field.setText("")
        self.label.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>Calibration coefficient (<span style=\" font-style:italic;\">N</span><span style=\" font-size:11pt; font-style:italic; vertical-align:sub;\">D,w</span>):</p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("PreferencesDialog", u"Edit", None))
        self.pushButton.setText(QCoreApplication.translate("PreferencesDialog", u"Add...", None))
        self.pushButton_2.setText(QCoreApplication.translate("PreferencesDialog", u"Delete", None))
        self.devices_tab_widget.setTabText(self.devices_tab_widget.indexOf(self.chambers_tab), QCoreApplication.translate("PreferencesDialog", u"Ionization Chambers", None))
    # retranslateUi

