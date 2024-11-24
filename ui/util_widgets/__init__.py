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

from PySide6.QtWidgets import QWidget, QFileDialog

def worksheet_save_report(parent: QWidget = None):
    file_path = QFileDialog.getSaveFileName(caption="Save To File...", 
                                            filter="PDF (*.pdf)",
                                            parent=parent)
        
    if file_path[0] != "":
        path = file_path[0].split("/")
            
        if not path[-1].endswith(".pdf"):
            path[-1] = path[-1] + ".pdf"

        return "/".join(path)

    else:
        return ""
