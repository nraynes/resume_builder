import tkinter as tk
from typing import Optional


class BaseFrame:
    _frame: tk.Frame

    @property
    def frame(self):
        return self._frame

    def spacing(self, master: Optional[tk.BaseWidget] = None, height: int = 5, width: int = 5):
        return tk.Frame(master if master is not None else self._frame, height=height, width=width)
