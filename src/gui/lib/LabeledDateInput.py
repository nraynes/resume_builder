from src.gui.base.BaseComponent import BaseComponent
import tkinter as tk
from src.gui.lib.DateEntry import DateEntry
from datetime import datetime


class LabeledDateInput(BaseComponent):
    def __init__(self, master, lbl_text: str = "", *args, **kwargs):
        self._frame = tk.Frame(master)
        lbl = tk.Label(self._frame, text=lbl_text)
        self._inp = DateEntry(self._frame, *args, **kwargs)
        self._frame.columnconfigure(1, weight=1)
        self._frame.columnconfigure(1, weight=1)
        lbl.grid(row=0, sticky="E")
        self._inp.grid(row=0, column=1, sticky="EW")

    def get(self):
        return datetime.combine(self._inp.get_date(), datetime.min.time())

    def clear(self):
        self._inp.delete(0, tk.END)

    def setValue(self, date: datetime):
        self.clear()
        self._inp.set_date(date)

    @property
    def inp(self):
        return self._inp
