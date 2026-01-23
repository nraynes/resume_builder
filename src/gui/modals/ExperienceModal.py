import tkinter as tk
from src.gui.base.BaseModal import BaseModal
from src.gui.components.ExperienceEditor import ExperienceEditor
from src.models.Experience import Experience
from typing import Callable


class ExperienceModal(BaseModal):

    def __init__(
        self,
        master: tk.Frame,
        experience: Experience,
        save_experience_cb: Callable
    ):
        self._frame = tk.Toplevel(master)
        self._frame.title("Experience Editor")
        self.save_experience_cb = save_experience_cb
        self._edt_experience = ExperienceEditor(self._frame, save_experience_cb=self.save)

        self._edt_experience.pack()
        self.populateData(experience)

    @property
    def edtExperience(self) -> ExperienceEditor:
        return self._edt_experience

    def populateData(self, experience: Experience):
        self._edt_experience.populateData(experience)

    def save(self) -> Experience:
        self.save_experience_cb(self._edt_experience.getObject())
