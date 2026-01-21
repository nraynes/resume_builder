import tkinter as tk
from tkinter import ttk
from src.gui.Base.BaseWindow import BaseWindow
from src.gui.components.NewResumeForm import NewResumeForm
from src.gui.components.PickResumeList import PickResumeList


class MainWindow(BaseWindow):

    def __init__(self, master, openEditorCb, show: bool = True):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self.openEditor = openEditorCb
        self._btn_open_cv = ttk.Button(self._frame, text="View/Edit CV", command=self.openCv)
        self._btn_open_cv.pack()
        self.spacing().pack()
        self._frm_new_resume = NewResumeForm(self._frame)
        self._frm_new_resume.pack()
        self.spacing().pack()
        self._lst_pick_resume = PickResumeList(self._frame)
        self._lst_pick_resume.pack()
        if show:
            self.show()

    def openCv(self):
        self.openEditor()

    def openResume(self):
        self.openEditor()

    @property
    def btnOpenCv(self):
        return self._btn_open_cv

    @property
    def frmNewResume(self):
        return self._frm_new_resume

    @property
    def lstPickResume(self):
        return self._lst_pick_resume
