from PySide6 import QtWidgets
from PySide6.QtCore import QDir, QUrl, QFile, QIODevice, Qt
from PySide6.QtUiTools import QUiLoader

from ui.appMainWin import AppMainWin
from core.tools.devices import DeviceManager

import sys

app = QtWidgets.QApplication(sys.argv)

def initFiles():
    DeviceManager.loadDevices("core/tools/list.json")

if __name__ == "__main__":

    initFiles()
    
    QMainWin = AppMainWin()
    QMainWin.show()

    app.setStyleSheet("QLineEdit, QDateEdit, QPushButton, QDoubleSpinBox,"
                      "QComboBox, QSpinBox { min-height: 20px;}")
    app.exec()
