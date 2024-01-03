import io
from PySide6.QtCore import Signal, Slot, QObject, QCoreApplication
from pylinac.core import image
from pylinac.core.image_generator.simulators import Simulator
from pylinac.core.image_generator.layers import (FilteredFieldLayer,
                                                 FilterFreeFieldLayer,
                                                 PerfectFieldLayer, 
                                                 Layer)
from pylinac.picketfence import PicketFence, MLC, MLCArrangement, Orientation

import matplotlib.pyplot as plt
import traceback
import os.path as osp
import numpy as np
import pyqtgraph as pg
from scipy import ndimage
from py_linq import Enumerable
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import BinaryIO, Optional, Union, Sequence
import time

import gc

pg.setConfigOptions(antialias = True, imageAxisOrder='row-major', enableExperimental=True)

class QPicketFence(PicketFence):

    def __init__(self, filename: Union[str, list[str], Path, BinaryIO],
                 update_signal: Signal = None,
                 filter: int | None = None,
                 log: str | None = None,
                 use_filename: bool = False,
                 mlc: Union[MLC, MLCArrangement, str] = MLC.MILLENNIUM,
                 crop_mm: int = 3,
                 image_kwargs: Optional[dict] = None):

        self.mlc_type = mlc
        
        # Widgets for analyzed image plots
        self.analyzed_image_plot_widget = pg.GraphicsLayoutWidget()
        
        if isinstance(filename, list):
            with TemporaryDirectory() as tmp:
                temp_file = osp.join(tmp, "temp_self.pf.dcm")
                image.load_multiples(filename, dtype = np.uint16,
                                     kwargs = image_kwargs).save(temp_file)

                super().__init__(temp_file, filter, log,
                                 use_filename, mlc, crop_mm, image_kwargs)
        else:
            super().__init__(filename, filter, log,
                        use_filename, mlc, crop_mm, image_kwargs)
                    
        self.update_signal = update_signal

    def set_update_signal(self, update_signal: Signal):
        self.update_signal = update_signal

    def init_profile_plot(self):
        # Widgets for leaf profile plots
        self.profile_plot_widget = pg.PlotWidget()
        self.profile_plot_widget.getPlotItem().setMouseEnabled(x=False, y=False)
        
        """
        self.legend = self.profile_plot_widget.getPlotItem().addLegend(
                        offset=(50,50), size = (50,50),
                        labelTextColor=(255,255,255),
                        brush=pg.mkBrush((27, 38, 59, 200))
                        )
        """

    def qplot_analyzed_image(self):
        """
        Plot the analyzed picket fence image
        """
        
        self.analyzed_image_plot_widget.clear()
        
        g_layout = self.analyzed_image_plot_widget.ci.layout

        tol_line_pen = pg.mkPen(color = (255, 0, 0), width = 2)

        if self.orientation == Orientation.UP_DOWN:
            self.analyzed_image_plot_widget.addLabel("<b>Analyzed picket fence image</b>", colspan = 2)
            self.analyzed_image_plot_widget.nextRow()

            image_plot_item = self.analyzed_image_plot_widget.addPlot(name="Image_Plot",
                                                                 row = 1,
                                                                 col = 0)
            error_plot_item = self.analyzed_image_plot_widget.addPlot(name = "Error_Plot",
                                                                 row = 1,
                                                                 col = 1)
            
            self.analyzed_image_plot_widget.nextRow()

            self.analyzed_image_plot_widget.addLabel('Maximum leaf pair error (mm)',
                                                     col = 1)
            
            image_plot_item.invertY(True)
            error_plot_item.invertY(True)
            xMax = self.tolerance if self.max_error < self.tolerance else self.max_error
            error_plot_item.setLimits(xMin = -0.01, xMax = xMax + 1.0)
            error_plot_item.setYLink('Image_Plot')
            
            g_layout.setColumnStretchFactor(0,2)
            g_layout.setColumnStretchFactor(1,1)

            tolerance_line = pg.InfiniteLine(pos = self.tolerance, pen = tol_line_pen,
                                             movable = False, angle=90)
            
        else:
            self.analyzed_image_plot_widget.addLabel("<b>Analyzed picket fence image</b>",
                                                     col = 1,
                                                     colspan = 2)
            
            self.analyzed_image_plot_widget.nextRow()

            image_plot_item = self.analyzed_image_plot_widget.addPlot(name="Image_Plot",
                                                                 row = 1,
                                                                 col = 1)
            
            self.analyzed_image_plot_widget.nextRow()

            self.analyzed_image_plot_widget.addLabel('Maximum leaf pair error (mm)',
                                                     row = 2,
                                                     col = 0,
                                                     angle = -90)

            error_plot_item = self.analyzed_image_plot_widget.addPlot(name = "Error_Plot",
                                                                 row = 2,
                                                                 col = 1)
            
            error_plot_item.setLimits(yMin = -0.01, yMax = self.tolerance + 1.5)
            error_plot_item.setXLink('Image_Plot')

            g_layout.setRowStretchFactor(1,2)
            g_layout.setRowStretchFactor(2,1)

            tolerance_line = pg.InfiniteLine(pos = self.tolerance, pen = tol_line_pen,
                                             movable = False, angle = 0)

        # limit image range to 50% beyond the bounds
        image_plot_item.setLimits(xMin = -self.image.shape[1] * 0.5, xMax = self.image.shape[1] * 1.5,
                                  yMin = -self.image.shape[0] * 0.5, yMax = self.image.shape[0] * 1.5)    
        image_plot_item.getViewBox().setAspectLocked(True)

        #------ Add image plot data
        image_plot_item.addItem(pg.ImageItem(self.image.array))

        #------ Add error plot data
        error_plot_item.addItem(tolerance_line)

        # add errors
        if self.orientation == Orientation.UP_DOWN:
            pos = [
                position.marker_lines[0].center.y
                for position in self.pickets[0].mlc_meas
            ]
            
        else:
            pos = [
                position.marker_lines[0].center.x
                for position in self.pickets[0].mlc_meas
            ]

        error_stdev = []
        error_vals = []
        
        for leaf_num in {m.leaf_num for m in self.mlc_meas}:
            error_vals.append(
                np.max(
                    [np.abs(m.error) for m in self.mlc_meas if m.leaf_num == leaf_num]
                )
            )
            error_stdev.append(
                np.std([m.error for m in self.mlc_meas if m.leaf_num == leaf_num])
            )

        pos = np.array(pos)
        error_stdev = np.array(error_stdev)
        error_vals = np.array(error_vals)

        bar_brush = (0, 0, 255, 100)

        if self.orientation == Orientation.UP_DOWN:
            error_bars = pg.ErrorBarItem(x = error_vals, y = pos,
                                         left = error_stdev, right = error_stdev, beam = 1.0)
            
            bars = pg.BarGraphItem(x0 = 0, x1 = error_vals,
                                   y = pos, y0 = pos - 2.5, y1 = pos + 2.5,
                                   brush= bar_brush)

            #error_plot_item.addItem(error_bars)
            error_plot_item.addItem(bars)

            # Add EPID CAX line here to make it above image
            epid_cax_line = pg.InfiniteLine(pos = self.image.shape[1]/2.0,
                                            pen = pg.mkPen('y', width=2.0),
                                            angle = 90)
            image_plot_item.addItem(epid_cax_line)
            
        else:
            error_bars = pg.ErrorBarItem(x = pos, y = error_vals,
                                         top = error_stdev, bottom = error_stdev, beam = 1.0)
            
            bars = pg.BarGraphItem(x=pos, height = error_vals, width = 5, brush= bar_brush)
            
            #error_plot_item.addItem(error_bars)
            error_plot_item.addItem(bars)

            # Add EPID CAX line here to make it above image
            epid_cax_line = pg.InfiniteLine(pos = self.image.shape[0]/2.0,
                                            pen = pg.mkPen('y', width=2.0),
                                            angle = 0)
            image_plot_item.addItem(epid_cax_line)

        # Add guard rails
        if self.orientation == Orientation.UP_DOWN:
            length = self.image.shape[0]
        else:
            length = self.image.shape[1]
    
        x_data = np.arange(length)

        guards_pen = pg.mkPen(color = (0, 255, 0), width = 1.5)

        for picket in self.pickets:

            left_y_data = picket.left_guard_separated
            right_y_data = picket.right_guard_separated
            
            left_y_data = [[f(x_data[0]), f(x_data[-1])] for f in left_y_data]
            right_y_data = [[f(x_data[0]), f(x_data[-1])] for f in right_y_data]

            x_data = [x_data[0],x_data[-1]]

            if self.orientation == Orientation.UP_DOWN:
                image_plot_item.multiDataPlot(x=left_y_data, y=x_data, 
                                              **{"pen": [guards_pen]*len(left_y_data)}
                                              )
                image_plot_item.multiDataPlot(x=right_y_data, y=x_data,
                                              **{"pen": [guards_pen]*len(left_y_data)}
                                              )

            else:
                image_plot_item.multiDataPlot(x=x_data, y=left_y_data,
                                              **{"pen": [guards_pen]*len(left_y_data)}
                                              )
                image_plot_item.multiDataPlot(x=x_data, y=right_y_data, 
                                              **{"pen": [guards_pen]*len(left_y_data)}
                                              )

        image_plot_item.disableAutoRange()
        now = time.time()
        # Add mlc peaks
        for mlc_meas in self.mlc_meas:
            # plot mlc peaks 
            for idx, line in enumerate(mlc_meas.marker_lines):
                
                curve = pg.PlotCurveItem(x=[line.point1.x, line.point2.x], y=[line.point1.y, line.point2.y],
                                         pen=pg.mkPen(color = mlc_meas.bg_color[idx], width = 2.0),
                                         skipFiniteCheck=False,
                                         )
                pg.arrayToQPath
                image_plot_item.addItem(curve)
                QCoreApplication.processEvents()
        
        image_plot_item.enableAutoRange()
        error_plot_item.autoRange()

        gc.collect()
        
    def qplot_leaf_profile(self, leaf: int | str, picket: int):
        """
        Plot the profile of a leaf
        """

        self.profile_plot_widget.clear()
        #self.legend.clear()

        mlc = Enumerable(self.mlc_meas).single(
            lambda m: leaf in m.full_leaf_nums and m.picket_num == picket)
        self.profile_plot_widget.getPlotItem().setTitle(f"Leaf error: {mlc.max_abs_error:2.3f} mm")

        #plot the pixel values 
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
                       pen = mlc.bg_color[0], label=f'MLC position ({pos:2.2f})', 
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
        #self.legend.addItem(mlc_pos_plot, "MLC position")
        #self.legend.addItem(picket_pos_plot, "Fitted picket position")

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

            #self.legend.addItem(lg_plot, "Guard rail")
            #self.legend.addItem(rg_plot, "Guard rail")

    def get_publishable_plot(self) -> io.BytesIO:
        """
        Custom plot implementation to get smaller, high quality pdf images
        """
        pf_plot_data = io.BytesIO()

        self.plot_analyzed_image(
            True,
            True,
            False,
            False,
            False,
        )

        plt.savefig(pf_plot_data, format = "pdf", pad_inches = 0.0, bbox_inches='tight')

        return pf_plot_data

class QPicketFenceWorker(QObject):

    analysis_progress = Signal(str)
    analysis_results_ready =  Signal(dict)
    thread_finished = Signal()
    analysis_failed = Signal(str)

    def __init__(self,filename: Union[str, list[str], Path, BinaryIO],
                 update_signal: Signal = None,
                 filter: Optional[int] = None,
                 log: Optional[str] = None,
                 use_filename: bool = False,
                 invert: bool = False,
                 mlc: Union[MLC, MLCArrangement, str] = MLC.MILLENNIUM,
                 crop_mm: int = 3,
                 nominal_gap: float = 3.0,
                 tolerance: float = 0.5,
                 separate_leaves: bool = False,
                 num_pickets: int | None = None,
                 image_kwargs: Optional[dict] = None,):
        super().__init__()

        self._filename = filename
        self._update_signal = update_signal
        self._filter = filter
        self._log = log
        self._use_filename = use_filename
        self._invert = invert
        self._mlc = mlc
        self._tolerance = tolerance
        self._crop_mm = crop_mm
        self._nominal_gap = nominal_gap
        self._num_pickets = num_pickets
        self._separate_leaves = separate_leaves
        self._image_kwargs = image_kwargs

        self._pf = QPicketFence(self._filename,
                          self._update_signal,
                          self._filter,
                          self._log,
                          self._use_filename,
                          self._mlc,
                          self._crop_mm,
                          image_kwargs = self._image_kwargs)

    @Slot()
    def analyze(self):
        """
        Perform an analysis of a picket fence image or series of picket fence images
        """
        try:
            self._pf.analyze(tolerance=self._tolerance, invert=self._invert, 
                             separate_leaves=self._separate_leaves, num_pickets=self._num_pickets, 
                             nominal_gap_mm=self._nominal_gap)

            summary_text = [["Gantry angle:", f"{self._pf.image.gantry_angle:2.2f}°"],
                       ["Collimator angle:", f"{self._pf.image.collimator_angle:2.2f}°"],
                       ["Number of leaves failing:", str(len(self._pf.failed_leaves()))],
                       ["Absolute median error:", f"{self._pf.abs_median_error:2.2f} mm"],
                       ["Mean picket spacing:", f"{self._pf.mean_picket_spacing:2.2f} mm"]]
            
            if self._separate_leaves:
                leaf_name = self._pf.max_error_leaf[0] + f"-{(int(self._pf.max_error_leaf[1:]) + 1)}"
                summary_text.append(["Max Error:", f"{self._pf.max_error:2.3f} mm " \
                 f"(Picket: {self._pf.max_error_picket + 1}, Leaf: {leaf_name})"])

            else:
                summary_text.append(["Max Error:", f"{self._pf.max_error:2.3f} mm " \
                 f"(Picket: {self._pf.max_error_picket + 1}, Leaf: {self._pf.max_error_leaf + 1})"])  
            
            results = {"summary_text": summary_text,
                       "picket_fence_obj": self._pf}
            
            self.analysis_results_ready.emit(results)
            self.thread_finished.emit()
        
        except Exception as err:
            self.analysis_failed.emit(traceback.format_exception_only(err)[-1])
            self.thread_finished.emit()
            raise err

def generate_picket_fence(
        simulator: Simulator,
        field_layer: type[FilterFreeFieldLayer | FilteredFieldLayer | PerfectFieldLayer],
        file_out: str,
        final_layers: list[Layer] = None,
        pickets: int = 11,
        picket_spacing_mm: int = 20,
        picket_width_mm: int = 2,
        picket_height_mm: int = 300,
        gantry_angle: int = 0,
        orientation: Orientation = Orientation.UP_DOWN,
        picket_offset_error: Sequence | None = None,
        image_rotation: float = 0.0
    ):

    picket_pos_mm = range(
        -int((pickets - 1) * picket_spacing_mm / 2),
        int((pickets - 1) * picket_spacing_mm / 2) + 1,
        picket_spacing_mm,
    )
    for idx, pos in enumerate(picket_pos_mm):
        if picket_offset_error is not None:
            if len(picket_offset_error) != pickets:
                raise ValueError(
                    "The length of the error array must be the same as the number of pickets."
                )
            pos += picket_offset_error[idx]
        if orientation == orientation.UP_DOWN:
            position = (0, pos)
            layout = (picket_height_mm, picket_width_mm)
        else:
            position = (pos, 0)
            layout = (picket_width_mm, picket_height_mm)
        simulator.add_layer(field_layer(layout, cax_offset_mm=position))
    if final_layers is not None:
        for layer in final_layers:
            simulator.add_layer(layer)

    # Rotate the image before DICOM generation
    simulator.image = ndimage.rotate(simulator.image, -image_rotation,
                                     reshape = False, mode = 'nearest')

    simulator.generate_dicom(file_out, gantry_angle=gantry_angle)
