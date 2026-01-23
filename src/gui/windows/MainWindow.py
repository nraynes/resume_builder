import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.NewResumeForm import NewResumeForm
from src.gui.components.PickResumeList import PickResumeList


class MainWindow(BaseWindow):

    def __init__(self, master, openEditorCb, newResumeCb, newCvResumeCb, deleteResumeCb):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self._btn_open_cv = ttk.Button(
            self._frame, text="View/Edit CV", command=openEditorCb
        )
        self._btn_open_cv.pack()
        self.spacing().pack()
        self._frm_new_resume = NewResumeForm(
            self._frame, cmd_new=newResumeCb, cmd_new_from_cv=newCvResumeCb
        )
        self._frm_new_resume.pack()
        self.spacing().pack()
        self._lst_pick_resume = PickResumeList(self._frame, cmd_open=openEditorCb, cmd_delete=deleteResumeCb)
        self._lst_pick_resume.pack()

    def setResumeList(self, resume_list):
        self._lst_pick_resume.setResumeList(resume_list)

    def show(self):
        self._frame.pack(anchor="center", expand=True)

    def hide(self):
        self._frame.pack_forget()

    @property
    def btnOpenCv(self):
        return self._btn_open_cv

    @property
    def frmNewResume(self):
        return self._frm_new_resume

    @property
    def lstPickResume(self):
        return self._lst_pick_resume
