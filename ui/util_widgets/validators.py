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

from PySide6.QtCore import QObject, QLocale
from typing import Optional, overload
from PySide6.QtGui import QDoubleValidator, QValidator

class DoubleValidator(QDoubleValidator):

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        locale = QLocale.c()
        locale.setNumberOptions(QLocale.NumberOption.RejectGroupSeparator)
        self.setLocale(locale)
        self.setNotation(QDoubleValidator.Notation.StandardNotation)

    @classmethod
    def from_args(cls, 
                  bottom: float, 
                  top: float, 
                  decimals: int = 4,
                  notation = QDoubleValidator.Notation.StandardNotation,
                  parent: Optional[QObject] = None):
        
        validator = cls(parent)
        validator.setBottom(bottom)
        validator.setTop(top)
        validator.setDecimals(decimals)
        validator.setNotation(notation)

        return validator

    def fixup(self, input: str) -> str:
        if input != "" and self.validate(input, 0)[0] == QValidator.State.Intermediate:
            if float(input) < self.bottom():
                return str(self.bottom())
            elif float(input) > self.top():
                return str(self.top())
