import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent


class BulletEditor(BaseComponent):
    def __init__(self, master, cmd_close):
        self._frame = tk.Frame(master, padx=10, pady=10, borderwidth=1, relief="solid")
        self.cmd_close = cmd_close
        lbl_bullet = tk.Label(self._frame, text="Bullet Text", font=("Helvetica", 16, "bold"))
        self._txt_bullet = tk.Text(self._frame, borderwidth=1, relief="solid", height=10)
        self._btn_submit = ttk.Button(self._frame, text="Save", command=self.save)

        lbl_bullet.pack(anchor="w")
        self.spacing().pack()
        self._txt_bullet.pack(fill=tk.BOTH)
        self.spacing().pack()
        self._btn_submit.pack(anchor="e")
        
    def save(self):
        self.cmd_close()

    @property
    def txtBullet(self):
        return self._txt_bullet

    @property
    def btnSubmit(self):
        return self._btn_submit
