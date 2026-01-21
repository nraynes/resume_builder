import tkinter as tk


class BaseFrame:
    _frame: tk.Frame

    def spacing(self, master = None, height: int = 5, width: int = 5):
        return tk.Frame(master if master is not None else self._frame, height=height, width=width)

    @property
    def frame(self):
        return self._frame
