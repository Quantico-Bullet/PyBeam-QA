import math
import logging
from scipy.interpolate import CubicSpline

class TRS398:

    __pulsedConstants = {2.0: {"a0": 2.337, "a1": -3.636, "a2": 2.299},
                         2.5: {"a0": 1.474, "a1": -1.587, "a2": 1.114},
                         3.0: {"a0": 1.198, "a1": -0.875, "a2": 0.677},
                         3.5: {"a0": 1.080, "a1": -0.542, "a2": 0.463},
                         4.0: {"a0": 1.022, "a1": -0.363, "a2": 0.341},
                         5.0: {"a0": 0.975, "a1": -0.188, "a2": 0.214}}
    
    __pulsedScannedConstants = {2.0: {"a0": 4.711, "a1": -8.242, "a2": 4.533},
                         2.5: {"a0": 2.719, "a1": -3.977, "a2": 2.261},
                         3.0: {"a0": 2.001, "a1": -2.402, "a2": 1.404},
                         3.5: {"a0": 1.665, "a1": -1.647, "a2": 0.984},
                         4.0: {"a0": 1.468, "a1": -1.200, "a2": 0.734},
                         5.0: {"a0": 1.279, "a1": -0.750, "a2": 0.474}}

    def __init__(self, mRaw: float = 1.0, nDW: float = 1.0, kTP: float = 1.0, 
                 kS: float = 1.0, kPol: float = 1.0, kElec: float = 1.0, kQQo: float = 1.0):
        self.mRaw = mRaw
        self.nDW = nDW
        self.kTP = kTP
        self.kS = kS
        self.kPol = kPol
        self.kElec = kElec
        self.kQQo = kQQo

        self.refTemp = 20.0
        self.refPress = 101.325
        self.refHumidity = 50.0

        self.ksCalcMethod = "direct"
    
    def setMRaw(self, mRaw):
        self.mRaw = mRaw
    
    def kTP_corr(self, temp: float, press: float) -> float:
        self.kTP = (273.2 + temp) * self.refPress / ((273.2 + self.refTemp) * press)
        return self.kTP

    def kPol_corr(self, mPositive: float, mNegative: float, isPositivePref: bool) -> float:
        if isPositivePref: self.kPol = (abs(mPositive) + abs(mNegative)) / abs(2.0*mPositive)
        else: self.kPol = (abs(mPositive) + abs(mNegative)) / abs(2.0*mNegative)

        return self.kPol

    def kElec_corr(self, kElec: float) -> float:
        self.kElec = kElec
        return self.kElec

    def kS_corr(self, refVoltage: float, redVoltage: float, refM: float, redM,
                isPulsedScanned: bool) -> float:
        
        vRatio = refVoltage / redVoltage
        mRatio = refM / redM

        if self.ksCalcMethod == "direct":
            maxIter = 10000

            if isPulsedScanned:
                #initial conditions
                a = -0.1
                b = 1.7
                delta = 1E-7

                fZeta = lambda x: self.__phi(x)/self.__phi(x*vRatio) - mRatio
                fZetaA = fZeta(a)

                #Bisection method
                for i in range(1, maxIter+1):
                    p = (a + b) / 2.0
                    fZetaB = fZeta(p)

                    if fZetaB == 0.0 or abs(b-a) / 2.0 < delta:
                        self.kS = 1.0 / self.__phi(p)
                        return self.kS

                    if fZetaA * fZetaB > 0: 
                        a = p
                        fZetaA = fZeta(a)
                    else: b = p

            else:
                #initial conditions
                e = mRatio / vRatio
                delta = 1E-7
                uParam = 0.0005

                #Fixed point iteration
                for i in range(0, maxIter+1):
                    u = pow(1.0 + uParam*vRatio, e) - 1

                    if abs(u - uParam) < delta:
                        self.kS = u / math.log(u + 1.0)
                        return self.kS
                    
                    uParam = u
        elif self.ksCalcMethod == "interpolate":
            minRatio = 2.0
            maxRatio = 5.0

            try:
                if vRatio < minRatio or vRatio > maxRatio:
                    raise ValueError(f"Voltage ratio %{vRatio} not within allowed range (%{minRatio} - ${maxRatio})")
                else:
                    # Apply spline interpolation to determine the ion recombination correction factor
                    if isPulsedScanned: fitConstants = self.__pulsedScannedConstants 
                    else: fitConstants = self.__pulsedConstants

                    vRatioData = list(fitConstants.keys())
                    a0Data = [x["a0"] for x in fitConstants.values()]
                    a1Data = [x["a1"] for x in fitConstants.values()]
                    a2Data = [x["a2"] for x in fitConstants.values()]

                    a0Spline = CubicSpline(vRatioData, a0Data)
                    a1Spline = CubicSpline(vRatioData, a1Data)
                    a2Spline = CubicSpline(vRatioData, a2Data)

                    self.kS = a0Spline(vRatio) + a1Spline(vRatio)*mRatio + a2Spline(vRatio)*pow(mRatio, 2)
                    return self.kS

            except ValueError as verr:
                print("Voltage ratio out of range")
                raise

        else:
            try:
                raise ValueError(f"Invalid option {self.ksCalcMethod} for determining ion recombination correction" + \
                                 " only the following values are allowed: \'direct\' or \'interpolate\'")
            except ValueError:
                logging.exception("Invalid option")
                

    def __phi(self, zeta: float) -> float:
        v = zeta / (zeta + 1.0)
        phi = 0.0
        preCoeff = 0.0
        order = 100

        for i in range(1, order+1):
            newCoeff = preCoeff + (1.0 / i)
            phi += (1.0 / i) * newCoeff * pow(v, i)
            preCoeff = newCoeff
        
        return phi * (1.0 / zeta)

    def pdd2010_to_tpr2010(self, pdd2010: float) -> float:
        return 1.2661*pdd2010 - 0.0595

    def pdd10_to_tpr2010(self, pdd10: float) -> float:
        return -0.7898 + 0.0329*pdd10 - 0.000166*pow(pdd10, 2)

    def get_Mcorrected(self) -> float:
        return self.mRaw * self.kTP * self.kElec * self.kPol * self.kS

    def get_DwQ_zref(self) -> float:
        return self.get_Mcorrected() * self.nDW * self.kQQo

    def get_DwQ_zmax_ssdSetup(self, pddZref: float) -> float:
        return 100 * self.get_DwQ_zref() / pddZref
    
    def get_DwQ_zmax_tmrSetup(self, tmrZref: float) -> float:
        return self.get_DwQ_zref() / tmrZref
        

        
class TRS398Photons(TRS398):
    def __init__(self, mRaw: float = 1.0, nDW: float = 1.0, kTP: float = 1.0, 
                 kS: float = 1.0, kPol: float = 1.0, kElec: float = 1.0, kQQo: float = 1.0):
        super().__init__(mRaw = mRaw, nDW = nDW, kTP = kTP,kS = kS, kPol = kPol, kElec = kElec, kQQo = kQQo)
    
    def tpr2010_to_kQ(self, tpr2010: float, tpr_kQ: dict) -> float:
        '''
            Determines the beam quality correction factor from TPR-20,10 (using cubic spline interpolation)
            tpr2010 (float) : The beam quality index defined as the ratio of the absorbed doses at 20 and 10 g/cm2
            tpr_kQ (dict) : Dictionary with tpr2010 values as dict keys and kQ values as dict values
        '''
        tprValues = [float(x) for x in tpr_kQ.keys()]
        tprValues.sort()
        kQValues = [float(x) for x in tpr_kQ.values()]
        kQValues.sort(reverse=True)

        # check if TPR-20,10 value is within bounds
        if tpr2010 < tprValues[0] or tpr2010 > tprValues[-1]:
            raise ValueError(f"TPR-20,10 value {tpr2010} is not within the acceptable range: {tprValues[0]} - {tprValues[-1]}")
        else:
            kQSpline = CubicSpline(tprValues, kQValues)
            self.kQQo = float(kQSpline(tpr2010))
            return self.kQQo
        
class TRS398Electrons(TRS398):
    def __init__(self, mRaw: float = 1.0, nDW: float = 1.0, kTP: float = 1.0, 
                 kS: float = 1.0, kPol: float = 1.0, kElec: float = 1.0, kQQo: float = 1.0):
        super().__init__(mRaw = mRaw, nDW = nDW, kTP = kTP,kS = kS, kPol = kPol, kElec = kElec, kQQo = kQQo)

    def r50ion_to_r50(self, r50ion: float, r50ionDepth: float) -> float:
        if r50ionDepth <= 10.0:
            return 1.029 * r50ion - 0.06
        else:
            return 1.059 * r50ion - 0.37
        
    def r50_to_kQ(self, r50: float, r50_kQ: dict) -> float:
        r50Values = [float(x) for x in r50_kQ.keys()]
        kQValues = [float(x) for x in r50_kQ.values()]
        r50Values.sort()
        kQValues.sort(reverse=True)

        #check if R50 value is within bounds
        if r50 < r50Values[0] or r50 > r50Values[-1]:
            raise ValueError(f"R-50 value {r50} is not within an acceptable range: {r50Values[0]} - {r50Values[-1]}")
        else:
            kQSpline = CubicSpline(r50Values, kQValues)
            return float(kQSpline(r50))

    def r50_to_kQQint(self, r50: float, r50_kQQint: dict) -> float:
        r50Values = [float(x) for x in r50_kQQint.keys()]
        kQQintValues = [float(x) for x in r50_kQQint.values()]
        r50Values.sort()
        kQQintValues.sort(reverse=True)

        #check if R50 value is within bounds
        if r50 < r50Values[0] or r50 > r50Values[-1]:
            raise ValueError(f"R-50 value {r50} is not within an acceptable range: {r50Values[0]} - {r50Values[-1]}")
        else:
            kQSpline = CubicSpline(r50Values, kQQintValues)
            return float(kQSpline(r50))