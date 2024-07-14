# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'picket_fence_worksheet.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

class Ui_QPicketFenceWorksheet(object):
    def setupUi(self, QPicketFenceWorksheet):
        if not QPicketFenceWorksheet.objectName():
            QPicketFenceWorksheet.setObjectName(u"QPicketFenceWorksheet")
        QPicketFenceWorksheet.resize(1237, 480)
        self.verticalLayout = QVBoxLayout(QPicketFenceWorksheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(QPicketFenceWorksheet)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.analysisPage = QWidget()
        self.analysisPage.setObjectName(u"analysisPage")
        self.gridLayout = QGridLayout(self.analysisPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.frame_2 = QFrame(self.analysisPage)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
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

        self.configFormLayout = QFormLayout()
        self.configFormLayout.setObjectName(u"configFormLayout")
        self.toleranceLabel = QLabel(self.frame_2)
        self.toleranceLabel.setObjectName(u"toleranceLabel")

        self.configFormLayout.setWidget(0, QFormLayout.LabelRole, self.toleranceLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toleranceDSB = QDoubleSpinBox(self.frame_2)
        self.toleranceDSB.setObjectName(u"toleranceDSB")
        self.toleranceDSB.setDecimals(2)
        self.toleranceDSB.setMaximum(4.000000000000000)
        self.toleranceDSB.setSingleStep(0.500000000000000)
        self.toleranceDSB.setValue(2.000000000000000)

        self.horizontalLayout_4.addWidget(self.toleranceDSB)


        self.configFormLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.mLCTypeLabel = QLabel(self.frame_2)
        self.mLCTypeLabel.setObjectName(u"mLCTypeLabel")

        self.configFormLayout.setWidget(1, QFormLayout.LabelRole, self.mLCTypeLabel)

        self.mlcTypeCB = QComboBox(self.frame_2)
        self.mlcTypeCB.setObjectName(u"mlcTypeCB")

        self.configFormLayout.setWidget(1, QFormLayout.FieldRole, self.mlcTypeCB)

        self.numPicketsLabel = QLabel(self.frame_2)
        self.numPicketsLabel.setObjectName(u"numPicketsLabel")

        self.configFormLayout.setWidget(2, QFormLayout.LabelRole, self.numPicketsLabel)

        self.numPicketsCB = QComboBox(self.frame_2)
        self.numPicketsCB.setObjectName(u"numPicketsCB")

        self.configFormLayout.setWidget(2, QFormLayout.FieldRole, self.numPicketsCB)

        self.numPicketsSB = QSpinBox(self.frame_2)
        self.numPicketsSB.setObjectName(u"numPicketsSB")
        self.numPicketsSB.setMinimum(1)
        self.numPicketsSB.setMaximum(20)
        self.numPicketsSB.setValue(5)

        self.configFormLayout.setWidget(3, QFormLayout.FieldRole, self.numPicketsSB)

        self.cropLabel = QLabel(self.frame_2)
        self.cropLabel.setObjectName(u"cropLabel")

        self.configFormLayout.setWidget(5, QFormLayout.LabelRole, self.cropLabel)

        self.cropDSB = QDoubleSpinBox(self.frame_2)
        self.cropDSB.setObjectName(u"cropDSB")
        self.cropDSB.setDecimals(1)
        self.cropDSB.setSingleStep(0.100000000000000)
        self.cropDSB.setValue(3.000000000000000)

        self.configFormLayout.setWidget(5, QFormLayout.FieldRole, self.cropDSB)

        self.combLeafAnalysisLabel = QLabel(self.frame_2)
        self.combLeafAnalysisLabel.setObjectName(u"combLeafAnalysisLabel")

        self.configFormLayout.setWidget(6, QFormLayout.LabelRole, self.combLeafAnalysisLabel)

        self.combLeafAnalysisCheckB = QCheckBox(self.frame_2)
        self.combLeafAnalysisCheckB.setObjectName(u"combLeafAnalysisCheckB")
        self.combLeafAnalysisCheckB.setChecked(True)

        self.configFormLayout.setWidget(6, QFormLayout.FieldRole, self.combLeafAnalysisCheckB)

        self.nominalGapLabel = QLabel(self.frame_2)
        self.nominalGapLabel.setObjectName(u"nominalGapLabel")

        self.configFormLayout.setWidget(7, QFormLayout.LabelRole, self.nominalGapLabel)

        self.nominalGapDSB = QDoubleSpinBox(self.frame_2)
        self.nominalGapDSB.setObjectName(u"nominalGapDSB")
        self.nominalGapDSB.setDecimals(1)
        self.nominalGapDSB.setMinimum(0.100000000000000)
        self.nominalGapDSB.setMaximum(50.000000000000000)
        self.nominalGapDSB.setValue(3.000000000000000)

        self.configFormLayout.setWidget(7, QFormLayout.FieldRole, self.nominalGapDSB)

        self.useFilenameSLabel = QLabel(self.frame_2)
        self.useFilenameSLabel.setObjectName(u"useFilenameSLabel")

        self.configFormLayout.setWidget(8, QFormLayout.LabelRole, self.useFilenameSLabel)

        self.useFilenameSCheckB = QCheckBox(self.frame_2)
        self.useFilenameSCheckB.setObjectName(u"useFilenameSCheckB")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.useFilenameSCheckB.sizePolicy().hasHeightForWidth())
        self.useFilenameSCheckB.setSizePolicy(sizePolicy2)

        self.configFormLayout.setWidget(8, QFormLayout.FieldRole, self.useFilenameSCheckB)

        self.invertImageLabel = QLabel(self.frame_2)
        self.invertImageLabel.setObjectName(u"invertImageLabel")

        self.configFormLayout.setWidget(9, QFormLayout.LabelRole, self.invertImageLabel)

        self.invertImageCheckB = QCheckBox(self.frame_2)
        self.invertImageCheckB.setObjectName(u"invertImageCheckB")

        self.configFormLayout.setWidget(9, QFormLayout.FieldRole, self.invertImageCheckB)


        self.verticalLayout_4.addLayout(self.configFormLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
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
        self.outcomeLE.setMinimumSize(QSize(250, 0))
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

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.frame_2, 1, 3, 1, 1)

        self.mainActionsHL = QHBoxLayout()
        self.mainActionsHL.setSpacing(10)
        self.mainActionsHL.setObjectName(u"mainActionsHL")
        self.analyzeBtn = QPushButton(self.analysisPage)
        self.analyzeBtn.setObjectName(u"analyzeBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.analyzeBtn.sizePolicy().hasHeightForWidth())
        self.analyzeBtn.setSizePolicy(sizePolicy3)
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

        self.mainActionsHL.addWidget(self.analyzeBtn, 0, Qt.AlignLeft)

        self.advancedViewBtn = QPushButton(self.analysisPage)
        self.advancedViewBtn.setObjectName(u"advancedViewBtn")
        sizePolicy3.setHeightForWidth(self.advancedViewBtn.sizePolicy().hasHeightForWidth())
        self.advancedViewBtn.setSizePolicy(sizePolicy3)
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

        self.mainActionsHL.addWidget(self.advancedViewBtn)

        self.genReportBtn = QPushButton(self.analysisPage)
        self.genReportBtn.setObjectName(u"genReportBtn")
        sizePolicy3.setHeightForWidth(self.genReportBtn.sizePolicy().hasHeightForWidth())
        self.genReportBtn.setSizePolicy(sizePolicy3)
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

        self.mainActionsHL.addWidget(self.genReportBtn, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.mainActionsHL.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.mainActionsHL, 2, 1, 1, 1)

        self.frame = QFrame(self.analysisPage)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.analysisSummaryLabel = QFrame(self.frame)
        self.analysisSummaryLabel.setObjectName(u"analysisSummaryLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.analysisSummaryLabel.sizePolicy().hasHeightForWidth())
        self.analysisSummaryLabel.setSizePolicy(sizePolicy5)
        self.analysisSummaryLabel.setMaximumSize(QSize(16777215, 1))
        self.analysisSummaryLabel.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.analysisSummaryLabel.setFrameShape(QFrame.HLine)
        self.analysisSummaryLabel.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.analysisSummaryLabel)

        self.buttonSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.buttonSpacer)

        self.analysisInfoVL = QVBoxLayout()
        self.analysisInfoVL.setObjectName(u"analysisInfoVL")

        self.verticalLayout_3.addLayout(self.analysisInfoVL)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.importedImgLabel = QLabel(self.analysisPage)
        self.importedImgLabel.setObjectName(u"importedImgLabel")
        self.importedImgLabel.setFont(font)

        self.gridLayout.addWidget(self.importedImgLabel, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.analysisPage)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analysisSumLabel = QLabel(self.analysisPage)
        self.analysisSumLabel.setObjectName(u"analysisSumLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.analysisSumLabel.sizePolicy().hasHeightForWidth())
        self.analysisSumLabel.setSizePolicy(sizePolicy6)
        self.analysisSumLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.analysisSumLabel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.imageListWidget = QListWidget(self.analysisPage)
        self.imageListWidget.setObjectName(u"imageListWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.imageListWidget.sizePolicy().hasHeightForWidth())
        self.imageListWidget.setSizePolicy(sizePolicy7)
        self.imageListWidget.setMinimumSize(QSize(350, 0))
        self.imageListWidget.setMaximumSize(QSize(350, 16777215))
        self.imageListWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.imageListWidget.setDefaultDropAction(Qt.MoveAction)
        self.imageListWidget.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.imageListWidget, 1, 0, 1, 1)

        self.addImgBtn = QPushButton(self.analysisPage)
        self.addImgBtn.setObjectName(u"addImgBtn")
        sizePolicy2.setHeightForWidth(self.addImgBtn.sizePolicy().hasHeightForWidth())
        self.addImgBtn.setSizePolicy(sizePolicy2)
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

        self.gridLayout.addWidget(self.addImgBtn, 2, 0, 1, 1, Qt.AlignVCenter)

        self.line_2 = QFrame(self.analysisPage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.analysisPage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(QPicketFenceWorksheet)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(QPicketFenceWorksheet)
    # setupUi

    def retranslateUi(self, QPicketFenceWorksheet):
        QPicketFenceWorksheet.setWindowTitle(QCoreApplication.translate("QPicketFenceWorksheet", u"Form", None))
        self.toleranceLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Tolerance:", None))
        self.toleranceDSB.setSuffix(QCoreApplication.translate("QPicketFenceWorksheet", u" mm", None))
        self.mLCTypeLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"MLC type:", None))
        self.numPicketsLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Number of Pickets:", None))
        self.cropLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Crop:", None))
        self.cropDSB.setSuffix(QCoreApplication.translate("QPicketFenceWorksheet", u" mm", None))
        self.combLeafAnalysisLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Combined leaf analysis:", None))
        self.nominalGapLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Nominal gap:", None))
        self.nominalGapDSB.setPrefix("")
        self.nominalGapDSB.setSuffix(QCoreApplication.translate("QPicketFenceWorksheet", u" mm", None))
        self.useFilenameSLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Use filename(s):", None))
        self.invertImageLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Invert image:", None))
        self.label_2.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis Outcome</span></p></body></html>", None))
        self.outcomeLE.setPlaceholderText(QCoreApplication.translate("QPicketFenceWorksheet", u"N/A", None))
        self.analyzeBtn.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Analyze images", None))
        self.advancedViewBtn.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Advanced results", None))
        self.genReportBtn.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Generate report", None))
        self.importedImgLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Imported images", None))
        self.label.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Configuration</span></p></body></html>", None))
        self.analysisSumLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis summary</span></p></body></html>", None))
        self.addImgBtn.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Add image(s)", None))
    # retranslateUi

