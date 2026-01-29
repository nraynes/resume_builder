import tkinter as tk
from src.gui.base.BaseModal import BaseModal
from src.models.Education import Education
from src.gui.components.EducationEditor import EducationEditor
from typing import Callable
from src.gui.lib.Toplevel import Toplevel


class EducationModal(BaseModal):

    def __init__(
        self,
        master: tk.Frame,
        education: Education,
        save_education_cb: Callable
    ):
        self._frame = Toplevel(master)
        self._frame.title("Education Editor")
        self.save_education_cb = save_education_cb
        self._edt_education = EducationEditor(self._frame, save_education_cb=self.save)

        self._edt_education.pack()
        self.populateData(education)

    @property
    def edtEducation(self) -> EducationEditor:
        return self._edt_education

    def populateData(self, education: Education):
        self._edt_education.populateData(education)

    def save(self) -> Education:
        self.save_education_cb(self._edt_education.getObject())
