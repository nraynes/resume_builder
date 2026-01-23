import tkinter as tk
from src.gui.base.BaseWindow import BaseWindow
from src.models.Education import Education
from src.gui.components.ResumeEditor.subcomponents.EducationEditor import EducationEditor


class EducationWindow(BaseWindow):

    def __init__(self, master, education: Education, cmd_save):
        self._frame = tk.Toplevel(master)
        self._frame.title("Education Editor")
        self._cmd_save = cmd_save
        self._edt_education = EducationEditor(self._frame, cmd_close=self.save)
        self._edt_education.pack()
        self.populateData(education)

    def populateData(self, education: Education):
        self._edt_education.populateData(education)

    def save(self) -> Education:
        self._cmd_save(self._edt_education.getObject())

    def show(self):
        pass

    def hide(self):
        self._frame.destroy()
