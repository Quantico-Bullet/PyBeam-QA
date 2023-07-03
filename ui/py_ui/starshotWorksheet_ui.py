# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'starshotWorksheet.ui'
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
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_QStarshotWorksheet(object):
    def setupUi(self, QStarshotWorksheet):
        if not QStarshotWorksheet.objectName():
            QStarshotWorksheet.setObjectName(u"QStarshotWorksheet")
        QStarshotWorksheet.resize(1237, 480)
        self.verticalLayout = QVBoxLayout(QStarshotWorksheet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(QStarshotWorksheet)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
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
        self.toleranceDSB.setMaximum(3.000000000000000)
        self.toleranceDSB.setSingleStep(0.500000000000000)
        self.toleranceDSB.setValue(0.500000000000000)

        self.horizontalLayout_4.addWidget(self.toleranceDSB)


        self.configFormLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.cropLabel = QLabel(self.frame_2)
        self.cropLabel.setObjectName(u"cropLabel")

        self.configFormLayout.setWidget(1, QFormLayout.LabelRole, self.cropLabel)

        self.radiusSB = QDoubleSpinBox(self.frame_2)
        self.radiusSB.setObjectName(u"radiusSB")
        self.radiusSB.setMinimum(0.050000000000000)
        self.radiusSB.setMaximum(0.950000000000000)
        self.radiusSB.setSingleStep(0.050000000000000)
        self.radiusSB.setValue(0.850000000000000)

        self.configFormLayout.setWidget(1, QFormLayout.FieldRole, self.radiusSB)

        self.minPeakHeightLabel = QLabel(self.frame_2)
        self.minPeakHeightLabel.setObjectName(u"minPeakHeightLabel")

        self.configFormLayout.setWidget(2, QFormLayout.LabelRole, self.minPeakHeightLabel)

        self.miniPeakHeightDSB = QDoubleSpinBox(self.frame_2)
        self.miniPeakHeightDSB.setObjectName(u"miniPeakHeightDSB")
        self.miniPeakHeightDSB.setMinimum(0.050000000000000)
        self.miniPeakHeightDSB.setMaximum(0.950000000000000)
        self.miniPeakHeightDSB.setSingleStep(0.050000000000000)
        self.miniPeakHeightDSB.setValue(0.250000000000000)

        self.configFormLayout.setWidget(2, QFormLayout.FieldRole, self.miniPeakHeightDSB)

        self.recursiveSearchLabel = QLabel(self.frame_2)
        self.recursiveSearchLabel.setObjectName(u"recursiveSearchLabel")

        self.configFormLayout.setWidget(6, QFormLayout.LabelRole, self.recursiveSearchLabel)

        self.recursiveSearchCB = QCheckBox(self.frame_2)
        self.recursiveSearchCB.setObjectName(u"recursiveSearchCB")
        self.recursiveSearchCB.setChecked(True)

        self.configFormLayout.setWidget(6, QFormLayout.FieldRole, self.recursiveSearchCB)

        self.forceImageInversionLabel = QLabel(self.frame_2)
        self.forceImageInversionLabel.setObjectName(u"forceImageInversionLabel")

        self.configFormLayout.setWidget(7, QFormLayout.LabelRole, self.forceImageInversionLabel)

        self.forceInvertCB = QCheckBox(self.frame_2)
        self.forceInvertCB.setObjectName(u"forceInvertCB")

        self.configFormLayout.setWidget(7, QFormLayout.FieldRole, self.forceInvertCB)

        self.useFWHMLabel = QLabel(self.frame_2)
        self.useFWHMLabel.setObjectName(u"useFWHMLabel")

        self.configFormLayout.setWidget(5, QFormLayout.LabelRole, self.useFWHMLabel)

        self.useFWHMCB = QCheckBox(self.frame_2)
        self.useFWHMCB.setObjectName(u"useFWHMCB")
        self.useFWHMCB.setChecked(True)

        self.configFormLayout.setWidget(5, QFormLayout.FieldRole, self.useFWHMCB)

        self.SIDValueLabel = QLabel(self.frame_2)
        self.SIDValueLabel.setObjectName(u"SIDValueLabel")

        self.configFormLayout.setWidget(3, QFormLayout.LabelRole, self.SIDValueLabel)

        self.SIDValueCB = QComboBox(self.frame_2)
        self.SIDValueCB.setObjectName(u"SIDValueCB")

        self.configFormLayout.setWidget(3, QFormLayout.FieldRole, self.SIDValueCB)

        self.sIDConfigVL = QVBoxLayout()
        self.sIDConfigVL.setObjectName(u"sIDConfigVL")
        self.sIDLabel = QLabel(self.frame_2)
        self.sIDLabel.setObjectName(u"sIDLabel")

        self.sIDConfigVL.addWidget(self.sIDLabel)

        self.sIDDSB = QDoubleSpinBox(self.frame_2)
        self.sIDDSB.setObjectName(u"sIDDSB")
        self.sIDDSB.setDecimals(0)
        self.sIDDSB.setMinimum(1.000000000000000)
        self.sIDDSB.setMaximum(2000.000000000000000)
        self.sIDDSB.setSingleStep(100.000000000000000)
        self.sIDDSB.setValue(1000.000000000000000)

        self.sIDConfigVL.addWidget(self.sIDDSB)


        self.configFormLayout.setLayout(4, QFormLayout.FieldRole, self.sIDConfigVL)


        self.verticalLayout_4.addLayout(self.configFormLayout)

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

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.frame_2, 1, 3, 1, 1)

        self.mainActionsHL = QHBoxLayout()
        self.mainActionsHL.setSpacing(10)
        self.mainActionsHL.setObjectName(u"mainActionsHL")
        self.analyzeBtn = QPushButton(self.analysisPage)
        self.analyzeBtn.setObjectName(u"analyzeBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.analyzeBtn.sizePolicy().hasHeightForWidth())
        self.analyzeBtn.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.genReportBtn.sizePolicy().hasHeightForWidth())
        self.genReportBtn.setSizePolicy(sizePolicy2)
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.mainActionsHL.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.mainActionsHL, 2, 1, 1, 1)

        self.frame = QFrame(self.analysisPage)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.analysisSummaryLabel = QFrame(self.frame)
        self.analysisSummaryLabel.setObjectName(u"analysisSummaryLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.analysisSummaryLabel.sizePolicy().hasHeightForWidth())
        self.analysisSummaryLabel.setSizePolicy(sizePolicy4)
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

        self.verticalSpacer_4 = QSpacerItem(10, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

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
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analysisSumLabel = QLabel(self.analysisPage)
        self.analysisSumLabel.setObjectName(u"analysisSumLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.analysisSumLabel.sizePolicy().hasHeightForWidth())
        self.analysisSumLabel.setSizePolicy(sizePolicy5)
        self.analysisSumLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.analysisSumLabel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.imageListWidget = QListWidget(self.analysisPage)
        self.imageListWidget.setObjectName(u"imageListWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
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

        self.stackedWidget.addWidget(self.analysisPage)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(QStarshotWorksheet)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(QStarshotWorksheet)
    # setupUi

    def retranslateUi(self, QStarshotWorksheet):
        QStarshotWorksheet.setWindowTitle(QCoreApplication.translate("QStarshotWorksheet", u"Form", None))
        self.toleranceLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"Tolerance:", None))
        self.toleranceDSB.setSuffix(QCoreApplication.translate("QStarshotWorksheet", u" mm", None))
        self.cropLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"Radius:", None))
        self.minPeakHeightLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"Minimum peak height", None))
        self.recursiveSearchLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"Recursive search:", None))
        self.forceImageInversionLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"Force image inversion:", None))
        self.useFWHMLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"Use FWHM:", None))
        self.SIDValueLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"SID value:", None))
        self.sIDLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"SID:", None))
        self.sIDDSB.setSuffix(QCoreApplication.translate("QStarshotWorksheet", u" mm", None))
        self.label_2.setText(QCoreApplication.translate("QStarshotWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis Outcome</span></p></body></html>", None))
        self.outcomeLE.setPlaceholderText(QCoreApplication.translate("QStarshotWorksheet", u"N/A", None))
        self.analyzeBtn.setText(QCoreApplication.translate("QStarshotWorksheet", u"Analyze images", None))
        self.genReportBtn.setText(QCoreApplication.translate("QStarshotWorksheet", u"Generate report", None))
        self.importedImgLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"Imported images", None))
        self.label.setText(QCoreApplication.translate("QStarshotWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Configuration</span></p></body></html>", None))
        self.analysisSumLabel.setText(QCoreApplication.translate("QStarshotWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis summary</span></p></body></html>", None))
        self.addImgBtn.setText(QCoreApplication.translate("QStarshotWorksheet", u"Add image(s)", None))
    # retranslateUi

