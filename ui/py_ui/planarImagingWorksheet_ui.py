# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'planarImagingWorksheet.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_QPlanarImagingWorksheet(object):
    def setupUi(self, QPlanarImagingWorksheet):
        if not QPlanarImagingWorksheet.objectName():
            QPlanarImagingWorksheet.setObjectName(u"QPlanarImagingWorksheet")
        QPlanarImagingWorksheet.resize(1337, 593)
        self.verticalLayout = QVBoxLayout(QPlanarImagingWorksheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(QPlanarImagingWorksheet)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(350, 0))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setMinimumSize(QSize(350, 0))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(False)
        self.configFrame = QFrame(self.splitter)
        self.configFrame.setObjectName(u"configFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.configFrame.sizePolicy().hasHeightForWidth())
        self.configFrame.setSizePolicy(sizePolicy3)
        self.configFrame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.configFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.configScrollArea = QScrollArea(self.configFrame)
        self.configScrollArea.setObjectName(u"configScrollArea")
        sizePolicy3.setHeightForWidth(self.configScrollArea.sizePolicy().hasHeightForWidth())
        self.configScrollArea.setSizePolicy(sizePolicy3)
        self.configScrollArea.setStyleSheet(u"QScrollArea#configScrollArea{\n"
"background-color: transparent\n"
"}")
        self.configScrollArea.setFrameShape(QFrame.NoFrame)
        self.configScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 336, 396))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents {\n"
"	background-color: transparent\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.configFormLayout = QFormLayout()
        self.configFormLayout.setObjectName(u"configFormLayout")
        self.phantomTypeLabel = QLabel(self.frame_3)
        self.phantomTypeLabel.setObjectName(u"phantomTypeLabel")

        self.configFormLayout.setWidget(0, QFormLayout.LabelRole, self.phantomTypeLabel)

        self.phantomTypeCB = QComboBox(self.frame_3)
        self.phantomTypeCB.setObjectName(u"phantomTypeCB")

        self.configFormLayout.setWidget(0, QFormLayout.FieldRole, self.phantomTypeCB)

        self.lConstrastThresholdLabel = QLabel(self.frame_3)
        self.lConstrastThresholdLabel.setObjectName(u"lConstrastThresholdLabel")

        self.configFormLayout.setWidget(1, QFormLayout.LabelRole, self.lConstrastThresholdLabel)

        self.lConstrastThresholdDSB = QDoubleSpinBox(self.frame_3)
        self.lConstrastThresholdDSB.setObjectName(u"lConstrastThresholdDSB")
        self.lConstrastThresholdDSB.setMaximum(1.000000000000000)
        self.lConstrastThresholdDSB.setSingleStep(0.010000000000000)
        self.lConstrastThresholdDSB.setValue(0.050000000000000)

        self.configFormLayout.setWidget(1, QFormLayout.FieldRole, self.lConstrastThresholdDSB)

        self.lConstrastMethodLabel = QLabel(self.frame_3)
        self.lConstrastMethodLabel.setObjectName(u"lConstrastMethodLabel")

        self.configFormLayout.setWidget(2, QFormLayout.LabelRole, self.lConstrastMethodLabel)

        self.lConstrastMethodCB = QComboBox(self.frame_3)
        self.lConstrastMethodCB.setObjectName(u"lConstrastMethodCB")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lConstrastMethodCB.sizePolicy().hasHeightForWidth())
        self.lConstrastMethodCB.setSizePolicy(sizePolicy4)

        self.configFormLayout.setWidget(2, QFormLayout.FieldRole, self.lConstrastMethodCB)

        self.hConstrastThresholdLabel = QLabel(self.frame_3)
        self.hConstrastThresholdLabel.setObjectName(u"hConstrastThresholdLabel")

        self.configFormLayout.setWidget(3, QFormLayout.LabelRole, self.hConstrastThresholdLabel)

        self.hConstrastThresholdDSB = QDoubleSpinBox(self.frame_3)
        self.hConstrastThresholdDSB.setObjectName(u"hConstrastThresholdDSB")
        self.hConstrastThresholdDSB.setMaximum(1.000000000000000)
        self.hConstrastThresholdDSB.setSingleStep(0.100000000000000)
        self.hConstrastThresholdDSB.setValue(0.500000000000000)

        self.configFormLayout.setWidget(3, QFormLayout.FieldRole, self.hConstrastThresholdDSB)

        self.visThresholdLabel = QLabel(self.frame_3)
        self.visThresholdLabel.setObjectName(u"visThresholdLabel")

        self.configFormLayout.setWidget(4, QFormLayout.LabelRole, self.visThresholdLabel)

        self.visThresholdDSB = QDoubleSpinBox(self.frame_3)
        self.visThresholdDSB.setObjectName(u"visThresholdDSB")
        self.visThresholdDSB.setDecimals(0)
        self.visThresholdDSB.setValue(100.000000000000000)

        self.configFormLayout.setWidget(4, QFormLayout.FieldRole, self.visThresholdDSB)

        self.sSDLabel = QLabel(self.frame_3)
        self.sSDLabel.setObjectName(u"sSDLabel")

        self.configFormLayout.setWidget(5, QFormLayout.LabelRole, self.sSDLabel)

        self.sSDDSB = QDoubleSpinBox(self.frame_3)
        self.sSDDSB.setObjectName(u"sSDDSB")
        self.sSDDSB.setDecimals(0)
        self.sSDDSB.setMinimum(1.000000000000000)
        self.sSDDSB.setMaximum(3000.000000000000000)
        self.sSDDSB.setValue(1000.000000000000000)

        self.configFormLayout.setWidget(5, QFormLayout.FieldRole, self.sSDDSB)

        self.phantomAngleOverrLabel = QLabel(self.frame_3)
        self.phantomAngleOverrLabel.setObjectName(u"phantomAngleOverrLabel")

        self.configFormLayout.setWidget(6, QFormLayout.LabelRole, self.phantomAngleOverrLabel)

        self.phantomAngleOverrCB = QComboBox(self.frame_3)
        self.phantomAngleOverrCB.setObjectName(u"phantomAngleOverrCB")
        sizePolicy4.setHeightForWidth(self.phantomAngleOverrCB.sizePolicy().hasHeightForWidth())
        self.phantomAngleOverrCB.setSizePolicy(sizePolicy4)

        self.configFormLayout.setWidget(6, QFormLayout.FieldRole, self.phantomAngleOverrCB)

        self.phantomAngleConfigVL = QVBoxLayout()
        self.phantomAngleConfigVL.setObjectName(u"phantomAngleConfigVL")
        self.phantomAngleLabel = QLabel(self.frame_3)
        self.phantomAngleLabel.setObjectName(u"phantomAngleLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.phantomAngleLabel.sizePolicy().hasHeightForWidth())
        self.phantomAngleLabel.setSizePolicy(sizePolicy5)

        self.phantomAngleConfigVL.addWidget(self.phantomAngleLabel)

        self.phantomAngleDSB = QDoubleSpinBox(self.frame_3)
        self.phantomAngleDSB.setObjectName(u"phantomAngleDSB")
        self.phantomAngleDSB.setMaximum(359.990000000000009)

        self.phantomAngleConfigVL.addWidget(self.phantomAngleDSB)


        self.configFormLayout.setLayout(7, QFormLayout.FieldRole, self.phantomAngleConfigVL)

        self.phantomCenterOverrLabel = QLabel(self.frame_3)
        self.phantomCenterOverrLabel.setObjectName(u"phantomCenterOverrLabel")

        self.configFormLayout.setWidget(8, QFormLayout.LabelRole, self.phantomCenterOverrLabel)

        self.phantomCenterOverrCB = QComboBox(self.frame_3)
        self.phantomCenterOverrCB.setObjectName(u"phantomCenterOverrCB")
        sizePolicy4.setHeightForWidth(self.phantomCenterOverrCB.sizePolicy().hasHeightForWidth())
        self.phantomCenterOverrCB.setSizePolicy(sizePolicy4)

        self.configFormLayout.setWidget(8, QFormLayout.FieldRole, self.phantomCenterOverrCB)

        self.phantomCenterConfigVL = QVBoxLayout()
        self.phantomCenterConfigVL.setObjectName(u"phantomCenterConfigVL")
        self.xCenterLabel = QLabel(self.frame_3)
        self.xCenterLabel.setObjectName(u"xCenterLabel")
        sizePolicy5.setHeightForWidth(self.xCenterLabel.sizePolicy().hasHeightForWidth())
        self.xCenterLabel.setSizePolicy(sizePolicy5)

        self.phantomCenterConfigVL.addWidget(self.xCenterLabel)

        self.xCenterDSB = QDoubleSpinBox(self.frame_3)
        self.xCenterDSB.setObjectName(u"xCenterDSB")
        self.xCenterDSB.setMaximum(1000.000000000000000)

        self.phantomCenterConfigVL.addWidget(self.xCenterDSB)

        self.yCenterLabel = QLabel(self.frame_3)
        self.yCenterLabel.setObjectName(u"yCenterLabel")
        sizePolicy5.setHeightForWidth(self.yCenterLabel.sizePolicy().hasHeightForWidth())
        self.yCenterLabel.setSizePolicy(sizePolicy5)

        self.phantomCenterConfigVL.addWidget(self.yCenterLabel)

        self.yCenterDSB = QDoubleSpinBox(self.frame_3)
        self.yCenterDSB.setObjectName(u"yCenterDSB")
        self.yCenterDSB.setMaximum(1000.000000000000000)

        self.phantomCenterConfigVL.addWidget(self.yCenterDSB)


        self.configFormLayout.setLayout(9, QFormLayout.FieldRole, self.phantomCenterConfigVL)

        self.invertImageCheckB = QCheckBox(self.frame_3)
        self.invertImageCheckB.setObjectName(u"invertImageCheckB")

        self.configFormLayout.setWidget(10, QFormLayout.FieldRole, self.invertImageCheckB)

        self.invertImageLabel = QLabel(self.frame_3)
        self.invertImageLabel.setObjectName(u"invertImageLabel")

        self.configFormLayout.setWidget(10, QFormLayout.LabelRole, self.invertImageLabel)


        self.verticalLayout_6.addLayout(self.configFormLayout)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.configScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.configScrollArea)

        self.splitter.addWidget(self.configFrame)
        self.outcomeFrame = QFrame(self.splitter)
        self.outcomeFrame.setObjectName(u"outcomeFrame")
        sizePolicy3.setHeightForWidth(self.outcomeFrame.sizePolicy().hasHeightForWidth())
        self.outcomeFrame.setSizePolicy(sizePolicy3)
        self.outcomeFrame.setFrameShape(QFrame.NoFrame)
        self.outcomeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.outcomeFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.outcomeFrame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)

        self.verticalLayout_7.addWidget(self.label_2)

        self.line_3 = QFrame(self.outcomeFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_3)

        self.outcomeLE = QLineEdit(self.outcomeFrame)
        self.outcomeLE.setObjectName(u"outcomeLE")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.outcomeLE.sizePolicy().hasHeightForWidth())
        self.outcomeLE.setSizePolicy(sizePolicy6)
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

        self.verticalLayout_7.addWidget(self.outcomeLE)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.outcomeFrame)

        self.verticalLayout_4.addWidget(self.splitter)


        self.gridLayout.addWidget(self.frame_2, 1, 3, 1, 1)

        self.mainActionsHL = QHBoxLayout()
        self.mainActionsHL.setSpacing(10)
        self.mainActionsHL.setObjectName(u"mainActionsHL")
        self.analyzeBtn = QPushButton(self.analysisPage)
        self.analyzeBtn.setObjectName(u"analyzeBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.analyzeBtn.sizePolicy().hasHeightForWidth())
        self.analyzeBtn.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.advancedViewBtn.sizePolicy().hasHeightForWidth())
        self.advancedViewBtn.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.genReportBtn.sizePolicy().hasHeightForWidth())
        self.genReportBtn.setSizePolicy(sizePolicy7)
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

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.mainActionsHL.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.mainActionsHL, 2, 1, 1, 1)

        self.frame = QFrame(self.analysisPage)
        self.frame.setObjectName(u"frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy8)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.analysisSummaryLabel = QFrame(self.frame)
        self.analysisSummaryLabel.setObjectName(u"analysisSummaryLabel")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.analysisSummaryLabel.sizePolicy().hasHeightForWidth())
        self.analysisSummaryLabel.setSizePolicy(sizePolicy9)
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

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.importedImgLabel = QLabel(self.analysisPage)
        self.importedImgLabel.setObjectName(u"importedImgLabel")
        self.importedImgLabel.setFont(font)

        self.gridLayout.addWidget(self.importedImgLabel, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.analysisPage)
        self.label.setObjectName(u"label")
        sizePolicy8.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy8)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analysisSumLabel = QLabel(self.analysisPage)
        self.analysisSumLabel.setObjectName(u"analysisSumLabel")
        sizePolicy6.setHeightForWidth(self.analysisSumLabel.sizePolicy().hasHeightForWidth())
        self.analysisSumLabel.setSizePolicy(sizePolicy6)
        self.analysisSumLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.analysisSumLabel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.imageListWidget = QListWidget(self.analysisPage)
        self.imageListWidget.setObjectName(u"imageListWidget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.imageListWidget.sizePolicy().hasHeightForWidth())
        self.imageListWidget.setSizePolicy(sizePolicy10)
        self.imageListWidget.setMinimumSize(QSize(350, 0))
        self.imageListWidget.setMaximumSize(QSize(350, 16777215))
        self.imageListWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.imageListWidget.setDefaultDropAction(Qt.MoveAction)
        self.imageListWidget.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.imageListWidget, 1, 0, 1, 1)

        self.addImgBtn = QPushButton(self.analysisPage)
        self.addImgBtn.setObjectName(u"addImgBtn")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.addImgBtn.sizePolicy().hasHeightForWidth())
        self.addImgBtn.setSizePolicy(sizePolicy11)
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


        self.retranslateUi(QPlanarImagingWorksheet)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(QPlanarImagingWorksheet)
    # setupUi

    def retranslateUi(self, QPlanarImagingWorksheet):
        self.phantomTypeLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Phantom type:", None))
        self.lConstrastThresholdLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Low constrast threshold:", None))
        self.lConstrastMethodLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Low constrast method:", None))
        self.hConstrastThresholdLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"High constrast threshold:", None))
        self.visThresholdLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Visibility threshold:", None))
        self.visThresholdDSB.setSuffix("")
        self.sSDLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"SSD:", None))
        self.sSDDSB.setSuffix(QCoreApplication.translate("QPlanarImagingWorksheet", u" mm", None))
        self.phantomAngleOverrLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Phantom angle override:", None))
        self.phantomAngleLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Angle:", None))
        self.phantomAngleDSB.setSuffix(QCoreApplication.translate("QPlanarImagingWorksheet", u"\u00b0", None))
        self.phantomCenterOverrLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Phantom center override:", None))
        self.xCenterLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"X:", None))
        self.yCenterLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Y:", None))
        self.invertImageLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Invert image:", None))
        self.label_2.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis Outcome</span></p></body></html>", None))
        self.outcomeLE.setPlaceholderText(QCoreApplication.translate("QPlanarImagingWorksheet", u"N/A", None))
        self.analyzeBtn.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Analyze images", None))
        self.advancedViewBtn.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Advanced results", None))
        self.genReportBtn.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Generate report", None))
        self.importedImgLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Imported images", None))
        self.label.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Configuration</span></p></body></html>", None))
        self.analysisSumLabel.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis summary</span></p></body></html>", None))
        self.addImgBtn.setText(QCoreApplication.translate("QPlanarImagingWorksheet", u"Add image(s)", None))
        pass
    # retranslateUi

