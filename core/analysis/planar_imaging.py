from PySide6.QtCore import Signal, Slot, QObject

from pylinac.planar_imaging import (ImagePhantomBase, LeedsTOR, LeedsTORBlue, LasVegas,
                                    SNCkV, SNCMV, SNCMV12510, PTWEPIDQC, IBAPrimusA,
                                    DoselabMC2kV, DoselabMC2MV, StandardImagingQC3,
                                    StandardImagingQCkV)
from pylinac.core.contrast import Contrast
from pylinac.core.geometry import Circle, Rectangle

from matplotlib.patches import Rectangle as MatplotRect
from pathlib import Path
from typing import BinaryIO

import numpy as np
import pyqtgraph as pg
import enum
import traceback

class PHANTOM(enum.Enum):
    DOSELAB_MC2_KV = "Doselab MC2 kV"
    DOSELAB_MC2_MV = "Doselab MC2 MV"
    IBA_PRIMUS_A = "IBA Primus A"
    LAS_VEGAS = "Las Vegas"
    LEEDS_TOR_RED = "Leeds TOR 18 (Red)"
    LEEDS_TOR_BLUE = "Leeds TOR 18 (Blue)"
    PTW_EPID_QC = "PTW EPID QC"
    SNC_MV = "SNC MV"
    SNC_MV_12510 = "SNC MV (12510)"
    SNC_KV = "SNC kV"
    STANDARD_IMAGING_QC3 = "Standard Imaging QC-3 MV"
    STANDARD_IMAGING_QC_KV = "Standard Imaging QC kV"

class QPlanarImaging():

    def __init__(self, phantom: ImagePhantomBase):
        self._phantom = phantom

        # Widgets for analyzed image plots
        self.analyzed_image_plot_widget = pg.GraphicsLayoutWidget()
        g_layout = self.analyzed_image_plot_widget.ci.layout

        # Add the image plot 
        self.image_plot = self.analyzed_image_plot_widget.addPlot(name="Image_Plot",
                                                                  title="<b>Analyzed image</b>",
                                                                  row = 1,
                                                                  col = 0,
                                                                  colspan=2)
        self.image_plot.setLabel("left", "Pixel")
        self.image_plot.setLabel("bottom", "Pixel")
        self.image_plot.invertY(True)
        self.image_plot.addLegend(size = (50,50), pen=pg.mkPen(13, 27, 42),
                                  labelTextColor='w', brush=pg.mkBrush((27, 38, 59, 200)))
        
        # Add low contrast plot
        self.low_contr_plot = self.analyzed_image_plot_widget.addPlot(name="Low_Contrast_Plot",
                                                                  title="<b>Low frequency constrast</b>",
                                                                  row = 1,
                                                                  col = 2)
        self.low_contr_plot.setLabel('left', "Contrast")
        self.low_contr_plot.setLabel('bottom', "ROI #")
        
        # Add high frequency plot
        self.high_freq_plot = self.analyzed_image_plot_widget.addPlot(name="High_Frequency_Plot",
                                                                  title="<b>High frequency rMTF</b>",
                                                                  row = 1,
                                                                  col = 3)
        self.high_freq_plot.setLabel('left', "relative MTF")
        self.high_freq_plot.setLabel('bottom', "Line pairs / mm")

        g_layout.setColumnStretchFactor(0,2)

    def qplot_analyzed_image(self):
        self.image_plot.clear()
        self.low_contr_plot.clear()
        self.high_freq_plot.clear()

        #-------- Plot the image and phantom outline (if any) --------
        self.image_plot.addItem(pg.ImageItem(self._phantom.image.array))

        if self._phantom.phantom_outline_object is not None:
            outline_obj, settings = self._phantom._create_phantom_outline_object()

            if isinstance(outline_obj, Circle):
                outline_x_data = outline_obj.radius*np.cos(np.linspace(0, 2*np.pi, 500)) + outline_obj.center.x
                outline_y_data = outline_obj.radius*np.sin(np.linspace(0, 2*np.pi, 500)) + outline_obj.center.y

                self.image_plot.plot(outline_x_data, outline_y_data, pen = pg.mkPen((252, 163, 17), width=2.5),
                                     name = "Phantom outline")
            
            elif isinstance(outline_obj, Rectangle):
                
                rect = MatplotRect((outline_obj.bl_corner.x, outline_obj.bl_corner.y),
                                   width=outline_obj.width,
                                   height=outline_obj.height,
                                   angle=settings["angle"]
                                   )
                
                data = rect.get_verts()
                
                self.image_plot.plot(data, pen = pg.mkPen((252, 163, 17), width=2.5),
                                     name = "Phantom Outline")
                
        #-------- Plot a symbol for the center of the phantom --------
        self.image_plot.plot([self._phantom.phantom_center.x], [self._phantom.phantom_center.y],
                             symbolBrush = (206, 255, 26), symbol="o", symbolSize=14,
                             symbolPen = pg.mkPen((0,0,0), width=2.5), name="Phantom Center",
                             pen = pg.mkPen((0,0,0), width=2.5))

        #-------- Plot the low, high contrast ROIs and their contrast/MTF graphs --------
        if any(self._phantom.low_contrast_rois):
            for num, roi in enumerate(self._phantom.low_contrast_background_rois):
                roi_x_data = roi.radius * np.cos(np.linspace(0, 2*np.pi, 500)) + roi.center.x
                roi_y_data = roi.radius * np.sin(np.linspace(0, 2*np.pi, 500)) + roi.center.y

                self.image_plot.plot(roi_x_data, roi_y_data,
                                     pen = pg.mkPen((2, 116, 162), width=2.0),
                                     name = f"Low Contrast Background ROI #{num + 1}")
            
            data_x = []
            data_y = []

            for num, roi in enumerate(self._phantom.low_contrast_rois):
                # ROI outlines
                roi_x_data = roi.radius * np.cos(np.linspace(0, 2*np.pi, 500)) + roi.center.x
                roi_y_data = roi.radius * np.sin(np.linspace(0, 2*np.pi, 500)) + roi.center.y

                self.image_plot.plot(roi_x_data, roi_y_data,
                                     pen = pg.mkPen(color = roi.plot_color, width=2.0))
                
                text = pg.TextItem(text=f"L-{num + 1}", color="w", anchor=(0.5,0.5), fill=roi.plot_color)
                text.setPos(roi.center.x, roi.center.y - roi.radius)

                self.image_plot.addItem(text)

                data_x.append(num + 1)
                data_y.append(roi.contrast)

            # Contrast graph
            self.low_contr_plot.plot(data_x, data_y, symbolBrush = (183, 195, 243), symbol="o", symbolSize=12,
                                     symbolPen = None,
                                     pen = pg.mkPen((183, 195, 243), width=2.0))
            
            self.low_contr_plot.addItem(pg.InfiniteLine(pos = self._phantom._low_contrast_threshold, pen = 'r',
                                                        movable = False, angle=0))
        
        else:
            self.low_contr_plot.hide()

        if any(self._phantom.high_contrast_rois):
            for num, (roi, mtf) in enumerate(
                zip(self._phantom.high_contrast_rois, self._phantom.mtf.norm_mtfs.values())
            ):
                
                color = 'green' if mtf > self._phantom._high_contrast_threshold else 'red'

                roi_x_data = roi.radius * np.cos(np.linspace(0, 2*np.pi, 500)) + roi.center.x
                roi_y_data = roi.radius * np.sin(np.linspace(0, 2*np.pi, 500)) + roi.center.y

                self.image_plot.plot(roi_x_data, roi_y_data,
                                     pen = pg.mkPen(color = color, width=2.0))
                
                text = pg.TextItem(text=f"H-{num + 1}", color="w", anchor=(0.5,0.5), fill=color)
                text.setPos(roi.center.x, roi.center.y - roi.radius)

                self.image_plot.addItem(text)

            # High frequency rMTF graph
            self.high_freq_plot.plot(self._phantom.mtf.spacings, list(self._phantom.mtf.norm_mtfs.values()),
                                     symbolBrush = (183, 195, 243), symbol="d", symbolSize=12,
                                     symbolPen = None, pen = pg.mkPen((183, 195, 243), width=2.0))
            
            self.high_freq_plot.addItem(pg.InfiniteLine(pos = self._phantom._high_contrast_threshold, pen = 'r',
                                                        movable = False, angle=0))
            
        else:
            self.high_freq_plot.hide()

class QPlanarImagingWorker(QObject):

    analysis_progress = Signal(str)
    analysis_results_ready =  Signal(dict)
    thread_finished = Signal()
    analysis_failed = Signal(str)

    def __init__(self, phantom_name: str,
                 filepath: str | BinaryIO | Path,
                 normalize: bool = True,
                 low_contrast_threshold: float = 0.05,
                 high_contrast_threshold: float = 0.5,
                 invert: bool = False,
                 angle_override: float | None = None,
                 center_override: tuple | None = None,
                 size_override: float | None = None,
                 ssd: float = 1000,
                 low_contrast_method: str = Contrast.MICHELSON,
                 visibility_threshold: float = 100,
                 image_kwargs: dict | None = None):
        super().__init__()

        self._angle_override = angle_override
        self._size_override = size_override
        self._center_override = center_override
        self._high_contrast_threshold = high_contrast_threshold
        self._low_contrast_threshold = low_contrast_threshold
        self._low_contrast_method = low_contrast_method
        self._invert = invert
        self._visibility_threshold = visibility_threshold
        self._ssd = ssd

        if phantom_name == PHANTOM.LEEDS_TOR_RED.value:
            self._phantom = LeedsTOR(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.LEEDS_TOR_BLUE.value:
            self._phantom = LeedsTORBlue(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.STANDARD_IMAGING_QC3.value:
            self._phantom = StandardImagingQC3(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.STANDARD_IMAGING_QC_KV.value:
            self._phantom = StandardImagingQCkV(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.DOSELAB_MC2_MV.value:
            self._phantom = DoselabMC2MV(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.DOSELAB_MC2_KV.value:
            self._phantom =  DoselabMC2kV(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.SNC_MV.value:
            self._phantom = SNCMV(filepath, normalize, image_kwargs)
        
        elif phantom_name == PHANTOM.SNC_MV_12510.value:
            self._phantom = SNCMV12510(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.SNC_KV.value:
            self._phantom = SNCkV(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.IBA_PRIMUS_A.value:
            self._phantom = IBAPrimusA(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.PTW_EPID_QC.value:
            self._phantom = PTWEPIDQC(filepath, normalize, image_kwargs)

        elif phantom_name == PHANTOM.LAS_VEGAS.value:
            self._phantom = LasVegas(filepath, normalize, image_kwargs)

        else:
            raise ValueError("Invalid phantom name passsed. Pass one of the following: " +
                             str.join(", ", [x for x in PHANTOM]))
        
        self._planar_img = QPlanarImaging(self._phantom)
    
    @Slot()
    def analyze(self):
        """
        Perform an analysis of a phantom image from a 2D kV or MV linac imager.
        """
        try:
            self._phantom.analyze(low_contrast_method=self._low_contrast_method,
                                  low_contrast_threshold=self._low_contrast_threshold,
                                  high_contrast_threshold=self._high_contrast_threshold,
                                  visibility_threshold=self._visibility_threshold,
                                  invert=self._invert,
                                  center_override=self._center_override,
                                  angle_override=self._angle_override,
                                  size_override=self._size_override,
                                  ssd=self._ssd
                                  )
            
            results_data = self._phantom.results_data()
            
            summary_text = [["No. of low contrast ROI found:", str(results_data.num_contrast_rois_seen)],
                            ["Phantom center (X):", f"{results_data.phantom_center_x_y[0]}"],
                            ["Phantom center (Y):", f"{results_data.phantom_center_x_y[1]}"],
                            ["Median contrast:", f"{results_data.median_contrast: 2.2f}"],
                            ["Median CNR:", f"{results_data.median_cnr: 2.2f}"]
            ]

            if self._phantom.mtf is not None:
                summary_text.append(["MTF 80% (lp/mm):", f"{results_data.mtf_lp_mm[0][80]: 2.2f}"])
                summary_text.append(["MTF 50% (lp/mm):", f"{results_data.mtf_lp_mm[1][50]: 2.2f}"])
                summary_text.append(["MTF 30% (lp/mm):", f"{results_data.mtf_lp_mm[2][30]: 2.2f}"])

            results = {"summary_text": summary_text,
                       "planar_img_obj": self._planar_img}

            self.analysis_results_ready.emit(results)
            self.thread_finished.emit()
            
        except Exception as err:
            self.analysis_failed.emit(traceback.format_exception_only(err)[-1])
            self.thread_finished.emit()

            raise err