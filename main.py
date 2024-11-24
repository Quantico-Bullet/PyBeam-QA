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

import sys
import json

workspace_path = "core/configuration/workspace.json"

app = QApplication(sys.argv)

app.setWindowIcon(QIcon(u":/misc_icons/icons/ic_app_alt.svg").pixmap(48))
app.setStyle('Fusion')
app.setStyleSheet("QLineEdit, QDateEdit, QPushButton, QDoubleSpinBox," \
                  "QComboBox, QSpinBox { min-height: 20px;}")

def initFiles():
    DeviceManager.loadDevices("core/tools/list.json")
    
    with open(workspace_path, 'r') as workspace_file:
        workspace = json.load(workspace_file)

    if workspace["workspace_dir"] == None:
        init_setup_wizard()

if __name__ == "__main__":

    initFiles()
    
    QMainWin = AppMainWin()
    QMainWin.show()

    app.exec()
    
