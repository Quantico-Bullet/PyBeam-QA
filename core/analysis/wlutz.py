import os
import os.path as osp
import copy
import traceback
from typing import Sequence
from PySide6.QtCore import Signal, Slot, QObject

import pyqtgraph as pg

from pylinac import WinstonLutz
from pylinac.winston_lutz import bb_projection_gantry_plane, bb_projection_long
from pylinac.picketfence import Orientation
from pylinac.core.geometry import cos, sin
from pylinac.core.scale import MachineScale
from pylinac.core.image_generator.simulators import Simulator
from pylinac.core.image_generator.layers import (FilteredFieldLayer,
                                                 FilterFreeFieldLayer,
                                                 PerfectFieldLayer,
                                                 PerfectBBLayer, 
                                                 Layer)
from pathlib import Path
import io
import matplotlib.pyplot as plt
from scipy import ndimage
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

    def analyze(self, bb_size_mm: float = 5,
                machine_scale: MachineScale = MachineScale.IEC61217,
                low_density_bb: bool = False):
        counter = 0
        self.machine_scale = machine_scale

        for img in self.images:
            img.analyze(bb_size_mm, low_density_bb)

            self.image_data.append({
                "file_path": str(img.path),
                "filename": Path(str(img.path)).name,
                "bb_location": {"x": img.bb.x, "y": img.bb.y},
                "field_cax": {"x": img.field_cax.x, "y": img.field_cax.y},
                "epid": {"x": img.epid.x, "y": img.epid.y},
                "cax_to_bb_dist": img.cax2bb_distance,
                "cax_to_epid_dist": img.cax2epid_distance,
                "gantry_angle": f"{img.gantry_angle:3.2f}",
                "collimator_angle": f"{img.collimator_angle:3.2f}",
                "couch_angle": f"{img.couch_angle:3.2f}",
                "delta_u": f"{(img.bb.y - img.field_cax.y) / img.dpmm:3.2f}",
                "delta_v": f"{(img.bb.x - img.field_cax.x) / img.dpmm:3.2f}"
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

    def __init__(self, images: list[str],
                 bb_size: float = 5.0,
                 use_filenames: bool = False):
        super().__init__()

        self.bb_size = bb_size
        self._wl = QWinstonLutz(images, update_signal = self.images_analyzed,
                          use_filenames = use_filenames)

    @Slot()
    def analyze(self):
        try:
            self._wl.analyze(bb_size_mm = self.bb_size)
        
            wl_data = self._wl.results_data(as_dict=True)
            wl_data["image_details"] = self._wl.image_data

            summary_image_data = io.BytesIO()
            self._wl.save_summary(summary_image_data, format = "pdf",
                                  pad_inches = 0.0, bbox_inches='tight')
            wl_data["summary_plot"] = summary_image_data

            self.analysis_results_changed.emit(wl_data)
            self.bb_shift_info_changed.emit(self._wl.bb_shift_instructions())
            del self._wl
            self.thread_finished.emit()

        except Exception as err:
            self.analysis_failed.emit(traceback.format_exception_only(err)[-1])
            self.thread_finished.emit()

def generate_winstonlutz(
    simulator: Simulator,
    field_layer: type[Layer],
    dir_out: str,
    field_size_mm: tuple[float, float] = (30, 30),
    final_layers: list[Layer] | None = None,
    bb_size_mm: float = 5,
    offset_mm_left: float = 0,
    offset_mm_up: float = 0,
    offset_mm_in: float = 0,
    image_axes: ((int, int, int), ...) = (
        (0, 0, 0),
        (90, 0, 0),
        (180, 0, 0),
        (270, 0, 0),
    ),
    gantry_tilt: float = 0,
    gantry_sag: float = 0,
    clean_dir: bool = True,
    field_alpha: float = 1.0,
    bb_alpha: float = -0.5,
) -> list[str]:
    
    if field_alpha + bb_alpha > 1:
        raise ValueError("field_alpha and bb_alpha must sum to <=1")
    if field_alpha - bb_alpha < 0:
        raise ValueError("field_alpha and bb_alpha must have a sum >=0")
    if not osp.isdir(dir_out):
        os.mkdir(dir_out)
    if clean_dir:
        for pdir, _, files in os.walk(dir_out):
            [os.remove(osp.join(pdir, f)) for f in files]
    file_names = []
    for gantry, coll, couch in image_axes:
        sim_single = copy.copy(simulator)
        sim_single.add_layer(
            field_layer(
                field_size_mm=field_size_mm,
                cax_offset_mm=(gantry_tilt * cos(gantry), gantry_sag * sin(gantry)),
                alpha=field_alpha,
            )
        )

        # Rotate the image now
        sim_single.image = ndimage.rotate(sim_single.image, -coll,
                                          reshape = False, mode = 'nearest')

        long_offset = bb_projection_long(
            offset_in=offset_mm_in,
            offset_up=offset_mm_up,
            offset_left=offset_mm_left,
            sad=1000,
            gantry=gantry,
        )
        gplane_offset = bb_projection_gantry_plane(
            offset_left=offset_mm_left, offset_up=offset_mm_up, sad=1000, gantry=gantry
        )
        sim_single.add_layer(
            PerfectBBLayer(
                cax_offset_mm=(long_offset, gplane_offset),
                bb_size_mm=bb_size_mm,
                alpha=bb_alpha,
            )
        )
        if final_layers is not None:
            for layer in final_layers:
                sim_single.add_layer(layer)
        file_name = f"WL G={gantry}, C={coll}, P={couch}; Field={field_size_mm}mm; BB={bb_size_mm}mm @ left={offset_mm_left}, in={offset_mm_in}, up={offset_mm_up}; Gantry tilt={gantry_tilt}, Gantry sag={gantry_sag}.dcm"
        sim_single.generate_dicom(
            osp.join(dir_out, file_name),
            gantry_angle=gantry,
            coll_angle=coll,
            table_angle=couch,
        )
        file_names.append(file_name)
    return file_names