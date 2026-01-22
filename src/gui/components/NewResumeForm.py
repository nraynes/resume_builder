import tkinter as tk
from tkinter import ttk
from src.gui.components.ResumeEditor.subcomponents.ResumeMetaDataForm import ResumeMetaDataForm


class NewResumeForm(ResumeMetaDataForm):

    def __init__(self, master):
        super().__init__(master, False)
        self._btn_submit = ttk.Button(self._frame, text="New Resume")
        self._btn_submit.pack(fill=tk.BOTH)

    @property
    def btnSubmit(self):
        return self._btn_submit
