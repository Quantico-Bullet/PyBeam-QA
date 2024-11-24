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

import os
import os.path as osp
import copy
import traceback
from typing import Sequence
from PySide6.QtCore import Signal, Slot, QObject

import pyqtgraph as pg

from pylinac import WinstonLutz, WinstonLutz2D
from pylinac.winston_lutz import bb_projection_with_rotation, BB3D, BBArrangement
from pylinac.picketfence import Orientation
from pylinac.core.geometry import cos, sin
from pylinac.core.scale import MachineScale
from pylinac.core.image_generator.simulators import Simulator
from pylinac.core.image_generator.layers import (FilteredFieldLayer,
                                                 FilterFreeFieldLayer,
                                                 PerfectFieldLayer,
                                                 PerfectBBLayer, 
                                                 Layer)

import gc
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

    def analyze(self,
                bb_size_mm: float = 5,
                machine_scale: MachineScale = MachineScale.IEC61217, 
                low_density_bb: bool = False,
                open_field: bool = False,
                apply_virtual_shift: bool = False,):
        
        # Initial counter value for the progress bar
        self.progress_counter = 0
        self.machine_scale = machine_scale

        self.machine_scale = machine_scale
        if self.is_from_cbct:
            low_density_bb = True
            open_field = True
        for img in self.images:
            img.analyze(bb_size_mm, low_density_bb, open_field)

            self.update_image_info(img)
            
        # we need to construct the BB representation to get the shift vector
        bb_config = BBArrangement.ISO[0]
        bb_config.bb_size_mm = bb_size_mm
        self.bb = BB3D(
            bb_config=bb_config,
            bb_matches=[img.arrangement_matches["Iso"] for img in self.images],
            scale=self.machine_scale,
        )
        if apply_virtual_shift:
            shift = self.bb_shift_vector
            self._virtual_shift = self.bb_shift_instructions()
            for img in self.images:
                img.analyze(bb_size_mm, low_density_bb, open_field, shift_vector=shift)

        # in the vanilla WL case, the BB can only be represented by non-couch-kick images
        # the ray trace cannot handle the kick currently
        self.bb = BB3D(
            bb_config=bb_config,
            bb_matches=[img.arrangement_matches["Iso"] for img in self.images],
            scale=self.machine_scale,
        )
        self._is_analyzed = True
        self._bb_diameter = bb_size_mm

    def update_image_info(self, img: WinstonLutz2D):
        self.image_data.append({
                "file_path": str(img.path),
                "filename": Path(str(img.path)).name,
                "bb_location": {"x": img.bb.x, "y": img.bb.y},
                "bb_outline_coords": img.bb,
                "field_cax": {"x": img.field_cax.x, "y": img.field_cax.y},
                "epid": {"x": img.epid.x, "y": img.epid.y},
                "cax_to_bb_dist": img.cax2bb_distance,
                "cax_to_epid_dist": img.cax2epid_distance,
                "gantry_angle": f"{img.gantry_angle:.2f}",
                "collimator_angle": f"{img.collimator_angle:.2f}",
                "couch_angle": f"{img.couch_angle:.2f}",
                "delta_u": f"{(img.bb.x - img.field_cax.x) / img.dpmm:.2f}",
                "delta_v": f"{(img.bb.y - img.field_cax.y) / img.dpmm:.2f}"
            })

        self.progress_counter += 1
        self.update_signal.emit(self.progress_counter)

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

            #summary_image_data = io.BytesIO()
            #self._wl.save_summary(summary_image_data, format = "pdf",
            #                      pad_inches = 0.0, bbox_inches='tight')
            #wl_data["summary_plot"] = summary_image_data

            self.analysis_results_changed.emit(wl_data)
            self.bb_shift_info_changed.emit(str(self._wl.bb_shift_instructions()))
            del self._wl
            gc.collect()
            self.thread_finished.emit()


        except Exception as err:
            self.analysis_failed.emit(traceback.format_exception_only(err)[-1])
            self.thread_finished.emit()

            raise err

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

        gplane_offset, long_offset = bb_projection_with_rotation(
            offset_left=offset_mm_left,
            offset_up=offset_mm_up,
            offset_in=offset_mm_in,
            gantry=gantry,
            couch=couch,
            sad=1000,
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
        file_name = f"WL G={gantry}, C={coll}, P={couch}; Field={field_size_mm}mm; " \
                    f"BB={bb_size_mm}mm @ left={offset_mm_left}, in={offset_mm_in}, " \
                    f"up={offset_mm_up}; Gantry tilt={gantry_tilt}, Gantry sag={gantry_sag}.dcm"
        sim_single.generate_dicom(
            osp.join(dir_out, file_name),
            gantry_angle=gantry,
            coll_angle=coll,
            table_angle=couch,
        )
        file_names.append(file_name)
    return file_names
