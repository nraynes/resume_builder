from src.gui.base.BaseEntry import BaseEntry
import tkinter as tk
from src.gui.lib.Frame import Frame
from src.gui.lib.Label import Label
from src.gui.lib.Entry import Entry


class LabeledInput(BaseEntry):
    def __init__(self, master: tk.BaseWidget, lbl_text: str = ""):
        self._frame = Frame(master)
        self._frame.columnconfigure(1, weight=1)
        lbl = Label(self._frame, text=lbl_text)
        self._inp = Entry(self._frame)

        lbl.grid(row=0, sticky="E")
        self._inp.grid(row=0, column=1, sticky="EW")

    def get(self) -> str:
        return self._inp.get()

    def clear(self):
        self._inp.delete(0, tk.END)

    def setValue(self, x: str):
        self.clear()
        self._inp.insert(0, x)
