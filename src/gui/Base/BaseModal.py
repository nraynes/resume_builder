import tkinter as tk
from src.gui.base.BaseFrame import BaseFrame


class BaseModal(BaseFrame):
    _frame: tk.Toplevel

    def setLocationTopLeft(self):
        w = self._frame.winfo_width()
        h = self._frame.winfo_height()
        x = 0
        y = 0
        self._frame.geometry(f"{w}x{h}+{x}+{y}")
        self._frame.geometry("")

    def close(self):
        self._frame.destroy()
