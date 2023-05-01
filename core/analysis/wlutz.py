from PySide6.QtCore import Signal, Slot, QObject

from pylinac import WinstonLutz
from pylinac.core.scale import MachineScale
from pathlib import Path

class QWinstonLutz(WinstonLutz):

    def __init__(self, directory: str | list[str] | Path,
                 updateSignal: Signal = Signal(int),
                 use_filenames: bool = False,
                 axis_mapping: dict[str, tuple[int, int, int]] | None = None):
        super().__init__(directory, use_filenames, axis_mapping)
        self.updateSignal = updateSignal

    def analyze(self, bb_size_mm: float = 5,
                machine_scale: MachineScale = MachineScale.IEC61217,
                low_density_bb: bool = False):
        
        counter = 0

        self.machine_scale = machine_scale
        for img in self.images:
            img.analyze(bb_size_mm, low_density_bb)
            counter = counter + 1
            self.updateSignal.emit(counter)
        self._is_analyzed = True

        del self.updateSignal
        
    def getUpdateSignal(self) -> Signal:
        return self.updateSignal

class QWinstonLutzWorker(QObject):

    imagesAnalyzed = Signal(int)
    threadFinished = Signal()
    analysisResultsChanged = Signal(dict)
    bbShiftInfoChanged = Signal(str)

    def __init__(self, images):
        super().__init__()
        self.images = images

    @Slot()
    def analyze(self):
        wl = QWinstonLutz(self.images, updateSignal=self.imagesAnalyzed, use_filenames=True)
        wl.analyze()
        
        self.analysisResultsChanged.emit(wl.results_data(as_dict=True))
        self.bbShiftInfoChanged.emit(wl.bb_shift_instructions())
        del wl
        self.threadFinished.emit()