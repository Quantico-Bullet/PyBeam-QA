from PySide6.QtWidgets import QDialog, QWidget, QDialogButtonBox, QFileDialog

from ui.py_ui.winston_lutz_test_dialog_ui import Ui_WLTestDialog

import ast

class WLTestDialog(QDialog):
    
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.ui = Ui_WLTestDialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Winston Lutz Benchmark Testing")

        self.apply_btn = self.ui.button_box.button(QDialogButtonBox.StandardButton.Apply)
        self.apply_btn.clicked.connect(self.accept)

        self.ui.field_type_cb.currentIndexChanged.connect(self.on_field_type_changed)
        self.ui.image_axes_le.textChanged.connect(self.validate_info)
        self.ui.test_name_le.textChanged.connect(self.validate_info)
        self.ui.out_dir_le.textChanged.connect(self.validate_info)
        self.ui.select_dir_btn.clicked.connect(self.select_directory)

        self.ui.sim_image_cb.addItems(["AS500", "AS1000", "AS1200"])
        self.ui.field_type_cb.addItems(["Rectangle", "Cone"])

        self.ui.final_layer_cb.addItems(["Gaussian filter"])
        self.apply_btn.setEnabled(False)

        self.image_axes = []

    def select_directory(self):
        folder = QFileDialog.getExistingDirectory(self)

        if folder:
            self.ui.out_dir_le.setText(folder)

    def on_field_type_changed(self):
        if self.ui.field_type_cb.currentText() == "Rectangle":
            self.ui.cone_field_size_dsb.hide()
            self.ui.rec_field_width_label.show()
            self.ui.rec_field_height_label.show()
            self.ui.rec_field_width_dsb.show()
            self.ui.rec_field_height_dsb.show()

            self.ui.field_layer_cb.clear()
            self.ui.field_layer_cb.addItems(["Filtered field", "Filter free field",
                                         "Perfect field"])

        else:
            self.ui.cone_field_size_dsb.show()
            self.ui.rec_field_width_label.hide()
            self.ui.rec_field_height_label.hide()
            self.ui.rec_field_width_dsb.hide()
            self.ui.rec_field_height_dsb.hide()

            self.ui.field_layer_cb.clear()
            self.ui.field_layer_cb.addItems(["Filter free cone",
                                         "Perfect cone"])

    def validate_info(self):        
        image_axes_text = self.ui.image_axes_le.text()
        self.image_axes.clear()

        if image_axes_text != "":
            axes_list = image_axes_text.split("; ")

            if len(axes_list) > 1:
                for axes in axes_list:
                    try:
                        axes = ast.literal_eval(axes)
                        if len(axes) == 3:
                            valid = isinstance(axes[0], int) \
                                  and isinstance(axes[1], int) \
                                  and isinstance(axes[2], int)
                            
                            if valid:
                                self.image_axes.append(axes)
                                self.apply_btn.setEnabled(True)

                        else:
                            return self.apply_btn.setEnabled(False)

                    except Exception as err:
                        return self.apply_btn.setEnabled(False)

            else: 
                return self.apply_btn.setEnabled(False)
            
        else: return

        if self.ui.test_name_le.text() == "" or self.ui.out_dir_le.text() == "":
            return self.apply_btn.setEnabled(False)

        else:
            self.apply_btn.setEnabled(True)