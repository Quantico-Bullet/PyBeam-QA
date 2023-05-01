import json

class Device:
    ''' Base class for some devices used in radiotherapy/QA
    '''
    def __init__(self, name: str, 
                 manufacturer: str,
                 modelName: str, 
                 serialNum: str):
        
        self.__name = name
        self.__manufacturer = manufacturer
        self.__modelName = modelName
        self.__serialNum = serialNum
    
    def setName(self, name: str):
        self.__name = name
    
    def setManufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

    def setModelName(self, modelName: str):
        self.__modelName = modelName

    def setSerialNum(self, serialNum: str):
        self.__serialNum = serialNum

    def getName(self) -> str:
        return self.__name 
    
    def getManufacturer(self) -> str:
        return self.__manufacturer 

    def getModelName(self) -> str:
        return self.__modelName 

    def getSerialNum(self) -> str:
        return self.__serialNum

class Linac(Device):
    def __init__(self, name: str, 
                 manufacturer: str,
                 modelName: str, 
                 serialNum: str,
                 beams: dict):
        super().__init__(name=name, manufacturer=manufacturer, serialNum=serialNum, modelName=modelName)

        self.__beams = beams

    def getBeams(self) -> dict:
        return self.__beams
    
    @classmethod
    def fromDictionary(cls, name: str, properties: dict):
        ''' Loads the device from a dictionary object
        '''
        for key in properties.keys():
            if key == "manufacturer":
                manufacturer = properties[key]
            elif key == "modelName":
                modelName = properties[key]
            elif key == "serialNum":
                serialNum = properties[key]
            elif key == "beams":
                beams = properties[key]

        #TODO check if the values exist
        return cls(name, manufacturer, modelName, serialNum, beams)

class IonChamber(Device):

    ionChamberTypes = ("Cylindrical", "Plane-parallel")

    def __init__(self, name: str, 
                 manufacturer: str,
                 modelName: str, 
                 serialNum: str,
                 calibrationLab: str,
                 calibrationDate: str,
                 calibrationSource: str,
                 chamberType: str):
        super().__init__(name=name, manufacturer=manufacturer, serialNum=serialNum, modelName=modelName)

        self.__calibrationLab = calibrationLab
        self.__calibrationDate = calibrationDate
        self.__calibrationSource = calibrationSource
        self.__chamberType = chamberType

    def setCalibrationLab(self, calibrationDate: str):
        self.__calibrationDate = calibrationDate

    def setCalibrationDate(self, calibrationDate: str):
        self.__calibrationDate = calibrationDate
    
    def setCalibrationSource(self, calibrationSource: str):
        self.__calibrationSource = calibrationSource
    
    @classmethod
    def fromDictionary(cls, name: str, properties: dict):
        ''' Loads the device from a dictionary object
        '''
        for key in properties.keys():
            if key == "manufacturer":
                manufacturer = properties[key]
            elif key == "modelName":
                modelName = properties[key]
            elif key == "serialNum":
                serialNum = properties[key]
            elif key == "calibrationDate":
                calDate = properties[key]
            elif key == "calibrationLab":
                calLab = properties[key]
            elif key == "calibrationSource":
                calSource = properties[key]

        #TODO check if the values exist
        return cls(name, manufacturer, modelName, serialNum, calLab, calDate, calSource)

class Electrometer(Device):
    def __init__(self, name: str, 
                 manufacturer: str,
                 modelName: str, 
                 serialNum: str,
                 calibrationLab: str,
                 calibrationDate: str):
        super().__init__(name=name, manufacturer=manufacturer, serialNum=serialNum, modelName=modelName)

    def setCalibrationLab(self, calibrationDate: str):
        self.calibrationDate = calibrationDate

    def setCalibrationDate(self, calibrationDate: str):
        self.calibrationDate = calibrationDate

class DeviceManager:
    deviceList = {"linacs": [], "ionChambers": [], "electrometer": []}

    @classmethod
    def loadDevices(cls, pathToDevices: str):
        with open(pathToDevices, 'r') as devicesFile:
            savedDevices = json.load(devicesFile)
        
        for deviceType in set(savedDevices).intersection(set(cls.deviceList)):
            if deviceType == "linacs":
                for linac in savedDevices[deviceType]:
                    cls.deviceList[deviceType].append(Linac.fromDictionary(linac,
                                                    savedDevices[deviceType][linac]))

    @classmethod
    def addDevice(cls, device: Device):
        if isinstance(device, Linac):
            cls.deviceList["linacs"] = device
