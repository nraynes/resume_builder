import tkinter as tk
from src.gui.Base.BaseWindow import BaseWindow
from src.gui.components.ResumeEditor.ResumeEditor import ResumeEditor


class EditorWindow(BaseWindow):
    def __init__(self, master, openMainCb, show: bool = True):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self._frm_resume = ResumeEditor(self._frame, openMainCb)
        self._frm_resume.pack()
        if show:
            self.show()

    @property
    def frmResume(self):
        return self._frm_resume
