import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.Listbox import Listbox
from typing import Callable


class PickResumeList(BaseComponent):
    def __init__(
        self,
        master: tk.Frame,
        open_editor_cb: Callable,
        delete_resume_cb: Callable
    ):
        self._frame = tk.Frame(master, padx=5, pady=5)
        self.open_editor_cb = open_editor_cb
        self.delete_resume_cb = delete_resume_cb
        self._lst_resumes = Listbox(self._frame)
        self._btn_open_resume = ttk.Button(self._frame, text="View/Edit Resume", command=self.openResume)
        self._btn_delete_resume = ttk.Button(self._frame, text="Delete Resume", command=self.deleteResume)

        self._lst_resumes.grid(row=0, column=0, columnspan=2, sticky="EW")
        self._btn_open_resume.grid(row=1, column=0, sticky="EW")
        self._btn_delete_resume.grid(row=1, column=1, sticky="EW")

    @property
    def lstResumes(self) -> Listbox:
        return self._lst_resumes

    @property
    def btnOpenResume(self) -> ttk.Button:
        return self._btn_open_resume

    @property
    def btnDeleteResume(self) -> ttk.Button:
        return self._btn_delete_resume

    def deleteResume(self):
        title = self._lst_resumes.selected()
        if title is not None:
            self.delete_resume_cb(title)

    def setResumeList(self, resume_list: list[str]):
        self._lst_resumes.clear()
        for resume in resume_list:
            self._lst_resumes.add(resume)

    def openResume(self):
        title = self._lst_resumes.selected()
        if title is not None:
            self.open_editor_cb(title)
