import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.Listbox import Listbox


class PickResumeList(BaseComponent):
    def __init__(self, master, cmd_open):
        self._frame = tk.Frame(master, padx=5, pady=5)
        self.cmd_open = cmd_open
        self._lst_resumes = Listbox(self._frame)
        self._btn_open_resume = ttk.Button(self._frame, text="View/Edit Resume", command=self.openResume)

        self._lst_resumes.grid(row=0)
        self._btn_open_resume.grid(row=1)

    def setResumeList(self, resume_list):
        self._lst_resumes.clear()
        for resume in resume_list:
            self._lst_resumes.add(resume)

    def openResume(self):
        title = self._lst_resumes.selected()
        if title is not None:
            self.cmd_open(title)

    @property
    def lstResumes(self):
        return self._lst_resumes

    @property
    def btnOpenResume(self):
        return self._btn_open_resume
