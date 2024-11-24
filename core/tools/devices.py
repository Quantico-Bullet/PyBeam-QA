# PyBeam QA
# Copyright (C) 2024 Kagiso Lebang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json

class Device:
    ''' Base class for some devices used in radiotherapy/QA
    '''
    def __init__(self, name: str, 
                 manufacturer: str,
                 model_name: str, 
                 serial_num: str):
        
        self._name = name
        self._manufacturer = manufacturer
        self._model_name = model_name
        self._serial_num = serial_num
    
    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def manufacturer(self):
        return self._manufacturer 
    
    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self._manufacturer = manufacturer

    @property
    def model_name(self):
        return self._model_name 

    @model_name.setter
    def model_name(self, model_name: str):
        self._model_name = model_name

    @property
    def serial_num(self) -> str:
        return self._serial_num

    @serial_num.setter
    def serial_num(self, serial_num: str):
        self._serial_num = serial_num

class Linac(Device):
    def __init__(self, name: str, 
                 manufacturer: str,
                 model_name: str, 
                 serial_num: str,
                 beams: dict):
        super().__init__(name=name, manufacturer=manufacturer, serial_num=serial_num,
                         model_name=model_name)

        self._beams = beams

    @property
    def beams(self):
        return self._beams

    @beams.setter
    def beams(self, beams: dict):
        self._beams = beams
    
    @classmethod
    def fromDictionary(cls, name: str, properties: dict):
        ''' Loads the device from a dictionary object
        '''
        for key in properties.keys():
            if key == "manufacturer":
                manufacturer = properties[key]
            elif key == "modelName":
                model_name = properties[key]
            elif key == "serialNum":
                serial_num = properties[key]
            elif key == "beams":
                beams = properties[key]

        #TODO check if the values exist
        return cls(name, manufacturer, model_name, serial_num, beams)

class IonChamber(Device):

    ionChamberTypes = ("Cylindrical", "Plane-parallel")

    def __init__(self, name: str, 
                 manufacturer: str,
                 model_name: str, 
                 serial_num: str,
                 calibration_lab: str,
                 calibration_date: str,
                 calibration_source: str,
                 chamber_type: str):
        super().__init__(name=name, manufacturer=manufacturer, serial_num=serial_num,
                         model_name=model_name)

        self._calibration_lab = calibration_lab
        self._calibration_date = calibration_date
        self._calibration_source = calibration_source
        self._chamber_type = chamber_type

    @property
    def calibration_lab(self):
        return self._calibration_lab

    @calibration_lab.setter
    def calibration_lab(self, calibration_lab: str):
        self._calibration_lab = calibration_lab

    @property
    def calibration_date(self):
        return self._calibration_date
    
    @calibration_date.setter
    def calibration_date(self, calibration_date: str):
        self._calibration_date = calibration_date
    
    @property
    def calibration_source(self):
        return self._calibration_source
    
    @calibration_source.setter
    def calibration_source(self, calibration_source: str):
        self._calibration_source = calibration_source
    
    @classmethod
    def fromDictionary(cls, name: str, properties: dict):
        ''' Loads the device from a dictionary object
        '''
        for key in properties.keys():
            if key == "manufacturer":
                manufacturer = properties[key]
            elif key == "modelName":
                model_name = properties[key]
            elif key == "serialNum":
                serial_num = properties[key]
            elif key == "calibrationDate":
                cal_date = properties[key]
            elif key == "calibrationLab":
                cal_lab = properties[key]
            elif key == "calibrationSource":
                cal_source = properties[key]

        #TODO check if the values exist
        return cls(name,
                   manufacturer,
                   model_name,
                   serial_num,
                   cal_lab,
                   cal_date,
                   cal_source)

class Electrometer(Device):
    def __init__(self, name: str, 
                 manufacturer: str,
                 model_name: str, 
                 serial_num: str,
                 calibration_lab: str,
                 calibration_date: str):
        super().__init__(name=name, manufacturer=manufacturer, serial_num=serial_num, model_name=model_name)

        self._calibration_lab = calibration_lab
        self._calibration_date = calibration_date

    @property
    def calibration_lab(self):
        return self.calibration_lab

    @calibration_lab.setter
    def calibration_lab(self, calibration_lab: str):
        self.calibration_lab = calibration_lab

    @property
    def calibration_date(self):
        return self._calibration_date
    
    @calibration_date.setter
    def calibration_date(self, calibration_date: str):
        self.calibration_date = calibration_date

class DeviceManager:
    device_list = {"linacs": [], "ionChambers": [], "electrometer": []}

    @classmethod
    def loadDevices(cls, path: str):
        with open(path, 'r') as devicesFile:
            saved_devices = json.load(devicesFile)
        
        for device_type in set(saved_devices).intersection(set(cls.device_list)):
            if device_type == "linacs":
                for linac in saved_devices[device_type]:
                    cls.device_list[device_type].append(Linac.fromDictionary(linac,
                                                    saved_devices[device_type][linac]))

    @classmethod
    def addDevice(cls, device: Device):
        if isinstance(device, Linac):
            cls.device_list["linacs"] = device
