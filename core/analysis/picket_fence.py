from PySide6.QtCore import Signal, Slot, QObject

from pylinac.picketfence import PicketFence, MLC, MLCArrangement

from pathlib import Path
from typing import BinaryIO, Optional, Union

class QPicketFence(PicketFence):

    def __init__(self, filename: Union[str, Path, BinaryIO],
        filter: Optional[int] = None,
        log: Optional[str] = None,
        use_filename: bool = False,
        mlc: Union[MLC, MLCArrangement, str] = MLC.MILLENNIUM,
        crop_mm: int = 3,
        image_kwargs: Optional[dict] = None,):

        super().__init__(self, filename, filter, log,
                        use_filename, mlc, crop_mm, image_kwargs,)
