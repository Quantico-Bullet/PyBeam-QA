from PySide6.QtCore import Signal, Slot, QObject

from pylinac.core import image
from pylinac.picketfence import PicketFence, MLC, MLCArrangement, Orientation

import os.path as osp
import numpy as np
import pyqtgraph as pg
from py_linq import Enumerable
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import BinaryIO, Optional, Union

class QPicketFence(PicketFence):

    def __init__(self, filename: Union[str, list[str], Path, BinaryIO],
                 update_signal: Signal = None,
                 filter: Optional[int] = None,
                 log: Optional[str] = None,
                 use_filename: bool = False,
                 mlc: Union[MLC, MLCArrangement, str] = MLC.MILLENNIUM,
                 crop_mm: int = 3,
                 tolerance: float = 0.5,
                 image_kwargs: Optional[dict] = None,):
        
        # Widgets for leaf profile plots
        self.profile_plot_widget = pg.PlotWidget()
        self.profile_plot_widget.getPlotItem().setMouseEnabled(x=False, y=False)
        self.legend = self.profile_plot_widget.getPlotItem().addLegend(offset=(50,50), size = (50,50))
        
        if isinstance(filename, list):
            with TemporaryDirectory() as tmp:
                temp_file = osp.join(tmp, "temp_pf.dcm")
                image.load_multiples(filename, dtype = np.uint16,
                                     kwargs = image_kwargs).save(temp_file)

                super().__init__(temp_file, filter, log,
                                 use_filename, mlc, crop_mm, image_kwargs,)
        else:
            super().__init__(filename, filter, log,
                        use_filename, mlc, crop_mm, image_kwargs,)
            
        self.action_tolerance = tolerance
        self.tolerance = tolerance
        
        self.update_signal = update_signal

    def set_update_signal(self, update_signal: Signal):
        self.update_signal = update_signal

    def qplot_leaf_profile(self, leaf: int, picket: int):
        self.profile_plot_widget.clear()
        self.legend.clear()
        
        #plot the pixel values 
        mlc = Enumerable(self.mlc_meas).single(
            lambda m: leaf in m.full_leaf_nums and m.picket_num == picket)
        
        if mlc._orientation == Orientation.UP_DOWN:
            pix_vals = np.median(mlc._image_window, axis=0)
        else:
            pix_vals = np.median(mlc._image_window, axis=1)

        offset_pixels = max(mlc._approximate_idx - mlc._spacing / 2, 0)
        x_values = np.array(range(len(pix_vals))) + offset_pixels

        self.profile_plot_widget.plot(x=x_values, y=pix_vals)

        #plot the mlc position
        pos = mlc.get_peak_positions()[0]
        mlc_pos_plot = pg.InfiniteLine(pos=pos,movable=False, angle=90, 
                       pen = (135,206,235), label=f'MLC position ({pos:2.2f})', 
                       labelOpts={'position':0.1, 'color': (135,206,235), 
                                  'fill': (135,206,235,50), 'movable': True})

        mlc_pos_plot.opts = {"pen": mlc_pos_plot.pen}
        
        #plot the picket position
        for picket_position in mlc.picket_positions:
            pos = picket_position * mlc._image.dpmm

            picket_pos_plot = pg.InfiniteLine(pos=pos,movable=False, angle=90,
                            pen = (230,230,250), label=f'Fitted picket position ({pos:2.2f})', 
                            labelOpts={'position':0.15, 'color': (230,230,250), 
                                       'fill': (230,230,250,50), 'movable': True})
        
        picket_pos_plot.opts = {"pen": picket_pos_plot.pen}
        
        self.profile_plot_widget.addItem(mlc_pos_plot)
        self.profile_plot_widget.addItem(picket_pos_plot)
        self.legend.addItem(mlc_pos_plot, "MLC position")
        self.legend.addItem(picket_pos_plot, "Fitted picket position")

        #plot the guard rails
        for lg, rg, m in zip(
            self.pickets[picket].left_guard_separated,
            self.pickets[picket].right_guard_separated,
            mlc.marker_lines,
        ):

            if mlc._orientation == Orientation.UP_DOWN:
                lg_pos = lg(m.point1.y)
                rg_pos = rg(m.point1.y)

            else:
                lg_pos = lg(m.point1.x)
                rg_pos = rg(m.point1.x)

            lg_plot = pg.InfiniteLine(pos=lg_pos,movable=False, angle=90, pen = (124,252,0))
            rg_plot = pg.InfiniteLine(pos=rg_pos,movable=False, angle=90, pen = (124,252,0))

            lg_plot.opts = {"pen": lg_plot.pen}
            rg_plot.opts = {"pen": rg_plot.pen}

            self.profile_plot_widget.addItem(lg_plot)
            self.profile_plot_widget.addItem(rg_plot)

            self.legend.addItem(lg_plot, "Guard rail")
            self.legend.addItem(rg_plot, "Guard rail")

class QPicketFenceWorker(QObject):

    analysis_progress = Signal(str)
    analysis_results_ready =  Signal(dict)
    thread_finished = Signal()

    def __init__(self, qPicketFence: QPicketFence):
        super().__init__()

        self._pf = qPicketFence

    @Slot()
    def analyze(self):

        if self._pf is not None:
            self._pf.analyze(tolerance=self._pf.tolerance, action_tolerance= self._pf.action_tolerance)

            summary_text = [["Gantry angle:", f"{self._pf.image.gantry_angle:2.2f}°"],
                       ["Collimator angle:", f"{self._pf.image.collimator_angle:2.2f}°"],
                       ["Leaves passing:", f"{self._pf.percent_passing:2.1f}%"],
                       ["Absolute median error:", f"{self._pf.abs_median_error:2.2f} mm"],
                       ["Mean picket spacing:", f"{self._pf.mean_picket_spacing:2.2f} mm"],
                       ["Max Error:", f"{self._pf.max_error:2.3f} mm (Picket: {self._pf.max_error_picket + 1}, Leaf: {self._pf.max_error_leaf + 1})"]]
            
            results = {"summary_text": summary_text,
                       "picket_fence_obj": self._pf}

            self.analysis_results_ready.emit(results)
            self.thread_finished.emit()