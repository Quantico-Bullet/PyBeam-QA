from PySide6.QtCore import Signal, Slot, QObject

from pylinac import WinstonLutz
from pylinac.core.scale import MachineScale
from pathlib import Path

class QWinstonLutz(WinstonLutz):

    def __init__(self, directory: str | list[str] | Path,
                 image_data: list = [],
                 update_signal: Signal = Signal(int),
                 use_filenames: bool = False,
                 axis_mapping: dict[str, tuple[int, int, int]] | None = None):
        super().__init__(directory, use_filenames, axis_mapping)
        self.update_signal = update_signal
        self.image_data = image_data

    def analyze(self, bb_size_mm: float = 5,
                machine_scale: MachineScale = MachineScale.IEC61217,
                low_density_bb: bool = False):
        counter = 0
        self.machine_scale = machine_scale

        for img in self.images:
            img.analyze(bb_size_mm, low_density_bb)

            self.image_data.append({
                "file_path": str(img.path),
                "bb_location": {"x": img.bb.x, "y": img.bb.y},
                "field_cax": {"x": img.field_cax.x, "y": img.field_cax.y},
                "epid": {"x": img.epid.x, "y": img.epid.y}
            })

            counter += 1
            self.update_signal.emit(counter)
        self._is_analyzed = True

        del self.update_signal
        
    def get_update_signal(self) -> Signal:
        return self.update_signal

class QWinstonLutzWorker(QObject):

    images_analyzed = Signal(int)
    thread_finished = Signal()
    analysis_results_changed = Signal(dict)
    bb_shift_info_changed = Signal(str)

    def __init__(self, images):
        super().__init__()
        self.images = images
        self.image_data = []

    @Slot()
    def analyze(self):
        wl = QWinstonLutz(self.images, self.image_data, 
                          update_signal=self.images_analyzed, use_filenames=True)
        wl.analyze()
        
        wl_data = wl.results_data(as_dict=True)
        wl_data["image_details"] = self.image_data

        self.analysis_results_changed.emit(wl_data)
        self.bb_shift_info_changed.emit(wl.bb_shift_instructions())
        del wl
        self.thread_finished.emit()