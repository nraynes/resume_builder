import tkinter as tk
from src.gui.base.BaseWindow import BaseWindow
from src.models.Education import Education
from src.gui.components.ResumeEditor.subcomponents.EducationEditor import EducationEditor


class EducationWindow(BaseWindow):
    def __init__(self, master, education: Education):
        self._frame = tk.Toplevel(master)
        self._frame.title("Education Editor")
        self._edt_education = EducationEditor(self._frame, self._frame.destroy)
        self._edt_education.pack()
        self.populateData(education)

    def populateData(self, education: Education):
        self._edt_education.populateData(education)

    def show(self):
        pass

    def hide(self):
        pass
