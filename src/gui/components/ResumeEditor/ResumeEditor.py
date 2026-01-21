import tkinter as tk
from src.gui.Base.BaseComponent import BaseComponent
from src.gui.components.ResumeEditor.ResumeMetaDataForm import ResumeMetaDataForm
from src.gui.components.ResumeEditor.HeaderForm import HeaderForm
from src.gui.components.ResumeEditor.ButtonPanel import ButtonPanel
from src.gui.components.ResumeEditor.SummaryForm import SummaryForm
from src.gui.components.ResumeEditor.SkillsForm import SkillsForm


class ResumeEditor(BaseComponent):
    def __init__(self, master, openMainCb):
        self._frame = tk.Frame(master, padx=5, pady=5)

        # Build first layer.
        layer_one = tk.Frame(self._frame)
        self._frm_meta_data = ResumeMetaDataForm(layer_one)
        self._pnl_commands = ButtonPanel(layer_one, openMainCb)
        layer_one.columnconfigure(0, weight=1)
        self._frm_meta_data.grid(row=0, column=0, sticky="EW")
        self.spacing(layer_one).grid(row=0, column=1)
        self._pnl_commands.grid(row=0, column=2, sticky="E")
        layer_one.pack(fill=tk.BOTH)
        self.spacing().pack()

        # Build second layer.
        self._frm_header = HeaderForm(self._frame)
        self._frm_header.pack(fill=tk.BOTH)
        self.spacing().pack()

        # Build third layer.
        layer_three = tk.Frame(self._frame)
        layer_three.columnconfigure(0, weight=1)
        self._frm_summary = SummaryForm(layer_three)
        self._frm_skills = SkillsForm(layer_three)
        self._frm_summary.grid(row=0, column=0, sticky="EW")
        self.spacing(layer_three).grid(row=0, column=1)
        self._frm_skills.grid(row=0, column=2, sticky="NSEW")
        layer_three.pack(fill=tk.BOTH)

    @property
    def frmMetaData(self):
        return self._frm_meta_data

    @property
    def frmHeader(self):
        return self._frm_header

    @property
    def txtSummary(self):
        return self._txt_summary
