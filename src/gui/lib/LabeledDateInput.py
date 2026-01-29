from src.gui.base.BaseEntry import BaseEntry
import tkinter as tk
from src.gui.lib.DateEntry import DateEntry
from datetime import datetime
from src.utils.DateUtils import DateUtils
from src.gui.lib.Frame import Frame
from src.gui.lib.Label import Label


class LabeledDateInput(BaseEntry):
    def __init__(self, master: tk.BaseWidget, lbl_text: str = "", *args, **kwargs):
        self._frame = Frame(master)
        self._frame.columnconfigure(1, weight=1)
        self._stored_date = None
        lbl = Label(self._frame, text=lbl_text)
        self._inp = DateEntry(self._frame, *args, **kwargs)
        lbl.grid(row=0, sticky="E")
        self._inp.grid(row=0, column=1, sticky="EW")
        self._inp.set_date(datetime.now())

    def get(self) -> datetime:
        return datetime.combine(self._inp.get_date(), datetime.min.time())

    def getString(self) -> str:
        return DateUtils.string(self.get())

    def clear(self):
        self._inp.delete(0, tk.END)

    def setValue(self, x: datetime):
        self.clear()
        self._inp.set_date(x)
