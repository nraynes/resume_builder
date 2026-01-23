import tkinter as tk
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.ResumeEditor.subcomponents.ExperienceEditor import ExperienceEditor
from src.models.Experience import Experience


class ExperienceWindow(BaseWindow):

    def __init__(self, master, experience: Experience, cmd_save):
        self._frame = tk.Toplevel(master)
        self._frame.title("Experience Editor")
        self._cmd_save = cmd_save
        self._edt_experience = ExperienceEditor(self._frame, cmd_close=self.save)
        self._edt_experience.pack()
        self.populateData(experience)

    def populateData(self, experience: Experience):
        self._edt_experience.populateData(experience)

    def save(self) -> Experience:
        self._cmd_save(self._edt_experience.getObject())

    def getObject(self) -> Experience:
        return self._edt_experience.getObject()

    def show(self):
        pass

    def hide(self):
        self._frame.destroy()
