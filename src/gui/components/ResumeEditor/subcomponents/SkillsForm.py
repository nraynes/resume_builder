import tkinter as tk
from src.gui.base.BaseListForm import BaseListForm


class SkillsForm(BaseListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Skills"
        super().__init__(*args, **kwargs)
        self._inp_skill = tk.Entry(self._frame)
        self._inp_skill.grid(row=4, column=1)

    @property
    def inpSkill(self):
        return self._inp_skill
