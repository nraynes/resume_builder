from src.gui.base.BaseEntry import BaseEntry
import tkinter as tk
from tkinter import ttk


class LabeledCombo(BaseEntry):
    def __init__(self, master, lbl_text: str = "", *args, **kwargs):
        self._frame = tk.Frame(master)
        self._frame.columnconfigure(1, weight=1)
        lbl = tk.Label(self._frame, text=lbl_text)
        self._inp = ttk.Combobox(self._frame, *args, **kwargs)

        lbl.grid(row=0, sticky="E")
        self._inp.grid(row=0, column=1, sticky="EW")

    def get(self):
        return self._inp.get()

    def clear(self):
        self._inp.set("")

    def setValue(self, x: str):
        if x in self._inp["values"]:
            self.clear()
            self._inp.set(x)
