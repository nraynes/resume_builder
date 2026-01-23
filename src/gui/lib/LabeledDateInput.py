from src.gui.base.BaseComponent import BaseComponent
import tkinter as tk
from src.gui.lib.DateEntry import DateEntry
from datetime import datetime
from src.validation.Validate import Validate


class LabeledDateInput(BaseComponent):
    def __init__(self, master, lbl_text: str = "", *args, **kwargs):
        self._frame = tk.Frame(master)
        self._stored_date = None
        lbl = tk.Label(self._frame, text=lbl_text)
        self._inp = DateEntry(self._frame, *args, **kwargs)
        self._frame.columnconfigure(1, weight=1)
        self._frame.columnconfigure(1, weight=1)
        lbl.grid(row=0, sticky="E")
        self._inp.grid(row=0, column=1, sticky="EW")

    def get(self):
        return datetime.combine(self._inp.get_date(), datetime.min.time())
    
    def getString(self):
        return datetime.strftime(self.get(), Validate.isodateformat)

    def clear(self):
        self._inp.delete(0, tk.END)

    def setValue(self, date: datetime):
        self.clear()
        self._inp.set_date(date)
        
    def undefault(self):
        if self._stored_date is not None:
            self.setValue(self._stored_date)
        
    def default(self):
        self._stored_date = self.get()
        self.setValue(datetime.strptime(Validate.epoch, Validate.isodateformat))

    @property
    def inp(self):
        return self._inp
