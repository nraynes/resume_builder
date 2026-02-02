import tkinter as tk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.Frame import Frame
from src.gui.lib.Label import Label
from src.gui.lib.Text import Text


class SummaryForm(BaseComponent):
    def __init__(self, master: tk.Frame):
        self._frame = Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        self._frame.columnconfigure(0, weight=1)
        lbl_summary = Label(self._frame, text="Summary", font=("Helvetica", 18, "bold"))
        self._txt_summary = Text(self._frame, borderwidth=1, relief="solid", width=40)

        lbl_summary.grid(row=0, sticky="EW")
        self.spacing().grid(row=1)
        self._txt_summary.grid(row=2, sticky="EW")

    @property
    def txtSummary(self) -> tk.Text:
        return self._txt_summary

    def get(self) -> str:
        return self._txt_summary.get("1.0", "end-1c")

    def populateData(self, summary: str):
        self._txt_summary.delete("1.0", tk.END)
        self._txt_summary.insert(tk.END, summary)
