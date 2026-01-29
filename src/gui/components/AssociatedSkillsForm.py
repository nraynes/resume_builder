import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseListForm import BaseListForm


class AssociatedSkillsForm(BaseListForm):

    def __init__(self, *args, skills: list[str] = [] , **kwargs):
        self._heading = "Associated Skills"
        super().__init__(*args, **kwargs)
        self._frame.rowconfigure(2, weight=1)
        self._cmb_skill = ttk.Combobox(self._frame, values=skills)

        self._cmb_skill.grid(row=4, column=2)

    @property
    def cmbSkill(self) -> ttk.Combobox:
        return self._cmb_skill

    def cmdAdd(self):
        skill = self._cmb_skill.get()
        self.addItem(skill, skill)

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)

    def populateData(self, skills: list[str]):
        self.clear()
        for skill in skills:
            self.addItem(skill, skill)
