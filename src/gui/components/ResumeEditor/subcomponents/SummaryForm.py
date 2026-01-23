import tkinter as tk
from src.gui.base.BaseComponent import BaseComponent


class SummaryForm(BaseComponent):
    def __init__(self, master):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        lbl_summary = tk.Label(self._frame, text="Summary", font=("Helvetica", 18, "bold"))
        self._txt_summary = tk.Text(self._frame, borderwidth=1, relief="solid")
        lbl_summary.grid(row=0, sticky="EW")
        self.spacing().grid(row=1)
        self._txt_summary.grid(row=2)

    def get(self):
        return self._txt_summary.get("1.0", "end-1c")

    def populateData(self, summary: str):
        self._txt_summary.delete("1.0", tk.END)
        self._txt_summary.insert(tk.END, summary)

    @property
    def txtSummary(self):
        return self._txt_summary
