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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_QWLutzWorksheet(object):
    def setupUi(self, QWLutzWorksheet):
        if not QWLutzWorksheet.objectName():
            QWLutzWorksheet.setObjectName(u"QWLutzWorksheet")
        QWLutzWorksheet.resize(875, 480)
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
        self.gridLayout.setHorizontalSpacing(30)
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
        font = QFont()
        font.setPointSize(13)
        self.importedImgLabel.setFont(font)

        self.gridLayout.addWidget(self.importedImgLabel, 0, 0, 1, 1)

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
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.addImgBtn.sizePolicy().hasHeightForWidth())
        self.addImgBtn.setSizePolicy(sizePolicy5)
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
"}")
        self.addImgBtn.setAutoDefault(False)

        self.gridLayout.addWidget(self.addImgBtn, 2, 0, 1, 1, Qt.AlignVCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.analysisSumLabel = QLabel(self.analysisPage)
        self.analysisSumLabel.setObjectName(u"analysisSumLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.analysisSumLabel.sizePolicy().hasHeightForWidth())
        self.analysisSumLabel.setSizePolicy(sizePolicy6)
        self.analysisSumLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.analysisSumLabel)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.analyzeBtn = QPushButton(self.analysisPage)
        self.analyzeBtn.setObjectName(u"analyzeBtn")
        sizePolicy5.setHeightForWidth(self.analyzeBtn.sizePolicy().hasHeightForWidth())
        self.analyzeBtn.setSizePolicy(sizePolicy5)
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

        self.horizontalLayout_3.addWidget(self.analyzeBtn, 0, Qt.AlignLeft)

        self.shiftInfoBtn = QPushButton(self.analysisPage)
        self.shiftInfoBtn.setObjectName(u"shiftInfoBtn")
        sizePolicy5.setHeightForWidth(self.shiftInfoBtn.sizePolicy().hasHeightForWidth())
        self.shiftInfoBtn.setSizePolicy(sizePolicy5)
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

        self.horizontalLayout_3.addWidget(self.shiftInfoBtn, 0, Qt.AlignLeft)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

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
        self.importedImgLabel.setText(QCoreApplication.translate("QWLutzWorksheet", u"Imported images", None))
        self.addImgBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"Add image(s)", None))
        self.analysisSumLabel.setText(QCoreApplication.translate("QWLutzWorksheet", u"<html><head/><body><p><span style=\" font-weight:700;\">Analysis summary</span></p></body></html>", None))
        self.analyzeBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"Analyze images", None))
        self.shiftInfoBtn.setText(QCoreApplication.translate("QWLutzWorksheet", u"View shift instructions", None))
    # retranslateUi

