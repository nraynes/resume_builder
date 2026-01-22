import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseListForm import BaseListForm


class BaseEditorListForm(BaseListForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._btn_edit = ttk.Button(self._frame, text="Edit")
        self._btn_edit.grid(row=4, column=1)

    @property
    def btnEdit(self):
        return self._btn_edit
