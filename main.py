from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from ui.app_main_win import AppMainWin
from core.tools.devices import DeviceManager

import sys

app = QtWidgets.QApplication(sys.argv)

def initFiles():
    DeviceManager.loadDevices("core/tools/list.json")

if __name__ == "__main__":

    initFiles()
    
    QMainWin = AppMainWin()
    QMainWin.show()

    app.setStyleSheet("QLineEdit, QDateEdit, QPushButton, QDoubleSpinBox," \
                      "QComboBox, QSpinBox { min-height: 20px;}")

    app.setWindowIcon(QIcon(u":/misc_icons/icons/ic_app_alt.svg").pixmap(48))
    app.exec()
    
