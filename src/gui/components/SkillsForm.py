import tkinter as tk
from src.gui.base.BaseListForm import BaseListForm


class SkillsForm(BaseListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Skills"
        super().__init__(*args, **kwargs)
        self._frame.rowconfigure(2, weight=1)
        self._inp_skill = tk.Entry(self._frame)

        self._inp_skill.grid(row=4, column=2)

    @property
    def inpSkill(self) -> tk.Entry:
        return self._inp_skill

    def cmdAdd(self):
        skill = self._inp_skill.get()
        self.addItem(skill, skill)

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)

    def populateData(self, skills: list[str]):
        self.clear()
        for skill in skills:
            self.addItem(skill, skill)
