from PySide6.QtCore import QObject
from typing import Optional, overload
from PySide6.QtGui import QDoubleValidator, QValidator

class DoubleValidator(QDoubleValidator):

    def __init__(self, 
                 bottom: float, 
                 top: float, 
                 decimals: int = 4,
                 notation = QDoubleValidator.Notation.StandardNotation,
                 parent: Optional[QObject] = None) -> None:
        
        super().__init__(bottom, top, decimals, parent)
        self.setNotation(notation)

    def fixup(self, input: str) -> str:
        if input != "" and self.validate(input, 0)[0] == QValidator.State.Intermediate:
            if float(input) < self.bottom():
                return str(self.bottom())
            elif float(input) > self.top():
                return str(self.top())
