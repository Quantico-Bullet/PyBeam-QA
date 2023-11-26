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
