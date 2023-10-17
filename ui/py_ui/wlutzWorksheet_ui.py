# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wlutzWorksheet.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_QWLutzWorksheet(object):
    def setupUi(self, QWLutzWorksheet):
        if not QWLutzWorksheet.objectName():
            QWLutzWorksheet.setObjectName(u"QWLutzWorksheet")
        QWLutzWorksheet.resize(1268, 405)
        self.verticalLayout = QVBoxLayout(QWLutzWorksheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(QWLutzWorksheet)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.introPage = QWidget()
        self.introPage.setObjectName(u"introPage")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.introPage.sizePolicy().hasHeightForWidth())
        self.introPage.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.introPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.introDetailsLabel = QLabel(self.introPage)
        self.introDetailsLabel.setObjectName(u"introDetailsLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.introDetailsLabel.sizePolicy().hasHeightForWidth())
        self.introDetailsLabel.setSizePolicy(sizePolicy2)
        self.introDetailsLabel.setMinimumSize(QSize(450, 0))
        self.introDetailsLabel.setMaximumSize(QSize(450, 16777215))
        self.introDetailsLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.introDetailsLabel, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.importImgBtn = QPushButton(self.introPage)
        self.importImgBtn.setObjectName(u"importImgBtn")
        self.importImgBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 142, 122);\n"
"    min-width: 150px;\n"
"	min-height:20px;\n"
"    padding: 6px;\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	font: bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(52, 91, 78);\n"
"}\n"
"\n"
"QPushButton:!enabled{\n"
"	background-color: rgba(52, 91, 78, 50);\n"
"}")

        self.horizontalLayout.addWidget(self.importImgBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.introPage)
        self.analysisPage = QWidget()
        self.analysisPage.setObjectName(u"analysisPage")
        self.gridLayout = QGridLayout(self.analysisPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.analysisPage)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 3, 1, 1)

        self.frame_2 = QFrame(self.analysisPage)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.toleranceLabel = QLabel(self.frame_2)
        self.toleranceLabel.setObjectName(u"toleranceLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.toleranceLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toleranceDSB = QDoubleSpinBox(self.frame_2)
        self.toleranceDSB.setObjectName(u"toleranceDSB")
        self.toleranceDSB.setMaximumSize(QSize(100, 16777215))
        self.toleranceDSB.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.toleranceDSB.setDecimals(2)
        self.toleranceDSB.setMaximum(3.000000000000000)
        self.toleranceDSB.setSingleStep(0.500000000000000)
        self.toleranceDSB.setValue(1.000000000000000)

        self.horizontalLayout_4.addWidget(self.toleranceDSB)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.coordSysCB = QComboBox(self.frame_2)
        self.coordSysCB.setObjectName(u"coordSysCB")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.coordSysCB)

        self.lowDensityBBLabel = QLabel(self.frame_2)
        self.lowDensityBBLabel.setObjectName(u"lowDensityBBLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lowDensityBBLabel)

        self.lowDensityBBCheckBox = QCheckBox(self.frame_2)
        self.lowDensityBBCheckBox.setObjectName(u"lowDensityBBCheckBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lowDensityBBCheckBox)

        self.useFilenameSLabel = QLabel(self.frame_2)
        self.useFilenameSLabel.setObjectName(u"useFilenameSLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.useFilenameSLabel)

        self.useFilenameSCheckBox = QCheckBox(self.frame_2)
        self.useFilenameSCheckBox.setObjectName(u"useFilenameSCheckBox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.useFilenameSCheckBox)

        self.bb_size_label = QLabel(self.frame_2)
        self.bb_size_label.setObjectName(u"bb_size_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.bb_size_label)

        self.bb_size_dsb = QDoubleSpinBox(self.frame_2)
        self.bb_size_dsb.setObjectName(u"bb_size_dsb")
        self.bb_size_dsb.setMaximumSize(QSize(100, 16777215))
        self.bb_size_dsb.setDecimals(1)
        self.bb_size_dsb.setMinimum(1.000000000000000)
        self.bb_size_dsb.setMaximum(20.000000000000000)
        self.bb_size_dsb.setValue(5.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.bb_size_dsb)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_4.addWidget(self.label_2)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.outcomeLE = QLineEdit(self.frame_2)
        self.outcomeLE.setObjectName(u"outcomeLE")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.outcomeLE.sizePolicy().hasHeightForWidth())
        self.outcomeLE.setSizePolicy(sizePolicy4)
        self.outcomeLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.outcomeLE.setStyleSheet(u"border-color: rgb(95, 200, 26);\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"background-color: rgba(95, 200, 26,150);\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold;\n"
"\n"
"")
        self.outcomeLE.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.outcomeLE)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.frame_2, 1, 3, 1, 1)

        self.imageListWidget = QListWidget(self.analysisPage)
        self.imageListWidget.setObjectName(u"imageListWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.imageListWidget.sizePolicy().hasHeightForWidth())
        self.imageListWidget.setSizePolicy(sizePolicy5)
        self.imageListWidget.setMinimumSize(QSize(350, 0))
        self.imageListWidget.setMaximumSize(QSize(350, 16777215))
        self.imageListWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.imageListWidget.setDefaultDropAction(Qt.MoveAction)
        self.imageListWidget.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.imageListWidget, 1, 0, 1, 1)

        self.importedImgLabel = QLabel(self.analysisPage)
        self.importedImgLabel.setObjectName(u"importedImgLabel")
        self.importedImgLabel.setFont(font)

        self.gridLayout.addWidget(self.importedImgLabel, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analysisSumLabel = QLabel(self.analysisPage)
        self.analysisSumLabel.setObjectName(u"analysisSumLabel")
        sizePolicy4.setHeightForWidth(self.analysisSumLabel.sizePolicy().hasHeightForWidth())
        self.analysisSumLabel.setSizePolicy(sizePolicy4)
        self.analysisSumLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.analysisSumLabel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.frame = QFrame(self.analysisPage)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.analysisSummaryLabel = QFrame(self.frame)
        self.analysisSummaryLabel.setObjectName(u"analysisSummaryLabel")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.analysisSummaryLabel.sizePolicy().hasHeightForWidth())
        self.analysisSummaryLabel.setSizePolicy(sizePolicy7)
        self.analysisSummaryLabel.setMaximumSize(QSize(16777215, 1))
        self.analysisSummaryLabel.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.analysisSummaryLabel.setFrameShape(QFrame.HLine)
        self.analysisSummaryLabel.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.analysisSummaryLabel)

        self.buttonSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.buttonSpacer)

        self.analysisInfoVL = QVBoxLayout()
        self.analysisInfoVL.setObjectName(u"analysisInfoVL")

        self.verticalLayout_3.addLayout(self.analysisInfoVL)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.line_2 = QFrame(self.analysisPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.analyzeBtn = QPushButton(self.analysisPage)
        self.analyzeBtn.setObjectName(u"analyzeBtn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.analyzeBtn.sizePolicy().hasHeightForWidth())
        self.analyzeBtn.setSizePolicy(sizePolicy8)
        self.analyzeBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 142, 122);\n"
"    min-width: 150px;\n"
"	min-height:20px;\n"
"    padding: 6px;\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	font: bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(52, 91, 78);\n"
"}\n"
"\n"
"QPushButton:!enabled{\n"
"	background-color: rgba(52, 91, 78, 50);\n"
"	color: rgba(255,255,255,100)\n"
"}")

        self.gridLayout_2.addWidget(self.analyzeBtn, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.shiftInfoBtn = QPushButton(self.analysisPage)
        self.shiftInfoBtn.setObjectName(u"shiftInfoBtn")
        sizePolicy8.setHeightForWidth(self.shiftInfoBtn.sizePolicy().hasHeightForWidth())
        self.shiftInfoBtn.setSizePolicy(sizePolicy8)
        self.shiftInfoBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 142, 122);\n"
"    min-width: 150px;\n"
"	min-height:20px;\n"
"    padding: 6px;\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	font: bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(52, 91, 78);\n"
"}\n"
"\n"
"QPushButton:!enabled{\n"
"	background-color: rgba(52, 91, 78, 50);\n"
"	color: rgba(255,255,255,100)\n"
"}")

        self.gridLayout_2.addWidget(self.shiftInfoBtn, 0, 1, 1, 1)

        self.genReportBtn = QPushButton(self.analysisPage)
        self.genReportBtn.setObjectName(u"genReportBtn")
        sizePolicy8.setHeightForWidth(self.genReportBtn.sizePolicy().hasHeightForWidth())
        self.genReportBtn.setSizePolicy(sizePolicy8)
        self.genReportBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 142, 122);\n"
"    min-width: 150px;\n"
"	min-height:20px;\n"
"    padding: 6px;\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	font: bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(52, 91, 78);\n"
"}\n"
"\n"
"QPushButton:!enabled{\n"
"	background-color: rgba(52, 91, 78, 50);\n"
"	color: rgba(255,255,255,100)\n"
"}")

        self.gridLayout_2.addWidget(self.genReportBtn, 0, 2, 1, 1)

        self.advancedViewBtn = QPushButton(self.analysisPage)
        self.advancedViewBtn.setObjectName(u"advancedViewBtn")
        self.advancedViewBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 142, 122);\n"
"    min-width: 150px;\n"
"	min-height:20px;\n"
"    padding: 6px;\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	font: bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(52, 91, 78);\n"
"}\n"
"\n"
"QPushButton:!enabled{\n"
"	background-color: rgba(52, 91, 78, 50);\n"
"	color: rgba(255,255,255,100)\n"
"}")

        self.gridLayout_2.addWidget(self.advancedViewBtn, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 1, 1, 1)

        self.addImgBtn = QPushButton(self.analysisPage)
        self.addImgBtn.setObjectName(u"addImgBtn")
        sizePolicy8.setHeightForWidth(self.addImgBtn.sizePolicy().hasHeightForWidth())
        self.addImgBtn.setSizePolicy(sizePolicy8)
        self.addImgBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(82, 142, 122);\n"
"    min-width: 150px;\n"
"	min-height:20px;\n"
"    padding: 6px;\n"
"	border-radius: 15px;\n"
"	color: white;\n"
"	font: bold;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(52, 91, 78);\n"
"}\n"
"\n"
"QPushButton:!enabled{\n"
"	background-color: rgba(52, 91, 78, 50);\n"
"	color: rgba(255,255,255,100)\n"
"}")
        self.addImgBtn.setAutoDefault(False)

        self.gridLayout.addWidget(self.addImgBtn, 2, 0, 1, 1, Qt.AlignTop)

        self.stackedWidget.addWidget(self.analysisPage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(QWLutzWorksheet)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(QWLutzWorksheet)
    # setupUi

    def retranslateUi(self, QWLutzWorksheet):
        QWLutzWorksheet.setWindowTitle(QCoreApplication.translate("QWLutzWorksheet", u"Form", None))
        self.introDetailsLabel.setText(QCoreApplication.translate("QWLutzWorksheet", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hi, to get started with your Winston-Lutz analysis simply &quot;import&quot; the EPID DICOM images. Please note the following:</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700; color:#000000;\"></span><span style=\" font-weight:700;\">\u273b The BB should be fully within the field of view."
                        "</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u273b The MLC field should be symmetric.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u273b The BB should be less than 2 cm from the isocenter.</span></p></body></html>", None))
        self.importImgBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"Import images", None))
        self.label.setText(QCoreApplication.translate("QWLutzWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Configuration</span></p></body></html>", None))
        self.toleranceLabel.setText(QCoreApplication.translate("QWLutzWorksheet", u"Tolerance:", None))
        self.toleranceDSB.setSuffix(QCoreApplication.translate("QWLutzWorksheet", u" mm", None))
        self.label_3.setText(QCoreApplication.translate("QWLutzWorksheet", u"Coordinate system:", None))
        self.lowDensityBBLabel.setText(QCoreApplication.translate("QWLutzWorksheet", u"Low density BB:", None))
        self.useFilenameSLabel.setText(QCoreApplication.translate("QWLutzWorksheet", u"Use filename(s):", None))
        self.bb_size_label.setText(QCoreApplication.translate("QWLutzWorksheet", u"Ball bearing size:", None))
        self.bb_size_dsb.setSuffix(QCoreApplication.translate("QWLutzWorksheet", u" mm", None))
        self.label_2.setText(QCoreApplication.translate("QWLutzWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis Outcome</span></p></body></html>", None))
        self.outcomeLE.setPlaceholderText(QCoreApplication.translate("QWLutzWorksheet", u"N/A", None))
        self.importedImgLabel.setText(QCoreApplication.translate("QWLutzWorksheet", u"Imported images", None))
        self.analysisSumLabel.setText(QCoreApplication.translate("QWLutzWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis summary</span></p></body></html>", None))
        self.analyzeBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"Analyze images", None))
        self.shiftInfoBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"View shift instructions", None))
        self.genReportBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"Generate report", None))
        self.advancedViewBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"Advanced results", None))
        self.addImgBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"Add image(s)", None))
    # retranslateUi

