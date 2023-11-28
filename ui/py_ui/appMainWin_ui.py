# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appMainWin.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(674, 621)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_1 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_1)

        self.mainStackWidget = QStackedWidget(self.centralwidget)
        self.mainStackWidget.setObjectName(u"mainStackWidget")
        self.mainStackWidget.setEnabled(True)
        self.linacQAPage = QWidget()
        self.linacQAPage.setObjectName(u"linacQAPage")
        self.verticalLayout_8 = QVBoxLayout(self.linacQAPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.currentPageTitle = QLabel(self.linacQAPage)
        self.currentPageTitle.setObjectName(u"currentPageTitle")
        font = QFont()
        font.setPointSize(16)
        self.currentPageTitle.setFont(font)

        self.verticalLayout_4.addWidget(self.currentPageTitle, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.navigationFrame = QFrame(self.linacQAPage)
        self.navigationFrame.setObjectName(u"navigationFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.navigationFrame.sizePolicy().hasHeightForWidth())
        self.navigationFrame.setSizePolicy(sizePolicy1)
        self.navigationFrame.setStyleSheet(u"QPushButton:!checked{\n"
"	background-color: rgb(82, 142, 122);\n"
"    min-width: 150px;\n"
"	min-height:25px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton#qaToolsBtn{\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius: 15px ;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#qaReportsBtn{\n"
"	border-radius: 0px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#devicesBtn{\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius: 15px ;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(52, 91, 78);\n"
"	font: bold;\n"
"}\n"
"")
        self.navigationFrame.setFrameShape(QFrame.NoFrame)
        self.navigationFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.navigationFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.qaToolsBtn = QPushButton(self.navigationFrame)
        self.navTabBtnGroup = QButtonGroup(MainWindow)
        self.navTabBtnGroup.setObjectName(u"navTabBtnGroup")
        self.navTabBtnGroup.addButton(self.qaToolsBtn)
        self.qaToolsBtn.setObjectName(u"qaToolsBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.qaToolsBtn.sizePolicy().hasHeightForWidth())
        self.qaToolsBtn.setSizePolicy(sizePolicy2)
        self.qaToolsBtn.setStyleSheet(u"")
        self.qaToolsBtn.setCheckable(True)
        self.qaToolsBtn.setChecked(True)

        self.horizontalLayout_2.addWidget(self.qaToolsBtn)

        self.qaReportsBtn = QPushButton(self.navigationFrame)
        self.navTabBtnGroup.addButton(self.qaReportsBtn)
        self.qaReportsBtn.setObjectName(u"qaReportsBtn")
        sizePolicy2.setHeightForWidth(self.qaReportsBtn.sizePolicy().hasHeightForWidth())
        self.qaReportsBtn.setSizePolicy(sizePolicy2)
        self.qaReportsBtn.setMinimumSize(QSize(162, 37))
        self.qaReportsBtn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.qaReportsBtn)

        self.devicesBtn = QPushButton(self.navigationFrame)
        self.navTabBtnGroup.addButton(self.devicesBtn)
        self.devicesBtn.setObjectName(u"devicesBtn")
        sizePolicy2.setHeightForWidth(self.devicesBtn.sizePolicy().hasHeightForWidth())
        self.devicesBtn.setSizePolicy(sizePolicy2)
        self.devicesBtn.setAutoFillBackground(False)
        self.devicesBtn.setCheckable(True)
        self.devicesBtn.setAutoDefault(False)
        self.devicesBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.devicesBtn)


        self.verticalLayout_4.addWidget(self.navigationFrame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.navigationStackedWidget = QStackedWidget(self.linacQAPage)
        self.navigationStackedWidget.setObjectName(u"navigationStackedWidget")
        sizePolicy.setHeightForWidth(self.navigationStackedWidget.sizePolicy().hasHeightForWidth())
        self.navigationStackedWidget.setSizePolicy(sizePolicy)
        self.QAToolsPage = QWidget()
        self.QAToolsPage.setObjectName(u"QAToolsPage")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.QAToolsPage.sizePolicy().hasHeightForWidth())
        self.QAToolsPage.setSizePolicy(sizePolicy3)
        self.verticalLayout_6 = QVBoxLayout(self.QAToolsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea = QScrollArea(self.QAToolsPage)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 614, 401))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.testListFrame = QFrame(self.scrollAreaWidgetContents)
        self.testListFrame.setObjectName(u"testListFrame")
        self.testListFrame.setStyleSheet(u"QFrame#photonCalib:hover {\n"
"	background-color: rgba(82, 142, 122,50);\n"
"}\n"
"\n"
"QFrame#electronCalib:hover {\n"
"	background-color: rgba(82, 142, 122,50);\n"
"}\n"
"\n"
"QFrame#winstonLutzAnalysis:hover {\n"
"	background-color: rgba(82, 142, 122,50);\n"
"}\n"
"\n"
"QFrame#planarImagingAnalysis:hover {\n"
"	background-color: rgba(82, 142, 122,50);\n"
"}\n"
"\n"
"QFrame#starshotAnalysis:hover {\n"
"	background-color: rgba(82, 142, 122,50);\n"
"}\n"
"\n"
"QFrame#fieldAnalysis:hover {\n"
"	background-color: rgba(82, 142, 122,50);\n"
"}\n"
"\n"
"QFrame#picketFence:hover {\n"
"	background-color: rgba(82, 142, 122,50);\n"
"}")
        self.testListFrame.setFrameShape(QFrame.NoFrame)
        self.testListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.testListFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.linacQALabel = QLabel(self.testListFrame)
        self.linacQALabel.setObjectName(u"linacQALabel")
        sizePolicy1.setHeightForWidth(self.linacQALabel.sizePolicy().hasHeightForWidth())
        self.linacQALabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.linacQALabel)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.photonCalib = QFrame(self.testListFrame)
        self.photonCalib.setObjectName(u"photonCalib")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.photonCalib.sizePolicy().hasHeightForWidth())
        self.photonCalib.setSizePolicy(sizePolicy4)
        self.photonCalib.setStyleSheet(u"")
        self.photonCalib.setFrameShape(QFrame.NoFrame)
        self.photonCalib.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.photonCalib)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, 0, 0)
        self.photonCalibIcon = QLabel(self.photonCalib)
        self.photonCalibIcon.setObjectName(u"photonCalibIcon")
        sizePolicy2.setHeightForWidth(self.photonCalibIcon.sizePolicy().hasHeightForWidth())
        self.photonCalibIcon.setSizePolicy(sizePolicy2)
        self.photonCalibIcon.setMaximumSize(QSize(32, 32))
        self.photonCalibIcon.setPixmap(QPixmap(u":/colorIcons/icons/module.png"))
        self.photonCalibIcon.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.photonCalibIcon, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.photonCalibLabel = QLabel(self.photonCalib)
        self.photonCalibLabel.setObjectName(u"photonCalibLabel")
        sizePolicy.setHeightForWidth(self.photonCalibLabel.sizePolicy().hasHeightForWidth())
        self.photonCalibLabel.setSizePolicy(sizePolicy)
        self.photonCalibLabel.setMinimumSize(QSize(0, 48))
        self.photonCalibLabel.setStyleSheet(u"border-bottom-color: rgb(82, 142, 122);\n"
"border-bottom-width: 1px;\n"
"border-style: solid;\n"
"")
        self.photonCalibLabel.setWordWrap(False)
        self.photonCalibLabel.setMargin(0)

        self.horizontalLayout_12.addWidget(self.photonCalibLabel)


        self.verticalLayout_5.addWidget(self.photonCalib)

        self.electronCalib = QFrame(self.testListFrame)
        self.electronCalib.setObjectName(u"electronCalib")
        self.electronCalib.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.electronCalib.sizePolicy().hasHeightForWidth())
        self.electronCalib.setSizePolicy(sizePolicy4)
        self.electronCalib.setStyleSheet(u"")
        self.electronCalib.setFrameShape(QFrame.NoFrame)
        self.electronCalib.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.electronCalib)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, 0, 0)
        self.dailyElectronIcon = QLabel(self.electronCalib)
        self.dailyElectronIcon.setObjectName(u"dailyElectronIcon")
        sizePolicy2.setHeightForWidth(self.dailyElectronIcon.sizePolicy().hasHeightForWidth())
        self.dailyElectronIcon.setSizePolicy(sizePolicy2)
        self.dailyElectronIcon.setMaximumSize(QSize(32, 32))
        self.dailyElectronIcon.setPixmap(QPixmap(u":/colorIcons/icons/module.png"))
        self.dailyElectronIcon.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.dailyElectronIcon, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.dailyElectronsLabel = QLabel(self.electronCalib)
        self.dailyElectronsLabel.setObjectName(u"dailyElectronsLabel")
        sizePolicy.setHeightForWidth(self.dailyElectronsLabel.sizePolicy().hasHeightForWidth())
        self.dailyElectronsLabel.setSizePolicy(sizePolicy)
        self.dailyElectronsLabel.setMinimumSize(QSize(0, 48))
        self.dailyElectronsLabel.setStyleSheet(u"border-bottom-color: rgb(82, 142, 122);\n"
"border-bottom-width: 1px;\n"
"border-style:solid;")

        self.horizontalLayout_13.addWidget(self.dailyElectronsLabel)


        self.verticalLayout_5.addWidget(self.electronCalib)

        self.planarImagingAnalysis = QFrame(self.testListFrame)
        self.planarImagingAnalysis.setObjectName(u"planarImagingAnalysis")
        sizePolicy4.setHeightForWidth(self.planarImagingAnalysis.sizePolicy().hasHeightForWidth())
        self.planarImagingAnalysis.setSizePolicy(sizePolicy4)
        self.planarImagingAnalysis.setFrameShape(QFrame.NoFrame)
        self.planarImagingAnalysis.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.planarImagingAnalysis)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, 0, 0)
        self.planarImagingIcon = QLabel(self.planarImagingAnalysis)
        self.planarImagingIcon.setObjectName(u"planarImagingIcon")
        sizePolicy2.setHeightForWidth(self.planarImagingIcon.sizePolicy().hasHeightForWidth())
        self.planarImagingIcon.setSizePolicy(sizePolicy2)
        self.planarImagingIcon.setMaximumSize(QSize(32, 32))
        self.planarImagingIcon.setPixmap(QPixmap(u":/colorIcons/icons/module.png"))
        self.planarImagingIcon.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.planarImagingIcon, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.planarImagingLabel = QLabel(self.planarImagingAnalysis)
        self.planarImagingLabel.setObjectName(u"planarImagingLabel")
        sizePolicy.setHeightForWidth(self.planarImagingLabel.sizePolicy().hasHeightForWidth())
        self.planarImagingLabel.setSizePolicy(sizePolicy)
        self.planarImagingLabel.setMinimumSize(QSize(0, 48))
        self.planarImagingLabel.setStyleSheet(u"border-bottom-color: rgb(82, 142, 122);\n"
"border-bottom-width: 1px;\n"
"border-style: solid;\n"
"")
        self.planarImagingLabel.setWordWrap(False)
        self.planarImagingLabel.setMargin(0)

        self.horizontalLayout_19.addWidget(self.planarImagingLabel)


        self.verticalLayout_5.addWidget(self.planarImagingAnalysis)

        self.winstonLutzAnalysis = QFrame(self.testListFrame)
        self.winstonLutzAnalysis.setObjectName(u"winstonLutzAnalysis")
        sizePolicy4.setHeightForWidth(self.winstonLutzAnalysis.sizePolicy().hasHeightForWidth())
        self.winstonLutzAnalysis.setSizePolicy(sizePolicy4)
        self.winstonLutzAnalysis.setFrameShape(QFrame.NoFrame)
        self.winstonLutzAnalysis.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.winstonLutzAnalysis)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, 0, 0)
        self.winstonLutzIcon = QLabel(self.winstonLutzAnalysis)
        self.winstonLutzIcon.setObjectName(u"winstonLutzIcon")
        sizePolicy2.setHeightForWidth(self.winstonLutzIcon.sizePolicy().hasHeightForWidth())
        self.winstonLutzIcon.setSizePolicy(sizePolicy2)
        self.winstonLutzIcon.setMaximumSize(QSize(32, 32))
        self.winstonLutzIcon.setPixmap(QPixmap(u":/colorIcons/icons/module.png"))
        self.winstonLutzIcon.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.winstonLutzIcon, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.winstonLutzLabel = QLabel(self.winstonLutzAnalysis)
        self.winstonLutzLabel.setObjectName(u"winstonLutzLabel")
        sizePolicy.setHeightForWidth(self.winstonLutzLabel.sizePolicy().hasHeightForWidth())
        self.winstonLutzLabel.setSizePolicy(sizePolicy)
        self.winstonLutzLabel.setMinimumSize(QSize(0, 48))
        self.winstonLutzLabel.setStyleSheet(u"border-bottom-color: rgb(82, 142, 122);\n"
"border-bottom-width: 1px;\n"
"border-style: solid;\n"
"")
        self.winstonLutzLabel.setWordWrap(False)
        self.winstonLutzLabel.setMargin(0)

        self.horizontalLayout_14.addWidget(self.winstonLutzLabel)


        self.verticalLayout_5.addWidget(self.winstonLutzAnalysis)

        self.picketFence = QFrame(self.testListFrame)
        self.picketFence.setObjectName(u"picketFence")
        sizePolicy4.setHeightForWidth(self.picketFence.sizePolicy().hasHeightForWidth())
        self.picketFence.setSizePolicy(sizePolicy4)
        self.picketFence.setFrameShape(QFrame.NoFrame)
        self.picketFence.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.picketFence)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, 0, 0)
        self.picketFenceIcon = QLabel(self.picketFence)
        self.picketFenceIcon.setObjectName(u"picketFenceIcon")
        sizePolicy2.setHeightForWidth(self.picketFenceIcon.sizePolicy().hasHeightForWidth())
        self.picketFenceIcon.setSizePolicy(sizePolicy2)
        self.picketFenceIcon.setMaximumSize(QSize(32, 32))
        self.picketFenceIcon.setPixmap(QPixmap(u":/colorIcons/icons/module.png"))
        self.picketFenceIcon.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.picketFenceIcon, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.picketFenceLabel = QLabel(self.picketFence)
        self.picketFenceLabel.setObjectName(u"picketFenceLabel")
        sizePolicy.setHeightForWidth(self.picketFenceLabel.sizePolicy().hasHeightForWidth())
        self.picketFenceLabel.setSizePolicy(sizePolicy)
        self.picketFenceLabel.setMinimumSize(QSize(0, 48))
        self.picketFenceLabel.setStyleSheet(u"border-bottom-color: rgb(82, 142, 122);\n"
"border-bottom-width: 1px;\n"
"border-style: solid;\n"
"")
        self.picketFenceLabel.setWordWrap(False)
        self.picketFenceLabel.setMargin(0)

        self.horizontalLayout_17.addWidget(self.picketFenceLabel)


        self.verticalLayout_5.addWidget(self.picketFence)

        self.starshotAnalysis = QFrame(self.testListFrame)
        self.starshotAnalysis.setObjectName(u"starshotAnalysis")
        sizePolicy4.setHeightForWidth(self.starshotAnalysis.sizePolicy().hasHeightForWidth())
        self.starshotAnalysis.setSizePolicy(sizePolicy4)
        self.starshotAnalysis.setFrameShape(QFrame.NoFrame)
        self.starshotAnalysis.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.starshotAnalysis)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, 0, 0)
        self.starshotIcon = QLabel(self.starshotAnalysis)
        self.starshotIcon.setObjectName(u"starshotIcon")
        sizePolicy2.setHeightForWidth(self.starshotIcon.sizePolicy().hasHeightForWidth())
        self.starshotIcon.setSizePolicy(sizePolicy2)
        self.starshotIcon.setMaximumSize(QSize(32, 32))
        self.starshotIcon.setPixmap(QPixmap(u":/colorIcons/icons/module.png"))
        self.starshotIcon.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.starshotIcon, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.starhshotLabel = QLabel(self.starshotAnalysis)
        self.starhshotLabel.setObjectName(u"starhshotLabel")
        sizePolicy.setHeightForWidth(self.starhshotLabel.sizePolicy().hasHeightForWidth())
        self.starhshotLabel.setSizePolicy(sizePolicy)
        self.starhshotLabel.setMinimumSize(QSize(0, 48))
        self.starhshotLabel.setStyleSheet(u"border-bottom-color: rgb(82, 142, 122);\n"
"border-bottom-width: 1px;\n"
"border-style: solid;\n"
"")
        self.starhshotLabel.setWordWrap(False)
        self.starhshotLabel.setMargin(0)

        self.horizontalLayout_18.addWidget(self.starhshotLabel)


        self.verticalLayout_5.addWidget(self.starshotAnalysis)

        self.fieldAnalysis = QFrame(self.testListFrame)
        self.fieldAnalysis.setObjectName(u"fieldAnalysis")
        sizePolicy4.setHeightForWidth(self.fieldAnalysis.sizePolicy().hasHeightForWidth())
        self.fieldAnalysis.setSizePolicy(sizePolicy4)
        self.fieldAnalysis.setFrameShape(QFrame.NoFrame)
        self.fieldAnalysis.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.fieldAnalysis)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, 0, 0)
        self.fieldAnalysisIcon = QLabel(self.fieldAnalysis)
        self.fieldAnalysisIcon.setObjectName(u"fieldAnalysisIcon")
        sizePolicy2.setHeightForWidth(self.fieldAnalysisIcon.sizePolicy().hasHeightForWidth())
        self.fieldAnalysisIcon.setSizePolicy(sizePolicy2)
        self.fieldAnalysisIcon.setMaximumSize(QSize(32, 32))
        self.fieldAnalysisIcon.setPixmap(QPixmap(u":/colorIcons/icons/module.png"))
        self.fieldAnalysisIcon.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.fieldAnalysisIcon, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.fieldAnalysisLabel = QLabel(self.fieldAnalysis)
        self.fieldAnalysisLabel.setObjectName(u"fieldAnalysisLabel")
        sizePolicy.setHeightForWidth(self.fieldAnalysisLabel.sizePolicy().hasHeightForWidth())
        self.fieldAnalysisLabel.setSizePolicy(sizePolicy)
        self.fieldAnalysisLabel.setMinimumSize(QSize(0, 48))
        self.fieldAnalysisLabel.setStyleSheet(u"border-bottom-color: rgb(82, 142, 122);\n"
"border-bottom-width: 1px;\n"
"border-style: solid;\n"
"")
        self.fieldAnalysisLabel.setWordWrap(False)
        self.fieldAnalysisLabel.setMargin(0)

        self.horizontalLayout_21.addWidget(self.fieldAnalysisLabel)


        self.verticalLayout_5.addWidget(self.fieldAnalysis)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.testListFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.navigationStackedWidget.addWidget(self.QAToolsPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.reportsPage.sizePolicy().hasHeightForWidth())
        self.reportsPage.setSizePolicy(sizePolicy5)
        self.verticalLayout_11 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.reportsPage)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_11.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.navigationStackedWidget.addWidget(self.reportsPage)
        self.devicesPage = QWidget()
        self.devicesPage.setObjectName(u"devicesPage")
        self.verticalLayout_10 = QVBoxLayout(self.devicesPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.devicesPage)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.navigationStackedWidget.addWidget(self.devicesPage)

        self.verticalLayout_4.addWidget(self.navigationStackedWidget)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.linacQAPage)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.mainStackWidget.addWidget(self.linacQAPage)
        self.initCalibPage = QWidget()
        self.initCalibPage.setObjectName(u"initCalibPage")
        self.gridLayout = QGridLayout(self.initCalibPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.leftGridSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.leftGridSpacer, 1, 0, 1, 1)

        self.middleBottomSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.middleBottomSpacer, 1, 2, 1, 1)

        self.mainGridLayout = QGridLayout()
        self.mainGridLayout.setObjectName(u"mainGridLayout")
        self.scrollArea_2 = QScrollArea(self.initCalibPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy6)
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 450, 371))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.siteDetails = QFormLayout()
        self.siteDetails.setObjectName(u"siteDetails")
        self.siteDetails.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.institutionLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.institutionLabel.setObjectName(u"institutionLabel")

        self.siteDetails.setWidget(0, QFormLayout.LabelRole, self.institutionLabel)

        self.institutionLE = QLineEdit(self.scrollAreaWidgetContents_2)
        self.institutionLE.setObjectName(u"institutionLE")
        sizePolicy4.setHeightForWidth(self.institutionLE.sizePolicy().hasHeightForWidth())
        self.institutionLE.setSizePolicy(sizePolicy4)

        self.siteDetails.setWidget(0, QFormLayout.FieldRole, self.institutionLE)

        self.userLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.userLabel.setObjectName(u"userLabel")

        self.siteDetails.setWidget(1, QFormLayout.LabelRole, self.userLabel)

        self.userLE = QLineEdit(self.scrollAreaWidgetContents_2)
        self.userLE.setObjectName(u"userLE")

        self.siteDetails.setWidget(1, QFormLayout.FieldRole, self.userLE)


        self.verticalLayout_9.addLayout(self.siteDetails)

        self.verticalSpacer_7 = QSpacerItem(400, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.treatmentUnitLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.treatmentUnitLabel.setObjectName(u"treatmentUnitLabel")
        sizePolicy4.setHeightForWidth(self.treatmentUnitLabel.sizePolicy().hasHeightForWidth())
        self.treatmentUnitLabel.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setPointSize(13)
        self.treatmentUnitLabel.setFont(font1)

        self.verticalLayout_9.addWidget(self.treatmentUnitLabel)

        self.treatmentUnitFL = QFormLayout()
        self.treatmentUnitFL.setObjectName(u"treatmentUnitFL")
        self.treatmentUnitFL.setHorizontalSpacing(6)
        self.treatmentUnitFL.setContentsMargins(-1, 9, -1, -1)
        self.unitNameLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.unitNameLabel.setObjectName(u"unitNameLabel")

        self.treatmentUnitFL.setWidget(0, QFormLayout.LabelRole, self.unitNameLabel)

        self.linacNameCB = QComboBox(self.scrollAreaWidgetContents_2)
        self.linacNameCB.setObjectName(u"linacNameCB")
        sizePolicy4.setHeightForWidth(self.linacNameCB.sizePolicy().hasHeightForWidth())
        self.linacNameCB.setSizePolicy(sizePolicy4)
        self.linacNameCB.setDuplicatesEnabled(False)

        self.treatmentUnitFL.setWidget(0, QFormLayout.FieldRole, self.linacNameCB)

        self.linacSerialNumLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.linacSerialNumLabel.setObjectName(u"linacSerialNumLabel")

        self.treatmentUnitFL.setWidget(1, QFormLayout.LabelRole, self.linacSerialNumLabel)

        self.linacSerialNumField = QLabel(self.scrollAreaWidgetContents_2)
        self.linacSerialNumField.setObjectName(u"linacSerialNumField")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.linacSerialNumField.sizePolicy().hasHeightForWidth())
        self.linacSerialNumField.setSizePolicy(sizePolicy7)

        self.treatmentUnitFL.setWidget(1, QFormLayout.FieldRole, self.linacSerialNumField)

        self.linacModelLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.linacModelLabel.setObjectName(u"linacModelLabel")

        self.treatmentUnitFL.setWidget(2, QFormLayout.LabelRole, self.linacModelLabel)

        self.linacModelField = QLabel(self.scrollAreaWidgetContents_2)
        self.linacModelField.setObjectName(u"linacModelField")
        sizePolicy7.setHeightForWidth(self.linacModelField.sizePolicy().hasHeightForWidth())
        self.linacModelField.setSizePolicy(sizePolicy7)

        self.treatmentUnitFL.setWidget(2, QFormLayout.FieldRole, self.linacModelField)

        self.linacManufacLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.linacManufacLabel.setObjectName(u"linacManufacLabel")

        self.treatmentUnitFL.setWidget(3, QFormLayout.LabelRole, self.linacManufacLabel)

        self.linacManufacField = QLabel(self.scrollAreaWidgetContents_2)
        self.linacManufacField.setObjectName(u"linacManufacField")
        sizePolicy7.setHeightForWidth(self.linacManufacField.sizePolicy().hasHeightForWidth())
        self.linacManufacField.setSizePolicy(sizePolicy7)

        self.treatmentUnitFL.setWidget(3, QFormLayout.FieldRole, self.linacManufacField)

        self.doseRateSpacer = QSpacerItem(140, 9, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.treatmentUnitFL.setItem(4, QFormLayout.LabelRole, self.doseRateSpacer)

        self.linacBeamsLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.linacBeamsLabel.setObjectName(u"linacBeamsLabel")
        self.linacBeamsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.treatmentUnitFL.setWidget(5, QFormLayout.LabelRole, self.linacBeamsLabel)

        self.linacBeamsField = QGridLayout()
        self.linacBeamsField.setObjectName(u"linacBeamsField")

        self.treatmentUnitFL.setLayout(5, QFormLayout.FieldRole, self.linacBeamsField)


        self.verticalLayout_9.addLayout(self.treatmentUnitFL)

        self.verticalSpacer_9 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_9)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.mainGridLayout.addWidget(self.scrollArea_2, 2, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(450, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainGridLayout.addItem(self.verticalSpacer_6, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.mainGridLayout.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.backBtn = QPushButton(self.initCalibPage)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy2)
        self.backBtn.setAutoFillBackground(False)
        self.backBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 20px;\n"
"    min-width: 40px;\n"
"	min-height: 40px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(82, 142, 122,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(82, 142, 122,122);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/colorIcons/icons/left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setIconSize(QSize(32, 32))

        self.mainGridLayout.addWidget(self.backBtn, 0, 0, 1, 1, Qt.AlignTop)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainGridLayout.addItem(self.verticalSpacer_5, 3, 1, 1, 1)

        self.calibPageTitle = QLabel(self.initCalibPage)
        self.calibPageTitle.setObjectName(u"calibPageTitle")
        sizePolicy2.setHeightForWidth(self.calibPageTitle.sizePolicy().hasHeightForWidth())
        self.calibPageTitle.setSizePolicy(sizePolicy2)
        self.calibPageTitle.setFont(font)

        self.mainGridLayout.addWidget(self.calibPageTitle, 0, 1, 1, 1, Qt.AlignHCenter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.calibStartBtn = QPushButton(self.initCalibPage)
        self.calibStartBtn.setObjectName(u"calibStartBtn")
        sizePolicy2.setHeightForWidth(self.calibStartBtn.sizePolicy().hasHeightForWidth())
        self.calibStartBtn.setSizePolicy(sizePolicy2)
        self.calibStartBtn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.calibStartBtn)

        self.loadQABtn = QPushButton(self.initCalibPage)
        self.loadQABtn.setObjectName(u"loadQABtn")
        sizePolicy2.setHeightForWidth(self.loadQABtn.sizePolicy().hasHeightForWidth())
        self.loadQABtn.setSizePolicy(sizePolicy2)
        self.loadQABtn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.loadQABtn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.mainGridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)


        self.gridLayout.addLayout(self.mainGridLayout, 0, 2, 1, 1)

        self.rightGridSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.rightGridSpacer, 1, 3, 1, 1)

        self.mainStackWidget.addWidget(self.initCalibPage)

        self.verticalLayout_2.addWidget(self.mainStackWidget)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainStackWidget.setCurrentIndex(1)
        self.devicesBtn.setDefault(False)
        self.navigationStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.currentPageTitle.setText(QCoreApplication.translate("MainWindow", u"QA Tools", None))
        self.qaToolsBtn.setText(QCoreApplication.translate("MainWindow", u"QA Tools", None))
        self.qaReportsBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.devicesBtn.setText(QCoreApplication.translate("MainWindow", u"Devices", None))
        self.linacQALabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Linac QA</span></p></body></html>", None))
        self.photonCalibIcon.setText("")
        self.photonCalibLabel.setText(QCoreApplication.translate("MainWindow", u"Photon output calibration", None))
        self.dailyElectronIcon.setText("")
        self.dailyElectronsLabel.setText(QCoreApplication.translate("MainWindow", u"Electron output calibration", None))
        self.planarImagingIcon.setText("")
        self.planarImagingLabel.setText(QCoreApplication.translate("MainWindow", u"Planar imaging analysis", None))
        self.winstonLutzIcon.setText("")
        self.winstonLutzLabel.setText(QCoreApplication.translate("MainWindow", u"Winston-Lutz analysis", None))
        self.picketFenceIcon.setText("")
        self.picketFenceLabel.setText(QCoreApplication.translate("MainWindow", u"Picket-fence analysis", None))
        self.starshotIcon.setText("")
        self.starhshotLabel.setText(QCoreApplication.translate("MainWindow", u"Star-shot analysis", None))
        self.fieldAnalysisIcon.setText("")
        self.fieldAnalysisLabel.setText(QCoreApplication.translate("MainWindow", u"Field analysis", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"No content here!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"No content here!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PyBeam QA - v0.1.0 (Copyright \u00a9 2023 Kagiso Lebang)  ", None))
        self.institutionLabel.setText(QCoreApplication.translate("MainWindow", u"Institution:", None))
        self.userLabel.setText(QCoreApplication.translate("MainWindow", u"User:", None))
        self.treatmentUnitLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Treatment Unit</span></p></body></html>", None))
        self.unitNameLabel.setText(QCoreApplication.translate("MainWindow", u"Unit name:", None))
        self.linacSerialNumLabel.setText(QCoreApplication.translate("MainWindow", u"Serial No:", None))
        self.linacSerialNumField.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.linacModelLabel.setText(QCoreApplication.translate("MainWindow", u"Model name:", None))
        self.linacModelField.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.linacManufacLabel.setText(QCoreApplication.translate("MainWindow", u"Manufacturer:", None))
        self.linacManufacField.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.linacBeamsLabel.setText(QCoreApplication.translate("MainWindow", u"Beams to calibrate:", None))
        self.backBtn.setText("")
        self.calibPageTitle.setText(QCoreApplication.translate("MainWindow", u"Page Title", None))
        self.calibStartBtn.setText(QCoreApplication.translate("MainWindow", u"Start new QA", None))
        self.loadQABtn.setText(QCoreApplication.translate("MainWindow", u"Load QA file", None))
        pass
    # retranslateUi

