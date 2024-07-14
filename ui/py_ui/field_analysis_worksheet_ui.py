# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'field_analysis_worksheet.ui'
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
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_QFieldAnalysisWorksheet(object):
    def setupUi(self, QFieldAnalysisWorksheet):
        if not QFieldAnalysisWorksheet.objectName():
            QFieldAnalysisWorksheet.setObjectName(u"QFieldAnalysisWorksheet")
        QFieldAnalysisWorksheet.resize(1307, 702)
        self.verticalLayout = QVBoxLayout(QFieldAnalysisWorksheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(QFieldAnalysisWorksheet)
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
        self.mainActionsHL = QHBoxLayout()
        self.mainActionsHL.setSpacing(10)
        self.mainActionsHL.setObjectName(u"mainActionsHL")
        self.analyzeBtn = QPushButton(self.analysisPage)
        self.analyzeBtn.setObjectName(u"analyzeBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.analyzeBtn.sizePolicy().hasHeightForWidth())
        self.analyzeBtn.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.advancedViewBtn.sizePolicy().hasHeightForWidth())
        self.advancedViewBtn.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.genReportBtn.sizePolicy().hasHeightForWidth())
        self.genReportBtn.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.analysisSummaryLabel = QFrame(self.frame)
        self.analysisSummaryLabel.setObjectName(u"analysisSummaryLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.analysisSummaryLabel.sizePolicy().hasHeightForWidth())
        self.analysisSummaryLabel.setSizePolicy(sizePolicy3)
        self.analysisSummaryLabel.setMaximumSize(QSize(16777215, 1))
        self.analysisSummaryLabel.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.analysisSummaryLabel.setFrameShape(QFrame.HLine)
        self.analysisSummaryLabel.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.analysisSummaryLabel)

        self.buttonSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.buttonSpacer)

        self.analysisInfoVL = QVBoxLayout()
        self.analysisInfoVL.setObjectName(u"analysisInfoVL")
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea#scrollArea {\n"
"	background-color: transparent\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.summaryScrollArea = QWidget()
        self.summaryScrollArea.setObjectName(u"summaryScrollArea")
        self.summaryScrollArea.setGeometry(QRect(0, 0, 505, 546))
        self.summaryScrollArea.setStyleSheet(u"QWidget#summaryScrollArea {\n"
"	background-color: transparent\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.summaryScrollArea)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.summaryTE = QTextEdit(self.summaryScrollArea)
        self.summaryTE.setObjectName(u"summaryTE")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.summaryTE.sizePolicy().hasHeightForWidth())
        self.summaryTE.setSizePolicy(sizePolicy4)
        self.summaryTE.setContextMenuPolicy(Qt.NoContextMenu)
        self.summaryTE.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_8.addWidget(self.summaryTE)

        self.scrollArea.setWidget(self.summaryScrollArea)

        self.analysisInfoVL.addWidget(self.scrollArea)


        self.verticalLayout_3.addLayout(self.analysisInfoVL)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.importedImgLabel = QLabel(self.analysisPage)
        self.importedImgLabel.setObjectName(u"importedImgLabel")
        font = QFont()
        font.setPointSize(13)
        self.importedImgLabel.setFont(font)

        self.gridLayout.addWidget(self.importedImgLabel, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.analysisPage)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analysisSumLabel = QLabel(self.analysisPage)
        self.analysisSumLabel.setObjectName(u"analysisSumLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.analysisSumLabel.sizePolicy().hasHeightForWidth())
        self.analysisSumLabel.setSizePolicy(sizePolicy5)
        self.analysisSumLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.analysisSumLabel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.imageListWidget = QListWidget(self.analysisPage)
        self.imageListWidget.setObjectName(u"imageListWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.imageListWidget.sizePolicy().hasHeightForWidth())
        self.imageListWidget.setSizePolicy(sizePolicy6)
        self.imageListWidget.setMinimumSize(QSize(350, 0))
        self.imageListWidget.setMaximumSize(QSize(350, 16777215))
        self.imageListWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.imageListWidget.setDefaultDropAction(Qt.MoveAction)
        self.imageListWidget.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.imageListWidget, 1, 0, 1, 1)

        self.addImgBtn = QPushButton(self.analysisPage)
        self.addImgBtn.setObjectName(u"addImgBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.addImgBtn.sizePolicy().hasHeightForWidth())
        self.addImgBtn.setSizePolicy(sizePolicy7)
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

        self.frame_2 = QFrame(self.analysisPage)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy8)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"")
        self.splitter.setOrientation(Qt.Vertical)
        self.frame_5 = QFrame(self.splitter)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(320, 0))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.configScrollArea = QScrollArea(self.frame_5)
        self.configScrollArea.setObjectName(u"configScrollArea")
        sizePolicy4.setHeightForWidth(self.configScrollArea.sizePolicy().hasHeightForWidth())
        self.configScrollArea.setSizePolicy(sizePolicy4)
        self.configScrollArea.setStyleSheet(u"QScrollArea#configScrollArea{\n"
"background-color: transparent\n"
"}")
        self.configScrollArea.setFrameShape(QFrame.NoFrame)
        self.configScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 306, 511))
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy9)
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget#scrollAreaWidgetContents {\n"
"	background-color: transparent\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.configFormLayout = QFormLayout()
        self.configFormLayout.setObjectName(u"configFormLayout")
        self.configFormLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.protocolLabel = QLabel(self.frame_3)
        self.protocolLabel.setObjectName(u"protocolLabel")

        self.configFormLayout.setWidget(0, QFormLayout.LabelRole, self.protocolLabel)

        self.protocolCB = QComboBox(self.frame_3)
        self.protocolCB.setObjectName(u"protocolCB")

        self.configFormLayout.setWidget(0, QFormLayout.FieldRole, self.protocolCB)

        self.centeringLabel = QLabel(self.frame_3)
        self.centeringLabel.setObjectName(u"centeringLabel")

        self.configFormLayout.setWidget(1, QFormLayout.LabelRole, self.centeringLabel)

        self.centeringCB = QComboBox(self.frame_3)
        self.centeringCB.setObjectName(u"centeringCB")

        self.configFormLayout.setWidget(1, QFormLayout.FieldRole, self.centeringCB)

        self.centeringConfigVL = QVBoxLayout()
        self.centeringConfigVL.setObjectName(u"centeringConfigVL")
        self.vertPosLabel = QLabel(self.frame_3)
        self.vertPosLabel.setObjectName(u"vertPosLabel")

        self.centeringConfigVL.addWidget(self.vertPosLabel)

        self.vertPosDSB = QDoubleSpinBox(self.frame_3)
        self.vertPosDSB.setObjectName(u"vertPosDSB")
        self.vertPosDSB.setMaximum(1.000000000000000)
        self.vertPosDSB.setSingleStep(0.050000000000000)
        self.vertPosDSB.setValue(0.500000000000000)

        self.centeringConfigVL.addWidget(self.vertPosDSB)

        self.horPosLabel = QLabel(self.frame_3)
        self.horPosLabel.setObjectName(u"horPosLabel")

        self.centeringConfigVL.addWidget(self.horPosLabel)

        self.horPosDSB = QDoubleSpinBox(self.frame_3)
        self.horPosDSB.setObjectName(u"horPosDSB")
        self.horPosDSB.setMaximum(1.000000000000000)
        self.horPosDSB.setSingleStep(0.050000000000000)
        self.horPosDSB.setValue(0.500000000000000)

        self.centeringConfigVL.addWidget(self.horPosDSB)


        self.configFormLayout.setLayout(2, QFormLayout.FieldRole, self.centeringConfigVL)

        self.normalizationLabel = QLabel(self.frame_3)
        self.normalizationLabel.setObjectName(u"normalizationLabel")

        self.configFormLayout.setWidget(3, QFormLayout.LabelRole, self.normalizationLabel)

        self.normalizationCB = QComboBox(self.frame_3)
        self.normalizationCB.setObjectName(u"normalizationCB")

        self.configFormLayout.setWidget(3, QFormLayout.FieldRole, self.normalizationCB)

        self.edgeDetLabel = QLabel(self.frame_3)
        self.edgeDetLabel.setObjectName(u"edgeDetLabel")

        self.configFormLayout.setWidget(4, QFormLayout.LabelRole, self.edgeDetLabel)

        self.edgeDetCB = QComboBox(self.frame_3)
        self.edgeDetCB.setObjectName(u"edgeDetCB")

        self.configFormLayout.setWidget(4, QFormLayout.FieldRole, self.edgeDetCB)

        self.edgeDetConfigVL = QVBoxLayout()
        self.edgeDetConfigVL.setObjectName(u"edgeDetConfigVL")
        self.edgeSmoothLabel = QLabel(self.frame_3)
        self.edgeSmoothLabel.setObjectName(u"edgeSmoothLabel")

        self.edgeDetConfigVL.addWidget(self.edgeSmoothLabel)

        self.edgeSmoothDSB = QDoubleSpinBox(self.frame_3)
        self.edgeSmoothDSB.setObjectName(u"edgeSmoothDSB")
        self.edgeSmoothDSB.setDecimals(3)
        self.edgeSmoothDSB.setMinimum(0.000000000000000)
        self.edgeSmoothDSB.setMaximum(1.000000000000000)
        self.edgeSmoothDSB.setSingleStep(0.005000000000000)

        self.edgeDetConfigVL.addWidget(self.edgeSmoothDSB)

        self.hillWinRatioLabel = QLabel(self.frame_3)
        self.hillWinRatioLabel.setObjectName(u"hillWinRatioLabel")

        self.edgeDetConfigVL.addWidget(self.hillWinRatioLabel)

        self.hillWinRatioDSB = QDoubleSpinBox(self.frame_3)
        self.hillWinRatioDSB.setObjectName(u"hillWinRatioDSB")
        self.hillWinRatioDSB.setMaximum(1.000000000000000)
        self.hillWinRatioDSB.setSingleStep(0.050000000000000)
        self.hillWinRatioDSB.setValue(0.150000000000000)

        self.edgeDetConfigVL.addWidget(self.hillWinRatioDSB)


        self.configFormLayout.setLayout(5, QFormLayout.FieldRole, self.edgeDetConfigVL)

        self.interpolationLabel = QLabel(self.frame_3)
        self.interpolationLabel.setObjectName(u"interpolationLabel")

        self.configFormLayout.setWidget(6, QFormLayout.LabelRole, self.interpolationLabel)

        self.interpolationCB = QComboBox(self.frame_3)
        self.interpolationCB.setObjectName(u"interpolationCB")

        self.configFormLayout.setWidget(6, QFormLayout.FieldRole, self.interpolationCB)

        self.interpolationConfigVL = QVBoxLayout()
        self.interpolationConfigVL.setObjectName(u"interpolationConfigVL")
        self.interpolationResLabel = QLabel(self.frame_3)
        self.interpolationResLabel.setObjectName(u"interpolationResLabel")

        self.interpolationConfigVL.addWidget(self.interpolationResLabel)

        self.interpolationResDSB = QDoubleSpinBox(self.frame_3)
        self.interpolationResDSB.setObjectName(u"interpolationResDSB")
        self.interpolationResDSB.setMinimum(0.100000000000000)
        self.interpolationResDSB.setSingleStep(0.100000000000000)

        self.interpolationConfigVL.addWidget(self.interpolationResDSB)


        self.configFormLayout.setLayout(7, QFormLayout.FieldRole, self.interpolationConfigVL)

        self.invertImageLabel = QLabel(self.frame_3)
        self.invertImageLabel.setObjectName(u"invertImageLabel")

        self.configFormLayout.setWidget(11, QFormLayout.LabelRole, self.invertImageLabel)

        self.invertImageCheckB = QCheckBox(self.frame_3)
        self.invertImageCheckB.setObjectName(u"invertImageCheckB")

        self.configFormLayout.setWidget(11, QFormLayout.FieldRole, self.invertImageCheckB)

        self.fffBeamLabel = QLabel(self.frame_3)
        self.fffBeamLabel.setObjectName(u"fffBeamLabel")

        self.configFormLayout.setWidget(10, QFormLayout.LabelRole, self.fffBeamLabel)

        self.fffBeamCheckB = QCheckBox(self.frame_3)
        self.fffBeamCheckB.setObjectName(u"fffBeamCheckB")

        self.configFormLayout.setWidget(10, QFormLayout.FieldRole, self.fffBeamCheckB)

        self.inFieldRatioLabel = QLabel(self.frame_3)
        self.inFieldRatioLabel.setObjectName(u"inFieldRatioLabel")

        self.configFormLayout.setWidget(8, QFormLayout.LabelRole, self.inFieldRatioLabel)

        self.inFieldRatioDSB = QDoubleSpinBox(self.frame_3)
        self.inFieldRatioDSB.setObjectName(u"inFieldRatioDSB")
        self.inFieldRatioDSB.setMaximum(1.000000000000000)
        self.inFieldRatioDSB.setSingleStep(0.100000000000000)
        self.inFieldRatioDSB.setValue(0.800000000000000)

        self.configFormLayout.setWidget(8, QFormLayout.FieldRole, self.inFieldRatioDSB)

        self.slopeExclRatioLabel = QLabel(self.frame_3)
        self.slopeExclRatioLabel.setObjectName(u"slopeExclRatioLabel")

        self.configFormLayout.setWidget(9, QFormLayout.LabelRole, self.slopeExclRatioLabel)

        self.slopeExclRatioDSB = QDoubleSpinBox(self.frame_3)
        self.slopeExclRatioDSB.setObjectName(u"slopeExclRatioDSB")
        self.slopeExclRatioDSB.setMaximum(1.000000000000000)
        self.slopeExclRatioDSB.setSingleStep(0.100000000000000)
        self.slopeExclRatioDSB.setValue(0.200000000000000)

        self.configFormLayout.setWidget(9, QFormLayout.FieldRole, self.slopeExclRatioDSB)

        self.groundLabel = QLabel(self.frame_3)
        self.groundLabel.setObjectName(u"groundLabel")

        self.configFormLayout.setWidget(12, QFormLayout.LabelRole, self.groundLabel)

        self.groundCheckB = QCheckBox(self.frame_3)
        self.groundCheckB.setObjectName(u"groundCheckB")
        self.groundCheckB.setChecked(True)

        self.configFormLayout.setWidget(12, QFormLayout.FieldRole, self.groundCheckB)


        self.verticalLayout_5.addLayout(self.configFormLayout)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.configScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_7.addWidget(self.configScrollArea)

        self.splitter.addWidget(self.frame_5)
        self.analysisOutcomeFrame = QFrame(self.splitter)
        self.analysisOutcomeFrame.setObjectName(u"analysisOutcomeFrame")
        self.analysisOutcomeFrame.setFrameShape(QFrame.NoFrame)
        self.analysisOutcomeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.analysisOutcomeFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.label_2 = QLabel(self.analysisOutcomeFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_6.addWidget(self.label_2)

        self.line_3 = QFrame(self.analysisOutcomeFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.outcomeLE = QLineEdit(self.analysisOutcomeFrame)
        self.outcomeLE.setObjectName(u"outcomeLE")
        self.outcomeLE.setMinimumSize(QSize(270, 0))
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

        self.verticalLayout_6.addWidget(self.outcomeLE)

        self.verticalSpacer_5 = QSpacerItem(10, 66, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.splitter.addWidget(self.analysisOutcomeFrame)

        self.verticalLayout_4.addWidget(self.splitter)


        self.gridLayout.addWidget(self.frame_2, 1, 3, 1, 1)

        self.stackedWidget.addWidget(self.analysisPage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(QFieldAnalysisWorksheet)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(QFieldAnalysisWorksheet)
    # setupUi

    def retranslateUi(self, QFieldAnalysisWorksheet):
        QFieldAnalysisWorksheet.setWindowTitle(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Form", None))
        self.analyzeBtn.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Analyze images", None))
        self.advancedViewBtn.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Advanced results", None))
        self.genReportBtn.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Generate report", None))
        self.importedImgLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Imported images", None))
        self.label.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Configuration</span></p></body></html>", None))
        self.analysisSumLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis summary</span></p></body></html>", None))
        self.addImgBtn.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Add image(s)", None))
        self.protocolLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Protocol:", None))
        self.centeringLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Centering:", None))
        self.vertPosLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Vertical Position:", None))
        self.horPosLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Horizontal Position:", None))
        self.normalizationLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Normalization:", None))
        self.edgeDetLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Edge detection:", None))
        self.edgeSmoothLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Edge smoothing ratio:", None))
        self.hillWinRatioLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Hill window ratio:", None))
        self.interpolationLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Interpolation:", None))
        self.interpolationResLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Interpolation resolution:", None))
        self.interpolationResDSB.setSuffix(QCoreApplication.translate("QFieldAnalysisWorksheet", u" mm", None))
        self.invertImageLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Invert image:", None))
        self.fffBeamLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"FFF beam:", None))
        self.inFieldRatioLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"In-field ratio:", None))
        self.slopeExclRatioLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Slope exclusion ratio:", None))
        self.groundLabel.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"Ground:", None))
        self.label_2.setText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis Outcome</span></p></body></html>", None))
        self.outcomeLE.setPlaceholderText(QCoreApplication.translate("QFieldAnalysisWorksheet", u"N/A", None))
    # retranslateUi

