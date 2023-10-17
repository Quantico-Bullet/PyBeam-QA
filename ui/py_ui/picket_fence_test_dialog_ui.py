# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'picket_fence_test_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_PFTestDialog(object):
    def setupUi(self, PFTestDialog):
        if not PFTestDialog.objectName():
            PFTestDialog.setObjectName(u"PFTestDialog")
        PFTestDialog.resize(600, 455)
        self.gridLayout = QGridLayout(PFTestDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(PFTestDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 582, 391))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.test_name_le.sizePolicy().hasHeightForWidth())
        self.test_name_le.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.out_file_le.sizePolicy().hasHeightForWidth())
        self.out_file_le.setSizePolicy(sizePolicy2)
        self.out_file_le.setMinimumSize(QSize(245, 0))
        self.out_file_le.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.out_file_le)

        self.select_file_btn = QPushButton(self.frame)
        self.select_file_btn.setObjectName(u"select_file_btn")

        self.horizontalLayout_2.addWidget(self.select_file_btn)

        self.horizontalSpacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.sim_image_label = QLabel(self.frame)
        self.sim_image_label.setObjectName(u"sim_image_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sim_image_label)

        self.sim_image_cb = QComboBox(self.frame)
        self.sim_image_cb.setObjectName(u"sim_image_cb")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sim_image_cb.sizePolicy().hasHeightForWidth())
        self.sim_image_cb.setSizePolicy(sizePolicy3)
        self.sim_image_cb.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sim_image_cb)

        self.image_orientation_label = QLabel(self.frame)
        self.image_orientation_label.setObjectName(u"image_orientation_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.image_orientation_label)

        self.image_orientation_cb = QComboBox(self.frame)
        self.image_orientation_cb.setObjectName(u"image_orientation_cb")
        sizePolicy2.setHeightForWidth(self.image_orientation_cb.sizePolicy().hasHeightForWidth())
        self.image_orientation_cb.setSizePolicy(sizePolicy2)
        self.image_orientation_cb.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.image_orientation_cb)

        self.image_rotation_label = QLabel(self.frame)
        self.image_rotation_label.setObjectName(u"image_rotation_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.image_rotation_label)

        self.image_rotation_dsb = QDoubleSpinBox(self.frame)
        self.image_rotation_dsb.setObjectName(u"image_rotation_dsb")
        sizePolicy2.setHeightForWidth(self.image_rotation_dsb.sizePolicy().hasHeightForWidth())
        self.image_rotation_dsb.setSizePolicy(sizePolicy2)
        self.image_rotation_dsb.setMinimumSize(QSize(100, 0))
        self.image_rotation_dsb.setDecimals(2)
        self.image_rotation_dsb.setMinimum(-5.000000000000000)
        self.image_rotation_dsb.setMaximum(5.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.image_rotation_dsb)

        self.sid_label = QLabel(self.frame)
        self.sid_label.setObjectName(u"sid_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.sid_label)

        self.sid_sb = QDoubleSpinBox(self.frame)
        self.sid_sb.setObjectName(u"sid_sb")
        self.sid_sb.setMaximumSize(QSize(100, 16777215))
        self.sid_sb.setDecimals(0)
        self.sid_sb.setMinimum(500.000000000000000)
        self.sid_sb.setMaximum(2500.000000000000000)
        self.sid_sb.setValue(1000.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.sid_sb)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.line_3)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.line_2)

        self.image_axes_label = QLabel(self.frame)
        self.image_axes_label.setObjectName(u"image_axes_label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.image_axes_label)

        self.num_pickets_sb = QSpinBox(self.frame)
        self.num_pickets_sb.setObjectName(u"num_pickets_sb")
        sizePolicy2.setHeightForWidth(self.num_pickets_sb.sizePolicy().hasHeightForWidth())
        self.num_pickets_sb.setSizePolicy(sizePolicy2)
        self.num_pickets_sb.setMinimumSize(QSize(100, 0))
        self.num_pickets_sb.setMinimum(4)
        self.num_pickets_sb.setMaximum(10)
        self.num_pickets_sb.setValue(6)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.num_pickets_sb)

        self.picket_spacing_label = QLabel(self.frame)
        self.picket_spacing_label.setObjectName(u"picket_spacing_label")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.picket_spacing_label)

        self.picket_spacing_sb = QSpinBox(self.frame)
        self.picket_spacing_sb.setObjectName(u"picket_spacing_sb")
        sizePolicy2.setHeightForWidth(self.picket_spacing_sb.sizePolicy().hasHeightForWidth())
        self.picket_spacing_sb.setSizePolicy(sizePolicy2)
        self.picket_spacing_sb.setMinimumSize(QSize(100, 0))
        self.picket_spacing_sb.setMinimum(10)
        self.picket_spacing_sb.setMaximum(30)
        self.picket_spacing_sb.setValue(20)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.picket_spacing_sb)

        self.picket_width_label = QLabel(self.frame)
        self.picket_width_label.setObjectName(u"picket_width_label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.picket_width_label)

        self.picket_width_sb = QSpinBox(self.frame)
        self.picket_width_sb.setObjectName(u"picket_width_sb")
        sizePolicy2.setHeightForWidth(self.picket_width_sb.sizePolicy().hasHeightForWidth())
        self.picket_width_sb.setSizePolicy(sizePolicy2)
        self.picket_width_sb.setMinimumSize(QSize(100, 0))
        self.picket_width_sb.setMinimum(1)
        self.picket_width_sb.setMaximum(20)
        self.picket_width_sb.setValue(5)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.picket_width_sb)

        self.picket_offsets_label = QLabel(self.frame)
        self.picket_offsets_label.setObjectName(u"picket_offsets_label")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.picket_offsets_label)

        self.picket_offsets_le = QLineEdit(self.frame)
        self.picket_offsets_le.setObjectName(u"picket_offsets_le")
        self.picket_offsets_le.setMaximumSize(QSize(350, 16777215))

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.picket_offsets_le)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.line_4)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.line)

        self.set_leaf_offsets_btn = QPushButton(self.frame)
        self.set_leaf_offsets_btn.setObjectName(u"set_leaf_offsets_btn")
        self.set_leaf_offsets_btn.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.set_leaf_offsets_btn.sizePolicy().hasHeightForWidth())
        self.set_leaf_offsets_btn.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.set_leaf_offsets_btn)

        self.leaf_pair_offsets_label = QLabel(self.frame)
        self.leaf_pair_offsets_label.setObjectName(u"leaf_pair_offsets_label")
        self.leaf_pair_offsets_label.setEnabled(False)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.leaf_pair_offsets_label)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_3.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.buttons_spacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.buttons_spacer, 1, 0, 1, 1)

        self.button_box = QDialogButtonBox(PFTestDialog)
        self.button_box.setObjectName(u"button_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy4)
        self.button_box.setStyleSheet(u"")
        self.button_box.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)

        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 1)


        self.retranslateUi(PFTestDialog)
        self.button_box.accepted.connect(PFTestDialog.accept)
        self.button_box.rejected.connect(PFTestDialog.reject)

        QMetaObject.connectSlotsByName(PFTestDialog)
    # setupUi

    def retranslateUi(self, PFTestDialog):
        self.test_name_label.setText(QCoreApplication.translate("PFTestDialog", u"Test name:", None))
        self.output_file_label.setText(QCoreApplication.translate("PFTestDialog", u"Output file:", None))
        self.select_file_btn.setText(QCoreApplication.translate("PFTestDialog", u"Save to...", None))
        self.sim_image_label.setText(QCoreApplication.translate("PFTestDialog", u"Simulation image:", None))
        self.image_orientation_label.setText(QCoreApplication.translate("PFTestDialog", u"Image orientation:", None))
        self.image_rotation_label.setText(QCoreApplication.translate("PFTestDialog", u"Image rotation:", None))
        self.image_rotation_dsb.setSuffix(QCoreApplication.translate("PFTestDialog", u"\u00b0", None))
        self.sid_label.setText(QCoreApplication.translate("PFTestDialog", u"SID:", None))
        self.sid_sb.setSuffix(QCoreApplication.translate("PFTestDialog", u" mm", None))
        self.image_axes_label.setText(QCoreApplication.translate("PFTestDialog", u"Number of pickets:", None))
        self.picket_spacing_label.setText(QCoreApplication.translate("PFTestDialog", u"Picket spacing:", None))
        self.picket_spacing_sb.setSuffix(QCoreApplication.translate("PFTestDialog", u" mm", None))
        self.picket_width_label.setText(QCoreApplication.translate("PFTestDialog", u"Picket width:", None))
        self.picket_width_sb.setSuffix(QCoreApplication.translate("PFTestDialog", u" mm", None))
        self.picket_offsets_label.setText(QCoreApplication.translate("PFTestDialog", u"Picket offset errors:", None))
        self.picket_offsets_le.setText("")
        self.picket_offsets_le.setPlaceholderText(QCoreApplication.translate("PFTestDialog", u"Format: 1.00; 2.00; 3.00; ...", None))
        self.set_leaf_offsets_btn.setText(QCoreApplication.translate("PFTestDialog", u"Set values", None))
        self.leaf_pair_offsets_label.setText(QCoreApplication.translate("PFTestDialog", u"Leaf pair offsets:", None))
        pass
    # retranslateUi

