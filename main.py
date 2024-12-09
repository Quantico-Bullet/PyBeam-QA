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

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from ui.app_main_win import AppMainWin
from core.tools.devices import DeviceManager
from core.tools.setup import init_setup_wizard
from core.configuration.config import WorkspaceConfig

import platform
import sys
import json

app = QApplication(sys.argv)

app.setWindowIcon(QIcon(u":/misc_icons/icons/ic_app_alt.svg").pixmap(48))
app.setStyle('Fusion')
app.setStyleSheet("QLineEdit, QDateEdit, QPushButton, QDoubleSpinBox," \
                  "QComboBox, QSpinBox { min-height: 20px;}")

def initFiles():
    DeviceManager.loadDevices("core/tools/list.json")
    
    workspace = WorkspaceConfig().getConfig()

    if workspace["workspace_path"] == None:
        init_setup_wizard()

if __name__ == "__main__":

    initFiles()

    plt = platform.system()

    if plt == "Windows":
        import ctypes
        
        appID = u"radlab.pybeamqa-0.1.2"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)
    
    QMainWin = AppMainWin()
    QMainWin.show()

    app.exec()
    
