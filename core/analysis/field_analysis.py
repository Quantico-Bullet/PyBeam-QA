
from PySide6.QtCore import Signal, Slot, QObject

import io
import numpy as np
import pyqtgraph as pg
import traceback
from typing import BinaryIO, Tuple, Union

from pylinac.core.hill import Hill
from pylinac.core.profile import Edge, Interpolation, Normalization, SingleProfile
from pylinac.core.exceptions import NotAnalyzed
from pylinac.field_analysis import Centering, FieldAnalysis, Protocol

pg.setConfigOptions(antialias = True, imageAxisOrder='row-major')

class QFieldAnalysis(FieldAnalysis):

    def __init__(self, path: str | BinaryIO, 
                 filter: int | None = None, 
                 image_kwargs: dict | None = None):
        
        super().__init__(path, filter, image_kwargs)

        self.analyzed_image_plot_widget = pg.GraphicsLayoutWidget()

    def qplot_analyzed_image(self):
        self.analyzed_image_plot_widget.clear()

        g_layout = self.analyzed_image_plot_widget.ci.layout
        g_layout.setHorizontalSpacing(40)

        #------- Plot the image
        image_plot_item = self.analyzed_image_plot_widget.addPlot(title="<b>Analyzed image</b>",
                                                                  name = "Analyzed image",
                                                                  row = 0,
                                                                  rowspan = 2,
                                                                  col = 0)
        image_plot_item.invertY(True)
        image_plot_item.setLabel('left', 'Pixels')
        image_plot_item.setLabel('bottom', 'Pixels')
        
        image_plot_item.addItem(pg.ImageItem(self.image.array))

        #------- Add profile extraction regions
        width = abs(self._left_v_index - self._right_v_index)
        center = width/2+self._left_v_index
        width_h = abs(self._upper_h_index - self._lower_h_index)
        center_h = width_h / 2 + self._upper_h_index

        # vertical line (up-down)
        up_down_roi_line = pg.BarGraphItem(x = center, width = width,
                                           y = 0, y0 = 0, height = self.image.shape[0],
                                           pen = pg.mkPen(0, 0, 255),
                                           brush = pg.mkBrush((0, 0, 255, 150)))
        
        # horizontal line (left-right)
        left_right_roi_line = pg.BarGraphItem(x = 0, x0 = 0, width = self.image.shape[1],
                                              y = center_h, height = width_h,
                                              pen = pg.mkPen(0, 0, 255),
                                              brush = pg.mkBrush((0, 0, 255, 150)))
        
        image_plot_item.addItem(up_down_roi_line)
        image_plot_item.addItem(left_right_roi_line)
        image_plot_item.getViewBox().setAspectLocked(True)

        legend = image_plot_item.addLegend(offset=(10, 10), size = (50, 50))
        legend.addItem(up_down_roi_line, "Vert. profile extraction region")
        legend.addItem(left_right_roi_line, "Horiz. profile extraction region")

        vert_plot_item = self.analyzed_image_plot_widget.addPlot(title="<b>Vertical profile</b>",
                                                                  row = 0,
                                                                  col = 1)
        
        vert_plot_item.setLimits(yMin = -0.1, yMax = 1.5)

        hor_plot_item = self.analyzed_image_plot_widget.addPlot(title="<b>Horizontal profile</b>",
                                                                  row = 1,
                                                                  col = 1)
        hor_plot_item.setLimits(yMin = -0.1, yMax = 1.5)

        self.plot_profile(vert_plot_item, "vertical")
        self.plot_profile(hor_plot_item, "horizontal")

    def plot_profile(self, profile_plot: pg.PlotItem, profile_type: str):
        #------ Plot the profile

        if profile_type == "vertical":
            profile = self.vert_profile
            profile_labels = ["Top field edge", "Bottom field edge",
                              "T: In-field slope", "B: In-field slope"]
        else:
            profile = self.horiz_profile
            profile_labels = ["Left field edge", "Right field edge",
                              "L: In-field slope", "R: In-field slope"]
        
        profile_plot.setLabel('left', 'Normalized Response')
        profile_plot.setLabel('bottom', 'Pixels')
        profile_plot.addLegend()

        profile_plot.plot(profile.x_indices,
                            profile.values,
                            pen = pg.mkPen((254, 93, 38), width = 2.0))
        
        # plot the penumbra
        data = profile.penumbra(self._penumbra[0], self._penumbra[1])

        left_lower = data[f"left {self._penumbra[0]}% index (exact)"]
        left_lower_penumbra_plot = profile_plot.plot(x = [left_lower, left_lower],
                                                       y = [-5, 5],
                                                       pen = pg.mkPen(159, 204, 46))
        
        left_upper = data[f"left {self._penumbra[1]}% index (exact)"]
        left_upper_penumbra_plot = profile_plot.plot(x = [left_upper, left_upper],
                                                       y = [-5, 5],
                                                       pen = pg.mkPen(159, 204, 46))
        
        profile_plot.addItem(pg.FillBetweenItem(left_lower_penumbra_plot,
                                                  left_upper_penumbra_plot,
                                                  brush = (159, 204, 46, 100)))
        
        right_lower = data[f"right {self._penumbra[0]}% index (exact)"]
        right_lower_penumbra_plot = profile_plot.plot(x = [right_lower, right_lower],
                                                       y = [-5, 5],
                                                       pen = pg.mkPen(159, 204, 46))
        
        right_upper = data[f"right {self._penumbra[1]}% index (exact)"]
        right_upper_penumbra_plot = profile_plot.plot(x = [right_upper, right_upper],
                                                       y = [-5, 5],
                                                       pen = pg.mkPen(159, 204, 46))
        
        profile_plot.addItem(pg.FillBetweenItem(right_lower_penumbra_plot,
                                                  right_upper_penumbra_plot,
                                                  brush = (159, 204, 46, 100)))
        
        if self._edge_detection == Edge.INFLECTION_HILL:
            #Plot the hill fit
            fw = (
                profile.field_data(
                    in_field_ratio=1.0,
                    slope_exclusion_ratio=self._slope_exclusion_ratio,
                )["width (exact)"]
                * self._hill_window_ratio
                / 2
            )

            # plot right side Hill fit
            left_hill_idx = int(
                round(data[f"left {self._penumbra[0]}% index (exact)"] - fw)
            )
            right_hill_idx = int(
                round(data[f"left {self._penumbra[1]}% index (exact)"] + fw)
            )

            infl_data = profile.inflection_data()
            hill_fit = Hill.from_params(infl_data["left Hill params"])
            l_x_data = np.linspace(left_hill_idx, right_hill_idx, 200)

            profile_plot.plot(l_x_data, hill_fit.y(l_x_data), pen = pg.mkPen((191, 237, 239, 150),
                                                                               width = 3.0,
                                                                               connect = "finite"))
            
            # plot right side Hill fit
            left_hill_idx = int(
                round(data[f"right {self._penumbra[1]}% index (exact)"] - fw)
            )
            right_hill_idx = int(
                round(data[f"right {self._penumbra[0]}% index (exact)"] + fw)
            )

            hill_fit = Hill.from_params(infl_data["right Hill params"])
            r_x_data = np.linspace(left_hill_idx, right_hill_idx, 200)

            profile_plot.plot(r_x_data, hill_fit.y(r_x_data), pen = pg.mkPen((191, 237, 239, 150),
                                                                               width = 4.0,
                                                                               connect = "finite"))
            
        # plot field edges
        data = profile.field_data(
            in_field_ratio=1.0, slope_exclusion_ratio=self._slope_exclusion_ratio
        )

        profile_plot.plot([data["left index (rounded)"]], [data["left value (@rounded)"]],
                            symbolBrush = pg.mkBrush(128, 222, 217), symbolPen = 'w',
                            symbol='d', symbolSize = 14, name = profile_labels[0])
        
        profile_plot.plot([data["right index (rounded)"]], [data["right value (@rounded)"]],
                            symbolBrush = pg.mkBrush(128, 222, 217), symbolPen = 'w',
                            symbol='d', symbolSize = 14, name = profile_labels[1])
        
        if self._is_FFF:
            data = profile.field_data(self._in_field_ratio, self._slope_exclusion_ratio)
            x_model = np.linspace(
                data["left inner index (rounded)"],
                data["right inner index (rounded)"],
                1000,
            )

            y_model = (
                data["top params"][0] * x_model**2
                + data["top params"][1] * x_model
                + data["top params"][2]
            )

            # Plot the top part of the FFF beam
            profile_plot.plot(x_model, y_model,
                                pen = pg.mkPen((242, 222, 44, 150), width = 8, connect = 'finite'),
                                name = 'Top poly. fit')
            
            profile_plot.plot([data['"top" index (exact)']], [data['"top" value (@exact)']],
                                symbolBrush = pg.mkBrush(242, 222, 44), symbolPen = 'w',
                                symbol='t', symbolSize = 14, name = "Top (T) position")
            
            # Plot top/left slope
            left_x_values = range(data["left index (rounded)"], data["left inner index (rounded)"])
            left_y_values = data["left slope"] * left_x_values + data["left intercept"]

            profile_plot.plot(left_x_values, left_y_values,
                                     pen = pg.mkPen((25, 43, 194, 150), width = 8, connect= 'finite'),
                                     name = profile_labels[2])

            # Plot bottom/right slope
            right_x_values = range(data["right inner index (rounded)"], data["right index (rounded)"])
            right_y_values = data["right slope"] * right_x_values + data["right intercept"]

            profile_plot.plot(right_x_values, right_y_values,
                                     pen = pg.mkPen((25, 43, 194, 150), width = 8, connect= 'finite'),
                                     name = profile_labels[3])

    def format_text(self, text: str, font_size: int = 11, font_weight: str = "normal") -> str:
        text = f"<p><span style=\" font-weight: {font_weight}; font-size: {font_size}pt;\">" \
               f"{text}</span></p>"
        
        return text
    
    def results(self, as_str=True) -> str:
        """Get the results of the analysis.

        Parameters
        ----------
        as_str
            If True, return a simple string. If False, return a list of each line of text.
        """
        if not self._is_analyzed:
            raise NotAnalyzed("Image is not analyzed yet. Use analyze() first.")

        results = [
            "Field Analysis Results",
            "-----" * 10,
            f"File: {self._path}",
            f"Protocol: {self._protocol.name}",
        ]
        if not self._from_device:
            results += [
                f"Centering method: {self._centering.value}",
            ]
        results += [
            f"Normalization method: {self.horiz_profile._norm_method.value}",
            f"Interpolation: {self.horiz_profile._interp_method.value}",
            f"Edge detection method: {self.horiz_profile._edge_method.value}",
            "",
            f"Penumbra width ({self._penumbra[0]}/{self._penumbra[1]}):",
            "-----" * 10,
            f"Left: {self._results['left_penumbra_mm']:3.1f} mm",
            f"Right: {self._results['right_penumbra_mm']:3.1f} mm",
            f"Top: {self._results['top_penumbra_mm']:3.1f} mm",
            f"Bottom: {self._results['bottom_penumbra_mm']:3.1f} mm",
            "",
        ]
        if self._edge_detection == Edge.INFLECTION_HILL:
            results += [
                "Penumbra gradients:",
                "-----" * 10,
                f"Left gradient: {self._results['left_penumbra_percent_mm']:3.2f}% /mm",
                f"Right gradient: {self._results['right_penumbra_percent_mm']:3.2f}% /mm",
                f"Top gradient: {self._results['top_penumbra_percent_mm']:3.2f}% /mm",
                f"Bottom gradient: {self._results['bottom_penumbra_percent_mm']:3.2f}% /mm",
                "",
            ]
        results += [
            "Field Size:",
            "-----" * 10,
            f"Horizontal: {self._results['field_size_horizontal_mm']:3.1f} mm",
            f"Vertical: {self._results['field_size_vertical_mm']:3.1f} mm",
            "",
            "CAX to edge distances:",
            "-----" * 10,
            f"CAX -> Top edge: {self._results['cax_to_top_mm']:3.1f} mm",
            f"CAX -> Bottom edge: {self._results['cax_to_bottom_mm']:3.1f} mm",
            f"CAX -> Left edge: {self._results['cax_to_left_mm']:3.1f} mm",
            f"CAX -> Right edge: {self._results['cax_to_right_mm']:3.1f} mm",
            "",
        ]
        if not self._from_device:
            results += [
                "Central ROI stats:",
                "-----" * 10,
                f"Mean: {self.central_roi.mean:3.3f}",
                f"Max: {self.central_roi.max:3.3f}",
                f"Min: {self.central_roi.min:3.3f}",
                f"Standard deviation: {self.central_roi.std:3.3f}",
                "",
            ]
        if self._is_FFF:
            results += [
                "'Top' vertical distance from CAX: {:3.1f} mm".format(
                    self._results["top_vertical_distance_from_cax_mm"]
                ),
                "'Top' horizontal distance from CAX: {:3.1f} mm".format(
                    self._results["top_horizontal_distance_from_cax_mm"]
                ),
                "'Top' vertical distance from beam center: {:3.1f} mm".format(
                    self._results["top_vertical_distance_from_beam_center_mm"]
                ),
                "'Top' horizontal distance from beam center: {:3.1f} mm".format(
                    self._results["top_horizontal_distance_from_beam_center_mm"]
                ),
                "",
            ]
        results += [
            f"Top slope: {self._results['top_slope_percent_mm']:3.3f}% /mm",
            f"Bottom slope: {self._results['bottom_slope_percent_mm']:3.3f}% /mm",
            f"Left slope: {self._results['left_slope_percent_mm']:3.3f}% /mm",
            f"Right slope: {self._results['right_slope_percent_mm']:3.3f}% /mm",
            "",
            "Protocol data:",
            "-----" * 10,
        ]

        for name, item in self._protocol.value.items():
            results.append(
                f"Vertical {name}: {self._extra_results[name + '_vertical']:3.3f}{item['unit']}"
            )
            results.append(
                f"Horizontal {name}: {self._extra_results[name + '_horizontal']:3.3f}{item['unit']}"
            )
            results.append("")

        if as_str:
            results = "\n".join(result for result in results)
        return results

    def get_publishable_results(self) -> dict:
        results = {}

        results[f"Penumbra widths ({self._penumbra[0]}/{self._penumbra[1]}):"] = [
            ["Left width", f"{self._results['left_penumbra_mm']:3.1f} mm"],
            ["Right width", f"{self._results['right_penumbra_mm']:3.1f} mm"],
            ["Top width", f"{self._results['top_penumbra_mm']:3.1f} mm"],
            ["Bottom width", f"{self._results['bottom_penumbra_mm']:3.1f} mm"]
        ]

        if self._edge_detection == Edge.INFLECTION_HILL:
            
            results["Penumbra gradients:"] = [
                ["Left gradient",f"{self._results['left_penumbra_percent_mm']:3.2f}% /mm"],
                ["Right gradient", f"{self._results['right_penumbra_percent_mm']:3.2f}% /mm"],
                ["Top gradient", f"{self._results['top_penumbra_percent_mm']:3.2f}% /mm"],
                ["Bottom gradient", f"{self._results['bottom_penumbra_percent_mm']:3.2f}% /mm"],
            ]
        
        results["Field Size:"] = [
            ["Horizontal", f"{self._results['field_size_horizontal_mm']:3.1f} mm"],
            ["Vertical", f"{self._results['field_size_vertical_mm']:3.1f} mm"]
        ]

        results["CAX to edge distances:"] = [
            ["CAX to top edge", f"{self._results['cax_to_top_mm']:3.1f} mm"],
            ["CAX to bottom edge", f"{self._results['cax_to_bottom_mm']:3.1f} mm"],
            ["CAX to left edge", f"{self._results['cax_to_left_mm']:3.1f} mm"],
            ["CAX to right edge", f"{self._results['cax_to_right_mm']:3.1f} mm"],
        ]

        if not self._from_device:
            results["Central ROI statistics:"] = [
                ["Mean", f"{self.central_roi.mean:3.3f}"],
                ["Max", f"{self.central_roi.max:3.3f}"],
                ["Min", f"{self.central_roi.min:3.3f}"],
                ["Standard deviation", f"{self.central_roi.std:3.3f}"],
            ]

        if self._is_FFF:
            results["Central ROI statistics:"].extend([
                ["", ""],
                ["Top vertical distance from CAX", "{:3.1f} mm".format(
                    self._results["top_vertical_distance_from_cax_mm"]
                )],
                ["Top horizontal distance from CAX", "{:3.1f} mm".format(
                    self._results["top_horizontal_distance_from_cax_mm"]
                )],
                ["Top vertical distance from beam center", "{:3.1f} mm".format(
                    self._results["top_vertical_distance_from_beam_center_mm"]
                )],
                ["Top horizontal distance from beam center", "{:3.1f} mm".format(
                    self._results["top_horizontal_distance_from_beam_center_mm"]
                )],
            ])

        results["Central ROI statistics:"].extend([
            ["", ""],
            ["Top slope", f"{self._results['top_slope_percent_mm']:3.3f}% /mm"],
            ["Bottom slope", f"{self._results['bottom_slope_percent_mm']:3.3f}% /mm"],
            ["Left slope", f"{self._results['left_slope_percent_mm']:3.3f}% /mm"],
            ["Right slope", f"{self._results['right_slope_percent_mm']:3.3f}% /mm"]
        ])

        results["Protocol data:"] = []

        for name, item in self._protocol.value.items():
            results["Protocol data:"].extend([
                [f"Vertical {name}", f"{self._extra_results[name + '_vertical']:3.3f}{item['unit']}"],
                [f"Horizontal {name}", f"{self._extra_results[name + '_horizontal']:3.3f}{item['unit']}"]
            ])

        return results


    def get_publishable_plots(self) -> list[io.BytesIO]:
        # set files for the vertical and horizontal profile plots
        # setting figsize = (4.5, 4.5) seems to do wonders on the produced pdf
        # TODO code does not apply for device analysis
        files = [io.BytesIO(), io.BytesIO()]
        figs, names = self.plot_analyzed_image(
            show = False, split_plots=True, figsize = (4.5 ,4.5)
        )

        figs[1].savefig(files[0], format = "pdf") # vertical profile
        figs[2].savefig(files[1], format = "pdf") # horizontal profile

        return files

class QFieldAnalysisWorker(QObject):

    analysis_progress = Signal(str)
    analysis_results_ready =  Signal(dict)
    thread_finished = Signal()
    analysis_failed = Signal(str)

    def __init__(self,
                 path: str,
                 protocol: Protocol = Protocol.VARIAN,
                 centering: Centering | str = Centering.BEAM_CENTER,
                 vert_position: float = 0.5,
                 horiz_position: float = 0.5, 
                 vert_width: float = 0, 
                 horiz_width: float = 0, 
                 in_field_ratio: float = 0.8,
                 slope_exclusion_ratio: float = 0.2, 
                 invert: bool = False, 
                 is_FFF: bool = False, 
                 penumbra: Tuple[float, float] = ..., 
                 interpolation: Interpolation | str | None = Interpolation.LINEAR, 
                 interpolation_resolution_mm: float = 0.1, 
                 ground: bool = True,
                 normalization_method: Normalization | str = Normalization.BEAM_CENTER, 
                 edge_detection_method: Edge | str = Edge.INFLECTION_DERIVATIVE, 
                 edge_smoothing_ratio: float = 0.003, 
                 hill_window_ratio: float = 0.15):
        
        super().__init__()

        self._protocol = protocol
        self._centering = centering
        self._vert_position = vert_position
        self._horiz_position = horiz_position
        self._vert_width = vert_width
        self._horiz_width = horiz_width
        self._in_field_ratio = in_field_ratio
        self._slope_exclusion_ratio = slope_exclusion_ratio
        self._invert = invert
        self._is_FFF = is_FFF
        self._penumbra = penumbra
        self._interpolation = interpolation
        self._interpolation_res_mm = interpolation_resolution_mm
        self._ground = ground
        self._normalization_method = normalization_method
        self._edge_detection_method = edge_detection_method
        self._edge_smoothing_ratio = edge_smoothing_ratio
        self._hill_window_ratio = hill_window_ratio

        self._fa = QFieldAnalysis(path)

    def analyze(self):

        try:
            self._fa.analyze(protocol = self._protocol,
                             centering = self._centering,
                             vert_position = self._vert_position,
                             horiz_position = self._horiz_position,
                             vert_width = self._vert_width,
                             horiz_width = self._horiz_width,
                             in_field_ratio = self._in_field_ratio,
                             slope_exclusion_ratio = self._slope_exclusion_ratio,
                             invert = self._invert,
                             is_FFF = self._is_FFF,
                             interpolation = self._interpolation,
                             interpolation_resolution_mm = self._interpolation_res_mm,
                             normalization_method = self._normalization_method,
                             ground = self._ground,
                             edge_detection_method = self._edge_detection_method,
                             edge_smoothing_ratio = self._edge_smoothing_ratio,
                             hill_window_ratio = self._hill_window_ratio)

            data = self._fa.results()
            
            results = {"summary_text": data,
                       "field_analysis_obj": self._fa}

            self.analysis_results_ready.emit(results)
            self.thread_finished.emit()
            
        except Exception as err:
            self.analysis_failed.emit(traceback.format_exception_only(err)[-1])
            self.thread_finished.emit()
