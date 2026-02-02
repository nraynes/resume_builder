from tkinter import ttk
from src.gui.base.BaseListForm import BaseListForm
from abc import abstractmethod
from src.gui.lib.Button import Button


class BaseEditorListForm(BaseListForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._btn_edit = Button(self._frame, text="Edit", command=self.cmdEdit)
        self._btn_copy = Button(self._frame, text="Copy", command=self.cmdCopy)
        self._btn_edit.grid(row=4, column=2, sticky="EW")
        self.spacing().grid(row=4, column=3)
        self._btn_copy.grid(row=4, column=4, sticky="EW")

    @property
    def btnEdit(self) -> ttk.Button:
        return self._btn_edit

    @property
    def btnCopy(self) -> ttk.Button:
        return self._btn_copy

    @abstractmethod
    def cmdEdit(self):
        pass

    @abstractmethod
    def cmdCopy(self):
        pass
