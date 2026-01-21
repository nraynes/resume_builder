import tkinter as tk
from tkinter import ttk
from src.gui.Base.BaseComponent import BaseComponent


class SkillsForm(BaseComponent):
    def __init__(self, master):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        self._frame.rowconfigure(2, weight=1)
        self._frame.columnconfigure(1, weight=1)

        lbl_heading = tk.Label(self._frame, text="Skills", font=("Helvetica", 18, "bold"))
        self._lst_skills = tk.Listbox(self._frame)
        self._btn_delete = ttk.Button(self._frame, text="Delete Skill")
        self._inp_skill = tk.Entry(self._frame)
        self._btn_submit = ttk.Button(self._frame, text="Add Skill")

        lbl_heading.grid(row=0, column=0, sticky="W")
        self.spacing().grid(row=1, column=0)
        self._lst_skills.grid(row=2, column=0, columnspan=4, sticky="NSEW")
        self.spacing().grid(row=3, column=0)
        self._btn_delete.grid(row=4, column=0)
        self._inp_skill.grid(row=4, column=1)
        self._btn_submit.grid(row=4, column=3)

    @property
    def lstSkills(self):
        return self._lst_skills

    @property
    def btnDelete(self):
        return self._btn_delete

    @property
    def inpSkill(self):
        return self._inp_skill

    @property
    def btnSubmit(self):
        return self._btn_submit
