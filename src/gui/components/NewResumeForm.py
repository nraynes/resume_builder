import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseMetaDataForm import BaseMetaDataForm
from typing import Callable, Optional


class NewResumeForm(BaseMetaDataForm):

    def __init__(
        self,
        master: tk.Frame,
        new_resume_cb: Callable, 
        new_cv_resume_cb: Callable
    ):
        super().__init__(master)
        self.packBase()
        self.new_resume_cb = new_resume_cb
        self.new_cv_resume_cb = new_cv_resume_cb
        self._btn_new_resume = ttk.Button(self._frame, text="New Resume", command=self.newResume)
        self._btn_new_cv_resume = ttk.Button(
            self._frame, text="New Resume from CV", command=self.newResumeFromCv
        )

        self._btn_new_resume.pack(fill=tk.BOTH)
        self._btn_new_cv_resume.pack(fill=tk.BOTH)

    @property
    def btnNewResume(self) -> ttk.Button:
        return self._btn_new_resume

    @property
    def btnNewCvResume(self) -> ttk.Button:
        return self._btn_new_cv_resume

    def newResume(self):
        fields = self.extractFields()
        if fields is not None:
            self.new_resume_cb(*fields)

    def newResumeFromCv(self):
        fields = self.extractFields()
        if fields is not None:
            self.new_cv_resume_cb(*fields)

    def extractFields(self) -> Optional[tuple[str]]:
        title = self._inp_title.get()
        author = self._inp_author.get()
        if title and author:
            self._inp_title.clear()
            self._inp_author.clear()
            return (title, author)
        return None
