import traceback
from PySide6.QtCore import Signal, Slot, QObject

import pyqtgraph as pg
from pylinac import WinstonLutz
from pylinac.core.scale import MachineScale
from pathlib import Path
import io
import matplotlib.pyplot as plt
plt.switch_backend('agg') # switch to non-gui backend to avoid runtime error

pg.setConfigOptions(antialias = True, imageAxisOrder='row-major')

class QWinstonLutz(WinstonLutz):

    def __init__(self, directory: str | list[str] | Path,
                 update_signal: Signal =  Signal(int),
                 use_filenames: bool = False,
                 axis_mapping: dict[str, tuple[int, int, int]] | None = None):
        super().__init__(directory, use_filenames, axis_mapping)

        self.update_signal = update_signal
        self.image_data = []

    def analyze(self, bb_size_mm: float = 8,
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

class QWinstonLutzWorker(QObject):

    images_analyzed = Signal(int)
    thread_finished = Signal()
    analysis_results_changed = Signal(dict)
    analysis_failed = Signal(str)
    bb_shift_info_changed = Signal(str)

    def __init__(self, images: list[str], use_filenames: bool = False):
        super().__init__()

        #TODO take in a QWinstonLutz object
        self._wl = QWinstonLutz(images, update_signal = self.images_analyzed,
                          use_filenames = use_filenames)

    @Slot()
    def analyze(self):
        try:
            self._wl.analyze()
        
            wl_data = self._wl.results_data(as_dict=True)
            wl_data["image_details"] = self._wl.image_data

            summary_image_data = io.BytesIO()
            self._wl.save_summary(summary_image_data, dpi=120, format = "pdf")
            wl_data["summary_plot"] = summary_image_data

            self.analysis_results_changed.emit(wl_data)
            self.bb_shift_info_changed.emit(self._wl.bb_shift_instructions())
            del self._wl
            self.thread_finished.emit()

        except Exception as err:
            self.analysis_failed.emit(traceback.format_exception_only(err)[-1])
            self.thread_finished.emit()