import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseWindow import BaseWindow


class ModalWindow(BaseWindow):

    def __init__(self, master, title: str = "Modal", message: str = ""):
        self._frame = tk.Toplevel(master, padx=20, pady=10)
        self._frame.title(title)
        lbl_message = tk.Label(self._frame, text=message)
        self._btn_ok = ttk.Button(self._frame, text="OK", command=self.hide)
        lbl_message.pack(fill=tk.BOTH, anchor="n")
        self._btn_ok.pack(anchor="center")
        
    def show(self):
        pass
    
    def hide(self):
        self._frame.destroy()
