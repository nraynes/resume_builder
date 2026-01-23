import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.base.BaseListItem import BaseListItem
from typing import Callable


class BulletEditor(BaseComponent):

    def __init__(self, master: tk.Frame, save_bullet_cb: Callable):
        self._frame = tk.Frame(master, padx=10, pady=10, borderwidth=1, relief="solid")
        self.save_bullet_cb = save_bullet_cb
        self._original_bullet = None
        lbl_bullet = tk.Label(self._frame, text="Bullet Text", font=("Helvetica", 16, "bold"))
        self._txt_bullet = tk.Text(self._frame, borderwidth=1, relief="solid", height=10)
        self._btn_submit = ttk.Button(self._frame, text="Save", command=self.save)

        lbl_bullet.pack(anchor="w")
        self.spacing().pack()
        self._txt_bullet.pack(fill=tk.BOTH)
        self.spacing().pack()
        self._btn_submit.pack(anchor="e")

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

    def save(self):
        new_bullet = self._txt_bullet.get("1.0", "end-1c")
        self.save_bullet_cb(
            BaseListItem(new_bullet, self._original_bullet.id, new_bullet)
        )
