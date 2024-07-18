# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'winston_lutz_test_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_WLTestDialog(object):
    def setupUi(self, WLTestDialog):
        if not WLTestDialog.objectName():
            WLTestDialog.setObjectName(u"WLTestDialog")
        WLTestDialog.resize(600, 600)
        self.gridLayout = QGridLayout(WLTestDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(WLTestDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 568, 605))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.test_name_le.sizePolicy().hasHeightForWidth())
        self.test_name_le.setSizePolicy(sizePolicy2)
        self.test_name_le.setMaximumSize(QSize(350, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.test_name_le)

        self.sim_image_label = QLabel(self.frame)
        self.sim_image_label.setObjectName(u"sim_image_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.sim_image_label)

        self.sim_image_cb = QComboBox(self.frame)
        self.sim_image_cb.setObjectName(u"sim_image_cb")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sim_image_cb.sizePolicy().hasHeightForWidth())
        self.sim_image_cb.setSizePolicy(sizePolicy3)
        self.sim_image_cb.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sim_image_cb)

        self.field_type_label = QLabel(self.frame)
        self.field_type_label.setObjectName(u"field_type_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.field_type_label)

        self.field_type_cb = QComboBox(self.frame)
        self.field_type_cb.setObjectName(u"field_type_cb")
        sizePolicy3.setHeightForWidth(self.field_type_cb.sizePolicy().hasHeightForWidth())
        self.field_type_cb.setSizePolicy(sizePolicy3)
        self.field_type_cb.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.field_type_cb)

        self.field_size_label = QLabel(self.frame)
        self.field_size_label.setObjectName(u"field_size_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.field_size_label)

        self.field_size_config = QVBoxLayout()
        self.field_size_config.setSpacing(6)
        self.field_size_config.setObjectName(u"field_size_config")
        self.field_size_config.setSizeConstraint(QLayout.SetFixedSize)
        self.cone_field_size_dsb = QDoubleSpinBox(self.frame)
        self.cone_field_size_dsb.setObjectName(u"cone_field_size_dsb")
        sizePolicy2.setHeightForWidth(self.cone_field_size_dsb.sizePolicy().hasHeightForWidth())
        self.cone_field_size_dsb.setSizePolicy(sizePolicy2)
        self.cone_field_size_dsb.setMinimumSize(QSize(100, 0))
        self.cone_field_size_dsb.setDecimals(0)
        self.cone_field_size_dsb.setMinimum(10.000000000000000)
        self.cone_field_size_dsb.setMaximum(200.000000000000000)

        self.field_size_config.addWidget(self.cone_field_size_dsb)

        self.rec_field_width_label = QLabel(self.frame)
        self.rec_field_width_label.setObjectName(u"rec_field_width_label")

        self.field_size_config.addWidget(self.rec_field_width_label)

        self.rec_field_width_dsb = QDoubleSpinBox(self.frame)
        self.rec_field_width_dsb.setObjectName(u"rec_field_width_dsb")
        sizePolicy2.setHeightForWidth(self.rec_field_width_dsb.sizePolicy().hasHeightForWidth())
        self.rec_field_width_dsb.setSizePolicy(sizePolicy2)
        self.rec_field_width_dsb.setMinimumSize(QSize(100, 0))
        self.rec_field_width_dsb.setDecimals(0)
        self.rec_field_width_dsb.setMinimum(10.000000000000000)
        self.rec_field_width_dsb.setMaximum(400.000000000000000)

        self.field_size_config.addWidget(self.rec_field_width_dsb)

        self.rec_field_height_label = QLabel(self.frame)
        self.rec_field_height_label.setObjectName(u"rec_field_height_label")

        self.field_size_config.addWidget(self.rec_field_height_label)

        self.rec_field_height_dsb = QDoubleSpinBox(self.frame)
        self.rec_field_height_dsb.setObjectName(u"rec_field_height_dsb")
        sizePolicy2.setHeightForWidth(self.rec_field_height_dsb.sizePolicy().hasHeightForWidth())
        self.rec_field_height_dsb.setSizePolicy(sizePolicy2)
        self.rec_field_height_dsb.setMinimumSize(QSize(100, 0))
        self.rec_field_height_dsb.setDecimals(0)
        self.rec_field_height_dsb.setMinimum(10.000000000000000)
        self.rec_field_height_dsb.setMaximum(400.000000000000000)

        self.field_size_config.addWidget(self.rec_field_height_dsb)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.field_size_config.addWidget(self.line_2)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.field_size_config)

        self.field_layer_le = QLabel(self.frame)
        self.field_layer_le.setObjectName(u"field_layer_le")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.field_layer_le)

        self.field_layer_cb = QComboBox(self.frame)
        self.field_layer_cb.setObjectName(u"field_layer_cb")
        sizePolicy3.setHeightForWidth(self.field_layer_cb.sizePolicy().hasHeightForWidth())
        self.field_layer_cb.setSizePolicy(sizePolicy3)
        self.field_layer_cb.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.field_layer_cb)

        self.final_layer_label = QLabel(self.frame)
        self.final_layer_label.setObjectName(u"final_layer_label")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.final_layer_label)

        self.final_layer_cb = QComboBox(self.frame)
        self.final_layer_cb.setObjectName(u"final_layer_cb")
        sizePolicy2.setHeightForWidth(self.final_layer_cb.sizePolicy().hasHeightForWidth())
        self.final_layer_cb.setSizePolicy(sizePolicy2)
        self.final_layer_cb.setMinimumSize(QSize(170, 0))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.final_layer_cb)

        self.image_axes_label = QLabel(self.frame)
        self.image_axes_label.setObjectName(u"image_axes_label")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.image_axes_label)

        self.bb_size_label = QLabel(self.frame)
        self.bb_size_label.setObjectName(u"bb_size_label")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.bb_size_label)

        self.bb_size_dsb = QDoubleSpinBox(self.frame)
        self.bb_size_dsb.setObjectName(u"bb_size_dsb")
        sizePolicy2.setHeightForWidth(self.bb_size_dsb.sizePolicy().hasHeightForWidth())
        self.bb_size_dsb.setSizePolicy(sizePolicy2)
        self.bb_size_dsb.setMinimumSize(QSize(100, 0))
        self.bb_size_dsb.setValue(5.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.bb_size_dsb)

        self.bb_offsets_label = QLabel(self.frame)
        self.bb_offsets_label.setObjectName(u"bb_offsets_label")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.bb_offsets_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.left_offset_label = QLabel(self.frame)
        self.left_offset_label.setObjectName(u"left_offset_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.left_offset_label.sizePolicy().hasHeightForWidth())
        self.left_offset_label.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.left_offset_label)

        self.left_offset_dsb = QDoubleSpinBox(self.frame)
        self.left_offset_dsb.setObjectName(u"left_offset_dsb")
        sizePolicy2.setHeightForWidth(self.left_offset_dsb.sizePolicy().hasHeightForWidth())
        self.left_offset_dsb.setSizePolicy(sizePolicy2)
        self.left_offset_dsb.setMinimumSize(QSize(100, 0))
        self.left_offset_dsb.setMinimum(-100.000000000000000)
        self.left_offset_dsb.setMaximum(100.000000000000000)

        self.verticalLayout.addWidget(self.left_offset_dsb)

        self.up_offset_label = QLabel(self.frame)
        self.up_offset_label.setObjectName(u"up_offset_label")
        sizePolicy4.setHeightForWidth(self.up_offset_label.sizePolicy().hasHeightForWidth())
        self.up_offset_label.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.up_offset_label)

        self.up_offset_dsb = QDoubleSpinBox(self.frame)
        self.up_offset_dsb.setObjectName(u"up_offset_dsb")
        sizePolicy2.setHeightForWidth(self.up_offset_dsb.sizePolicy().hasHeightForWidth())
        self.up_offset_dsb.setSizePolicy(sizePolicy2)
        self.up_offset_dsb.setMinimumSize(QSize(100, 0))
        self.up_offset_dsb.setMinimum(-100.000000000000000)
        self.up_offset_dsb.setMaximum(100.000000000000000)

        self.verticalLayout.addWidget(self.up_offset_dsb)

        self.in_offset_label = QLabel(self.frame)
        self.in_offset_label.setObjectName(u"in_offset_label")

        self.verticalLayout.addWidget(self.in_offset_label)

        self.in_offset_dsb = QDoubleSpinBox(self.frame)
        self.in_offset_dsb.setObjectName(u"in_offset_dsb")
        sizePolicy2.setHeightForWidth(self.in_offset_dsb.sizePolicy().hasHeightForWidth())
        self.in_offset_dsb.setSizePolicy(sizePolicy2)
        self.in_offset_dsb.setMinimumSize(QSize(100, 0))
        self.in_offset_dsb.setMinimum(-100.000000000000000)
        self.in_offset_dsb.setMaximum(100.000000000000000)

        self.verticalLayout.addWidget(self.in_offset_dsb)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.formLayout.setLayout(9, QFormLayout.FieldRole, self.verticalLayout)

        self.gantry_tilt_label = QLabel(self.frame)
        self.gantry_tilt_label.setObjectName(u"gantry_tilt_label")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.gantry_tilt_label)

        self.gantry_tilt_dsb = QDoubleSpinBox(self.frame)
        self.gantry_tilt_dsb.setObjectName(u"gantry_tilt_dsb")
        sizePolicy2.setHeightForWidth(self.gantry_tilt_dsb.sizePolicy().hasHeightForWidth())
        self.gantry_tilt_dsb.setSizePolicy(sizePolicy2)
        self.gantry_tilt_dsb.setMinimumSize(QSize(100, 0))
        self.gantry_tilt_dsb.setDecimals(2)
        self.gantry_tilt_dsb.setMaximum(359.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.gantry_tilt_dsb)

        self.gantry_sag_label = QLabel(self.frame)
        self.gantry_sag_label.setObjectName(u"gantry_sag_label")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.gantry_sag_label)

        self.gantry_sag_dsb = QDoubleSpinBox(self.frame)
        self.gantry_sag_dsb.setObjectName(u"gantry_sag_dsb")
        sizePolicy2.setHeightForWidth(self.gantry_sag_dsb.sizePolicy().hasHeightForWidth())
        self.gantry_sag_dsb.setSizePolicy(sizePolicy2)
        self.gantry_sag_dsb.setMinimumSize(QSize(100, 0))
        self.gantry_sag_dsb.setMaximum(100.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.gantry_sag_dsb)

        self.image_axes_le = QLineEdit(self.frame)
        self.image_axes_le.setObjectName(u"image_axes_le")
        sizePolicy2.setHeightForWidth(self.image_axes_le.sizePolicy().hasHeightForWidth())
        self.image_axes_le.setSizePolicy(sizePolicy2)
        self.image_axes_le.setMinimumSize(QSize(350, 0))

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.image_axes_le)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.out_dir_le = QLineEdit(self.frame)
        self.out_dir_le.setObjectName(u"out_dir_le")
        sizePolicy2.setHeightForWidth(self.out_dir_le.sizePolicy().hasHeightForWidth())
        self.out_dir_le.setSizePolicy(sizePolicy2)
        self.out_dir_le.setMinimumSize(QSize(245, 0))
        self.out_dir_le.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.out_dir_le)

        self.select_dir_btn = QPushButton(self.frame)
        self.select_dir_btn.setObjectName(u"select_dir_btn")

        self.horizontalLayout_2.addWidget(self.select_dir_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_3.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.buttons_spacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.buttons_spacer, 1, 0, 1, 1)

        self.button_box = QDialogButtonBox(WLTestDialog)
        self.button_box.setObjectName(u"button_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy5)
        self.button_box.setStyleSheet(u"")
        self.button_box.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)

        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 1)


        self.retranslateUi(WLTestDialog)
        self.button_box.accepted.connect(WLTestDialog.accept)
        self.button_box.rejected.connect(WLTestDialog.reject)

        QMetaObject.connectSlotsByName(WLTestDialog)
    # setupUi

    def retranslateUi(self, WLTestDialog):
        self.test_name_label.setText(QCoreApplication.translate("WLTestDialog", u"Test name:", None))
        self.sim_image_label.setText(QCoreApplication.translate("WLTestDialog", u"Simulation image:", None))
        self.field_type_label.setText(QCoreApplication.translate("WLTestDialog", u"Field type:", None))
        self.field_size_label.setText(QCoreApplication.translate("WLTestDialog", u"Field size:", None))
        self.cone_field_size_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.rec_field_width_label.setText(QCoreApplication.translate("WLTestDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Width:</span></p></body></html>", None))
        self.rec_field_width_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.rec_field_height_label.setText(QCoreApplication.translate("WLTestDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">Height:</span></p></body></html>", None))
        self.rec_field_height_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.field_layer_le.setText(QCoreApplication.translate("WLTestDialog", u"Field layer:", None))
        self.final_layer_label.setText(QCoreApplication.translate("WLTestDialog", u"Final layer:", None))
        self.image_axes_label.setText(QCoreApplication.translate("WLTestDialog", u"Image axes:", None))
        self.bb_size_label.setText(QCoreApplication.translate("WLTestDialog", u"Ball bearing size:", None))
        self.bb_size_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.bb_offsets_label.setText(QCoreApplication.translate("WLTestDialog", u"Ball bearing offsets:", None))
        self.left_offset_label.setText(QCoreApplication.translate("WLTestDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">LEFT:</span></p></body></html>", None))
        self.left_offset_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.up_offset_label.setText(QCoreApplication.translate("WLTestDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">UP:</span></p></body></html>", None))
        self.up_offset_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.in_offset_label.setText(QCoreApplication.translate("WLTestDialog", u"<html><head/><body><p><span style=\" font-weight:700;\">IN:</span></p></body></html>", None))
        self.in_offset_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.gantry_tilt_label.setText(QCoreApplication.translate("WLTestDialog", u"Gantry tilt:", None))
        self.gantry_tilt_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.gantry_sag_label.setText(QCoreApplication.translate("WLTestDialog", u"Gantry sag:", None))
        self.gantry_sag_dsb.setSuffix(QCoreApplication.translate("WLTestDialog", u" mm", None))
        self.image_axes_le.setInputMask("")
        self.image_axes_le.setPlaceholderText(QCoreApplication.translate("WLTestDialog", u"Format: (90, 0, 0); (180, 0, 0); ...", None))
        self.label.setText(QCoreApplication.translate("WLTestDialog", u"Output directory:", None))
        self.select_dir_btn.setText(QCoreApplication.translate("WLTestDialog", u"Select directory", None))
        pass
    # retranslateUi

