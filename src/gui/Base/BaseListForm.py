import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent


class BaseListForm(BaseComponent):
    _heading: str

    def __init__(self, master):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        self._frame.rowconfigure(2, weight=1)
        lbl_heading = tk.Label(
            self._frame, text=self._heading, font=("Helvetica", 18, "bold")
        )
        self._lst_items = tk.Listbox(self._frame)
        self._btn_delete = ttk.Button(self._frame, text="Delete")
        self._btn_add = ttk.Button(self._frame, text="Add")

        lbl_heading.grid(row=0, column=0, sticky="W")
        self.spacing().grid(row=1, column=0)
        self._lst_items.grid(row=2, column=0, columnspan=4, sticky="NSEW")
        self.spacing().grid(row=3, column=0)
        self._btn_delete.grid(row=4, column=0)
        self._btn_add.grid(row=4, column=2)

    @property
    def lstItems(self):
        return self._lst_items

    @property
    def btnDelete(self):
        return self._btn_delete

    @property
    def btnAdd(self):
        return self._btn_add
