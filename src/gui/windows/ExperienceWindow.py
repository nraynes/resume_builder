import tkinter as tk
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.ResumeEditor.subcomponents.ExperienceEditor import ExperienceEditor
from src.models.Experience import Experience


class ExperienceWindow(BaseWindow):
    def __init__(self, master, experience: Experience):
        self._frame = tk.Toplevel(master)
        self._frame.title("Experience Editor")
        self._edt_experience = ExperienceEditor(self._frame, cmd_close=self._frame.destroy)
        self._edt_experience.pack()
        self.populateData(experience)

    def populateData(self, experience: Experience):
        self._edt_experience.populateData(experience)

    def show(self):
        pass

    def hide(self):
        pass
