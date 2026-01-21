import tkinter as tk
from src.gui.components.BaseComponent import BaseComponent


class PickResumeList(BaseComponent):
    def __init__(self, master):
        self._frame = tk.Frame(master, padx=5, pady=5)
        self._lst_resumes = tk.Listbox(self._frame)
        self._btn_open_resume = tk.Button(self._frame, text="View/Edit Resume")

        self._lst_resumes.grid(row=0)
        self._btn_open_resume.grid(row=1)
        
    @property
    def lstResumes(self):
        return self._lst_resumes
    
    @property
    def btnOpenResume(self):
        return self._btn_open_resume
