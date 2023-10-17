<p align="center">
<img src="https://raw.github.com/Quantico-Bullet/PyBeam-QA/blob/main/ui/qt_ui/icons/ic_app_alt.svg?sanitize=true">
</p>

# PyBeam QA

PyBeam QA is a graphical user interface program for performing quality assurance tests in radiotherapy. The program is based on Pylinac and PySide6.

## Features
The program is still in early development and may contain bugs. Tools are flagged as either 
'Complete', 'In-progress' or 'Planned'. Planned features are those not yet implemented.

| QA Tool | Status |
| --------------- | --------------- |
| TRS 398 Photon & Electron output calibration | In-progress |
| Picket fence | Complete |
| Winston-Lutz analysis | Complete |
| Star-shot analysis | Complete |
| Field analysis | Complete |
| Planar imaging analysis | Complete |

## Requirements
As of current the program depends on the following:
- Python (3.10+)
- PySide6 (6.4+)
- pylinac (3.9.0+)
- pyqtgraph (0.13.2+)
- pdfrw (0.4)

## Installation
1. Download the source code from the repository.
2. (Optional but highly recommended) Create a virtual environment for PyBeam-QA to avoid dependency conflicts
with existing python libraries. You can use a dependency manager such as `Pipenv` to accomplish this.
3. Install all the required dependencies using `pip3` (e.g `pip3 install pdfrw==0.4`).

## Quick start
To run the application simply navigate to the source code directory and run the following command:\
`python3 main.py`
