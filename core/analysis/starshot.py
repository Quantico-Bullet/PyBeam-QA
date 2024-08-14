from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import Signal, Slot, QObject
from PySide6.QtGui import QTransform

import io
import traceback
import pyqtgraph as pg
import numpy as np
from typing import BinaryIO
from pylinac.core.geometry import Point
from pylinac.starshot import Starshot
from pylinac.settings import get_dicom_cmap

import matplotlib.pyplot as plt

pg.setConfigOptions(antialias = True, imageAxisOrder='row-major')

class QStarshot(Starshot):

    def __init__(self, filepath: str | BinaryIO, **kwargs):
        super().__init__(filepath, **kwargs)

        self.use_mm_units = True

        self.graphics_widget = pg.GraphicsLayoutWidget()
        self.plot_label = pg.LabelItem()
        self.img_plot_item = pg.PlotItem()
        self.img_plot_item.showAxes(True, showValues=(True, True, True, True))
        self.img_plot_item.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.img_plot_item.setAspectLocked(lock=True)
        self.img_plot_item.invertY(True)
        
        self.graphics_widget.addItem(self.plot_label, 0, 0)
        self.graphics_widget.addItem(self.img_plot_item, 1, 0)

        # Add actions to context menu
        context_menu = self.img_plot_item.getViewBox().menu
        context_menu.addSeparator()

        self.chg_axes_units_action = context_menu.addAction("Change axes units to mm or pixels")
        self.chg_axes_units_action.triggered.connect(lambda: self.set_axes_units(not self.use_mm_units))
        self.zoom_circle_action = context_menu.addAction("Zoom-in to minimum intersecting circle")
        #self.zoom_circle_action.triggered.connect(lambda: self.set_axes_units(not self.use_mm_units))
        self.show_profile_action = context_menu.addAction("Show starshot profile")
        self.show_profile_action.setCheckable(True)
        #self.show_profile_action.triggered.connect(lambda: self.set_axes_units(not self.use_mm_units))

    def analyze(self, 
                radius: float = 0.85,
                min_peak_height: float = 0.25,
                tolerance: float = 1,
                start_point: Point | tuple | None = None,
                fwhm: bool = True,
                recursive: bool = True,
                invert: bool = False):
        
        return super().analyze(radius, min_peak_height, tolerance, start_point, fwhm, recursive, invert)
    
    def plot_image(self):
        # plot the image
        self.image_dim = self.image.shape
        self.mm_per_dot = 1 / self.image.dpmm
        self.img_plot_item.addItem(pg.ImageItem(self.image.array))

        # plot the lines
        for line in self.lines:
            self.img_plot_item.plot(x = [line.point1.x, line.point2.x],
                                      y = [line.point1.y, line.point2.y],
                                      pen = pg.mkPen((255,0,255), width=1.5))
            
        # plot the circle profile
        width_ratio = self.circle_profile.width_ratio
        radius = self.circle_profile.radius
        center_x = self.circle_profile.center.x
        center_y = self.circle_profile.center.y
        x_outer = radius * (1 + width_ratio) * np.cos(np.linspace(0, 2*np.pi, 500)) + center_x
        y_outer = radius * (1 + width_ratio) * np.sin(np.linspace(0, 2*np.pi, 500)) + center_y
        self.img_plot_item.plot(x_outer, y_outer, pen = pg.mkPen((0, 255, 0), width = 2))

        x_outer = radius * (1 - width_ratio) * np.cos(np.linspace(0, 2*np.pi, 500)) + center_x
        y_outer = radius * (1 - width_ratio) * np.sin(np.linspace(0, 2*np.pi, 500)) + center_y

        self.img_plot_item.plot(x_outer, y_outer, pen = pg.mkPen((0, 255, 0), width = 2))

        # plot the wobble
        self.img_plot_item.addItem(
            pg.ScatterPlotItem([self.wobble.center.x], [self.wobble.center.y],
                           pen = pg.mkPen(None), brush = pg.mkBrush(0,0,200,150),
                           size = self.wobble.diameter, pxMode = False))
        self.img_plot_item.addItem(
            pg.ScatterPlotItem([self.wobble.center.x], [self.wobble.center.y],
                           pen = pg.mkPen(255,191,0), brush = pg.mkBrush(255,191,0,255),
                           size = self.wobble.diameter*0.02, pxMode = False))
        
        # plot the peaks
        peaks = self.circle_profile.peaks

        peak_x = [peak.x for peak in peaks]
        peak_y = [peak.y for peak in peaks]

        self.img_plot_item.addItem(pg.ScatterPlotItem(peak_x, peak_y,
                                                        size = 15, pxMode = False,
                                                        pen = pg.mkPen(None), brush = pg.mkBrush(255,0,255,150)))
        
        self.set_axes_units(self.use_mm_units)
        
    def set_axes_units(self, use_mm_units: bool):
        if use_mm_units:
            transform = QTransform() # The transformation to use
            transform.scale(self.mm_per_dot, self.mm_per_dot)
            transform.translate(-0.5*self.image_dim[1], -0.5*self.image_dim[0])

            for item in self.img_plot_item.items:
                item.setTransform(transform)

            self.img_plot_item.setLabel('left', '<b>Y CAX offset (mm)</b>')
            self.img_plot_item.setLabel('bottom', '<b>X CAX offset (mm)</b>')

            t_unit = "mm"
            diameter = self.wobble.diameter_mm
            x_coord = (self.wobble.center.x - 0.5*self.image_dim[1]) * self.mm_per_dot
            y_coord = (self.wobble.center.y - 0.5*self.image_dim[0]) * self.mm_per_dot      

        else:
            for item in self.img_plot_item.items:
                item.resetTransform()

            self.img_plot_item.setLabel('left', '<b>Y CAX offset (px)</b>')
            self.img_plot_item.setLabel('bottom', '<b>X CAX offset (px)</b>')
        
            t_unit = "px"
            diameter = self.wobble.diameter
            x_coord = self.wobble.center.x
            y_coord = self.wobble.center.y
        
        self.plot_label.setText(
            "<span style='color:powderblue'>"\
            f"<p><b>Diameter of minimum intersecting circle:</b> {diameter: 2.2f} {t_unit}</p>" \
            f"<p><b>Circle coordinates:</b> {x_coord:2.2f} {t_unit}, {y_coord:2.2f} {t_unit}</p>" \
            "</span>")
        self.use_mm_units = use_mm_units
        self.set_axes_ranges()

    def set_axes_ranges(self):
        if self.use_mm_units:
            xMin = -self.mm_per_dot * (0.5*self.image_dim[1]+350)
            xMax = self.mm_per_dot * (0.5*self.image_dim[1]+350)
            yMin = -self.mm_per_dot * (0.5*self.image_dim[0]+350)
            yMax = self.mm_per_dot * (0.5*self.image_dim[0]+350)
            xRange = (xMin + 50 * self.mm_per_dot, xMax - 50 * self.mm_per_dot)
            yRange = (yMin + 50 * self.mm_per_dot, yMax - 50 * self.mm_per_dot)
            
        else:
            xMin, yMin = -350, -350
            xMax, yMax= self.image_dim[1]+350, self.image_dim[0]+350
            xRange = (xMin + 50, xMax - 50)
            yRange = (yMin + 50, yMax - 50)
            
        self.img_plot_item.setRange(xRange=xRange, yRange=yRange)
        self.img_plot_item.setLimits(xMin=xMin, xMax=xMax, yMin=yMin, yMax=yMax)
        self.img_plot_item.autoRange()

    def get_publishable_plots(self) -> list[io.BytesIO]:
        """
        Custom plot implementation to get smaller, high quality pdf images
        """

        full_plot_data = io.BytesIO()
        wobble_plot_data = io.BytesIO()
        
        fig, ax = plt.subplots()
        # show analyzed image
        ax.imshow(self.image.array, cmap = get_dicom_cmap())
        self.lines.plot(ax)
        self.wobble.plot2axes(ax, edgecolor="green")
        self.circle_profile.plot2axes(ax, edgecolor="green")

        ax.axis('off')
        ax.set_aspect('auto')

        # Ensure that we fill the entire pdf page (pad_inches = 0.0  and box_inches = 'tight')
        fig.savefig(full_plot_data, format = "pdf", pad_inches = 0.0, bbox_inches='tight')

        x_limits = [self.wobble.center.x + self.wobble.diameter,
                    self.wobble.center.x - self.wobble.diameter]
        
        y_limits = [self.wobble.center.y + self.wobble.diameter,
                    self.wobble.center.y - self.wobble.diameter]
        
        ax.set_xlim(x_limits)
        ax.set_ylim(y_limits)

        fig.savefig(wobble_plot_data, format = "pdf", pad_inches = 0.0, bbox_inches='tight')

        return [full_plot_data, wobble_plot_data]

class QStarshotWorker(QObject):

    analysis_progress = Signal(str)
    analysis_results_ready =  Signal(dict)
    analysis_failed = Signal(str)
    thread_finished = Signal()

    def __init__(self, filepath: str | list[str],
                 radius: float = 0.85,
                 min_peak_height: float = 0.25,
                 tolerance: float = 1.0,
                 fwhm: bool = True,
                 recursive: bool = True,
                 invert: bool = False,
                 update_signal: Signal = None,
                 **kwargs):
        super().__init__()
        
        self._filepath = filepath
        self._radius = radius
        self._min_peak_height = min_peak_height
        self._tolerance = tolerance
        self._fwhm = fwhm
        self._recursive = recursive
        self._invert = invert
        self._update_signal = update_signal

        if type(self._filepath) == str:
            self.starshot = QStarshot(self._filepath, **kwargs)
        else:
            self.starshot = QStarshot.from_multiple_images(self._filepath, **kwargs)

    def analyze(self):
        try:
            self.starshot.analyze(radius = self._radius,
                              min_peak_height = self._min_peak_height,
                              tolerance = self._tolerance,
                              fwhm = self._fwhm,
                              recursive = self._recursive,
                              invert = self._invert)

            summary_text = [["Minimum circle (wobble) diameter:", 
                             f"{self.starshot.wobble.diameter_mm: 2.3f} mm"],
                             ["Position of the wobble circle:",
                              f"{self.starshot.wobble.center.x : 2.1f}, {self.starshot.wobble.center.y : 2.1f}"]]
        
            results = {"summary_text": summary_text,
                       "starshot_obj": self.starshot}
        
            self.analysis_results_ready.emit(results)
            self.thread_finished.emit()
        
        except Exception as err:
            self.analysis_failed.emit(traceback.format_exception_only(err)[-1])
            self.thread_finished.emit()

        
        