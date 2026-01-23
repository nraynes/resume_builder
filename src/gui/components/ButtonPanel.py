import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.modals.MessageModal import MessageModal
from typing import Callable


class ButtonPanel(BaseComponent):

    def __init__(
        self,
        master: tk.Frame,
        open_main_cb: Callable,
        save_resume_cb: Callable,
        generate_pdf_cb: Callable
    ):
        self.save_resume_cb = save_resume_cb
        self._sub_window = None
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=2, relief="sunken")
        self._btn_back = ttk.Button(self._frame, text="Back", command=open_main_cb)
        self._btn_save = ttk.Button(self._frame, text="Save Resume", command=self.saveResume)
        self._btn_generate = ttk.Button(
            self._frame, text="Generate PDF", command=generate_pdf_cb
        )

        self._btn_back.grid(row=0, column=0)
        self._btn_save.grid(row=0, column=1)
        self._btn_generate.grid(row=0, column=2)

    @property
    def btnBack(self) -> ttk.Button:
        return self._btn_back

    @property
    def btnSave(self) -> ttk.Button:
        return self._btn_save

    @property
    def btnGenerate(self) -> ttk.Button:
        return self._btn_generate

    def saveResume(self):
        self.save_resume_cb()
        self._sub_window = MessageModal(
            self._frame, title="Saved", message="Saved changes."
        )
