from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QGuiApplication

import pylinac.core.array_utils as array_utils
from pylinac.core.decorators import validate
from pylinac import __version__ as pylinac_version

import sys, os
import numpy as np

curr_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

#Add all paths pointing to icons here
sys.path.insert(0, curr_dir + "/ui/py_ui/")

#TODO Perform this monkey-patch for pylinac version <= 3.26

def array_not_empty(array: np.ndarray) -> None:
    """Check an array isn't empty"""
    if not array.size:
        raise ValueError("Array must not be empty")

@validate(array=array_not_empty)
def normalize(array: np.ndarray, value: float | None = None) -> np.ndarray:
    """Normalize an array to the passed value. If not value is passed, normalize to the maximum value"""
    if value is None:
        val = array.max()
    else:
        val = value
    array = array / val
    return array.astype(np.float16)

pylinac_version = pylinac_version.split(".")

if int(pylinac_version[0]) == 3 and int(pylinac_version[1]) <= 27:
    array_utils.normalize = normalize

# ---------- Utility functions for windows -------------
def move_to_screen_center(window: QMainWindow) -> None:
    """
    Place window at the center of the current screen
    """
    primary_screen = QGuiApplication.primaryScreen()
    screen_center = primary_screen.availableGeometry().center()

    window.move(screen_center - window.rect().center())

def resize_to_available_screen(window: QMainWindow, value: tuple):
    """
    Place window at the center of the current screen
    """
    primary_screen = QGuiApplication.primaryScreen()
    screen_size = primary_screen.availableSize().toTuple()

    window.resize(screen_size[0] * value[0], screen_size[1] * value[1])