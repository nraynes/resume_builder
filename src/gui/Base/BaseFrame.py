import tkinter as tk
from src.gui.lib.Frame import Frame
from typing import Optional


class BaseFrame:
    _frame: Frame

    @property
    def frame(self) -> Frame:
        return self._frame

    def spacing(self, master: Optional[tk.BaseWidget] = None, height: int = 5, width: int = 5) -> tk.Frame:
        return Frame(master if master is not None else self._frame, height=height, width=width)
