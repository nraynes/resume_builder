import tkinter as tk
from src.gui.base.BaseListForm import BaseListForm
from typing import Callable
from src.gui.lib.Entry import Entry


class SkillsForm(BaseListForm):
    def __init__(self, *args, update_skills_reference_cb: Callable, **kwargs):
        self._heading = "Skills"
        self.update_skills_reference_cb = update_skills_reference_cb
        super().__init__(*args, **kwargs)
        self._frame.rowconfigure(2, weight=1)
        self._inp_skill = Entry(self._frame)

        self._inp_skill.grid(row=4, column=2)

    @property
    def inpSkill(self) -> tk.Entry:
        return self._inp_skill

    def cmdAdd(self):
        skill = self._inp_skill.get()
        self.addItem(skill, skill)
        self.update_skills_reference_cb()

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)
            self.update_skills_reference_cb()

    def populateData(self, skills: list[str]):
        self.clear()
        for skill in skills:
            self.addItem(skill, skill)
        self.update_skills_reference_cb()
