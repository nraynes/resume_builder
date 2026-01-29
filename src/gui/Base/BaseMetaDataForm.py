import tkinter as tk
from src.gui.lib.LabeledInput import LabeledInput
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.Frame import Frame


class BaseMetaDataForm(BaseComponent):
    def __init__(self, master: tk.Frame):
        self._frame = Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        self._inp_title = LabeledInput(self._frame, "Title:")
        self._inp_author = LabeledInput(self._frame, "Author:")

    @property
    def inpTitle(self) -> LabeledInput:
        return self._inp_title

    @property
    def inpAuthor(self) -> LabeledInput:
        return self._inp_author

    def packBase(self):
        self._inp_title.pack(anchor="e", fill=tk.BOTH)
        self._inp_author.pack(anchor="e", fill=tk.BOTH)
