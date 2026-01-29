import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.base.BaseListItem import BaseListItem
from src.gui.components.AssociatedSkillsForm import AssociatedSkillsForm
from src.models.Bullet import Bullet
from typing import Callable
from src.gui.lib.Frame import Frame
from src.gui.lib.Label import Label
from src.gui.lib.Text import Text
from src.gui.lib.Button import Button


class BulletEditor(BaseComponent):

    def __init__(self, master: tk.Frame, save_bullet_cb: Callable, skills: list[str]):
        self._frame = Frame(master, padx=10, pady=10, borderwidth=1, relief="solid")
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)
        self._frame.columnconfigure(2, weight=0)
        self._frame.rowconfigure(1, weight=1)
        self.save_bullet_cb = save_bullet_cb
        self._original_bullet = None
        self._frm_associated_skills = AssociatedSkillsForm(self._frame, skills=skills, width=5)
        lbl_bullet = Label(self._frame, text="Bullet Text", font=("Helvetica", 16, "bold"))
        self._txt_bullet = Text(self._frame, borderwidth=1, relief="solid")
        self._btn_submit = Button(self._frame, text="Save", command=self.save)

        self._frm_associated_skills.pack(fill=tk.BOTH)
        self.spacing().pack()
        lbl_bullet.pack(anchor="w")
        self.spacing().pack()
        self._txt_bullet.pack(fill=tk.BOTH)
        self._btn_submit.pack(fill=tk.BOTH)

    @property
    def txtBullet(self) -> tk.Text:
        return self._txt_bullet

    @property
    def btnSubmit(self) -> ttk.Button:
        return self._btn_submit

    def populateData(self, bullet: BaseListItem):
        self._original_bullet = bullet
        self._txt_bullet.delete("1.0", tk.END)
        self._txt_bullet.insert(tk.END, bullet.text)
        self._frm_associated_skills.populateData(bullet.item.associatedSkills)

    def save(self):
        new_bullet = Bullet({
            "associated_skills": self._frm_associated_skills.items(),
            "text": self._txt_bullet.get("1.0", "end-1c")
        })
        self.save_bullet_cb(
            BaseListItem(new_bullet, self._original_bullet.id, new_bullet.text)
        )
