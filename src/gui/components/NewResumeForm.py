import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseMetaDataForm import BaseMetaDataForm


class NewResumeForm(BaseMetaDataForm):

    def __init__(self, master, cmd_new, cmd_new_from_cv):
        super().__init__(master)
        self.packBase()
        self._cmd_new = cmd_new
        self._cmd_new_from_cv = cmd_new_from_cv
        self._btn_new_resume = ttk.Button(self._frame, text="New Resume", command=self.newResume)
        self._btn_new_cv_resume = ttk.Button(
            self._frame, text="New Resume from CV", command=self.newResumeFromCv
        )
        self._btn_new_resume.pack(fill=tk.BOTH)
        self._btn_new_cv_resume.pack(fill=tk.BOTH)

    def newResume(self):
        self._cmd_new(*self.extractFields())

    def newResumeFromCv(self):
        self._cmd_new_from_cv(*self.extractFields())

    def extractFields(self):
        title = self._inp_title.get()
        author = self._inp_author.get()
        if title and author:
            self._inp_title.clear()
            self._inp_author.clear()
        return (title, author)

    @property
    def btnSubmit(self):
        return self._btn_submit
