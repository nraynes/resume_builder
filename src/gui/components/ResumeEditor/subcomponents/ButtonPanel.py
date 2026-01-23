import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.windows.ModalWindow import ModalWindow


class ButtonPanel(BaseComponent):

    def __init__(self, master, openMainCb, saveResumeCb, generatePDFCb):
        self._cmd_save = saveResumeCb
        self._sub_window = None
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=2, relief="sunken")
        self._btn_back = ttk.Button(self._frame, text="Back", command=openMainCb)
        self._btn_save = ttk.Button(self._frame, text="Save Resume", command=self.saveResume)
        self._btn_generate = ttk.Button(
            self._frame, text="Generate PDF", command=generatePDFCb
        )

        self._btn_back.grid(row=0, column=0)
        self._btn_save.grid(row=0, column=1)
        self._btn_generate.grid(row=0, column=2)

    def saveResume(self):
        self._cmd_save()
        self._sub_window = ModalWindow(self._frame, title="Saved", message="Saved changes.")

    @property
    def btnBack(self):
        return self._btn_back

    @property
    def btnSave(self):
        return self._btn_save

    @property
    def btnGenerate(self):
        return self._btn_generate
