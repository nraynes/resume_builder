import tkinter as tk
from src.gui.base.BaseModal import BaseModal
from src.gui.lib.Toplevel import Toplevel
from src.gui.lib.Label import Label
from src.gui.lib.Button import Button


class MessageModal(BaseModal):

    def __init__(
        self,
        master: tk.Frame,
        title: str = "Modal",
        message: str = ""
    ):
        self._frame = Toplevel(master, padx=20, pady=10)
        self._frame.title(title)
        lbl_message = Label(self._frame, text=message)
        self._btn_ok = Button(self._frame, text="OK", command=self.close)
        
        lbl_message.pack(fill=tk.BOTH, anchor="n")
        self._btn_ok.pack(anchor="center")
