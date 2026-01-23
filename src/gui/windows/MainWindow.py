import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.NewResumeForm import NewResumeForm
from src.gui.components.PickResumeList import PickResumeList
from typing import Callable


class MainWindow(BaseWindow):

    def __init__(
        self,
        master: tk.Tk,
        open_editor_cb: Callable,
        new_resume_cb: Callable,
        new_cv_resume_cb: Callable,
        delete_resume_cb: Callable
    ):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self._btn_open_cv = ttk.Button(
            self._frame, text="View/Edit CV", command=open_editor_cb
        )
        self._frm_new_resume = NewResumeForm(
            self._frame,
            new_resume_cb=new_resume_cb,
            new_cv_resume_cb=new_cv_resume_cb
        )
        self._lst_pick_resume = PickResumeList(
            self._frame,
            open_editor_cb=open_editor_cb,
            delete_resume_cb=delete_resume_cb,
        )

        self._btn_open_cv.pack()
        self.spacing().pack()
        self._frm_new_resume.pack()
        self.spacing().pack()
        self._lst_pick_resume.pack()

    @property
    def btnOpenCv(self) -> ttk.Button:
        return self._btn_open_cv

    @property
    def frmNewResume(self) -> NewResumeForm:
        return self._frm_new_resume

    @property
    def lstPickResume(self) -> PickResumeList:
        return self._lst_pick_resume

    def show(self):
        self._frame.pack(anchor="center", expand=True)

    def hide(self):
        self._frame.pack_forget()

    def setResumeList(self, resume_list: list[str]):
        self._lst_pick_resume.setResumeList(resume_list)
