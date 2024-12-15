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

from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import Signal, Slot, QObject
from PySide6.QtGui import QTransform, QActionGroup, QIcon

import sys
import copy
import gc
import io
import traceback
import pyqtgraph as pg
import numpy as np
from typing import BinaryIO
from pylinac.core.geometry import Point
from pylinac.starshot import Starshot
from pylinac.settings import get_dicom_cmap

import matplotlib.pyplot as plt
from ui.py_ui import icons_rc

pg.setConfigOptions(antialias = True, imageAxisOrder='row-major')

class QStarshot(Starshot):

    def __init__(self, filepath: str | BinaryIO, **kwargs):
        super().__init__(filepath, **kwargs)

    def analyze(self, 
                radius: float = 0.85,
                min_peak_height: float = 0.25,
                tolerance: float = 1,
                start_point: Point | tuple | None = None,
                fwhm: bool = True,
                recursive: bool = True,
                invert: bool = False):
        return super().analyze(radius, min_peak_height, tolerance, start_point, fwhm, recursive, invert)

    def get_publishable_plots(self) -> list[io.BytesIO]:
        """
        Custom plot implementation to get smaller, high quality pdf images
        """

        full_plot_data = io.BytesIO()
        wobble_plot_data = io.BytesIO()
        
        fig, ax = plt.subplots()
        # show analyzed image
        self.image.plot(ax, show=False)
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
        
        ax.axis('on')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xlim(x_limits)
        ax.set_ylim(y_limits)

        fig.savefig(wobble_plot_data, format = "pdf", pad_inches = 0.0, bbox_inches='tight')
        plt.close()

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
        super().__init__(parent = None)
        
        self._filepath = filepath
        self._radius = radius
        self._min_peak_height = min_peak_height
        self._tolerance = tolerance
        self._fwhm = fwhm
        self._recursive = recursive
        self._invert = invert
        self._update_signal = update_signal
        self._kwargs = kwargs
        
    def analyze(self):
        try:
            if type(self._filepath) == str:
                self.starshot = QStarshot(self._filepath, **self._kwargs)
            else:
                self.starshot = QStarshot.from_multiple_images(self._filepath, **self._kwargs)

            self.starshot.analyze(radius = self._radius,
                              min_peak_height = self._min_peak_height,
                              tolerance = self._tolerance,
                              fwhm = self._fwhm,
                              recursive = self._recursive,
                              invert = self._invert)
            
            analysis_data = {};
            analysis_data["image"] = self.starshot.image
            analysis_data["wobble"] = self.starshot.wobble
            analysis_data["spoke_lines"] = self.starshot.lines
            analysis_data["star_profile"] = self.starshot.circle_profile
            analysis_data["report_plots"] = self.starshot.get_publishable_plots()

            self.analysis_results_ready.emit(analysis_data)

            del self.starshot
            gc.collect()
            self.thread_finished.emit()
        
        except Exception as err:
            self.analysis_failed.emit(traceback.format_exception_only(err)[-1])
            self.thread_finished.emit()
            raise err

        
        
