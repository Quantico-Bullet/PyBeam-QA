# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'picketFenceWorksheet.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_QPicketFenceWorksheet(object):
    def setupUi(self, QPicketFenceWorksheet):
        if not QPicketFenceWorksheet.objectName():
            QPicketFenceWorksheet.setObjectName(u"QPicketFenceWorksheet")
        QPicketFenceWorksheet.resize(1236, 480)
        self.verticalLayout = QVBoxLayout(QPicketFenceWorksheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(QPicketFenceWorksheet)
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
        self.toleranceDSB.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.toleranceDSB.setDecimals(2)
        self.toleranceDSB.setMaximum(2.500000000000000)

        self.horizontalLayout_4.addWidget(self.toleranceDSB)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.mLCTypeLabel = QLabel(self.frame_2)
        self.mLCTypeLabel.setObjectName(u"mLCTypeLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.mLCTypeLabel)

        self.mlcTypeCB = QComboBox(self.frame_2)
        self.mlcTypeCB.setObjectName(u"mlcTypeCB")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mlcTypeCB)


        self.verticalLayout_4.addLayout(self.formLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

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

        self.mainActionsHL = QHBoxLayout()
        self.mainActionsHL.setSpacing(10)
        self.mainActionsHL.setObjectName(u"mainActionsHL")
        self.analyzeBtn = QPushButton(self.analysisPage)
        self.analyzeBtn.setObjectName(u"analyzeBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
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

        self.genReportBtn = QPushButton(self.analysisPage)
        self.genReportBtn.setObjectName(u"genReportBtn")
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

        self.mainActionsHL.addWidget(self.genReportBtn)


        self.gridLayout.addLayout(self.mainActionsHL, 2, 1, 1, 1)

        self.frame = QFrame(self.analysisPage)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.analysisSummaryLabel = QFrame(self.frame)
        self.analysisSummaryLabel.setObjectName(u"analysisSummaryLabel")
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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.analysisPage)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analysisSumLabel = QLabel(self.analysisPage)
        self.analysisSumLabel.setObjectName(u"analysisSumLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.analysisSumLabel.sizePolicy().hasHeightForWidth())
        self.analysisSumLabel.setSizePolicy(sizePolicy3)
        self.analysisSumLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.analysisSumLabel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.imageListWidget = QListWidget(self.analysisPage)
        self.imageListWidget.setObjectName(u"imageListWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.imageListWidget.sizePolicy().hasHeightForWidth())
        self.imageListWidget.setSizePolicy(sizePolicy4)
        self.imageListWidget.setMinimumSize(QSize(350, 0))
        self.imageListWidget.setMaximumSize(QSize(350, 16777215))
        self.imageListWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.imageListWidget.setDefaultDropAction(Qt.MoveAction)
        self.imageListWidget.setAlternatingRowColors(True)

        self.gridLayout.addWidget(self.imageListWidget, 1, 0, 1, 1)

        self.addImgBtn = QPushButton(self.analysisPage)
        self.addImgBtn.setObjectName(u"addImgBtn")
        sizePolicy1.setHeightForWidth(self.addImgBtn.sizePolicy().hasHeightForWidth())
        self.addImgBtn.setSizePolicy(sizePolicy1)
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
        self.label_2.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis Outcome</span></p></body></html>", None))
        self.outcomeLE.setPlaceholderText(QCoreApplication.translate("QPicketFenceWorksheet", u"N/A", None))
        self.analyzeBtn.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Analyze images", None))
        self.genReportBtn.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Generate report", None))
        self.importedImgLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Imported images", None))
        self.label.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Configuration</span></p></body></html>", None))
        self.analysisSumLabel.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis summary</span></p></body></html>", None))
        self.addImgBtn.setText(QCoreApplication.translate("QPicketFenceWorksheet", u"Add image(s)", None))
    # retranslateUi

