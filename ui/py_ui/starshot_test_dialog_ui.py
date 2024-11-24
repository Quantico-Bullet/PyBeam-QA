# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'starshot_test_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_StarshotTestDialog(object):
    def setupUi(self, StarshotTestDialog):
        if not StarshotTestDialog.objectName():
            StarshotTestDialog.setObjectName(u"StarshotTestDialog")
        StarshotTestDialog.resize(522, 241)
        self.gridLayout = QGridLayout(StarshotTestDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttons_spacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.buttons_spacer, 1, 0, 1, 1)

        self.button_box = QDialogButtonBox(StarshotTestDialog)
        self.button_box.setObjectName(u"button_box")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setStyleSheet(u"")
        self.button_box.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)

        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(StarshotTestDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 504, 177))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(15)
        self.test_name_label = QLabel(self.frame)
        self.test_name_label.setObjectName(u"test_name_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.test_name_label)

        self.test_name_le = QLineEdit(self.frame)
        self.test_name_le.setObjectName(u"test_name_le")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.test_name_le.sizePolicy().hasHeightForWidth())
        self.test_name_le.setSizePolicy(sizePolicy3)
        self.test_name_le.setMaximumSize(QSize(350, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.test_name_le)

        self.output_file_label = QLabel(self.frame)
        self.output_file_label.setObjectName(u"output_file_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.output_file_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.out_file_le = QLineEdit(self.frame)
        self.out_file_le.setObjectName(u"out_file_le")
        sizePolicy3.setHeightForWidth(self.out_file_le.sizePolicy().hasHeightForWidth())
        self.out_file_le.setSizePolicy(sizePolicy3)
        self.out_file_le.setMinimumSize(QSize(245, 0))
        self.out_file_le.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.out_file_le)

        self.select_file_btn = QPushButton(self.frame)
        self.select_file_btn.setObjectName(u"select_file_btn")

        self.horizontalLayout_2.addWidget(self.select_file_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.sim_image_label = QLabel(self.frame)
        self.sim_image_label.setObjectName(u"sim_image_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sim_image_label)

        self.sim_image_cb = QComboBox(self.frame)
        self.sim_image_cb.setObjectName(u"sim_image_cb")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sim_image_cb.sizePolicy().hasHeightForWidth())
        self.sim_image_cb.setSizePolicy(sizePolicy4)
        self.sim_image_cb.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sim_image_cb)

        self.num_spokes_label = QLabel(self.frame)
        self.num_spokes_label.setObjectName(u"num_spokes_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.num_spokes_label)

        self.num_spokes_sb = QSpinBox(self.frame)
        self.num_spokes_sb.setObjectName(u"num_spokes_sb")
        self.num_spokes_sb.setMaximumSize(QSize(100, 16777215))
        self.num_spokes_sb.setMinimum(5)
        self.num_spokes_sb.setMaximum(12)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.num_spokes_sb)

        self.cax_offset_label = QLabel(self.frame)
        self.cax_offset_label.setObjectName(u"cax_offset_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.cax_offset_label)

        self.cax_offset_dsb = QDoubleSpinBox(self.frame)
        self.cax_offset_dsb.setObjectName(u"cax_offset_dsb")
        sizePolicy4.setHeightForWidth(self.cax_offset_dsb.sizePolicy().hasHeightForWidth())
        self.cax_offset_dsb.setSizePolicy(sizePolicy4)
        self.cax_offset_dsb.setMinimumSize(QSize(100, 0))
        self.cax_offset_dsb.setDecimals(1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cax_offset_dsb)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_3.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(StarshotTestDialog)
        self.button_box.accepted.connect(StarshotTestDialog.accept)
        self.button_box.rejected.connect(StarshotTestDialog.reject)

        QMetaObject.connectSlotsByName(StarshotTestDialog)
    # setupUi

    def retranslateUi(self, StarshotTestDialog):
        self.test_name_label.setText(QCoreApplication.translate("StarshotTestDialog", u"Test name:", None))
        self.output_file_label.setText(QCoreApplication.translate("StarshotTestDialog", u"Output file:", None))
        self.select_file_btn.setText(QCoreApplication.translate("StarshotTestDialog", u"Save to...", None))
        self.sim_image_label.setText(QCoreApplication.translate("StarshotTestDialog", u"Simulation image:", None))
        self.num_spokes_label.setText(QCoreApplication.translate("StarshotTestDialog", u"Number of spokes:", None))
        self.cax_offset_label.setText(QCoreApplication.translate("StarshotTestDialog", u"CAX offset", None))
        self.cax_offset_dsb.setSuffix(QCoreApplication.translate("StarshotTestDialog", u" mm", None))
        pass
    # retranslateUi

