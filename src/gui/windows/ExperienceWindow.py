import tkinter as tk
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.ResumeEditor.subcomponents.ExperienceEditor import ExperienceEditor


class ExperienceWindow(BaseWindow):
    def __init__(self, master):
        self._frame = tk.Toplevel(master)
        self._frame.title("Experience Editor")
        self._edt_experience = ExperienceEditor(self._frame, cmd_close=self._frame.destroy)
        self._edt_experience.pack()

    def show(self):
        pass

    def hide(self):
        pass
