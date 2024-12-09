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
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from PySide6.QtWidgets import (QWidget, QLabel, QProgressBar, QVBoxLayout, QFileDialog,
                               QListWidgetItem, QMenu, QSizePolicy, QMessageBox, 
                               QMainWindow, QFormLayout, QComboBox,
                               QDialog, QDialogButtonBox, QLineEdit, QSpacerItem,
                               QPushButton, QCheckBox, QHBoxLayout, QPlainTextEdit,
                               QDateEdit)
from PySide6.QtGui import QIcon, QPixmap, QActionGroup, QTransform
from PySide6.QtCore import Qt, QSize, QEvent, QThread, Signal, QDate

from ui.py_ui import icons_rc
from ui.py_ui.starshot_worksheet_ui import Ui_QStarshotWorksheet
from ui.util_widgets import worksheet_save_report
from ui.util_widgets.dialogs import MessageDialog
from ui.util_widgets.statusbar import AnalysisInfoLabel
from ui.linac_qa.starshot_test_dialog import StarshotTestDialog
from ui.linac_qa.qa_tools_win import QAToolsWindow
from core.tools.report import StarshotReport
from core.tools.devices import DeviceManager
from core.analysis.starshot import QStarshotWorker

from pylinac.core.image import load
from pylinac.core.image_generator import (GaussianFilterLayer,
                                          FilteredFieldLayer,
                                          AS500Image,
                                          AS1000Image,
                                          AS1200Image)

from scipy import ndimage

import numpy as np
import traceback
import platform
import webbrowser
import subprocess
import pyqtgraph as pg
from pathlib import Path

from copy import copy

class StarshotMainWindow(QAToolsWindow):

    analysis_info_signal = Signal(dict)
    
    def __init__(self, initData: dict = None):
        super().__init__(initData)

        self.window_title = "Starshot Analysis ‒ PyBeam QA"
        self.setWindowTitle(self.window_title)

        self.add_new_worksheet()

        self.ui.menuFile.addAction("Add Image(s)", self.ui.tabWidget.currentWidget().add_files)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction("Add New Worksheet", self.add_new_worksheet)
        self.ui.menuTools.addAction("Benchmark Test", self.init_test_dialog, "Ctrl+T")

    def init_test_dialog(self):
        dialog = StarshotTestDialog()
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            sim_image = dialog.ui.sim_image_cb.currentText()
            
            if sim_image == "AS500":
                sim_image = AS500Image()
            
            elif sim_image == "AS1000":
                sim_image = AS1000Image()
            
            else: sim_image = AS1200Image()

            num_spokes = dialog.ui.num_spokes_sb.value()
            cax_offset = dialog.ui.cax_offset_dsb.value()

            for _ in range(num_spokes):
                sim_image.add_layer(FilteredFieldLayer((200, 5),
                                    alpha=0.5,
                                    cax_offset_mm = (cax_offset, cax_offset)))
                
                sim_image.image = ndimage.rotate(sim_image.image,
                                                 360 / num_spokes,
                                                 reshape = False,
                                                 mode = 'nearest')
                
            sim_image.add_layer(GaussianFilterLayer(sigma_mm = 3))
            sim_image.generate_dicom(dialog.ui.out_file_le.text())

            self.add_new_worksheet(dialog.ui.test_name_le.text() + " (Test)")
            self.ui.tabWidget.currentWidget().add_files([dialog.ui.out_file_le.text()])

    def add_new_worksheet(self, worksheet_name: str = None, enable_icon: bool = True):
        if worksheet_name is None:
            self.untitled_counter = self.untitled_counter + 1
            worksheet_name = f"Starshot (Untitled-{self.untitled_counter})"

        return super().add_new_worksheet(QStarshotWorksheet(), worksheet_name, enable_icon)

class QStarshotWorksheet(QWidget):

    analysis_info_signal = Signal(dict)
    save_info_signal = Signal(dict)

    def __init__(self):
        super().__init__()

        self.ui = Ui_QStarshotWorksheet()
        self.ui.setupUi(self)

        self.image_icon = QIcon()
        self.image_icon.addFile(u":/colorIcons/icons/picture.png", QSize(), QIcon.Normal, QIcon.Off)

        self.form_layout = QFormLayout()
        self.form_layout.setHorizontalSpacing(40)
        self.ui.analysisInfoVL.addLayout(self.form_layout)

        self.ui.analyzeBtn.setText("Analyze image(s)")
        self.ui.genReportBtn.setEnabled(False)

        #--------  add widgets --------
        self.progress_vl = QVBoxLayout()
        self.progress_vl.setSpacing(10)

        self.ui.analysisInfoVL.addLayout(self.progress_vl)

        # setup context menu for image list widget
        self.img_list_contextmenu = QMenu()
        self.img_list_contextmenu.addAction("View Original Image", self.view_dicom_image, "Ctrl+I")
        self.img_list_contextmenu.addAction("Show Containing Folder", self.open_file_folder)
        self.remove_file_action = self.img_list_contextmenu.addAction("Remove from List", self.remove_file)
        self.delete_file_action = self.img_list_contextmenu.addAction("Delete", self.delete_file)
        self.img_list_contextmenu.addAction("Properties")
        self.img_list_contextmenu.addSeparator()
        self.select_all_action = self.img_list_contextmenu.addAction("Select All", lambda: self.perform_selection("selectAll"), "Ctrl+A")
        self.select_all_action.setIcon(QIcon(u":/actionIcons/icons/select_all.svg"))
        self.unselect_all_action = self.img_list_contextmenu.addAction("Unselect All", lambda: self.perform_selection("unselectAll"),
                                                                        "Ctrl+Shift+A")
        self.unselect_all_action.setIcon(QIcon(u":/actionIcons/icons/deselect.svg"))
        self.invert_select_action = self.img_list_contextmenu.addAction("Invert Selection", lambda: self.perform_selection("invertSelection"))
        self.img_list_contextmenu.addSeparator()
        self.remove_selected_files_action = self.img_list_contextmenu.addAction("Remove Selected Files", self.remove_selected_files)
        self.remove_all_files_action = self.img_list_contextmenu.addAction("Remove All Files", self.remove_all_files)
        self.ui.imageListWidget.installEventFilter(self)

        #Add all context menu actions to this widget to use shortcuts
        self.addActions(self.img_list_contextmenu.actions())

        self.analysis_progress_bar = QProgressBar()
        self.analysis_progress_bar.setRange(0,0)
        self.analysis_progress_bar.setTextVisible(False)
        self.analysis_progress_bar.setMaximumSize(300, 10)
        self.analysis_progress_bar.setMinimumSize(300, 10)
        self.analysis_progress_bar.hide()

        self.analysis_message_label = QLabel("Analysis in progress")
        self.analysis_message_label.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred))
        self.analysis_message_label.hide()

        self.progress_vl.addWidget(self.analysis_progress_bar, 0, Qt.AlignHCenter)
        self.progress_vl.addWidget(self.analysis_message_label, 0, Qt.AlignHCenter)

        #--------  connect slots -------- 
        self.ui.addImgBtn.clicked.connect(self.add_files)
        self.ui.analyzeBtn.clicked.connect(self.start_analysis)
        self.ui.genReportBtn.clicked.connect(self.generate_report)
        self.ui.imageListWidget.itemChanged.connect(self.update_marked_images)
        self.ui.toleranceDSB.valueChanged.connect(self.set_analysis_outcome)

        #-------- init defaults --------
        self.marked_images = []
        self.current_plot = None
        self.analysis_data = None
        self.imageView_windows = []
        self.advanced_results_view = None
        self.analysis_in_progress = False
        self.has_analysis = False

        self.setup_config()
        self.update_marked_images()
        self.set_analysis_outcome()

        #Set analysis state and message for status bar
        self.analysis_message = None
        self.analysis_state = AnalysisInfoLabel.IDLE

        # Set initial session save info
        self.report_author = ""
        self.report_institution = ""
        self.report_date = QDate.currentDate()
        self.save_path = ""
        self.save_comment = ""

        self.init_plot_graphics()

    def init_plot_graphics(self) -> None:

        self.use_mm_units = True

        self.graphics_widget = pg.GraphicsLayoutWidget()
        self.plot_label = pg.LabelItem()
        self.img_plot_item = pg.PlotItem()
        self.img_plot_item.showAxes(True, showValues=(True, True, True, True))
        self.img_plot_item.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.img_plot_item.setAspectLocked(lock=True)
        self.img_plot_item.invertY(True)
        self.profile_plot_item = pg.PlotItem()
        self.profile_plot_item.showAxes(True, showValues=(True, True, True, True))
        self.profile_plot_item.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.profile_plot_item.setLabel('left', '<b>Normalised pixel value</b>')
        self.profile_plot_item.setLabel('bottom', '<b>A.U</b>')
        self.profile_plot_item.setLimits(xMin=-10, xMax=370, yMin=-0.05, yMax=1.05)
        
        self.graphics_widget.addItem(self.plot_label, 0, 0)
        self.graphics_widget.addItem(self.img_plot_item, 1, 0)

        # Add actions to context menus
        img_context_menu = self.img_plot_item.getViewBox().menu
        img_context_menu.addSeparator()

        prof_context_menu = self.profile_plot_item.getViewBox().menu
        prof_context_menu.addSeparator()

        self.chg_axes_units_action = img_context_menu.addAction("Change Axes Units To mm Or pixels")
        self.chg_axes_units_action.setIcon(QIcon(u":/actionIcons/icons/transform.svg"))
        self.chg_axes_units_action.triggered.connect(lambda: self.set_axes_units(not self.use_mm_units))
        self.zoom_circle_action = img_context_menu.addAction("Zoom-In To Minimum Intersecting Circle")
        self.zoom_circle_action.setIcon(QIcon(u":/actionIcons/icons/zoom_pan.svg"))
        self.zoom_circle_action.triggered.connect(self.zoom_to_circle)

        # Add action items to starshot view context menu
        img_context_menu.addSeparator()
        self.img_show_image_action = img_context_menu.addAction("Starshot Image View",
                                                        self.set_current_view,
                                                        "")
        self.img_show_image_action.setCheckable(True)
        self.img_show_profile_action = img_context_menu.addAction("Starshot Profile View",
                                                          self.set_current_view,
                                                          "")
        self.img_show_profile_action.setCheckable(True)

        img_action_group = QActionGroup(img_context_menu)
        img_action_group.addAction(self.img_show_image_action)
        img_action_group.addAction(self.img_show_profile_action)
        img_action_group.setExclusive(True)
        self.img_show_image_action.setChecked(True)
        self.current_view = "starshot_view"

        prof_context_menu.addSeparator()
        self.prof_show_image_action = prof_context_menu.addAction("Starshot Image View",
                                                        self.set_current_view,
                                                        "")
        self.prof_show_image_action.setCheckable(True)
        self.prof_show_profile_action = prof_context_menu.addAction("Starshot Profile View",
                                                          self.set_current_view,
                                                          "")
        self.prof_show_profile_action.setCheckable(True)

        prof_action_group = QActionGroup(prof_context_menu)
        prof_action_group.addAction(self.prof_show_image_action)
        prof_action_group.addAction(self.prof_show_profile_action)
        prof_action_group.setExclusive(True)
        self.prof_show_image_action.setChecked(True)
        self.current_view = "starshot_view"

    def setup_config(self):
        self.ui.SIDInputCB.addItems(["Auto", "Manual"])
        self.ui.DPIInputCB.addItems(["Auto", "Manual"])
        self.ui.DPIInputCB.currentIndexChanged.connect(self.on_config_change)
        self.ui.SIDInputCB.currentIndexChanged.connect(self.on_config_change)

        # call this one time to ensure correct config display
        self.on_config_change()

    def on_config_change(self):
        if self.ui.SIDInputCB.currentText() == "Manual":
            self.ui.configFormLayout.setRowVisible(4, True)
        else:
            self.ui.configFormLayout.setRowVisible(4, False)

        if self.ui.DPIInputCB.currentText() == "Manual":
            self.ui.configFormLayout.setRowVisible(6, True)
        else:
            self.ui.configFormLayout.setRowVisible(6, False)
     
    def add_files(self, files: tuple | list | None = None):

        if not files:
            files, _ = QFileDialog.getOpenFileNames(
                self,
                "Select Starshot Images",
                "",
                "Images (*.dcm *.png *.tiff *.tif);; " \
                "DICOM Images (*.dcm);; TIFF Images (*.tiff *.tif);; PNG Image (*.png)",
                )

        if files:
            for file in files:
                path = Path(file)

                itemData = {"file_path": str(path),
                            "analysis_data": None}
                
                listItemWidget = QListWidgetItem(self.ui.imageListWidget)
                listItemWidget.setText(path.name)
                listItemWidget.setIcon(self.image_icon)
                listItemWidget.setCheckState(Qt.Unchecked)
                listItemWidget.setData(Qt.UserRole, itemData)

    def remove_selected_files(self):
        index = 0
        while index < self.ui.imageListWidget.count():
            if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                listItemWidget = self.ui.imageListWidget.takeItem(index)
                del listItemWidget
            else:
                index += 1

        self.update_marked_images()

    def remove_all_files(self):
        item_count = self.ui.imageListWidget.count()
        for index in range(item_count):
            listItemWidget = self.ui.imageListWidget.takeItem(item_count-(index+1))
            del listItemWidget
        
        self.update_marked_images()

    def remove_file(self):
        listItemWidget = self.ui.imageListWidget.takeItem(self.ui.imageListWidget.currentRow())
        del listItemWidget

        self.update_marked_images()

    def open_file_folder(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()
        file_path = str(Path(listWidgetItem.data(Qt.UserRole)["file_path"]).parent.resolve())
        
        if platform.system() == "Windows":
            subprocess.Popen(["explorer", file_path])
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", file_path])
        else:
            subprocess.Popen(["xdg-open", file_path])

    def perform_selection(self, selection_type: str):

        if selection_type == "selectAll":
            for index in range(self.ui.imageListWidget.count()):
                self.ui.imageListWidget.item(index).setCheckState(Qt.CheckState.Checked)
        
        elif selection_type == "unselectAll":
            for index in range(self.ui.imageListWidget.count()):
                self.ui.imageListWidget.item(index).setCheckState(Qt.CheckState.Unchecked)
        
        elif selection_type == "invertSelection":
            for index in range(self.ui.imageListWidget.count()):
                if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                    self.ui.imageListWidget.item(index).setCheckState(Qt.CheckState.Unchecked)
                elif self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Unchecked:
                    self.ui.imageListWidget.item(index).setCheckState(Qt.CheckState.Checked)

        self.update_marked_images()

    def update_marked_images(self):
        self.marked_images.clear()

        for index in range(self.ui.imageListWidget.count()):
            if self.ui.imageListWidget.item(index).checkState() == Qt.CheckState.Checked:
                self.marked_images.append(self.ui.imageListWidget.item(index).data(Qt.UserRole)["file_path"])
        
        if len(self.marked_images) > 0:
            self.ui.analyzeBtn.setEnabled(True)

            if len(self.marked_images) > 1:
                self.analysis_message_label.setText(f"{len(self.marked_images)} images will be merged and analyzed")
                self.analysis_message_label.show()

            else:
                self.analysis_message_label.hide()

        else:
            self.ui.analyzeBtn.setEnabled(False)
            self.analysis_message_label.hide()

    def view_dicom_image(self):
        image_short_name = self.ui.imageListWidget.currentItem().text()
        image_path = self.ui.imageListWidget.selectedItems()[0].data(Qt.UserRole)["file_path"]
        image = load(image_path)

        imgView = pg.ImageView()
        imgView.setImage(image.array)
        imgView.setPredefinedGradient("grey")

        new_win = QMainWindow()
        new_win.setWindowTitle(image_short_name)
        new_win.setCentralWidget(imgView)
        new_win.setMinimumSize(600, 500)
        
        self.imageView_windows.append(new_win)
        new_win.show()
        new_win.setMinimumSize(0, 0)

    def delete_file(self):
        listWidgetItem = self.ui.imageListWidget.currentItem()

        warning_dialog = MessageDialog()
        warning_dialog.set_icon(MessageDialog.WARNING_ICON)
        warning_dialog.set_title("Delete File")
        warning_dialog.set_header_text(f"Are you sure you want to permanently delete {listWidgetItem.text()} ?")
        warning_dialog.set_info_text("This action is irreversible!")
        warning_dialog.set_standard_buttons(QDialogButtonBox.StandardButton.Yes | 
                                            QDialogButtonBox.StandardButton.Cancel)

        ret = warning_dialog.exec()

        if ret == QDialogButtonBox.StandardButton.Yes:
            path = Path(listWidgetItem.data(Qt.UserRole)["file_path"])
            path.unlink(missing_ok=True)
            self.ui.imageListWidget.takeItem(self.ui.imageListWidget.currentRow())
            del listWidgetItem

    def eventFilter(self, source, event: QEvent):
        if (event.type() == QEvent.ContextMenu and source is self.ui.imageListWidget):
            pos = self.ui.imageListWidget.mapFromGlobal(event.globalPos())

            if type(self.ui.imageListWidget.itemAt(pos)) == QListWidgetItem:
                # Show context menu
                if not self.analysis_in_progress:
                    if len(self.marked_images) > 0:
                        self.invert_select_action.setEnabled(True)
                        self.unselect_all_action.setEnabled(True)
                        self.remove_selected_files_action.setEnabled(True)
                    else:
                        self.invert_select_action.setEnabled(False)
                        self.unselect_all_action.setEnabled(False)
                        self.remove_selected_files_action.setEnabled(False)

                    if len(self.marked_images) == self.ui.imageListWidget.count():
                        self.select_all_action.setEnabled(False)
                    else:
                        self.select_all_action.setEnabled(True)
                    
                    self.remove_file_action.setEnabled(True)
                    self.delete_file_action.setEnabled(True)
                    self.remove_all_files_action.setEnabled(True)
                    self.select_all_action.setEnabled(True)
                
                else:
                    self.remove_file_action.setEnabled(False)
                    self.delete_file_action.setEnabled(False)
                    self.remove_selected_files_action.setEnabled(False)
                    self.remove_all_files_action.setEnabled(False)
                    self.select_all_action.setEnabled(False)
                    self.view_analyzed_img_action.setEnabled(False)

                self.img_list_contextmenu.exec(event.globalPos())

        return super().eventFilter(source, event)
    
    def on_analysis_failed(self, error_message: str = "Unknown Error"):
        self.analysis_info_signal.emit({"state": AnalysisInfoLabel.FAILED,
                                        "message": None})
        self.analysis_state =  AnalysisInfoLabel.FAILED
        self.analysis_message = None

        self.analysis_in_progress = False
        self.restore_list_checkmarks()

        self.ui.analyzeBtn.setText(f"Analyze images")
        self.ui.addImgBtn.setEnabled(True)
    
        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        self.error_dialog = MessageDialog()
        self.error_dialog.set_icon(MessageDialog.CRITICAL_ICON)
        self.error_dialog.set_title("Analysis Error")
        self.error_dialog.set_header_text("Oops! An error was encountered")
        self.error_dialog.set_info_text(error_message)
        self.error_dialog.set_standard_buttons(QDialogButtonBox.StandardButton.Ok)
        
        self.error_dialog.exec()

    def start_analysis(self):
        self.analysis_info_signal.emit({"state": AnalysisInfoLabel.IN_PROGRESS,
                                        "message": None})
        self.analysis_state =  AnalysisInfoLabel.IN_PROGRESS
        self.analysis_message = None

        self.analysis_in_progress = True
        self.ui.genReportBtn.setEnabled(False)
        self.remove_list_checkmarks()
        self.set_analysis_outcome()

        row_count = self.form_layout.rowCount()
        for i in range(row_count):
            self.form_layout.removeRow(row_count - (i+1))

        self.img_plot_item.clear()

        # Restore spacer size to prevent other widgets from moving
        self.ui.image_vl_spacer.changeSize(0, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.ui.addImgBtn.setEnabled(False)
        self.ui.genReportBtn.setEnabled(False)
        self.ui.analyzeBtn.setEnabled(False)
        self.ui.analyzeBtn.setText("Analysis in progress...")
        self.analysis_message_label.setText("Analysis in progress")
        self.analysis_progress_bar.show()
        self.analysis_message_label.show()

        if len(self.marked_images) < 2:
            images = self.marked_images[0]
            
        else:
            images = self.marked_images

        params = {}

        if self.ui.SIDInputCB.currentText() == "Manual":
            params["sid"] = self.ui.sIDDSB.value()

        if self.ui.DPIInputCB.currentText() == "Manual":
            params["dpi"] = self.ui.dPIDSB.value()

        try:
            self.worker = QStarshotWorker(filepath = images,
                                          radius = self.ui.radiusSB.value(),
                                          min_peak_height = self.ui.miniPeakHeightDSB.value(),
                                          tolerance = self.ui.toleranceDSB.value(),
                                          fwhm = self.ui.useFWHMCB.isChecked(),
                                          recursive = self.ui.recursiveSearchCB.isChecked(),
                                          invert = self.ui.forceInvertCB.isChecked(),
                                          **params
                                          )
            self.qthread = QThread()
            self.worker.moveToThread(self.qthread)
            self.worker.analysis_failed.connect(self.qthread.quit)
            self.worker.analysis_failed.connect(self.on_analysis_failed)
            self.worker.thread_finished.connect(self.qthread.quit)
            self.worker.thread_finished.connect(self.worker.deleteLater)
            self.worker.analysis_results_ready.connect(lambda data: self.show_analysis_results(data))
            self.qthread.started.connect(self.worker.analyze)
            self.qthread.finished.connect(self.worker.deleteLater)

            self.qthread.start()

        except Exception as err:
            self.on_analysis_failed(traceback.format_exception_only(err)[-1])

    def show_analysis_results(self, data: dict):
        self.has_analysis = True
        self.analysis_data = data
        self.analysis_in_progress = False
        self.ui.genReportBtn.setEnabled(True)
        self.restore_list_checkmarks()

        self.plot_analyzed_starshot()

        # Analyze button is auto-enabled by update_marked_images() on item data change
        self.ui.analyzeBtn.setText(f"Analyze images")
        self.ui.addImgBtn.setEnabled(True)
        self.ui.genReportBtn.setEnabled(True)
    
        # Update status bar message
        self.analysis_info_signal.emit({"state": AnalysisInfoLabel.COMPLETE,
                                        "message": None})
        self.analysis_state =  AnalysisInfoLabel.COMPLETE
        self.analysis_message = None

        self.analysis_progress_bar.hide()
        self.analysis_message_label.hide()

        #set outcome
        self.set_analysis_outcome()
        
        #---------- Update the plot --------------
        self.ui.analysisImageVL.addWidget(self.graphics_widget)
        
        # Change spacer size to allow the image widget to scale properly
        self.ui.image_vl_spacer.changeSize(0, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        #Update the summary
        #self.analysis_summary= {"Wobble (circle) diameter": f"{starshot.wobble.radius_mm*2.0:2.3f} mm",
        #                        "Number of spokes detected": f"{len(starshot.lines)}"}
        
    def plot_analyzed_starshot(self) -> None:
        #---------- Plot the image
        self.img_plot_item.addItem(pg.ImageItem(self.analysis_data["image"].array))

        # plot the lines
        for line in self.analysis_data["spoke_lines"]:
            self.img_plot_item.plot(x = [line.point1.x, line.point2.x],
                                    y = [line.point1.y, line.point2.y],
                                    pen = pg.mkPen((255,0,255), width=1.5))
            
        # Plot the rails used for the circle profile
        width_ratio = self.analysis_data["star_profile"].width_ratio
        radius = self.analysis_data["star_profile"].radius
        center_x = self.analysis_data["star_profile"].center.x
        center_y = self.analysis_data["star_profile"].center.y
        x_outer = radius * (1 + width_ratio) * np.cos(np.linspace(0, 2*np.pi, 500)) + center_x
        y_outer = radius * (1 + width_ratio) * np.sin(np.linspace(0, 2*np.pi, 500)) + center_y
        self.img_plot_item.plot(x_outer, y_outer, pen = pg.mkPen((0, 255, 0), width = 2))

        x_outer = radius * (1 - width_ratio) * np.cos(np.linspace(0, 2*np.pi, 500)) + center_x
        y_outer = radius * (1 - width_ratio) * np.sin(np.linspace(0, 2*np.pi, 500)) + center_y

        self.img_plot_item.plot(x_outer, y_outer, pen = pg.mkPen((0, 255, 0), width = 2))

        # Plot the wobble
        self.img_plot_item.addItem(
            pg.ScatterPlotItem([self.analysis_data["wobble"].center.x], 
                               [self.analysis_data["wobble"].center.y],
                               pen = pg.mkPen(None), brush = pg.mkBrush(0,0,200,150),
                               size = self.analysis_data["wobble"].diameter, pxMode = False))
        self.img_plot_item.addItem(
            pg.ScatterPlotItem([self.analysis_data["wobble"].center.x], 
                               [self.analysis_data["wobble"].center.y],
                               pen = pg.mkPen(255,191,0), brush = pg.mkBrush(255,191,0,255),
                               size = self.analysis_data["wobble"].diameter * 0.02, pxMode = False))
        
        # Plot the peaks
        peak_x = [peak.x for peak in self.analysis_data["star_profile"].peaks]
        peak_y = [peak.y for peak in self.analysis_data["star_profile"].peaks]

        self.img_plot_item.addItem(
            pg.ScatterPlotItem(peak_x, peak_y,
                               size = 15, pxMode = False,
                               pen = pg.mkPen(None), brush = pg.mkBrush(255,0,255,150)))
        
        self.set_axes_units(True)
    
    def set_current_view(self):
        if self.current_view == "starshot_view":
            self.graphics_widget.removeItem(self.img_plot_item)
            self.graphics_widget.addItem(self.profile_plot_item, 1, 0)
            self.current_view = "profile_view"
            self.img_show_profile_action.setChecked(True)
            self.prof_show_profile_action.setChecked(True)
        else:
            self.graphics_widget.removeItem(self.profile_plot_item)
            self.graphics_widget.addItem(self.img_plot_item, 1, 0)
            self.current_view = "starshot_view"
            self.img_show_image_action.setChecked(True)
            self.prof_show_image_action.setChecked(True)

    def set_axes_units(self, use_mm_units: bool):
        if use_mm_units:
            transform = QTransform() # The transformation to use
            transform.scale(1 / self.analysis_data["image"].dpmm, 
                            1 / self.analysis_data["image"].dpmm)
            transform.translate(-0.5 * self.analysis_data["image"].shape[1], 
                                -0.5 * self.analysis_data["image"].shape[0])

            for item in self.img_plot_item.items:
                item.setTransform(transform)

            self.img_plot_item.setLabel('left', '<b>Y CAX offset (mm)</b>')
            self.img_plot_item.setLabel('bottom', '<b>X CAX offset (mm)</b>')

            t_unit = "mm"
            diameter = self.analysis_data["wobble"].diameter_mm
            x_coord = ((self.analysis_data["wobble"].center.x - 0.5 * 
                       self.analysis_data["image"].shape[1]) / 
                       self.analysis_data["image"].dpmm)
            y_coord = ((self.analysis_data["wobble"].center.y - 0.5 * 
                       self.analysis_data["image"].shape[0]) / 
                       self.analysis_data["image"].dpmm)      

        else:
            for item in self.img_plot_item.items:
                item.resetTransform()

            self.img_plot_item.setLabel('left', '<b>Y CAX offset (px)</b>')
            self.img_plot_item.setLabel('bottom', '<b>X CAX offset (px)</b>')
        
            t_unit = "px"
            diameter = self.analysis_data["wobble"].diameter
            x_coord = self.analysis_data["wobble"].center.x
            y_coord = self.analysis_data["wobble"].center.y
        
        self.plot_label.setText(
            "<span style='color:powderblue'>"\
            f"<p><b>Diameter of minimum intersecting circle:</b> {diameter: 2.2f} {t_unit}</p>" \
            f"<p><b>Circle coordinates:</b> {x_coord:2.2f} {t_unit}, {y_coord:2.2f} {t_unit}</p>" \
            "</span>")
        self.use_mm_units = use_mm_units
        self.set_axes_ranges()

    def zoom_to_circle(self):
        mm_per_dot = 1 / self.analysis_data["image"].dpmm
        image_dim = self.analysis_data["image"].shape
        radius = self.analysis_data["wobble"].radius
        x_coord = self.analysis_data["wobble"].center.x 
        y_coord = self.analysis_data["wobble"].center.y
        x_margin = 1.20 * radius # Use a 120% radius margin
        y_margin = 1.20 * radius # Use a 120% radius margin

        if self.use_mm_units:
            x_min = mm_per_dot * (x_coord - 0.5 * image_dim[1] - radius - x_margin)
            x_max = mm_per_dot * (x_coord - 0.5 * image_dim[1] + radius + x_margin)
            y_min = mm_per_dot * (y_coord - 0.5 * image_dim[0] - radius - y_margin)
            y_max = mm_per_dot * (y_coord - 0.5 * image_dim[0] + radius + y_margin)
            
        else:
            x_min = x_coord - radius - x_margin
            x_max = x_coord + radius + x_margin
            y_min = y_coord - radius - y_margin
            y_max = y_coord + radius + y_margin
            
        self.img_plot_item.setRange(xRange=(x_min, x_max), yRange=(y_min, y_max))

    def set_axes_ranges(self):
        mm_per_dot = 1 / self.analysis_data["image"].dpmm
        image_dim = self.analysis_data["image"].shape
        x_lim_margin = 0.45 * image_dim[1] # Use a 45% width margin for limits
        y_lim_margin = 0.45 * image_dim[0] # Use a 45% height margin for limits

        if self.use_mm_units:
            x_min = -mm_per_dot * (0.5 * image_dim[1] + x_lim_margin)
            y_min = -mm_per_dot * (0.5 * image_dim[0] + y_lim_margin)               
            x_max = mm_per_dot * (0.5 * image_dim[1] + x_lim_margin)
            y_max = mm_per_dot * (0.5 * image_dim[0] + y_lim_margin)
            
        else:
            x_min, y_min = -x_lim_margin, -y_lim_margin
            x_max, y_max = x_lim_margin + image_dim[1], y_lim_margin + image_dim[0]
            
        self.img_plot_item.setLimits(xMin=x_min, xMax=x_max, yMin=y_min, yMax=y_max)
        self.img_plot_item.autoRange()

    def remove_list_checkmarks(self):
        for index in range(self.ui.imageListWidget.count()):
            listItemWidget = self.ui.imageListWidget.item(index)
            listItemWidget.setFlags(Qt.ItemFlag.ItemIsEnabled)

    def restore_list_checkmarks(self):
        for index in range(self.ui.imageListWidget.count()):
            listItemWidget = self.ui.imageListWidget.item(index)
            listItemWidget.setFlags(Qt.ItemFlag.ItemIsEnabled |
                                    Qt.ItemFlag.ItemIsUserCheckable |
                                    Qt.ItemFlag.ItemIsDragEnabled |
                                    Qt.ItemFlag.ItemIsSelectable)
            
            if listItemWidget.data(Qt.ItemDataRole.UserRole)["file_path"] in self.marked_images:
                listItemWidget.setCheckState(Qt.CheckState.Checked)

    def set_analysis_outcome(self):
        if not self.has_analysis or self.analysis_in_progress:
            self.ui.outcomeLE.clear()
            self.ui.outcomeLE.setStyleSheet(u"border-color: rgba(0, 0, 0,0);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(0, 0, 0, 0);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
            
        elif self.analysis_data["wobble"].radius_mm * 2.0 < self.ui.toleranceDSB.value():
            self.ui.outcomeLE.setText("PASS")
            self.ui.outcomeLE.setStyleSheet(u"border-color: rgb(95, 200, 26);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(95, 200, 26, 150);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
            
        else:
            self.ui.outcomeLE.setText("FAIL")
            self.ui.outcomeLE.setStyleSheet(u"border-color: rgb(231, 29, 14);\n"
                "border-radius: 15px;\n"
                "border-style: solid;\n"
                "border-width: 2px;\n"
                "background-color: rgba(231, 29, 14, 150);\n"
                "padding-left: 15px;\n"
                "height: 30px;\n"
                "font-weight: bold;\n")
    
    def generate_report(self):
        physicist_name_le = QLineEdit()
        institution_name_le = QLineEdit()
        treatment_unit_le = QComboBox()
        analysis_date = QDateEdit()
        comments_te = QPlainTextEdit()
        treatment_unit_le.setEditable(True)
        physicist_name_le.setMaximumWidth(250)
        physicist_name_le.setMinimumWidth(250)
        institution_name_le.setMaximumWidth(350)
        institution_name_le.setMinimumWidth(350)
        treatment_unit_le.setMaximumWidth(250)
        treatment_unit_le.setMinimumWidth(250)
        analysis_date.setMaximumWidth(120)
        analysis_date.setCalendarPopup(True)
        analysis_date.setDisplayFormat("dd MMMM yyyy")
        analysis_date.setMaximumDate(QDate.currentDate())

        # restore current save info
        physicist_name_le.setText(self.report_author)
        institution_name_le.setText(self.report_institution)
        analysis_date.setDate(self.report_date)
        comments_te.setPlainText(self.save_comment)

        save_path_le = QLineEdit()
        save_win_btn = QPushButton("Save to...")
        save_path_le.setReadOnly(True)
        save_location_layout = QHBoxLayout()
        save_location_layout.addWidget(save_path_le)
        save_location_layout.addWidget(save_win_btn)

        show_report_checkbox = QCheckBox()
        show_report_label = QLabel("Open report:")
        show_report_checkbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        show_report_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        show_report_layout = QHBoxLayout()
        show_report_layout.addWidget(show_report_label)
        show_report_layout.addWidget(show_report_checkbox)

        # get linac devices
        linac_devices = DeviceManager.device_list["linacs"]
        treatment_unit_le.addItems([linac.name for linac in linac_devices])

        user_details_layout = QFormLayout()
        user_details_layout.addRow("Physicist:", physicist_name_le)
        user_details_layout.addRow("Treatment unit:", treatment_unit_le)
        user_details_layout.addRow("Institution:", institution_name_le)
        user_details_layout.addRow("Save location:", save_location_layout)
        user_details_layout.addRow("Analysis date:", analysis_date)
        user_details_layout.addRow("Comments:", comments_te)
        user_details_layout.addRow("",show_report_layout)
        user_details_layout.addItem(QSpacerItem(1,10, QSizePolicy.Policy.Minimum,
                                                QSizePolicy.Policy.Minimum))
        
        layout = QVBoxLayout()
        layout.addLayout(user_details_layout)

        dialog_buttons = QDialogButtonBox()
        save_button = dialog_buttons.addButton(QDialogButtonBox.StandardButton(
            QDialogButtonBox.StandardButton.Save), )
        save_button.setEnabled(False)
        cancel_button = dialog_buttons.addButton(QDialogButtonBox.StandardButton(
            QDialogButtonBox.StandardButton.Cancel))
        
        # enable the save button once we have a path to save the report to
        save_path_le.textChanged.connect(lambda: save_button.setEnabled(True))
        
        layout.addWidget(dialog_buttons)

        report_dialog = QDialog()
        report_dialog.setWindowTitle("Generate Starshot Report ‒ PyBeam QA")
        report_dialog.setLayout(layout)
        report_dialog.setMinimumSize(report_dialog.sizeHint())
        report_dialog.setMaximumSize(report_dialog.sizeHint())

        cancel_button.clicked.connect(report_dialog.reject)
        save_button.clicked.connect(report_dialog.accept)
        save_win_btn.clicked.connect(lambda: save_path_le.setText(worksheet_save_report(self)))

        result = report_dialog.exec()

        if result == QDialog.DialogCode.Accepted:

            # Amend save info
            self.report_author = physicist_name_le.text()
            self.report_institution = institution_name_le.text()
            self.save_comment = comments_te.toPlainText()
            self.report_date = analysis_date.date()

            physicist_name = "N/A" if physicist_name_le.text() == "" else physicist_name_le.text()
            institution_name = "N/A" if institution_name_le.text() == "" else institution_name_le.text()
            treatment_unit = "N/A" if treatment_unit_le.currentText() == "" else treatment_unit_le.currentText()

            report = StarshotReport(filename = save_path_le.text(),
                                    author = physicist_name,
                                    institution = institution_name,
                                    treatment_unit_name = treatment_unit,
                                    analysis_date = self.report_date.toString("dd MMMM yyyy"),
                                    tolerance = self.ui.toleranceDSB.value(),
                                    report_status = self.ui.outcomeLE.text(),
                                    comments = comments_te.toPlainText(),
                                    analysis_data = self.analysis_data
                                    )
            report.save_report()

            if show_report_checkbox.isChecked():
                webbrowser.open(save_path_le.text())