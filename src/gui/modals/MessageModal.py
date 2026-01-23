import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseModal import BaseModal


class MessageModal(BaseModal):

    def __init__(
        self,
        master: tk.Frame,
        title: str = "Modal",
        message: str = ""
    ):
        self._frame = tk.Toplevel(master, padx=20, pady=10)
        self._frame.title(title)
        lbl_message = tk.Label(self._frame, text=message)
        self._btn_ok = ttk.Button(self._frame, text="OK", command=self.close)
        
        lbl_message.pack(fill=tk.BOTH, anchor="n")
        self._btn_ok.pack(anchor="center")
