import tkinter as tk
from src.gui.components.BaseFrame import BaseFrame
from src.gui.components.NewResumeForm import NewResumeForm
from src.gui.components.PickResumeList import PickResumeList


class MainWindow(BaseFrame):
    def __init__(self, master):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self._btn_open_cv = tk.Button(self._frame, text="View/Edit CV")
        self._btn_open_cv.pack()
        self.addSpacing()
        self._frm_new_resume = NewResumeForm(self._frame)
        self._frm_new_resume.pack()
        self.addSpacing()
        self._lst_pick_resume = PickResumeList(self._frame)
        self._lst_pick_resume.pack()
        self._frame.pack(anchor="center", expand=True)

    def addSpacing(self):
        spacing = tk.Frame(self._frame, height=5)
        spacing.pack()
    
    @property
    def btnOpenCv(self):
        return self._btn_open_cv
    
    @property
    def frmNewResume(self):
        return self._frm_new_resume
    
    @property
    def lstPickResume(self):
        return self._lst_pick_resume
