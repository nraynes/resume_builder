import tkinter as tk
from src.gui.base.BaseFrame import BaseFrame


class BaseModal(BaseFrame):
    _frame: tk.Toplevel

    def close(self):
        self._frame.destroy()
