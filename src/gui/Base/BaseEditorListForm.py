import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseListForm import BaseListForm
from abc import abstractmethod


class BaseEditorListForm(BaseListForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._btn_edit = ttk.Button(self._frame, text="Edit", command=self.cmdEdit)
        self._btn_edit.grid(row=4, column=2, sticky="EW")

    @property
    def btnEdit(self):
        return self._btn_edit
    
    @abstractmethod
    def cmdEdit(self):
        pass
