from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDate

from pathlib import Path
import os.path
import json

from ui.py_ui.electronsWorksheet_ui import Ui_QElectronsWorksheet
from core.calibration.trs398 import TRS398Photons

chambersConfig = Path(__file__).parent / "../config/chambers.json"
settingsConfig = Path(__file__).parent / "../config/settings.json"

with chambersConfig.open() as file:
        chambers = json.load(file)

with settingsConfig.open() as file:
        settings = json.load(file)

class QElectronsWorksheet(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_QElectronsWorksheet()
        self.ui.setupUi(self)

        self.initSetupComplete = False
        self.trs398 = TRS398Photons()

        # Load all ionization chambers
        self.allChambers = []
        self.setIonChamberList()

        #--- Set up basic functionality ---
        self.ui.dateDE.setDate(QDate.currentDate())
        self.ui.dateDE.setMaximumDate(QDate.currentDate())
        self.ui.chamberCalibDE.setMaximumDate(QDate.currentDate())
        self.ui.electCalDateDE.setMaximumDate(QDate.currentDate())

        self.ui.calibSetupGroup.buttonClicked.connect(self.setupChanged)
        self.setupChanged()
        self.ui.calibSeparateGroup.idToggled.connect(self.sameCalib) # use idToggled to allow other tab signals to enable fields
        self.sameCalib()
        self.ui.IonChamberModelComboB.currentIndexChanged.connect(self.chamberModelChanged)
        self.chamberModelChanged()
        self.ui.calibSetupGroup.buttonClicked.connect(self.setZmaxDepthDose)
        self.ui.IonChamberModelComboB.currentIndexChanged.connect(self.calcKQ)
        self.ui.beamQualityLE.textChanged.connect(self.calcKQ)
        self.ui.refPressureLE.textChanged.connect(self.calcKTP)
        self.ui.refTempLE.textChanged.connect(self.calcKTP)
        self.ui.refHumidityLE.textChanged.connect(self.calcKTP)
        self.ui.userPressureLE.textChanged.connect(self.calcKTP)
        self.ui.userTempLE.textChanged.connect(self.calcKTP)
        self.ui.userHumidityLE.textChanged.connect(self.calcKTP)
        self.ui.kElecLE_2.textChanged.connect(self.setKElec)
        self.ui.kElecLE_2.textChanged.connect(self.setRefDepthDose)
        self.ui.userPolarityGroup.buttonClicked.connect(self.calKPol)
        self.ui.readMPosLE.textChanged.connect(self.calKPol)
        self.ui.readMNegLE.textChanged.connect(self.calKPol)
        self.ui.beamTypeGroup.buttonClicked.connect(self.calcKS)
        self.ui.normReadLE.textChanged.connect(self.calcKS)
        self.ui.redReadLE.textChanged.connect(self.calcKS)
        self.ui.normVoltageLE.textChanged.connect(self.calcKS)
        self.ui.redVoltageLE.textChanged.connect(self.calcKS)
        self.ui.rawDosReadLE.textChanged.connect(self.setRatioReadMU)
        self.ui.corrLinacMULE.textChanged.connect(self.setRatioReadMU)
        self.ui.ratioReadMULE.setReadOnly(True)
        self.ui.ratioReadMULE.textChanged.connect(self.setRefDepthDose)
        self.ui.calibFactorLE.textChanged.connect(self.setNdw)
        self.ui.calibFactorLE.textChanged.connect(self.setRefDepthDose)
        self.ui.kQLE.textChanged.connect(self.setRefDepthDose)
        self.ui.kSLE.textChanged.connect(self.setRefDepthDose)
        self.ui.kTPLE.textChanged.connect(self.setRefDepthDose)
        self.ui.kElecLE.textChanged.connect(self.setRefDepthDose)
        self.ui.kPolLE.textChanged.connect(self.setRefDepthDose)
        self.ui.zrefDoseLE.textChanged.connect(self.setZmaxDepthDose)
        self.ui.pddLE.textChanged.connect(self.setZmaxDepthDose)

        # set reference condition values
        self.ui.refTempLE.setText(f"{self.trs398.refTemp}")
        self.ui.refPressureLE.setText(f"{self.trs398.refPress}")

        self.initSetupComplete = True

    def setIonChamberList(self):
        self.chambers = chambers
        self.allChambers.extend(self.chambers["cylindrical"])

        self.allChambers.sort()   
        self.ui.IonChamberModelComboB.addItems(self.allChambers)

    def chamberModelChanged(self):
        currentChamber = self.ui.IonChamberModelComboB.currentText()

        for type in self.chambers:
            if currentChamber in self.chambers[type]:
                self.ui.cWallMatLE.setText(self.chambers[type][currentChamber]["wall_material"])
                self.ui.cWallThickLE.setText(str(self.chambers[type][currentChamber]["wall_thickness"]))

    def setupChanged(self):
        if self.ui.calibSetupGroup.checkedButton() == self.ui.ssdRadioButton:
            self.ui.setupSW.setCurrentIndex(0)
        else: self.ui.setupSW.setCurrentIndex(1)

    def sameCalib(self):
        if self.ui.calibSeparateGroup.checkedButton() == self.ui.calibSepNoRadioButton:
            self.ui.electCalDateDE.setDate(self.ui.chamberCalibDE.date())
            self.ui.electCalDateDE.setEnabled(False)
            self.ui.electCalLabLE.setEnabled(False)
            self.ui.electmeterCorrSpacer.hide()
            self.ui.electmeterCorrLabel.hide()
            self.ui.kElecLabel_2.hide()
            self.ui.kElecLE_2.hide()
            self.ui.kElecLE_2.clear()
            self.ui.kElecLE.setText("1.000")
            self.trs398.kElec_corr(1.000)

        else:
            self.ui.electCalLabLE.clear()
            self.ui.electCalDateDE.setEnabled(True)
            self.ui.electCalLabLE.setEnabled(True)
            self.ui.electmeterCorrSpacer.show()
            self.ui.electmeterCorrLabel.show()
            self.ui.kElecLabel_2.show()
            self.ui.kElecLE_2.show()
            self.ui.kElecLE.clear() # kElec will still be 1.00 in TRS class until set

    def calcKQ(self):
        currChamber = self.ui.IonChamberModelComboB.currentText()
        tprValue = self.ui.beamQualityLE.text()

        if tprValue != "":
            for chamberType in chambers:
                if currChamber in chambers[chamberType]:
                    tpr_kQ: dict = chambers[chamberType][currChamber]["tpr_kQ"]
                    kQ = self.trs398.tpr2010_to_kQ(float(tprValue), tpr_kQ)
                    self.ui.kQLE.setText("%.3f" % kQ)
        else:
            self.ui.kQLE.clear()

    def calcKTP(self):
        userTemp = self.ui.userTempLE.text()
        userPress = self.ui.userPressureLE.text()
        userHumid = self.ui.userHumidityLE.text()

        if userTemp != "" and userPress != "" and userHumid != "":
            kTP = self.trs398.kTP_corr(float(userTemp), float(userPress))
            self.ui.kTPLE.setText("%.3f" % kTP)
        else:
            self.ui.kTPLE.clear()

    def calKPol(self):
        mPos = self.ui.readMPosLE.text()
        mNeg = self.ui.readMNegLE.text()

        if mPos != "" and mNeg != "":
            if self.ui.userPolarityGroup.checkedButton() == self.ui.userPosPolarRadioButton:
                isPosPref = True
            else:
                isPosPref = False

            kPol = self.trs398.kPol_corr(float(mPos), float(mNeg), isPosPref)
            self.ui.kPolLE.setText("%.3f" % kPol)
        else:
            self.ui.kPolLE.clear()

    def calcKS(self):
        vNorm = self.ui.normVoltageLE.text()
        vRed = self.ui.redVoltageLE.text()
        mNorm = self.ui.normReadLE.text()
        mRed = self.ui.redReadLE.text()

        if vNorm != "" and vRed != "" and mNorm != "" and mRed != "":
            if self.ui.beamTypeGroup.checkedButton() == self.ui.pulsedScanRadioButton:
                isPulsedScanned = True
            else:
                isPulsedScanned = False
            
            kS = self.trs398.kS_corr(float(vNorm), float(vRed), float(mNorm), float(mRed),
                                     isPulsedScanned)
            self.ui.kSLE.setText("%.3f" % kS)
        else:
            self.ui.kSLE.clear()
    
    def setKElec(self):
        kElec = self.ui.kElecLE_2.text()

        if kElec != "":
            self.ui.kElecLE.setText("%.3f" % self.trs398.kElec_corr(float(kElec)))
        else:
            self.ui.kElecLE.clear()

    def setRatioReadMU(self):
        rawRead = self.ui.rawDosReadLE.text()
        linacMU = self.ui.corrLinacMULE.text()

        if rawRead != "" and linacMU != "":
            rawRead = float(rawRead)
            linacMU = float(linacMU)

            self.trs398.mRaw = rawRead / linacMU
            self.ui.ratioReadMULE.setText("%.5f" % (rawRead / linacMU))
        else:
            self.ui.ratioReadMULE.clear()

    def setNdw(self):
        nDw = self.ui.calibFactorLE.text()

        if nDw != "":
            self.trs398.nDW = float(nDw)

    def setRefDepthDose(self):
        # use fields for checking validity, otherwise TRS398 values used for accuracy
        kTP = self.ui.kTPLE.text()
        kS = self.ui.kSLE.text()
        kElec = self.ui.kElecLE.text()
        kPol = self.ui.kPolLE.text()
        kQ = self.ui.kQLE.text()
        ratioRead = self.ui.ratioReadMULE.text()
        nDw = self.ui.calibFactorLE.text()

        areAllValid = (kTP != "" and kS != "" and kElec != "" and kPol != "" and kQ != "" and ratioRead != ""
            and nDw != "")

        if areAllValid:
            self.ui.zrefDoseLE.setText(("%.3f" % (self.trs398.get_DwQ_zref()*10.0)) + " cGy/MU")
        else:
            self.ui.zrefDoseLE.clear()

    def setZmaxDepthDose(self):
        if self.ui.calibSetupGroup.checkedButton() == self.ui.ssdRadioButton:
            zRefDD = self.ui.zrefDoseLE.text()
            pddzRef = self.ui.pddLE.text()

            if zRefDD != "" and pddzRef != "":
                dMax = self.trs398.get_DwQ_zmax_ssdSetup(float(pddzRef))
                self.ui.zmaxDoseLE.setText("%.3f" % (dMax * 10.0) + " cGy/MU")
            else:
                self.ui.zmaxDoseLE.clear()
        else:
            zRefDD = self.ui.zrefDoseLE.text()
            tmrRef = self.ui.tmrLE.text()

            if zRefDD != "" and pddzRef != "":
                dMax = self.trs398.get_DwQ_zmax_tmrSetup(float(tmrRef))
                self.ui.zmaxDoseLE.setText("%.3f" % (dMax * 10.0) + " cGy/MU")
            else:
                self.ui.zmaxDoseLE.clear()