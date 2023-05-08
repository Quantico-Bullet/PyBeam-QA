from PySide6.QtCore import Signal, Slot, QObject

from pylinac import WinstonLutz
from pylinac.core.scale import MachineScale
from pathlib import Path

class QWinstonLutz(WinstonLutz):

    def __init__(self, directory: str | list[str] | Path,
                 imageData: list = [],
                 updateSignal: Signal = Signal(int),
                 use_filenames: bool = False,
                 axis_mapping: dict[str, tuple[int, int, int]] | None = None):
        super().__init__(directory, use_filenames, axis_mapping)
        self.updateSignal = updateSignal
        self.imageData = imageData

    def analyze(self, bb_size_mm: float = 5,
                machine_scale: MachineScale = MachineScale.IEC61217,
                low_density_bb: bool = False):
        counter = 0
        self.machine_scale = machine_scale

        for img in self.images:
            img.analyze(bb_size_mm, low_density_bb)

            self.imageData.append({
                "file_path": str(img.path),
                "bb_location": {"x": img.bb.x, "y": img.bb.y},
                "field_cax": {"x": img.field_cax.x, "y": img.field_cax.y},
                "epid": {"x": img.epid.x, "y": img.epid.y}
            })

            counter += 1
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
        self.imageData = []

    @Slot()
    def analyze(self):
        wl = QWinstonLutz(self.images, self.imageData, 
                          updateSignal=self.imagesAnalyzed, use_filenames=True)
        wl.analyze()
        
        wlData = wl.results_data(as_dict=True)
        wlData["image_details"] = self.imageData

        self.analysisResultsChanged.emit(wlData)
        self.bbShiftInfoChanged.emit(wl.bb_shift_instructions())
        del wl
        self.threadFinished.emit()