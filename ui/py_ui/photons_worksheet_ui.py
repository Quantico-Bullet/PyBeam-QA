# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'photons_worksheet.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_QPhotonsWorksheet(object):
    def setupUi(self, QPhotonsWorksheet):
        if not QPhotonsWorksheet.objectName():
            QPhotonsWorksheet.setObjectName(u"QPhotonsWorksheet")
        QPhotonsWorksheet.resize(1109, 704)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QPhotonsWorksheet.sizePolicy().hasHeightForWidth())
        QPhotonsWorksheet.setSizePolicy(sizePolicy)
        QPhotonsWorksheet.setFocusPolicy(Qt.NoFocus)
        QPhotonsWorksheet.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(QPhotonsWorksheet)
        self.gridLayout.setObjectName(u"gridLayout")
        self.worksheetGrid = QGridLayout()
        self.worksheetGrid.setObjectName(u"worksheetGrid")
        self.worksheetGrid.setHorizontalSpacing(30)
        self.worksheetGrid.setVerticalSpacing(20)
        self.worksheetGrid.setContentsMargins(0, -1, 6, -1)
        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.worksheetGrid.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.worksheetScrollArea = QScrollArea(QPhotonsWorksheet)
        self.worksheetScrollArea.setObjectName(u"worksheetScrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.worksheetScrollArea.sizePolicy().hasHeightForWidth())
        self.worksheetScrollArea.setSizePolicy(sizePolicy1)
        self.worksheetScrollArea.setMaximumSize(QSize(630, 16777215))
        self.worksheetScrollArea.setStyleSheet(u"")
        self.worksheetScrollArea.setFrameShape(QFrame.StyledPanel)
        self.worksheetScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 605, 2002))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sectionOneGB = QGroupBox(self.scrollAreaWidgetContents)
        self.sectionOneGB.setObjectName(u"sectionOneGB")
        self.sectionOneGB.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sectionOneGB.sizePolicy().hasHeightForWidth())
        self.sectionOneGB.setSizePolicy(sizePolicy3)
        self.sectionOneGB.setMinimumSize(QSize(0, 0))
        self.sectionOneGB.setMaximumSize(QSize(16777215, 16777215))
        self.sectionOneGB.setAutoFillBackground(False)
        self.sectionOneGB.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.sectionOneGB)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sectionOneFL = QFormLayout()
        self.sectionOneFL.setObjectName(u"sectionOneFL")
        self.sectionOneFL.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.sectionOneFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.sectionOneFL.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.linacNameLabel = QLabel(self.sectionOneGB)
        self.linacNameLabel.setObjectName(u"linacNameLabel")

        self.sectionOneFL.setWidget(0, QFormLayout.LabelRole, self.linacNameLabel)

        self.linacNameLE = QLineEdit(self.sectionOneGB)
        self.linacNameLE.setObjectName(u"linacNameLE")
        sizePolicy2.setHeightForWidth(self.linacNameLE.sizePolicy().hasHeightForWidth())
        self.linacNameLE.setSizePolicy(sizePolicy2)
        self.linacNameLE.setMinimumSize(QSize(350, 0))
        self.linacNameLE.setClearButtonEnabled(True)

        self.sectionOneFL.setWidget(0, QFormLayout.FieldRole, self.linacNameLE)

        self.nomAccPotLabel = QLabel(self.sectionOneGB)
        self.nomAccPotLabel.setObjectName(u"nomAccPotLabel")

        self.sectionOneFL.setWidget(1, QFormLayout.LabelRole, self.nomAccPotLabel)

        self.nomAccPotHL = QHBoxLayout()
        self.nomAccPotHL.setObjectName(u"nomAccPotHL")
        self.nomAccPotLE = QLineEdit(self.sectionOneGB)
        self.nomAccPotLE.setObjectName(u"nomAccPotLE")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.nomAccPotLE.sizePolicy().hasHeightForWidth())
        self.nomAccPotLE.setSizePolicy(sizePolicy4)
        self.nomAccPotLE.setMinimumSize(QSize(0, 0))
        self.nomAccPotLE.setMaximumSize(QSize(100, 16777215))
        self.nomAccPotLE.setMouseTracking(False)
        self.nomAccPotLE.setFocusPolicy(Qt.ClickFocus)
        self.nomAccPotLE.setCursorPosition(0)
        self.nomAccPotLE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nomAccPotLE.setReadOnly(False)
        self.nomAccPotLE.setClearButtonEnabled(False)

        self.nomAccPotHL.addWidget(self.nomAccPotLE)

        self.nomAccPotUnit = QLabel(self.sectionOneGB)
        self.nomAccPotUnit.setObjectName(u"nomAccPotUnit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.nomAccPotUnit.sizePolicy().hasHeightForWidth())
        self.nomAccPotUnit.setSizePolicy(sizePolicy5)

        self.nomAccPotHL.addWidget(self.nomAccPotUnit)


        self.sectionOneFL.setLayout(1, QFormLayout.FieldRole, self.nomAccPotHL)

        self.nomDoseRateLabel = QLabel(self.sectionOneGB)
        self.nomDoseRateLabel.setObjectName(u"nomDoseRateLabel")

        self.sectionOneFL.setWidget(2, QFormLayout.LabelRole, self.nomDoseRateLabel)

        self.nomDoseRateHL = QHBoxLayout()
        self.nomDoseRateHL.setObjectName(u"nomDoseRateHL")
        self.nomDoseRateLE = QLineEdit(self.sectionOneGB)
        self.nomDoseRateLE.setObjectName(u"nomDoseRateLE")
        sizePolicy2.setHeightForWidth(self.nomDoseRateLE.sizePolicy().hasHeightForWidth())
        self.nomDoseRateLE.setSizePolicy(sizePolicy2)
        self.nomDoseRateLE.setMaximumSize(QSize(100, 16777215))

        self.nomDoseRateHL.addWidget(self.nomDoseRateLE)

        self.nomDoseRateUnit = QLabel(self.sectionOneGB)
        self.nomDoseRateUnit.setObjectName(u"nomDoseRateUnit")

        self.nomDoseRateHL.addWidget(self.nomDoseRateUnit)


        self.sectionOneFL.setLayout(2, QFormLayout.FieldRole, self.nomDoseRateHL)

        self.beamQualityLabel = QLabel(self.sectionOneGB)
        self.beamQualityLabel.setObjectName(u"beamQualityLabel")

        self.sectionOneFL.setWidget(3, QFormLayout.LabelRole, self.beamQualityLabel)

        self.beamQualityLE = QLineEdit(self.sectionOneGB)
        self.beamQualityLE.setObjectName(u"beamQualityLE")
        self.beamQualityLE.setMinimumSize(QSize(0, 0))
        self.beamQualityLE.setMaximumSize(QSize(100, 16777215))

        self.sectionOneFL.setWidget(3, QFormLayout.FieldRole, self.beamQualityLE)

        self.calibSetupLabel = QLabel(self.sectionOneGB)
        self.calibSetupLabel.setObjectName(u"calibSetupLabel")

        self.sectionOneFL.setWidget(4, QFormLayout.LabelRole, self.calibSetupLabel)

        self.calSetupHL = QHBoxLayout()
        self.calSetupHL.setObjectName(u"calSetupHL")
        self.ssdRadioButton = QRadioButton(self.sectionOneGB)
        self.calibSetupGroup = QButtonGroup(QPhotonsWorksheet)
        self.calibSetupGroup.setObjectName(u"calibSetupGroup")
        self.calibSetupGroup.addButton(self.ssdRadioButton)
        self.ssdRadioButton.setObjectName(u"ssdRadioButton")
        self.ssdRadioButton.setChecked(True)
        self.ssdRadioButton.setAutoExclusive(True)

        self.calSetupHL.addWidget(self.ssdRadioButton)

        self.sadRadioButton = QRadioButton(self.sectionOneGB)
        self.calibSetupGroup.addButton(self.sadRadioButton)
        self.sadRadioButton.setObjectName(u"sadRadioButton")

        self.calSetupHL.addWidget(self.sadRadioButton)


        self.sectionOneFL.setLayout(4, QFormLayout.FieldRole, self.calSetupHL)

        self.refPhantomLabel = QLabel(self.sectionOneGB)
        self.refPhantomLabel.setObjectName(u"refPhantomLabel")

        self.sectionOneFL.setWidget(5, QFormLayout.LabelRole, self.refPhantomLabel)

        self.refPhantomComboB = QComboBox(self.sectionOneGB)
        self.refPhantomComboB.addItem("")
        self.refPhantomComboB.setObjectName(u"refPhantomComboB")
        self.refPhantomComboB.setMinimumSize(QSize(100, 0))

        self.sectionOneFL.setWidget(5, QFormLayout.FieldRole, self.refPhantomComboB)

        self.refFieldSizeLabel = QLabel(self.sectionOneGB)
        self.refFieldSizeLabel.setObjectName(u"refFieldSizeLabel")

        self.sectionOneFL.setWidget(6, QFormLayout.LabelRole, self.refFieldSizeLabel)

        self.refFieldSizeHL = QHBoxLayout()
        self.refFieldSizeHL.setObjectName(u"refFieldSizeHL")
        self.reffieldSizeComboB = QComboBox(self.sectionOneGB)
        self.reffieldSizeComboB.addItem("")
        self.reffieldSizeComboB.setObjectName(u"reffieldSizeComboB")
        sizePolicy2.setHeightForWidth(self.reffieldSizeComboB.sizePolicy().hasHeightForWidth())
        self.reffieldSizeComboB.setSizePolicy(sizePolicy2)
        self.reffieldSizeComboB.setMinimumSize(QSize(100, 0))
        self.reffieldSizeComboB.setMaximumSize(QSize(100, 16777215))

        self.refFieldSizeHL.addWidget(self.reffieldSizeComboB)

        self.fieldSizeUnit = QLabel(self.sectionOneGB)
        self.fieldSizeUnit.setObjectName(u"fieldSizeUnit")

        self.refFieldSizeHL.addWidget(self.fieldSizeUnit)


        self.sectionOneFL.setLayout(6, QFormLayout.FieldRole, self.refFieldSizeHL)

        self.refDepthLabel = QLabel(self.sectionOneGB)
        self.refDepthLabel.setObjectName(u"refDepthLabel")

        self.sectionOneFL.setWidget(7, QFormLayout.LabelRole, self.refDepthLabel)

        self.refDepthHL = QHBoxLayout()
        self.refDepthHL.setObjectName(u"refDepthHL")
        self.refDepthComboB = QComboBox(self.sectionOneGB)
        self.refDepthComboB.addItem("")
        self.refDepthComboB.addItem("")
        self.refDepthComboB.setObjectName(u"refDepthComboB")
        sizePolicy2.setHeightForWidth(self.refDepthComboB.sizePolicy().hasHeightForWidth())
        self.refDepthComboB.setSizePolicy(sizePolicy2)
        self.refDepthComboB.setMinimumSize(QSize(100, 0))

        self.refDepthHL.addWidget(self.refDepthComboB)

        self.refDepthUnit = QLabel(self.sectionOneGB)
        self.refDepthUnit.setObjectName(u"refDepthUnit")

        self.refDepthHL.addWidget(self.refDepthUnit)


        self.sectionOneFL.setLayout(7, QFormLayout.FieldRole, self.refDepthHL)

        self.refDistanceLabel = QLabel(self.sectionOneGB)
        self.refDistanceLabel.setObjectName(u"refDistanceLabel")

        self.sectionOneFL.setWidget(8, QFormLayout.LabelRole, self.refDistanceLabel)

        self.refDistanceHL = QHBoxLayout()
        self.refDistanceHL.setObjectName(u"refDistanceHL")
        self.refDistanceLE = QLineEdit(self.sectionOneGB)
        self.refDistanceLE.setObjectName(u"refDistanceLE")
        sizePolicy2.setHeightForWidth(self.refDistanceLE.sizePolicy().hasHeightForWidth())
        self.refDistanceLE.setSizePolicy(sizePolicy2)
        self.refDistanceLE.setMinimumSize(QSize(100, 0))
        self.refDistanceLE.setMaximumSize(QSize(100, 16777215))
        self.refDistanceLE.setInputMethodHints(Qt.ImhDigitsOnly)

        self.refDistanceHL.addWidget(self.refDistanceLE)

        self.refDistanceUnit = QLabel(self.sectionOneGB)
        self.refDistanceUnit.setObjectName(u"refDistanceUnit")

        self.refDistanceHL.addWidget(self.refDistanceUnit)


        self.sectionOneFL.setLayout(8, QFormLayout.FieldRole, self.refDistanceHL)


        self.verticalLayout_2.addLayout(self.sectionOneFL)


        self.verticalLayout.addWidget(self.sectionOneGB)

        self.sectionTwoGB = QGroupBox(self.scrollAreaWidgetContents)
        self.sectionTwoGB.setObjectName(u"sectionTwoGB")
        self.verticalLayout_4 = QVBoxLayout(self.sectionTwoGB)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sectionTwoFL = QFormLayout()
        self.sectionTwoFL.setObjectName(u"sectionTwoFL")
        self.sectionTwoFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.ionChamberModelLabel = QLabel(self.sectionTwoGB)
        self.ionChamberModelLabel.setObjectName(u"ionChamberModelLabel")

        self.sectionTwoFL.setWidget(0, QFormLayout.LabelRole, self.ionChamberModelLabel)

        self.IonChamberModelComboB = QComboBox(self.sectionTwoGB)
        self.IonChamberModelComboB.setObjectName(u"IonChamberModelComboB")
        sizePolicy2.setHeightForWidth(self.IonChamberModelComboB.sizePolicy().hasHeightForWidth())
        self.IonChamberModelComboB.setSizePolicy(sizePolicy2)
        self.IonChamberModelComboB.setMinimumSize(QSize(200, 0))
        self.IonChamberModelComboB.setMaximumSize(QSize(300, 16777215))
        self.IonChamberModelComboB.setStyleSheet(u"combobox-popup: 0;")
        self.IonChamberModelComboB.setEditable(False)
        self.IonChamberModelComboB.setMaxVisibleItems(10)
        self.IonChamberModelComboB.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.IonChamberModelComboB.setFrame(True)

        self.sectionTwoFL.setWidget(0, QFormLayout.FieldRole, self.IonChamberModelComboB)

        self.chamberSerialNoLabel = QLabel(self.sectionTwoGB)
        self.chamberSerialNoLabel.setObjectName(u"chamberSerialNoLabel")

        self.sectionTwoFL.setWidget(1, QFormLayout.LabelRole, self.chamberSerialNoLabel)

        self.chamberSerialNoLE = QLineEdit(self.sectionTwoGB)
        self.chamberSerialNoLE.setObjectName(u"chamberSerialNoLE")
        sizePolicy2.setHeightForWidth(self.chamberSerialNoLE.sizePolicy().hasHeightForWidth())
        self.chamberSerialNoLE.setSizePolicy(sizePolicy2)
        self.chamberSerialNoLE.setMinimumSize(QSize(175, 0))
        self.chamberSerialNoLE.setMaximumSize(QSize(175, 16777215))

        self.sectionTwoFL.setWidget(1, QFormLayout.FieldRole, self.chamberSerialNoLE)

        self.calibFactorLabel = QLabel(self.sectionTwoGB)
        self.calibFactorLabel.setObjectName(u"calibFactorLabel")

        self.sectionTwoFL.setWidget(2, QFormLayout.LabelRole, self.calibFactorLabel)

        self.calibFactHL = QHBoxLayout()
        self.calibFactHL.setObjectName(u"calibFactHL")
        self.calibFactorLE = QLineEdit(self.sectionTwoGB)
        self.calibFactorLE.setObjectName(u"calibFactorLE")
        sizePolicy2.setHeightForWidth(self.calibFactorLE.sizePolicy().hasHeightForWidth())
        self.calibFactorLE.setSizePolicy(sizePolicy2)
        self.calibFactorLE.setMinimumSize(QSize(100, 0))
        self.calibFactorLE.setMaximumSize(QSize(100, 16777215))

        self.calibFactHL.addWidget(self.calibFactorLE)

        self.calibFactorUnit = QLabel(self.sectionTwoGB)
        self.calibFactorUnit.setObjectName(u"calibFactorUnit")

        self.calibFactHL.addWidget(self.calibFactorUnit)


        self.sectionTwoFL.setLayout(2, QFormLayout.FieldRole, self.calibFactHL)

        self.calibLabLabel = QLabel(self.sectionTwoGB)
        self.calibLabLabel.setObjectName(u"calibLabLabel")

        self.sectionTwoFL.setWidget(3, QFormLayout.LabelRole, self.calibLabLabel)

        self.calibLabLE = QLineEdit(self.sectionTwoGB)
        self.calibLabLE.setObjectName(u"calibLabLE")
        sizePolicy2.setHeightForWidth(self.calibLabLE.sizePolicy().hasHeightForWidth())
        self.calibLabLE.setSizePolicy(sizePolicy2)
        self.calibLabLE.setMinimumSize(QSize(350, 0))
        self.calibLabLE.setMaximumSize(QSize(350, 16777215))

        self.sectionTwoFL.setWidget(3, QFormLayout.FieldRole, self.calibLabLE)

        self.chamberCalibDateLabel = QLabel(self.sectionTwoGB)
        self.chamberCalibDateLabel.setObjectName(u"chamberCalibDateLabel")

        self.sectionTwoFL.setWidget(4, QFormLayout.LabelRole, self.chamberCalibDateLabel)

        self.chamberCalibDE = QDateEdit(self.sectionTwoGB)
        self.chamberCalibDE.setObjectName(u"chamberCalibDE")
        sizePolicy2.setHeightForWidth(self.chamberCalibDE.sizePolicy().hasHeightForWidth())
        self.chamberCalibDE.setSizePolicy(sizePolicy2)
        self.chamberCalibDE.setMinimumSize(QSize(100, 0))
        self.chamberCalibDE.setCalendarPopup(True)

        self.sectionTwoFL.setWidget(4, QFormLayout.FieldRole, self.chamberCalibDE)

        self.chamberWallMatLabel = QLabel(self.sectionTwoGB)
        self.chamberWallMatLabel.setObjectName(u"chamberWallMatLabel")

        self.sectionTwoFL.setWidget(5, QFormLayout.LabelRole, self.chamberWallMatLabel)

        self.cWallFL = QFormLayout()
        self.cWallFL.setObjectName(u"cWallFL")
        self.cWallFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.cWallMaterialLE = QLabel(self.sectionTwoGB)
        self.cWallMaterialLE.setObjectName(u"cWallMaterialLE")

        self.cWallFL.setWidget(0, QFormLayout.LabelRole, self.cWallMaterialLE)

        self.cWallMatLE = QLineEdit(self.sectionTwoGB)
        self.cWallMatLE.setObjectName(u"cWallMatLE")
        sizePolicy2.setHeightForWidth(self.cWallMatLE.sizePolicy().hasHeightForWidth())
        self.cWallMatLE.setSizePolicy(sizePolicy2)
        self.cWallMatLE.setMinimumSize(QSize(175, 0))
        self.cWallMatLE.setMaximumSize(QSize(175, 16777215))
        self.cWallMatLE.setReadOnly(True)

        self.cWallFL.setWidget(0, QFormLayout.FieldRole, self.cWallMatLE)

        self.cWallThickLabel = QLabel(self.sectionTwoGB)
        self.cWallThickLabel.setObjectName(u"cWallThickLabel")

        self.cWallFL.setWidget(1, QFormLayout.LabelRole, self.cWallThickLabel)

        self.cWallThickHL = QHBoxLayout()
        self.cWallThickHL.setObjectName(u"cWallThickHL")
        self.cWallThickLE = QLineEdit(self.sectionTwoGB)
        self.cWallThickLE.setObjectName(u"cWallThickLE")
        sizePolicy2.setHeightForWidth(self.cWallThickLE.sizePolicy().hasHeightForWidth())
        self.cWallThickLE.setSizePolicy(sizePolicy2)
        self.cWallThickLE.setMinimumSize(QSize(100, 0))
        self.cWallThickLE.setMaximumSize(QSize(100, 16777215))
        self.cWallThickLE.setReadOnly(True)

        self.cWallThickHL.addWidget(self.cWallThickLE)

        self.cWallThickUnit = QLabel(self.sectionTwoGB)
        self.cWallThickUnit.setObjectName(u"cWallThickUnit")

        self.cWallThickHL.addWidget(self.cWallThickUnit)


        self.cWallFL.setLayout(1, QFormLayout.FieldRole, self.cWallThickHL)


        self.sectionTwoFL.setLayout(5, QFormLayout.FieldRole, self.cWallFL)

        self.wSleeveLabel = QLabel(self.sectionTwoGB)
        self.wSleeveLabel.setObjectName(u"wSleeveLabel")

        self.sectionTwoFL.setWidget(6, QFormLayout.LabelRole, self.wSleeveLabel)

        self.wSleeveFL = QFormLayout()
        self.wSleeveFL.setObjectName(u"wSleeveFL")
        self.wSleeveFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.sleeveMatLabel = QLabel(self.sectionTwoGB)
        self.sleeveMatLabel.setObjectName(u"sleeveMatLabel")

        self.wSleeveFL.setWidget(0, QFormLayout.LabelRole, self.sleeveMatLabel)

        self.wSleeveMatlLE = QLineEdit(self.sectionTwoGB)
        self.wSleeveMatlLE.setObjectName(u"wSleeveMatlLE")
        sizePolicy2.setHeightForWidth(self.wSleeveMatlLE.sizePolicy().hasHeightForWidth())
        self.wSleeveMatlLE.setSizePolicy(sizePolicy2)
        self.wSleeveMatlLE.setMinimumSize(QSize(175, 0))

        self.wSleeveFL.setWidget(0, QFormLayout.FieldRole, self.wSleeveMatlLE)

        self.wsSleeveThickLabel = QLabel(self.sectionTwoGB)
        self.wsSleeveThickLabel.setObjectName(u"wsSleeveThickLabel")

        self.wSleeveFL.setWidget(1, QFormLayout.LabelRole, self.wsSleeveThickLabel)

        self.wSleeveThickHL = QHBoxLayout()
        self.wSleeveThickHL.setObjectName(u"wSleeveThickHL")
        self.wSleeveThickLE = QLineEdit(self.sectionTwoGB)
        self.wSleeveThickLE.setObjectName(u"wSleeveThickLE")
        sizePolicy2.setHeightForWidth(self.wSleeveThickLE.sizePolicy().hasHeightForWidth())
        self.wSleeveThickLE.setSizePolicy(sizePolicy2)
        self.wSleeveThickLE.setMinimumSize(QSize(100, 0))
        self.wSleeveThickLE.setMaximumSize(QSize(100, 16777215))

        self.wSleeveThickHL.addWidget(self.wSleeveThickLE)

        self.wSleeveThickUnit = QLabel(self.sectionTwoGB)
        self.wSleeveThickUnit.setObjectName(u"wSleeveThickUnit")

        self.wSleeveThickHL.addWidget(self.wSleeveThickUnit)


        self.wSleeveFL.setLayout(1, QFormLayout.FieldRole, self.wSleeveThickHL)


        self.sectionTwoFL.setLayout(6, QFormLayout.FieldRole, self.wSleeveFL)

        self.pWinLabel = QLabel(self.sectionTwoGB)
        self.pWinLabel.setObjectName(u"pWinLabel")

        self.sectionTwoFL.setWidget(7, QFormLayout.LabelRole, self.pWinLabel)

        self.phantomWinFL = QFormLayout()
        self.phantomWinFL.setObjectName(u"phantomWinFL")
        self.phantomWinFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.phantomWinMatLabel = QLabel(self.sectionTwoGB)
        self.phantomWinMatLabel.setObjectName(u"phantomWinMatLabel")

        self.phantomWinFL.setWidget(0, QFormLayout.LabelRole, self.phantomWinMatLabel)

        self.pWinMatLabel = QLineEdit(self.sectionTwoGB)
        self.pWinMatLabel.setObjectName(u"pWinMatLabel")
        sizePolicy2.setHeightForWidth(self.pWinMatLabel.sizePolicy().hasHeightForWidth())
        self.pWinMatLabel.setSizePolicy(sizePolicy2)
        self.pWinMatLabel.setMinimumSize(QSize(175, 0))
        self.pWinMatLabel.setMaximumSize(QSize(175, 16777215))

        self.phantomWinFL.setWidget(0, QFormLayout.FieldRole, self.pWinMatLabel)

        self.pWinThickLabel = QLabel(self.sectionTwoGB)
        self.pWinThickLabel.setObjectName(u"pWinThickLabel")

        self.phantomWinFL.setWidget(1, QFormLayout.LabelRole, self.pWinThickLabel)

        self.pWinThickHL = QHBoxLayout()
        self.pWinThickHL.setObjectName(u"pWinThickHL")
        self.pWinThickLE = QLineEdit(self.sectionTwoGB)
        self.pWinThickLE.setObjectName(u"pWinThickLE")
        sizePolicy2.setHeightForWidth(self.pWinThickLE.sizePolicy().hasHeightForWidth())
        self.pWinThickLE.setSizePolicy(sizePolicy2)
        self.pWinThickLE.setMinimumSize(QSize(100, 0))
        self.pWinThickLE.setMaximumSize(QSize(100, 16777215))

        self.pWinThickHL.addWidget(self.pWinThickLE)

        self.pWinThickUnit = QLabel(self.sectionTwoGB)
        self.pWinThickUnit.setObjectName(u"pWinThickUnit")

        self.pWinThickHL.addWidget(self.pWinThickUnit)


        self.phantomWinFL.setLayout(1, QFormLayout.FieldRole, self.pWinThickHL)


        self.sectionTwoFL.setLayout(7, QFormLayout.FieldRole, self.phantomWinFL)

        self.calibQualityLabel = QLabel(self.sectionTwoGB)
        self.calibQualityLabel.setObjectName(u"calibQualityLabel")

        self.sectionTwoFL.setWidget(8, QFormLayout.LabelRole, self.calibQualityLabel)

        self.calibQualityHL = QHBoxLayout()
        self.calibQualityHL.setObjectName(u"calibQualityHL")
        self.cobaltRadioButton = QRadioButton(self.sectionTwoGB)
        self.beamQualityGroup = QButtonGroup(QPhotonsWorksheet)
        self.beamQualityGroup.setObjectName(u"beamQualityGroup")
        self.beamQualityGroup.addButton(self.cobaltRadioButton)
        self.cobaltRadioButton.setObjectName(u"cobaltRadioButton")
        self.cobaltRadioButton.setChecked(True)

        self.calibQualityHL.addWidget(self.cobaltRadioButton)

        self.photonBeamRadioButton = QRadioButton(self.sectionTwoGB)
        self.beamQualityGroup.addButton(self.photonBeamRadioButton)
        self.photonBeamRadioButton.setObjectName(u"photonBeamRadioButton")

        self.calibQualityHL.addWidget(self.photonBeamRadioButton)


        self.sectionTwoFL.setLayout(8, QFormLayout.FieldRole, self.calibQualityHL)

        self.refConditionsLabel = QLabel(self.sectionTwoGB)
        self.refConditionsLabel.setObjectName(u"refConditionsLabel")

        self.sectionTwoFL.setWidget(9, QFormLayout.LabelRole, self.refConditionsLabel)

        self.refConditionsFL = QFormLayout()
        self.refConditionsFL.setObjectName(u"refConditionsFL")
        self.refConditionsFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.refPressureLabel = QLabel(self.sectionTwoGB)
        self.refPressureLabel.setObjectName(u"refPressureLabel")

        self.refConditionsFL.setWidget(0, QFormLayout.LabelRole, self.refPressureLabel)

        self.refPressureHL = QHBoxLayout()
        self.refPressureHL.setObjectName(u"refPressureHL")
        self.refPressureLE = QLineEdit(self.sectionTwoGB)
        self.refPressureLE.setObjectName(u"refPressureLE")
        sizePolicy2.setHeightForWidth(self.refPressureLE.sizePolicy().hasHeightForWidth())
        self.refPressureLE.setSizePolicy(sizePolicy2)
        self.refPressureLE.setMinimumSize(QSize(100, 0))
        self.refPressureLE.setMaximumSize(QSize(100, 16777215))

        self.refPressureHL.addWidget(self.refPressureLE)

        self.refPressureUnit = QLabel(self.sectionTwoGB)
        self.refPressureUnit.setObjectName(u"refPressureUnit")

        self.refPressureHL.addWidget(self.refPressureUnit)


        self.refConditionsFL.setLayout(0, QFormLayout.FieldRole, self.refPressureHL)

        self.refTempLabel = QLabel(self.sectionTwoGB)
        self.refTempLabel.setObjectName(u"refTempLabel")

        self.refConditionsFL.setWidget(1, QFormLayout.LabelRole, self.refTempLabel)

        self.refTempHL = QHBoxLayout()
        self.refTempHL.setObjectName(u"refTempHL")
        self.refTempLE = QLineEdit(self.sectionTwoGB)
        self.refTempLE.setObjectName(u"refTempLE")
        sizePolicy2.setHeightForWidth(self.refTempLE.sizePolicy().hasHeightForWidth())
        self.refTempLE.setSizePolicy(sizePolicy2)
        self.refTempLE.setMinimumSize(QSize(100, 0))
        self.refTempLE.setMaximumSize(QSize(100, 16777215))

        self.refTempHL.addWidget(self.refTempLE)

        self.refTempUnit = QLabel(self.sectionTwoGB)
        self.refTempUnit.setObjectName(u"refTempUnit")

        self.refTempHL.addWidget(self.refTempUnit)


        self.refConditionsFL.setLayout(1, QFormLayout.FieldRole, self.refTempHL)

        self.refHumidityLabel = QLabel(self.sectionTwoGB)
        self.refHumidityLabel.setObjectName(u"refHumidityLabel")

        self.refConditionsFL.setWidget(2, QFormLayout.LabelRole, self.refHumidityLabel)

        self.refHumidityHL = QHBoxLayout()
        self.refHumidityHL.setObjectName(u"refHumidityHL")
        self.refHumidityLE = QLineEdit(self.sectionTwoGB)
        self.refHumidityLE.setObjectName(u"refHumidityLE")
        sizePolicy2.setHeightForWidth(self.refHumidityLE.sizePolicy().hasHeightForWidth())
        self.refHumidityLE.setSizePolicy(sizePolicy2)
        self.refHumidityLE.setMinimumSize(QSize(100, 0))
        self.refHumidityLE.setMaximumSize(QSize(100, 16777215))

        self.refHumidityHL.addWidget(self.refHumidityLE)

        self.refHumidityUnit = QLabel(self.sectionTwoGB)
        self.refHumidityUnit.setObjectName(u"refHumidityUnit")

        self.refHumidityHL.addWidget(self.refHumidityUnit)


        self.refConditionsFL.setLayout(2, QFormLayout.FieldRole, self.refHumidityHL)


        self.sectionTwoFL.setLayout(9, QFormLayout.FieldRole, self.refConditionsFL)

        self.polarPotV1 = QLabel(self.sectionTwoGB)
        self.polarPotV1.setObjectName(u"polarPotV1")

        self.sectionTwoFL.setWidget(10, QFormLayout.LabelRole, self.polarPotV1)

        self.polarPotHL = QHBoxLayout()
        self.polarPotHL.setObjectName(u"polarPotHL")
        self.polarPotV1LE = QLineEdit(self.sectionTwoGB)
        self.polarPotV1LE.setObjectName(u"polarPotV1LE")
        sizePolicy2.setHeightForWidth(self.polarPotV1LE.sizePolicy().hasHeightForWidth())
        self.polarPotV1LE.setSizePolicy(sizePolicy2)
        self.polarPotV1LE.setMinimumSize(QSize(100, 0))
        self.polarPotV1LE.setMaximumSize(QSize(100, 16777215))

        self.polarPotHL.addWidget(self.polarPotV1LE)

        self.polarPotV1Unit = QLabel(self.sectionTwoGB)
        self.polarPotV1Unit.setObjectName(u"polarPotV1Unit")

        self.polarPotHL.addWidget(self.polarPotV1Unit)


        self.sectionTwoFL.setLayout(10, QFormLayout.FieldRole, self.polarPotHL)

        self.calibPolarLabel = QLabel(self.sectionTwoGB)
        self.calibPolarLabel.setObjectName(u"calibPolarLabel")

        self.sectionTwoFL.setWidget(11, QFormLayout.LabelRole, self.calibPolarLabel)

        self.calibPolarHL = QHBoxLayout()
        self.calibPolarHL.setObjectName(u"calibPolarHL")
        self.calPosPolarRadioButton = QRadioButton(self.sectionTwoGB)
        self.calibPolarityGroup = QButtonGroup(QPhotonsWorksheet)
        self.calibPolarityGroup.setObjectName(u"calibPolarityGroup")
        self.calibPolarityGroup.addButton(self.calPosPolarRadioButton)
        self.calPosPolarRadioButton.setObjectName(u"calPosPolarRadioButton")
        self.calPosPolarRadioButton.setChecked(True)

        self.calibPolarHL.addWidget(self.calPosPolarRadioButton)

        self.calNegPolarRadioButton = QRadioButton(self.sectionTwoGB)
        self.calibPolarityGroup.addButton(self.calNegPolarRadioButton)
        self.calNegPolarRadioButton.setObjectName(u"calNegPolarRadioButton")

        self.calibPolarHL.addWidget(self.calNegPolarRadioButton)


        self.sectionTwoFL.setLayout(11, QFormLayout.FieldRole, self.calibPolarHL)

        self.userPolarityLabel = QLabel(self.sectionTwoGB)
        self.userPolarityLabel.setObjectName(u"userPolarityLabel")

        self.sectionTwoFL.setWidget(12, QFormLayout.LabelRole, self.userPolarityLabel)

        self.userPolarHL = QHBoxLayout()
        self.userPolarHL.setObjectName(u"userPolarHL")
        self.userPosPolarRadioButton = QRadioButton(self.sectionTwoGB)
        self.userPolarityGroup = QButtonGroup(QPhotonsWorksheet)
        self.userPolarityGroup.setObjectName(u"userPolarityGroup")
        self.userPolarityGroup.addButton(self.userPosPolarRadioButton)
        self.userPosPolarRadioButton.setObjectName(u"userPosPolarRadioButton")
        self.userPosPolarRadioButton.setChecked(True)

        self.userPolarHL.addWidget(self.userPosPolarRadioButton)

        self.userNegPolarRadioButton = QRadioButton(self.sectionTwoGB)
        self.userPolarityGroup.addButton(self.userNegPolarRadioButton)
        self.userNegPolarRadioButton.setObjectName(u"userNegPolarRadioButton")

        self.userPolarHL.addWidget(self.userNegPolarRadioButton)


        self.sectionTwoFL.setLayout(12, QFormLayout.FieldRole, self.userPolarHL)

        self.corrPolarEffCheckB = QCheckBox(self.sectionTwoGB)
        self.corrPolarEffCheckB.setObjectName(u"corrPolarEffCheckB")
        self.corrPolarEffCheckB.setChecked(True)

        self.sectionTwoFL.setWidget(13, QFormLayout.FieldRole, self.corrPolarEffCheckB)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sectionTwoFL.setItem(14, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.electSectionLabel = QLabel(self.sectionTwoGB)
        self.electSectionLabel.setObjectName(u"electSectionLabel")

        self.sectionTwoFL.setWidget(15, QFormLayout.LabelRole, self.electSectionLabel)

        self.electModelLabel = QLabel(self.sectionTwoGB)
        self.electModelLabel.setObjectName(u"electModelLabel")

        self.sectionTwoFL.setWidget(16, QFormLayout.LabelRole, self.electModelLabel)

        self.electModelLE = QLineEdit(self.sectionTwoGB)
        self.electModelLE.setObjectName(u"electModelLE")
        sizePolicy2.setHeightForWidth(self.electModelLE.sizePolicy().hasHeightForWidth())
        self.electModelLE.setSizePolicy(sizePolicy2)
        self.electModelLE.setMinimumSize(QSize(175, 0))
        self.electModelLE.setMaximumSize(QSize(175, 16777215))

        self.sectionTwoFL.setWidget(16, QFormLayout.FieldRole, self.electModelLE)

        self.electSerialNoLabel = QLabel(self.sectionTwoGB)
        self.electSerialNoLabel.setObjectName(u"electSerialNoLabel")

        self.sectionTwoFL.setWidget(17, QFormLayout.LabelRole, self.electSerialNoLabel)

        self.electSerialNoLE = QLineEdit(self.sectionTwoGB)
        self.electSerialNoLE.setObjectName(u"electSerialNoLE")
        sizePolicy2.setHeightForWidth(self.electSerialNoLE.sizePolicy().hasHeightForWidth())
        self.electSerialNoLE.setSizePolicy(sizePolicy2)
        self.electSerialNoLE.setMinimumSize(QSize(175, 0))
        self.electSerialNoLE.setMaximumSize(QSize(175, 16777215))

        self.sectionTwoFL.setWidget(17, QFormLayout.FieldRole, self.electSerialNoLE)

        self.elecCalLabLabel = QLabel(self.sectionTwoGB)
        self.elecCalLabLabel.setObjectName(u"elecCalLabLabel")

        self.sectionTwoFL.setWidget(18, QFormLayout.LabelRole, self.elecCalLabLabel)

        self.electCalLabLE = QLineEdit(self.sectionTwoGB)
        self.electCalLabLE.setObjectName(u"electCalLabLE")
        self.electCalLabLE.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.electCalLabLE.sizePolicy().hasHeightForWidth())
        self.electCalLabLE.setSizePolicy(sizePolicy2)
        self.electCalLabLE.setMinimumSize(QSize(350, 0))
        self.electCalLabLE.setMaximumSize(QSize(350, 16777215))

        self.sectionTwoFL.setWidget(18, QFormLayout.FieldRole, self.electCalLabLE)

        self.electCalDateLabel = QLabel(self.sectionTwoGB)
        self.electCalDateLabel.setObjectName(u"electCalDateLabel")

        self.sectionTwoFL.setWidget(19, QFormLayout.LabelRole, self.electCalDateLabel)

        self.electCalDateDE = QDateEdit(self.sectionTwoGB)
        self.electCalDateDE.setObjectName(u"electCalDateDE")
        self.electCalDateDE.setEnabled(False)
        self.electCalDateDE.setMinimumSize(QSize(100, 0))
        self.electCalDateDE.setCalendarPopup(True)

        self.sectionTwoFL.setWidget(19, QFormLayout.FieldRole, self.electCalDateDE)

        self.electRangeSettLabel = QLabel(self.sectionTwoGB)
        self.electRangeSettLabel.setObjectName(u"electRangeSettLabel")

        self.sectionTwoFL.setWidget(20, QFormLayout.LabelRole, self.electRangeSettLabel)

        self.electRangeSettLE = QLineEdit(self.sectionTwoGB)
        self.electRangeSettLE.setObjectName(u"electRangeSettLE")
        sizePolicy4.setHeightForWidth(self.electRangeSettLE.sizePolicy().hasHeightForWidth())
        self.electRangeSettLE.setSizePolicy(sizePolicy4)
        self.electRangeSettLE.setMinimumSize(QSize(175, 0))
        self.electRangeSettLE.setMaximumSize(QSize(175, 16777215))

        self.sectionTwoFL.setWidget(20, QFormLayout.FieldRole, self.electRangeSettLE)

        self.calibSeparateFL = QFormLayout()
        self.calibSeparateFL.setObjectName(u"calibSeparateFL")
        self.calibSeparateLabel = QLabel(self.sectionTwoGB)
        self.calibSeparateLabel.setObjectName(u"calibSeparateLabel")

        self.calibSeparateFL.setWidget(0, QFormLayout.LabelRole, self.calibSeparateLabel)

        self.yesNoHL = QHBoxLayout()
        self.yesNoHL.setObjectName(u"yesNoHL")
        self.calibSepYesRadioButton = QRadioButton(self.sectionTwoGB)
        self.calibSeparateGroup = QButtonGroup(QPhotonsWorksheet)
        self.calibSeparateGroup.setObjectName(u"calibSeparateGroup")
        self.calibSeparateGroup.addButton(self.calibSepYesRadioButton)
        self.calibSepYesRadioButton.setObjectName(u"calibSepYesRadioButton")

        self.yesNoHL.addWidget(self.calibSepYesRadioButton)

        self.calibSepNoRadioButton = QRadioButton(self.sectionTwoGB)
        self.calibSeparateGroup.addButton(self.calibSepNoRadioButton)
        self.calibSepNoRadioButton.setObjectName(u"calibSepNoRadioButton")
        self.calibSepNoRadioButton.setChecked(True)

        self.yesNoHL.addWidget(self.calibSepNoRadioButton)


        self.calibSeparateFL.setLayout(0, QFormLayout.FieldRole, self.yesNoHL)


        self.sectionTwoFL.setLayout(21, QFormLayout.FieldRole, self.calibSeparateFL)


        self.verticalLayout_4.addLayout(self.sectionTwoFL)


        self.verticalLayout.addWidget(self.sectionTwoGB)

        self.sectionThreeGB = QGroupBox(self.scrollAreaWidgetContents)
        self.sectionThreeGB.setObjectName(u"sectionThreeGB")
        self.sectionThreeGB.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sectionThreeGB.sizePolicy().hasHeightForWidth())
        self.sectionThreeGB.setSizePolicy(sizePolicy6)
        self.sectionThreeGB.setFlat(False)
        self.sectionThreeGB.setCheckable(False)
        self.verticalLayout_6 = QVBoxLayout(self.sectionThreeGB)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sectionThreeFL = QFormLayout()
        self.sectionThreeFL.setObjectName(u"sectionThreeFL")
        self.sectionThreeFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.rawDosReadLabel = QLabel(self.sectionThreeGB)
        self.rawDosReadLabel.setObjectName(u"rawDosReadLabel")
        sizePolicy5.setHeightForWidth(self.rawDosReadLabel.sizePolicy().hasHeightForWidth())
        self.rawDosReadLabel.setSizePolicy(sizePolicy5)
        self.rawDosReadLabel.setTextFormat(Qt.MarkdownText)

        self.sectionThreeFL.setWidget(0, QFormLayout.LabelRole, self.rawDosReadLabel)

        self.rawDosReadHL = QHBoxLayout()
        self.rawDosReadHL.setObjectName(u"rawDosReadHL")
        self.rawDosReadLE = QLineEdit(self.sectionThreeGB)
        self.rawDosReadLE.setObjectName(u"rawDosReadLE")
        sizePolicy2.setHeightForWidth(self.rawDosReadLE.sizePolicy().hasHeightForWidth())
        self.rawDosReadLE.setSizePolicy(sizePolicy2)
        self.rawDosReadLE.setMinimumSize(QSize(100, 0))
        self.rawDosReadLE.setMaximumSize(QSize(100, 16777215))

        self.rawDosReadHL.addWidget(self.rawDosReadLE)

        self.rawDosReadUnit = QLabel(self.sectionThreeGB)
        self.rawDosReadUnit.setObjectName(u"rawDosReadUnit")

        self.rawDosReadHL.addWidget(self.rawDosReadUnit)


        self.sectionThreeFL.setLayout(0, QFormLayout.FieldRole, self.rawDosReadHL)

        self.corrLinacMULabel = QLabel(self.sectionThreeGB)
        self.corrLinacMULabel.setObjectName(u"corrLinacMULabel")

        self.sectionThreeFL.setWidget(1, QFormLayout.LabelRole, self.corrLinacMULabel)

        self.corrLinacMUHL = QHBoxLayout()
        self.corrLinacMUHL.setObjectName(u"corrLinacMUHL")
        self.corrLinacMULE = QLineEdit(self.sectionThreeGB)
        self.corrLinacMULE.setObjectName(u"corrLinacMULE")
        sizePolicy2.setHeightForWidth(self.corrLinacMULE.sizePolicy().hasHeightForWidth())
        self.corrLinacMULE.setSizePolicy(sizePolicy2)
        self.corrLinacMULE.setMinimumSize(QSize(100, 0))
        self.corrLinacMULE.setMaximumSize(QSize(100, 16777215))

        self.corrLinacMUHL.addWidget(self.corrLinacMULE)

        self.corrLinacMUUnit = QLabel(self.sectionThreeGB)
        self.corrLinacMUUnit.setObjectName(u"corrLinacMUUnit")

        self.corrLinacMUHL.addWidget(self.corrLinacMUUnit)


        self.sectionThreeFL.setLayout(1, QFormLayout.FieldRole, self.corrLinacMUHL)

        self.ratioReadMULabel = QLabel(self.sectionThreeGB)
        self.ratioReadMULabel.setObjectName(u"ratioReadMULabel")

        self.sectionThreeFL.setWidget(2, QFormLayout.LabelRole, self.ratioReadMULabel)

        self.ratioReadMUHL = QHBoxLayout()
        self.ratioReadMUHL.setObjectName(u"ratioReadMUHL")
        self.ratioReadMULE = QLineEdit(self.sectionThreeGB)
        self.ratioReadMULE.setObjectName(u"ratioReadMULE")
        sizePolicy2.setHeightForWidth(self.ratioReadMULE.sizePolicy().hasHeightForWidth())
        self.ratioReadMULE.setSizePolicy(sizePolicy2)
        self.ratioReadMULE.setMinimumSize(QSize(100, 0))
        self.ratioReadMULE.setMaximumSize(QSize(100, 16777215))

        self.ratioReadMUHL.addWidget(self.ratioReadMULE)

        self.ratioReadMUUnit = QLabel(self.sectionThreeGB)
        self.ratioReadMUUnit.setObjectName(u"ratioReadMUUnit")

        self.ratioReadMUHL.addWidget(self.ratioReadMUUnit)


        self.sectionThreeFL.setLayout(2, QFormLayout.FieldRole, self.ratioReadMUHL)

        self.tempPressCorrSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sectionThreeFL.setItem(3, QFormLayout.LabelRole, self.tempPressCorrSpacer)

        self.tempPressCorrLabel = QLabel(self.sectionThreeGB)
        self.tempPressCorrLabel.setObjectName(u"tempPressCorrLabel")

        self.sectionThreeFL.setWidget(4, QFormLayout.LabelRole, self.tempPressCorrLabel)

        self.tempPressCorrFL = QFormLayout()
        self.tempPressCorrFL.setObjectName(u"tempPressCorrFL")
        self.tempPressCorrFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.userPressureLabel = QLabel(self.sectionThreeGB)
        self.userPressureLabel.setObjectName(u"userPressureLabel")

        self.tempPressCorrFL.setWidget(0, QFormLayout.LabelRole, self.userPressureLabel)

        self.userPressureHL = QHBoxLayout()
        self.userPressureHL.setObjectName(u"userPressureHL")
        self.userPressureLE = QLineEdit(self.sectionThreeGB)
        self.userPressureLE.setObjectName(u"userPressureLE")
        sizePolicy2.setHeightForWidth(self.userPressureLE.sizePolicy().hasHeightForWidth())
        self.userPressureLE.setSizePolicy(sizePolicy2)
        self.userPressureLE.setMinimumSize(QSize(100, 0))
        self.userPressureLE.setMaximumSize(QSize(100, 16777215))

        self.userPressureHL.addWidget(self.userPressureLE)

        self.userPressureUnit = QLabel(self.sectionThreeGB)
        self.userPressureUnit.setObjectName(u"userPressureUnit")

        self.userPressureHL.addWidget(self.userPressureUnit)


        self.tempPressCorrFL.setLayout(0, QFormLayout.FieldRole, self.userPressureHL)

        self.userTempLabel = QLabel(self.sectionThreeGB)
        self.userTempLabel.setObjectName(u"userTempLabel")

        self.tempPressCorrFL.setWidget(1, QFormLayout.LabelRole, self.userTempLabel)

        self.userTempHL = QHBoxLayout()
        self.userTempHL.setObjectName(u"userTempHL")
        self.userTempLE = QLineEdit(self.sectionThreeGB)
        self.userTempLE.setObjectName(u"userTempLE")
        sizePolicy2.setHeightForWidth(self.userTempLE.sizePolicy().hasHeightForWidth())
        self.userTempLE.setSizePolicy(sizePolicy2)
        self.userTempLE.setMinimumSize(QSize(100, 0))
        self.userTempLE.setMaximumSize(QSize(100, 16777215))

        self.userTempHL.addWidget(self.userTempLE)

        self.userTempUnit = QLabel(self.sectionThreeGB)
        self.userTempUnit.setObjectName(u"userTempUnit")

        self.userTempHL.addWidget(self.userTempUnit)


        self.tempPressCorrFL.setLayout(1, QFormLayout.FieldRole, self.userTempHL)

        self.userHumidityLabel = QLabel(self.sectionThreeGB)
        self.userHumidityLabel.setObjectName(u"userHumidityLabel")

        self.tempPressCorrFL.setWidget(2, QFormLayout.LabelRole, self.userHumidityLabel)

        self.userHumidityHL = QHBoxLayout()
        self.userHumidityHL.setObjectName(u"userHumidityHL")
        self.userHumidityLE = QLineEdit(self.sectionThreeGB)
        self.userHumidityLE.setObjectName(u"userHumidityLE")
        sizePolicy2.setHeightForWidth(self.userHumidityLE.sizePolicy().hasHeightForWidth())
        self.userHumidityLE.setSizePolicy(sizePolicy2)
        self.userHumidityLE.setMinimumSize(QSize(100, 0))
        self.userHumidityLE.setMaximumSize(QSize(100, 16777215))

        self.userHumidityHL.addWidget(self.userHumidityLE)

        self.userHumidityUnit = QLabel(self.sectionThreeGB)
        self.userHumidityUnit.setObjectName(u"userHumidityUnit")

        self.userHumidityHL.addWidget(self.userHumidityUnit)


        self.tempPressCorrFL.setLayout(2, QFormLayout.FieldRole, self.userHumidityHL)


        self.sectionThreeFL.setLayout(4, QFormLayout.FieldRole, self.tempPressCorrFL)

        self.polarCorrSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sectionThreeFL.setItem(5, QFormLayout.LabelRole, self.polarCorrSpacer)

        self.polarCorrLabel = QLabel(self.sectionThreeGB)
        self.polarCorrLabel.setObjectName(u"polarCorrLabel")

        self.sectionThreeFL.setWidget(6, QFormLayout.LabelRole, self.polarCorrLabel)

        self.polarCorrFL = QFormLayout()
        self.polarCorrFL.setObjectName(u"polarCorrFL")
        self.polarCorrFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.readMPosLabel = QLabel(self.sectionThreeGB)
        self.readMPosLabel.setObjectName(u"readMPosLabel")

        self.polarCorrFL.setWidget(0, QFormLayout.LabelRole, self.readMPosLabel)

        self.readPosHL = QHBoxLayout()
        self.readPosHL.setObjectName(u"readPosHL")
        self.readMPosLE = QLineEdit(self.sectionThreeGB)
        self.readMPosLE.setObjectName(u"readMPosLE")
        sizePolicy2.setHeightForWidth(self.readMPosLE.sizePolicy().hasHeightForWidth())
        self.readMPosLE.setSizePolicy(sizePolicy2)
        self.readMPosLE.setMinimumSize(QSize(100, 0))
        self.readMPosLE.setMaximumSize(QSize(100, 16777215))

        self.readPosHL.addWidget(self.readMPosLE)

        self.readMPosUnit = QLabel(self.sectionThreeGB)
        self.readMPosUnit.setObjectName(u"readMPosUnit")

        self.readPosHL.addWidget(self.readMPosUnit)


        self.polarCorrFL.setLayout(0, QFormLayout.FieldRole, self.readPosHL)

        self.readMNegLabel = QLabel(self.sectionThreeGB)
        self.readMNegLabel.setObjectName(u"readMNegLabel")

        self.polarCorrFL.setWidget(1, QFormLayout.LabelRole, self.readMNegLabel)

        self.readNegHL = QHBoxLayout()
        self.readNegHL.setObjectName(u"readNegHL")
        self.readMNegLE = QLineEdit(self.sectionThreeGB)
        self.readMNegLE.setObjectName(u"readMNegLE")
        sizePolicy2.setHeightForWidth(self.readMNegLE.sizePolicy().hasHeightForWidth())
        self.readMNegLE.setSizePolicy(sizePolicy2)
        self.readMNegLE.setMinimumSize(QSize(100, 0))
        self.readMNegLE.setMaximumSize(QSize(100, 16777215))

        self.readNegHL.addWidget(self.readMNegLE)

        self.readMNegUnit = QLabel(self.sectionThreeGB)
        self.readMNegUnit.setObjectName(u"readMNegUnit")

        self.readNegHL.addWidget(self.readMNegUnit)


        self.polarCorrFL.setLayout(1, QFormLayout.FieldRole, self.readNegHL)


        self.sectionThreeFL.setLayout(6, QFormLayout.FieldRole, self.polarCorrFL)

        self.ionRecombCorrSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sectionThreeFL.setItem(7, QFormLayout.LabelRole, self.ionRecombCorrSpacer)

        self.ionRecombCorrLabel = QLabel(self.sectionThreeGB)
        self.ionRecombCorrLabel.setObjectName(u"ionRecombCorrLabel")

        self.sectionThreeFL.setWidget(8, QFormLayout.LabelRole, self.ionRecombCorrLabel)

        self.ionRecombCorrFL = QFormLayout()
        self.ionRecombCorrFL.setObjectName(u"ionRecombCorrFL")
        self.ionRecombCorrFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.ionRecombCorrFL.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.normVoltageLabel = QLabel(self.sectionThreeGB)
        self.normVoltageLabel.setObjectName(u"normVoltageLabel")

        self.ionRecombCorrFL.setWidget(0, QFormLayout.LabelRole, self.normVoltageLabel)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.normVoltageLE = QLineEdit(self.sectionThreeGB)
        self.normVoltageLE.setObjectName(u"normVoltageLE")
        sizePolicy2.setHeightForWidth(self.normVoltageLE.sizePolicy().hasHeightForWidth())
        self.normVoltageLE.setSizePolicy(sizePolicy2)
        self.normVoltageLE.setMinimumSize(QSize(100, 0))
        self.normVoltageLE.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_27.addWidget(self.normVoltageLE)

        self.normVoltageUnit = QLabel(self.sectionThreeGB)
        self.normVoltageUnit.setObjectName(u"normVoltageUnit")

        self.horizontalLayout_27.addWidget(self.normVoltageUnit)


        self.ionRecombCorrFL.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_27)

        self.normReadLabel = QLabel(self.sectionThreeGB)
        self.normReadLabel.setObjectName(u"normReadLabel")

        self.ionRecombCorrFL.setWidget(1, QFormLayout.LabelRole, self.normReadLabel)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.normReadLE = QLineEdit(self.sectionThreeGB)
        self.normReadLE.setObjectName(u"normReadLE")
        sizePolicy2.setHeightForWidth(self.normReadLE.sizePolicy().hasHeightForWidth())
        self.normReadLE.setSizePolicy(sizePolicy2)
        self.normReadLE.setMinimumSize(QSize(100, 0))
        self.normReadLE.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_28.addWidget(self.normReadLE)

        self.normReadUnit = QLabel(self.sectionThreeGB)
        self.normReadUnit.setObjectName(u"normReadUnit")

        self.horizontalLayout_28.addWidget(self.normReadUnit)


        self.ionRecombCorrFL.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_28)

        self.redVoltageLabel = QLabel(self.sectionThreeGB)
        self.redVoltageLabel.setObjectName(u"redVoltageLabel")

        self.ionRecombCorrFL.setWidget(2, QFormLayout.LabelRole, self.redVoltageLabel)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.redVoltageLE = QLineEdit(self.sectionThreeGB)
        self.redVoltageLE.setObjectName(u"redVoltageLE")
        sizePolicy2.setHeightForWidth(self.redVoltageLE.sizePolicy().hasHeightForWidth())
        self.redVoltageLE.setSizePolicy(sizePolicy2)
        self.redVoltageLE.setMinimumSize(QSize(100, 0))
        self.redVoltageLE.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_29.addWidget(self.redVoltageLE)

        self.redVoltageUnit = QLabel(self.sectionThreeGB)
        self.redVoltageUnit.setObjectName(u"redVoltageUnit")

        self.horizontalLayout_29.addWidget(self.redVoltageUnit)


        self.ionRecombCorrFL.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_29)

        self.redReadLabel = QLabel(self.sectionThreeGB)
        self.redReadLabel.setObjectName(u"redReadLabel")

        self.ionRecombCorrFL.setWidget(3, QFormLayout.LabelRole, self.redReadLabel)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.redReadLE = QLineEdit(self.sectionThreeGB)
        self.redReadLE.setObjectName(u"redReadLE")
        sizePolicy2.setHeightForWidth(self.redReadLE.sizePolicy().hasHeightForWidth())
        self.redReadLE.setSizePolicy(sizePolicy2)
        self.redReadLE.setMinimumSize(QSize(100, 0))
        self.redReadLE.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_30.addWidget(self.redReadLE)

        self.redReadUnit = QLabel(self.sectionThreeGB)
        self.redReadUnit.setObjectName(u"redReadUnit")

        self.horizontalLayout_30.addWidget(self.redReadUnit)


        self.ionRecombCorrFL.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_30)

        self.beamTypeLabel = QLabel(self.sectionThreeGB)
        self.beamTypeLabel.setObjectName(u"beamTypeLabel")

        self.ionRecombCorrFL.setWidget(4, QFormLayout.LabelRole, self.beamTypeLabel)

        self.beamTypeHL = QHBoxLayout()
        self.beamTypeHL.setObjectName(u"beamTypeHL")
        self.pulsedRadioButton = QRadioButton(self.sectionThreeGB)
        self.beamTypeGroup = QButtonGroup(QPhotonsWorksheet)
        self.beamTypeGroup.setObjectName(u"beamTypeGroup")
        self.beamTypeGroup.addButton(self.pulsedRadioButton)
        self.pulsedRadioButton.setObjectName(u"pulsedRadioButton")
        self.pulsedRadioButton.setChecked(True)
        self.pulsedRadioButton.setAutoExclusive(True)

        self.beamTypeHL.addWidget(self.pulsedRadioButton)

        self.pulsedScanRadioButton = QRadioButton(self.sectionThreeGB)
        self.beamTypeGroup.addButton(self.pulsedScanRadioButton)
        self.pulsedScanRadioButton.setObjectName(u"pulsedScanRadioButton")

        self.beamTypeHL.addWidget(self.pulsedScanRadioButton)


        self.ionRecombCorrFL.setLayout(4, QFormLayout.FieldRole, self.beamTypeHL)


        self.sectionThreeFL.setLayout(8, QFormLayout.FieldRole, self.ionRecombCorrFL)

        self.electmeterCorrLabel = QLabel(self.sectionThreeGB)
        self.electmeterCorrLabel.setObjectName(u"electmeterCorrLabel")

        self.sectionThreeFL.setWidget(10, QFormLayout.LabelRole, self.electmeterCorrLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.kElecLabel_2 = QLabel(self.sectionThreeGB)
        self.kElecLabel_2.setObjectName(u"kElecLabel_2")

        self.horizontalLayout.addWidget(self.kElecLabel_2)

        self.kElecLE_2 = QLineEdit(self.sectionThreeGB)
        self.kElecLE_2.setObjectName(u"kElecLE_2")
        sizePolicy2.setHeightForWidth(self.kElecLE_2.sizePolicy().hasHeightForWidth())
        self.kElecLE_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.kElecLE_2)


        self.sectionThreeFL.setLayout(10, QFormLayout.FieldRole, self.horizontalLayout)

        self.electmeterCorrSpacer = QWidget(self.sectionThreeGB)
        self.electmeterCorrSpacer.setObjectName(u"electmeterCorrSpacer")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.electmeterCorrSpacer.sizePolicy().hasHeightForWidth())
        self.electmeterCorrSpacer.setSizePolicy(sizePolicy7)
        self.electmeterCorrSpacer.setMinimumSize(QSize(20, 20))
        self.verticalLayout_7 = QVBoxLayout(self.electmeterCorrSpacer)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.sectionThreeFL.setWidget(9, QFormLayout.LabelRole, self.electmeterCorrSpacer)


        self.verticalLayout_6.addLayout(self.sectionThreeFL)


        self.verticalLayout.addWidget(self.sectionThreeGB)

        self.sectionFourGB = QGroupBox(self.scrollAreaWidgetContents)
        self.sectionFourGB.setObjectName(u"sectionFourGB")
        sizePolicy.setHeightForWidth(self.sectionFourGB.sizePolicy().hasHeightForWidth())
        self.sectionFourGB.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.sectionFourGB)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.depthDMaxFL = QFormLayout()
        self.depthDMaxFL.setObjectName(u"depthDMaxFL")
        self.depthDMaxFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.depthDMaxLabel = QLabel(self.sectionFourGB)
        self.depthDMaxLabel.setObjectName(u"depthDMaxLabel")

        self.depthDMaxFL.setWidget(0, QFormLayout.LabelRole, self.depthDMaxLabel)

        self.depthDMaxHL = QHBoxLayout()
        self.depthDMaxHL.setObjectName(u"depthDMaxHL")
        self.depthDMaxLE = QLineEdit(self.sectionFourGB)
        self.depthDMaxLE.setObjectName(u"depthDMaxLE")
        sizePolicy2.setHeightForWidth(self.depthDMaxLE.sizePolicy().hasHeightForWidth())
        self.depthDMaxLE.setSizePolicy(sizePolicy2)
        self.depthDMaxLE.setMinimumSize(QSize(100, 0))
        self.depthDMaxLE.setMaximumSize(QSize(100, 16777215))

        self.depthDMaxHL.addWidget(self.depthDMaxLE)

        self.depthDMaxUnit = QLabel(self.sectionFourGB)
        self.depthDMaxUnit.setObjectName(u"depthDMaxUnit")

        self.depthDMaxHL.addWidget(self.depthDMaxUnit)


        self.depthDMaxFL.setLayout(0, QFormLayout.FieldRole, self.depthDMaxHL)

        self.vSpacerSecFour = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.depthDMaxFL.setItem(1, QFormLayout.LabelRole, self.vSpacerSecFour)


        self.verticalLayout_3.addLayout(self.depthDMaxFL)

        self.setupSW = QStackedWidget(self.sectionFourGB)
        self.setupSW.setObjectName(u"setupSW")
        sizePolicy2.setHeightForWidth(self.setupSW.sizePolicy().hasHeightForWidth())
        self.setupSW.setSizePolicy(sizePolicy2)
        self.setupSW.setMinimumSize(QSize(100, 0))
        self.ssdPage = QWidget()
        self.ssdPage.setObjectName(u"ssdPage")
        sizePolicy2.setHeightForWidth(self.ssdPage.sizePolicy().hasHeightForWidth())
        self.ssdPage.setSizePolicy(sizePolicy2)
        self.verticalLayout_10 = QVBoxLayout(self.ssdPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.ssdPageVL = QVBoxLayout()
        self.ssdPageVL.setSpacing(10)
        self.ssdPageVL.setObjectName(u"ssdPageVL")
        self.ssdPageVL.setSizeConstraint(QLayout.SetMaximumSize)
        self.ssdSetupLabel = QLabel(self.ssdPage)
        self.ssdSetupLabel.setObjectName(u"ssdSetupLabel")
        sizePolicy5.setHeightForWidth(self.ssdSetupLabel.sizePolicy().hasHeightForWidth())
        self.ssdSetupLabel.setSizePolicy(sizePolicy5)

        self.ssdPageVL.addWidget(self.ssdSetupLabel)

        self.pddHL = QHBoxLayout()
        self.pddHL.setObjectName(u"pddHL")
        self.pddHL.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pddLabel = QLabel(self.ssdPage)
        self.pddLabel.setObjectName(u"pddLabel")
        sizePolicy.setHeightForWidth(self.pddLabel.sizePolicy().hasHeightForWidth())
        self.pddLabel.setSizePolicy(sizePolicy)

        self.pddHL.addWidget(self.pddLabel)

        self.pddLE = QLineEdit(self.ssdPage)
        self.pddLE.setObjectName(u"pddLE")
        sizePolicy.setHeightForWidth(self.pddLE.sizePolicy().hasHeightForWidth())
        self.pddLE.setSizePolicy(sizePolicy)
        self.pddLE.setMinimumSize(QSize(100, 0))
        self.pddLE.setMaximumSize(QSize(100, 16777215))

        self.pddHL.addWidget(self.pddLE)

        self.pddUnit = QLabel(self.ssdPage)
        self.pddUnit.setObjectName(u"pddUnit")
        sizePolicy.setHeightForWidth(self.pddUnit.sizePolicy().hasHeightForWidth())
        self.pddUnit.setSizePolicy(sizePolicy)

        self.pddHL.addWidget(self.pddUnit)


        self.ssdPageVL.addLayout(self.pddHL)


        self.verticalLayout_10.addLayout(self.ssdPageVL)

        self.setupSW.addWidget(self.ssdPage)
        self.sadPage = QWidget()
        self.sadPage.setObjectName(u"sadPage")
        sizePolicy2.setHeightForWidth(self.sadPage.sizePolicy().hasHeightForWidth())
        self.sadPage.setSizePolicy(sizePolicy2)
        self.verticalLayout_8 = QVBoxLayout(self.sadPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sadPageVL = QVBoxLayout()
        self.sadPageVL.setSpacing(10)
        self.sadPageVL.setObjectName(u"sadPageVL")
        self.sadPageVL.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.sadSetupLabel = QLabel(self.sadPage)
        self.sadSetupLabel.setObjectName(u"sadSetupLabel")
        sizePolicy5.setHeightForWidth(self.sadSetupLabel.sizePolicy().hasHeightForWidth())
        self.sadSetupLabel.setSizePolicy(sizePolicy5)

        self.sadPageVL.addWidget(self.sadSetupLabel)

        self.tmrHL = QHBoxLayout()
        self.tmrHL.setObjectName(u"tmrHL")
        self.tmrHL.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.tmrLabel = QLabel(self.sadPage)
        self.tmrLabel.setObjectName(u"tmrLabel")
        sizePolicy2.setHeightForWidth(self.tmrLabel.sizePolicy().hasHeightForWidth())
        self.tmrLabel.setSizePolicy(sizePolicy2)

        self.tmrHL.addWidget(self.tmrLabel)

        self.tmrLE = QLineEdit(self.sadPage)
        self.tmrLE.setObjectName(u"tmrLE")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tmrLE.sizePolicy().hasHeightForWidth())
        self.tmrLE.setSizePolicy(sizePolicy8)
        self.tmrLE.setMinimumSize(QSize(100, 0))
        self.tmrLE.setMaximumSize(QSize(100, 16777215))

        self.tmrHL.addWidget(self.tmrLE)

        self.tmrSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.tmrHL.addItem(self.tmrSpacer)


        self.sadPageVL.addLayout(self.tmrHL)


        self.verticalLayout_8.addLayout(self.sadPageVL)

        self.setupSW.addWidget(self.sadPage)

        self.verticalLayout_3.addWidget(self.setupSW)


        self.verticalLayout.addWidget(self.sectionFourGB)

        self.worksheetScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.worksheetGrid.addWidget(self.worksheetScrollArea, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.worksheetGrid.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.siteDataWidget = QWidget(QPhotonsWorksheet)
        self.siteDataWidget.setObjectName(u"siteDataWidget")
        sizePolicy2.setHeightForWidth(self.siteDataWidget.sizePolicy().hasHeightForWidth())
        self.siteDataWidget.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.siteDataWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.siteDataFL = QFormLayout()
        self.siteDataFL.setObjectName(u"siteDataFL")
        self.siteDataFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.institutionLabel = QLabel(self.siteDataWidget)
        self.institutionLabel.setObjectName(u"institutionLabel")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.institutionLabel.sizePolicy().hasHeightForWidth())
        self.institutionLabel.setSizePolicy(sizePolicy9)

        self.siteDataFL.setWidget(0, QFormLayout.LabelRole, self.institutionLabel)

        self.institutionLE = QLineEdit(self.siteDataWidget)
        self.institutionLE.setObjectName(u"institutionLE")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.institutionLE.sizePolicy().hasHeightForWidth())
        self.institutionLE.setSizePolicy(sizePolicy10)
        self.institutionLE.setMinimumSize(QSize(350, 0))
        self.institutionLE.setClearButtonEnabled(True)

        self.siteDataFL.setWidget(0, QFormLayout.FieldRole, self.institutionLE)

        self.userLabel = QLabel(self.siteDataWidget)
        self.userLabel.setObjectName(u"userLabel")
        sizePolicy.setHeightForWidth(self.userLabel.sizePolicy().hasHeightForWidth())
        self.userLabel.setSizePolicy(sizePolicy)

        self.siteDataFL.setWidget(1, QFormLayout.LabelRole, self.userLabel)

        self.userLE = QLineEdit(self.siteDataWidget)
        self.userLE.setObjectName(u"userLE")
        sizePolicy10.setHeightForWidth(self.userLE.sizePolicy().hasHeightForWidth())
        self.userLE.setSizePolicy(sizePolicy10)
        self.userLE.setMinimumSize(QSize(350, 0))

        self.siteDataFL.setWidget(1, QFormLayout.FieldRole, self.userLE)

        self.dateLabel = QLabel(self.siteDataWidget)
        self.dateLabel.setObjectName(u"dateLabel")
        sizePolicy.setHeightForWidth(self.dateLabel.sizePolicy().hasHeightForWidth())
        self.dateLabel.setSizePolicy(sizePolicy)

        self.siteDataFL.setWidget(2, QFormLayout.LabelRole, self.dateLabel)

        self.hlayoutDateTol = QHBoxLayout()
        self.hlayoutDateTol.setSpacing(6)
        self.hlayoutDateTol.setObjectName(u"hlayoutDateTol")
        self.dateDE = QDateEdit(self.siteDataWidget)
        self.dateDE.setObjectName(u"dateDE")
        self.dateDE.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.dateDE.sizePolicy().hasHeightForWidth())
        self.dateDE.setSizePolicy(sizePolicy2)
        self.dateDE.setMinimumSize(QSize(100, 0))
        self.dateDE.setInputMethodHints(Qt.ImhPreferNumbers)
        self.dateDE.setCalendarPopup(True)

        self.hlayoutDateTol.addWidget(self.dateDE)

        self.hSpacerDateTol = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.hlayoutDateTol.addItem(self.hSpacerDateTol)

        self.hLayoutTol = QHBoxLayout()
        self.hLayoutTol.setObjectName(u"hLayoutTol")
        self.hLayoutTol.setSizeConstraint(QLayout.SetFixedSize)
        self.toleranceLabel = QLabel(self.siteDataWidget)
        self.toleranceLabel.setObjectName(u"toleranceLabel")
        sizePolicy5.setHeightForWidth(self.toleranceLabel.sizePolicy().hasHeightForWidth())
        self.toleranceLabel.setSizePolicy(sizePolicy5)

        self.hLayoutTol.addWidget(self.toleranceLabel)

        self.toleranceDSB = QDoubleSpinBox(self.siteDataWidget)
        self.toleranceDSB.setObjectName(u"toleranceDSB")
        self.toleranceDSB.setDecimals(2)
        self.toleranceDSB.setMinimum(0.500000000000000)
        self.toleranceDSB.setMaximum(5.000000000000000)
        self.toleranceDSB.setValue(1.000000000000000)

        self.hLayoutTol.addWidget(self.toleranceDSB)


        self.hlayoutDateTol.addLayout(self.hLayoutTol)


        self.siteDataFL.setLayout(2, QFormLayout.FieldRole, self.hlayoutDateTol)


        self.verticalLayout_9.addLayout(self.siteDataFL)


        self.worksheetGrid.addWidget(self.siteDataWidget, 0, 0, 1, 1)

        self.gen_report_btn = QPushButton(QPhotonsWorksheet)
        self.gen_report_btn.setObjectName(u"gen_report_btn")
        self.gen_report_btn.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.gen_report_btn.sizePolicy().hasHeightForWidth())
        self.gen_report_btn.setSizePolicy(sizePolicy2)
        self.gen_report_btn.setStyleSheet(u"QPushButton {\n"
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

        self.worksheetGrid.addWidget(self.gen_report_btn, 0, 2, 1, 1)

        self.calibSummaryVL = QVBoxLayout()
        self.calibSummaryVL.setSpacing(0)
        self.calibSummaryVL.setObjectName(u"calibSummaryVL")
        self.calibSummaryWidget = QWidget(QPhotonsWorksheet)
        self.calibSummaryWidget.setObjectName(u"calibSummaryWidget")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.calibSummaryWidget.sizePolicy().hasHeightForWidth())
        self.calibSummaryWidget.setSizePolicy(sizePolicy11)
        self.calibSummaryWidget.setMaximumSize(QSize(450, 16777215))
        self.calibSummaryWidget.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.calibSummaryWidget)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.CalibSummaryLabel = QLabel(self.calibSummaryWidget)
        self.CalibSummaryLabel.setObjectName(u"CalibSummaryLabel")
        sizePolicy2.setHeightForWidth(self.CalibSummaryLabel.sizePolicy().hasHeightForWidth())
        self.CalibSummaryLabel.setSizePolicy(sizePolicy2)
        self.CalibSummaryLabel.setFrameShape(QFrame.NoFrame)
        self.CalibSummaryLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.CalibSummaryLabel)

        self.calibSummaryHLine = QFrame(self.calibSummaryWidget)
        self.calibSummaryHLine.setObjectName(u"calibSummaryHLine")
        sizePolicy10.setHeightForWidth(self.calibSummaryHLine.sizePolicy().hasHeightForWidth())
        self.calibSummaryHLine.setSizePolicy(sizePolicy10)
        self.calibSummaryHLine.setMaximumSize(QSize(16777215, 1))
        self.calibSummaryHLine.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.calibSummaryHLine.setFrameShape(QFrame.Shape.HLine)
        self.calibSummaryHLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.calibSummaryHLine)

        self.verticalSpacer_7 = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.scrollArea = QScrollArea(self.calibSummaryWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy7.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy7)
        self.scrollArea.setMinimumSize(QSize(0, 375))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.calSummaryScroll = QWidget()
        self.calSummaryScroll.setObjectName(u"calSummaryScroll")
        self.calSummaryScroll.setGeometry(QRect(0, 0, 379, 386))
        sizePolicy1.setHeightForWidth(self.calSummaryScroll.sizePolicy().hasHeightForWidth())
        self.calSummaryScroll.setSizePolicy(sizePolicy1)
        self.calSummaryScroll.setAutoFillBackground(False)
        self.calSummaryScroll.setStyleSheet(u"background-color: rgba(252, 247, 247, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.calSummaryScroll)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.corrFactorsLabel = QLabel(self.calSummaryScroll)
        self.corrFactorsLabel.setObjectName(u"corrFactorsLabel")
        sizePolicy2.setHeightForWidth(self.corrFactorsLabel.sizePolicy().hasHeightForWidth())
        self.corrFactorsLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.corrFactorsLabel)

        self.corrFactorFL = QFormLayout()
        self.corrFactorFL.setObjectName(u"corrFactorFL")
        self.corrFactorFL.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.corrFactorFL.setVerticalSpacing(4)
        self.kQLabel = QLabel(self.calSummaryScroll)
        self.kQLabel.setObjectName(u"kQLabel")

        self.corrFactorFL.setWidget(0, QFormLayout.LabelRole, self.kQLabel)

        self.kQLE = QLineEdit(self.calSummaryScroll)
        self.kQLE.setObjectName(u"kQLE")
        sizePolicy2.setHeightForWidth(self.kQLE.sizePolicy().hasHeightForWidth())
        self.kQLE.setSizePolicy(sizePolicy2)
        self.kQLE.setFocusPolicy(Qt.NoFocus)
        self.kQLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.kQLE.setStyleSheet(u"border-radius: 15px;\n"
"border-color: rgb(130, 160, 250);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"background-color: rgba(130, 160, 250,150);\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold")
        self.kQLE.setReadOnly(True)

        self.corrFactorFL.setWidget(0, QFormLayout.FieldRole, self.kQLE)

        self.kElecLabel = QLabel(self.calSummaryScroll)
        self.kElecLabel.setObjectName(u"kElecLabel")
        sizePolicy.setHeightForWidth(self.kElecLabel.sizePolicy().hasHeightForWidth())
        self.kElecLabel.setSizePolicy(sizePolicy)
        self.kElecLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.corrFactorFL.setWidget(1, QFormLayout.LabelRole, self.kElecLabel)

        self.kElecLE = QLineEdit(self.calSummaryScroll)
        self.kElecLE.setObjectName(u"kElecLE")
        self.kElecLE.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.kElecLE.sizePolicy().hasHeightForWidth())
        self.kElecLE.setSizePolicy(sizePolicy2)
        self.kElecLE.setFocusPolicy(Qt.NoFocus)
        self.kElecLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.kElecLE.setAutoFillBackground(False)
        self.kElecLE.setStyleSheet(u"border-radius: 15px;\n"
"border-color: rgb(130, 160, 250);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"background-color: rgba(130, 160, 250,150);\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold")
        self.kElecLE.setFrame(True)
        self.kElecLE.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kElecLE.setReadOnly(True)

        self.corrFactorFL.setWidget(1, QFormLayout.FieldRole, self.kElecLE)

        self.kTPLabel = QLabel(self.calSummaryScroll)
        self.kTPLabel.setObjectName(u"kTPLabel")

        self.corrFactorFL.setWidget(2, QFormLayout.LabelRole, self.kTPLabel)

        self.kTPLE = QLineEdit(self.calSummaryScroll)
        self.kTPLE.setObjectName(u"kTPLE")
        sizePolicy2.setHeightForWidth(self.kTPLE.sizePolicy().hasHeightForWidth())
        self.kTPLE.setSizePolicy(sizePolicy2)
        self.kTPLE.setFocusPolicy(Qt.NoFocus)
        self.kTPLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.kTPLE.setStyleSheet(u"border-radius: 15px;\n"
"border-color: rgb(130, 160, 250);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"background-color: rgba(130, 160, 250,150);\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold")
        self.kTPLE.setReadOnly(True)

        self.corrFactorFL.setWidget(2, QFormLayout.FieldRole, self.kTPLE)

        self.kPolLabel = QLabel(self.calSummaryScroll)
        self.kPolLabel.setObjectName(u"kPolLabel")

        self.corrFactorFL.setWidget(3, QFormLayout.LabelRole, self.kPolLabel)

        self.kPolLE = QLineEdit(self.calSummaryScroll)
        self.kPolLE.setObjectName(u"kPolLE")
        sizePolicy2.setHeightForWidth(self.kPolLE.sizePolicy().hasHeightForWidth())
        self.kPolLE.setSizePolicy(sizePolicy2)
        self.kPolLE.setFocusPolicy(Qt.NoFocus)
        self.kPolLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.kPolLE.setStyleSheet(u"border-radius: 15px;\n"
"border-color: rgb(130, 160, 250);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"background-color: rgba(130, 160, 250,150);\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold")
        self.kPolLE.setReadOnly(True)

        self.corrFactorFL.setWidget(3, QFormLayout.FieldRole, self.kPolLE)

        self.kSLabel = QLabel(self.calSummaryScroll)
        self.kSLabel.setObjectName(u"kSLabel")

        self.corrFactorFL.setWidget(5, QFormLayout.LabelRole, self.kSLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.kSLE = QLineEdit(self.calSummaryScroll)
        self.kSLE.setObjectName(u"kSLE")
        sizePolicy2.setHeightForWidth(self.kSLE.sizePolicy().hasHeightForWidth())
        self.kSLE.setSizePolicy(sizePolicy2)
        self.kSLE.setFocusPolicy(Qt.NoFocus)
        self.kSLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.kSLE.setStyleSheet(u"border-radius: 15px;\n"
"border-color: rgb(130, 160, 250);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"background-color: rgba(130, 160, 250,150);\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold")
        self.kSLE.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.kSLE)

        self.ks_status_icon = QLabel(self.calSummaryScroll)
        self.ks_status_icon.setObjectName(u"ks_status_icon")
        sizePolicy2.setHeightForWidth(self.ks_status_icon.sizePolicy().hasHeightForWidth())
        self.ks_status_icon.setSizePolicy(sizePolicy2)
        self.ks_status_icon.setMaximumSize(QSize(24, 24))
        self.ks_status_icon.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.ks_status_icon)


        self.corrFactorFL.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.kVolLabel = QLabel(self.calSummaryScroll)
        self.kVolLabel.setObjectName(u"kVolLabel")

        self.corrFactorFL.setWidget(4, QFormLayout.LabelRole, self.kVolLabel)

        self.kVolLE = QLineEdit(self.calSummaryScroll)
        self.kVolLE.setObjectName(u"kVolLE")
        sizePolicy2.setHeightForWidth(self.kVolLE.sizePolicy().hasHeightForWidth())
        self.kVolLE.setSizePolicy(sizePolicy2)
        self.kVolLE.setStyleSheet(u"border-radius: 15px;\n"
"border-color: rgb(130, 160, 250);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"background-color: rgba(130, 160, 250,150);\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold")
        self.kVolLE.setReadOnly(True)

        self.corrFactorFL.setWidget(4, QFormLayout.FieldRole, self.kVolLE)


        self.verticalLayout_5.addLayout(self.corrFactorFL)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)

        self.absorsedDoseLabel = QLabel(self.calSummaryScroll)
        self.absorsedDoseLabel.setObjectName(u"absorsedDoseLabel")
        sizePolicy2.setHeightForWidth(self.absorsedDoseLabel.sizePolicy().hasHeightForWidth())
        self.absorsedDoseLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.absorsedDoseLabel)

        self.absorbedDoseFL_2 = QFormLayout()
        self.absorbedDoseFL_2.setObjectName(u"absorbedDoseFL_2")
        self.absorbedDoseFL_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.absorbedDoseFL_2.setVerticalSpacing(4)
        self.zrefDoseLabel = QLabel(self.calSummaryScroll)
        self.zrefDoseLabel.setObjectName(u"zrefDoseLabel")
        sizePolicy5.setHeightForWidth(self.zrefDoseLabel.sizePolicy().hasHeightForWidth())
        self.zrefDoseLabel.setSizePolicy(sizePolicy5)

        self.absorbedDoseFL_2.setWidget(0, QFormLayout.LabelRole, self.zrefDoseLabel)

        self.zrefDoseLE = QLineEdit(self.calSummaryScroll)
        self.zrefDoseLE.setObjectName(u"zrefDoseLE")
        sizePolicy2.setHeightForWidth(self.zrefDoseLE.sizePolicy().hasHeightForWidth())
        self.zrefDoseLE.setSizePolicy(sizePolicy2)
        self.zrefDoseLE.setFocusPolicy(Qt.NoFocus)
        self.zrefDoseLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.zrefDoseLE.setStyleSheet(u"border-radius: 15px;\n"
"border-color: rgb(130, 160, 250);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"background-color: rgba(130, 160, 250,150);\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold")
        self.zrefDoseLE.setReadOnly(True)

        self.absorbedDoseFL_2.setWidget(0, QFormLayout.FieldRole, self.zrefDoseLE)

        self.zmaxDoseLabel = QLabel(self.calSummaryScroll)
        self.zmaxDoseLabel.setObjectName(u"zmaxDoseLabel")
        sizePolicy5.setHeightForWidth(self.zmaxDoseLabel.sizePolicy().hasHeightForWidth())
        self.zmaxDoseLabel.setSizePolicy(sizePolicy5)

        self.absorbedDoseFL_2.setWidget(1, QFormLayout.LabelRole, self.zmaxDoseLabel)

        self.zmaxDoseLE = QLineEdit(self.calSummaryScroll)
        self.zmaxDoseLE.setObjectName(u"zmaxDoseLE")
        sizePolicy2.setHeightForWidth(self.zmaxDoseLE.sizePolicy().hasHeightForWidth())
        self.zmaxDoseLE.setSizePolicy(sizePolicy2)
        self.zmaxDoseLE.setFocusPolicy(Qt.NoFocus)
        self.zmaxDoseLE.setContextMenuPolicy(Qt.NoContextMenu)
        self.zmaxDoseLE.setAutoFillBackground(False)
        self.zmaxDoseLE.setStyleSheet(u"border-radius: 15px;\n"
"border-color: rgb(250, 200, 83);\n"
"background-color: rgba(250, 200, 83,150);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"padding-left: 15px;\n"
"height: 30px;\n"
"font-weight: bold\n"
"\n"
"\n"
"")
        self.zmaxDoseLE.setFrame(False)
        self.zmaxDoseLE.setReadOnly(True)

        self.absorbedDoseFL_2.setWidget(1, QFormLayout.FieldRole, self.zmaxDoseLE)


        self.verticalLayout_5.addLayout(self.absorbedDoseFL_2)

        self.scrollArea.setWidget(self.calSummaryScroll)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.outcomeLabel = QLabel(self.calibSummaryWidget)
        self.outcomeLabel.setObjectName(u"outcomeLabel")
        sizePolicy2.setHeightForWidth(self.outcomeLabel.sizePolicy().hasHeightForWidth())
        self.outcomeLabel.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.outcomeLabel)

        self.outcomeHLine = QFrame(self.calibSummaryWidget)
        self.outcomeHLine.setObjectName(u"outcomeHLine")
        sizePolicy8.setHeightForWidth(self.outcomeHLine.sizePolicy().hasHeightForWidth())
        self.outcomeHLine.setSizePolicy(sizePolicy8)
        self.outcomeHLine.setMaximumSize(QSize(16777215, 1))
        self.outcomeHLine.setStyleSheet(u"background-color: rgb(82, 142, 122)")
        self.outcomeHLine.setFrameShape(QFrame.Shape.HLine)
        self.outcomeHLine.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.outcomeHLine)

        self.outcomeLE = QLineEdit(self.calibSummaryWidget)
        self.outcomeLE.setObjectName(u"outcomeLE")
        self.outcomeLE.setFocusPolicy(Qt.NoFocus)
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
        self.outcomeLE.setClearButtonEnabled(False)

        self.verticalLayout_12.addWidget(self.outcomeLE)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.calibSummaryVL.addWidget(self.calibSummaryWidget)


        self.worksheetGrid.addLayout(self.calibSummaryVL, 1, 2, 1, 1)

        self.worksheetGrid.setColumnStretch(0, 3)
        self.worksheetGrid.setColumnStretch(2, 1)

        self.gridLayout.addLayout(self.worksheetGrid, 2, 0, 1, 1)


        self.retranslateUi(QPhotonsWorksheet)

        QMetaObject.connectSlotsByName(QPhotonsWorksheet)
    # setupUi

    def retranslateUi(self, QPhotonsWorksheet):
        QPhotonsWorksheet.setWindowTitle(QCoreApplication.translate("QPhotonsWorksheet", u"Form", None))
        self.sectionOneGB.setTitle(QCoreApplication.translate("QPhotonsWorksheet", u"1. Radiation treatment unit and reference conditions ", None))
        self.linacNameLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Accelerator:", None))
        self.nomAccPotLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Nominal Acc. Potential:", None))
        self.nomAccPotUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"MV", None))
        self.nomDoseRateLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Nominal dose rate:", None))
        self.nomDoseRateUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"MU/min", None))
        self.beamQualityLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Beam quality, Q (TPR<span style=\" font-size:12pt; vertical-align:sub;\">20,10</span>) :</p></body></html>", None))
        self.calibSetupLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Set up:", None))
        self.ssdRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"SSD", None))
        self.sadRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"SAD", None))
        self.refPhantomLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Reference phantom:", None))
        self.refPhantomComboB.setItemText(0, QCoreApplication.translate("QPhotonsWorksheet", u"Water", None))

        self.refFieldSizeLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Reference field size:", None))
        self.reffieldSizeComboB.setItemText(0, QCoreApplication.translate("QPhotonsWorksheet", u"10 \u00d7 10", None))

        self.fieldSizeUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>cm<span style=\" font-size:11pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.refDepthLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Reference depth <span style=\" font-style:italic;\">z</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">ref  </span>:</p></body></html>", None))
        self.refDepthComboB.setItemText(0, QCoreApplication.translate("QPhotonsWorksheet", u"5.0", None))
        self.refDepthComboB.setItemText(1, QCoreApplication.translate("QPhotonsWorksheet", u"10.0", None))

        self.refDepthUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>g/cm<span style=\" font-size:11pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.refDistanceLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Reference distance:", None))
        self.refDistanceUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"cm", None))
        self.sectionTwoGB.setTitle(QCoreApplication.translate("QPhotonsWorksheet", u"2. Ionization chamber and electrometer", None))
        self.ionChamberModelLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Ionization chamber model:", None))
        self.chamberSerialNoLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Chamber serial No:", None))
        self.calibFactorLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Calibration factor <span style=\" font-style:italic;\">N</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">D,w,Qo </span>:</p></body></html>", None))
        self.calibFactorUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Gy/nC", None))
        self.calibLabLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Calibration laboratory:", None))
        self.chamberCalibDateLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Calibration date:", None))
        self.chamberCalibDE.setDisplayFormat(QCoreApplication.translate("QPhotonsWorksheet", u"dd MMM yyyy", None))
        self.chamberWallMatLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Chamber wall:", None))
        self.cWallMaterialLE.setText(QCoreApplication.translate("QPhotonsWorksheet", u"material:", None))
        self.cWallThickLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"thickness:", None))
        self.cWallThickUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>g/cm<span style=\" font-size:11pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.wSleeveLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Waterproof sleeve:", None))
        self.sleeveMatLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"material:", None))
        self.wsSleeveThickLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"thickness:", None))
        self.wSleeveThickUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>g/cm<span style=\" font-size:11pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.pWinLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Phantom window:", None))
        self.phantomWinMatLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"material:", None))
        self.pWinThickLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"thickness:", None))
        self.pWinThickUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>g/cm<span style=\" font-size:11pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.calibQualityLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Calibration quality, <span style=\" font-style:italic;\">Q</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">o</span> :</p></body></html>", None))
        self.cobaltRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Co-60", None))
        self.photonBeamRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Photon beam", None))
        self.refConditionsLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Reference conditions: ", None))
        self.refPressureLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Pressure, <span style=\" font-style:italic;\">P</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">o</span> :</p></body></html>", None))
        self.refPressureUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"kPa", None))
        self.refTempLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Temperature, <span style=\" font-style:italic;\">T</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">o</span> :</p></body></html>", None))
        self.refTempUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-size:11pt; vertical-align:super;\">o</span><span style=\" font-size:11pt;\">C</span></p></body></html>", None))
        self.refHumidityLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Relative humidity, <span style=\" font-style:italic;\">rH</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">o</span> :</p></body></html>", None))
        self.refHumidityUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"%", None))
        self.polarPotV1.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Polarizing potential, <span style=\" font-style:italic;\">V</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">1 </span>:</p></body></html>", None))
        self.polarPotV1Unit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"V", None))
        self.calibPolarLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Calibration polarity:", None))
        self.calPosPolarRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Positive (+)", None))
        self.calNegPolarRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Negative (-)", None))
        self.userPolarityLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"User polarity:", None))
        self.userPosPolarRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Positive (+)", None))
        self.userNegPolarRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Negative (-)", None))
        self.corrPolarEffCheckB.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Corrected for polarity effect", None))
        self.electSectionLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-weight:700; font-style:italic; text-decoration: underline;\">Electrometer details</span></p></body></html>", None))
        self.electModelLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Electrometer model:", None))
        self.electSerialNoLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Electrometer serial No:", None))
        self.elecCalLabLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Calibration laboratory:", None))
        self.electCalDateLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Calibration date:", None))
        self.electCalDateDE.setDisplayFormat(QCoreApplication.translate("QPhotonsWorksheet", u"dd MMM yyyy", None))
        self.electRangeSettLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Range setting:", None))
        self.calibSeparateLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Calibrated separately from chamber:", None))
        self.calibSepYesRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Yes", None))
        self.calibSepNoRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"No", None))
        self.sectionThreeGB.setTitle(QCoreApplication.translate("QPhotonsWorksheet", u"3. Dosimeter reading and correction for influence quantities", None))
        self.rawDosReadLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Raw dosimeter reading at <span style=\" font-style:italic;\">V</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">1</span> :</p></body></html>", None))
        self.rawDosReadUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"nC", None))
        self.corrLinacMULabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Corresponding linac monitor units:", None))
        self.corrLinacMUUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"MU", None))
        self.ratioReadMULabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Ratio of raw reading and monitor units:", None))
        self.ratioReadMUUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"nC/MU", None))
        self.tempPressCorrLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">(A)</span><span style=\" font-weight:700; font-style:italic; text-decoration: underline;\"> Temp. and pressure correction</span></p></body></html>", None))
        self.userPressureLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Pressure:", None))
        self.userPressureUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"kPa", None))
        self.userTempLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Temperature:", None))
        self.userTempUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-size:11pt; vertical-align:super;\">o</span>C</p></body></html>", None))
        self.userHumidityLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Relative humidity:", None))
        self.userHumidityUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"%", None))
        self.polarCorrLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">(B)</span><span style=\" font-weight:700; font-style:italic; text-decoration: underline;\"> Polarity correction</span></p></body></html>", None))
        self.readMPosLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Reading at +V<span style=\" font-size:12pt; vertical-align:sub;\">1 </span>(<span style=\" font-style:italic;\">M</span><span style=\" font-size:12pt; vertical-align:sub;\">+</span>) :</p></body></html>", None))
        self.readMPosUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"nC", None))
        self.readMNegLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Reading at \u208bV<span style=\" font-size:12pt; vertical-align:sub;\">1 </span>(<span style=\" font-style:italic;\">M</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">\u208b</span>) :</p></body></html>", None))
        self.readMNegUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"nC", None))
        self.ionRecombCorrLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">(C)</span><span style=\" font-weight:700; font-style:italic; text-decoration: underline;\"> Ion recombination correction</span></p></body></html>", None))
        self.normVoltageLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Voltage <span style=\" font-style:italic;\">V</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">1 </span>(normal):</p></body></html>", None))
        self.normVoltageUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"V", None))
        self.normReadLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Reading <span style=\" font-style:italic;\">M</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">1 </span>:</p></body></html>", None))
        self.normReadUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"nC", None))
        self.redVoltageLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Voltage <span style=\" font-style:italic;\">V</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">2 </span>(reduced):</p></body></html>", None))
        self.redVoltageUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"V", None))
        self.redReadLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Reading <span style=\" font-style:italic;\">M</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">2 </span>:</p></body></html>", None))
        self.redReadUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"nC", None))
        self.beamTypeLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Beam type:", None))
        self.pulsedRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Pulsed", None))
        self.pulsedScanRadioButton.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Pulsed-scanned", None))
        self.electmeterCorrLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-weight:700; font-style:italic; text-decoration: underline;\">(D) Electrometer correction:</span></p></body></html>", None))
        self.kElecLabel_2.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">k</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">elec </span>:</p></body></html>", None))
        self.sectionFourGB.setTitle(QCoreApplication.translate("QPhotonsWorksheet", u"4. Absorbed dose to water at the depth of dose maximum", None))
        self.depthDMaxLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>Depth of dose maximum, <span style=\" font-style:italic;\">z</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">max </span>:</p></body></html>", None))
        self.depthDMaxUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>g/cm<span style=\" font-size:11pt; vertical-align:super;\">2</span></p></body></html>", None))
        self.ssdSetupLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic; text-decoration: underline;\">SSD set-up</span></p></body></html>", None))
        self.pddLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">PDD</span> at <span style=\" font-style:italic;\">z</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">ref </span>:</p></body></html>", None))
        self.pddUnit.setText(QCoreApplication.translate("QPhotonsWorksheet", u"%", None))
        self.sadSetupLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic; text-decoration: underline;\">SAD set-up</span></p></body></html>", None))
        self.tmrLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">TMR</span> at  <span style=\" font-style:italic;\">z</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">ref </span>:</p></body></html>", None))
        self.institutionLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Institution:", None))
        self.institutionLE.setText("")
        self.userLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"User:", None))
        self.dateLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Date:", None))
        self.dateDE.setDisplayFormat(QCoreApplication.translate("QPhotonsWorksheet", u"dd MMM yyyy", None))
        self.toleranceLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Tolerance:", None))
        self.toleranceDSB.setSuffix(QCoreApplication.translate("QPhotonsWorksheet", u"%", None))
        self.gen_report_btn.setText(QCoreApplication.translate("QPhotonsWorksheet", u"Generate report", None))
        self.CalibSummaryLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-size:13pt; font-weight:704;\">Calibration Summary</span></p></body></html>", None))
        self.corrFactorsLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">Correction factors</span></p></body></html>", None))
        self.kQLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">k</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">Q,Qo </span>:</p></body></html>", None))
        self.kQLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
        self.kElecLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">k</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">elec </span>:</p></body></html>", None))
        self.kElecLE.setText("")
        self.kElecLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
        self.kTPLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">k</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">TP </span>:</p></body></html>", None))
        self.kTPLE.setText("")
        self.kTPLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
        self.kPolLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">k</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">pol </span>:</p></body></html>", None))
        self.kPolLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
        self.kSLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">k</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">s </span>:</p></body></html>", None))
        self.kSLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
        self.ks_status_icon.setText("")
        self.kVolLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-style:italic;\">k</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">vol </span>:</p></body></html>", None))
        self.kVolLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
        self.absorsedDoseLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-weight:700; text-decoration: underline;\">Absorbed dose to water</span></p></body></html>", None))
        self.zrefDoseLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>At reference depth, <span style=\" font-style:italic;\">D</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">w,Q </span>(<span style=\" font-style:italic;\">z</span><span style=\" font-size:12pt; font-style:italic; vertical-align:sub;\">ref </span>) :</p></body></html>", None))
        self.zrefDoseLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
        self.zmaxDoseLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p>At depth of dose max, <span style=\" font-weight:700; font-style:italic;\">D</span><span style=\" font-size:12pt; font-weight:700; font-style:italic; vertical-align:sub;\">w,Q </span><span style=\" font-weight:700;\">(</span><span style=\" font-weight:700; font-style:italic;\">z</span><span style=\" font-size:12pt; font-weight:700; font-style:italic; vertical-align:sub;\">max </span><span style=\" font-weight:700;\">)</span> :</p></body></html>", None))
        self.zmaxDoseLE.setText("")
        self.zmaxDoseLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
        self.outcomeLabel.setText(QCoreApplication.translate("QPhotonsWorksheet", u"<html><head/><body><p><span style=\" font-size:13pt; font-weight:704;\">Outcome</span></p></body></html>", None))
        self.outcomeLE.setText("")
        self.outcomeLE.setPlaceholderText(QCoreApplication.translate("QPhotonsWorksheet", u"N/A", None))
    # retranslateUi

