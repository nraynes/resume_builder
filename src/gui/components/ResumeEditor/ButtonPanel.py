import tkinter as tk
from tkinter import ttk
from src.gui.Base.BaseComponent import BaseComponent


class ButtonPanel(BaseComponent):
    def __init__(self, master, openMainCb):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=2, relief="sunken")
        self._btn_back = ttk.Button(self._frame, text="Back", command=openMainCb)
        self._btn_save = ttk.Button(self._frame, text="Save Resume")
        self._btn_generate = ttk.Button(self._frame, text="Generate PDF")

        self._btn_back.grid(row=0, column=0)
        self._btn_save.grid(row=0, column=1)
        self._btn_generate.grid(row=0, column=2)

    @property
    def btnBack(self):
        return self._btn_back

    @property
    def btnSave(self):
        return self._btn_save

    @property
    def btnGenerate(self):
        return self._btn_generate
