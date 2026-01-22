import tkinter as tk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.components.ResumeEditor.subcomponents.ResumeMetaDataForm import ResumeMetaDataForm
from src.gui.components.ResumeEditor.subcomponents.HeaderForm import HeaderForm
from src.gui.components.ResumeEditor.subcomponents.ButtonPanel import ButtonPanel
from src.gui.components.ResumeEditor.subcomponents.SummaryForm import SummaryForm
from src.gui.components.ResumeEditor.subcomponents.SkillsForm import SkillsForm
from src.gui.components.ResumeEditor.subcomponents.EducationForm import EducationForm
from src.gui.components.ResumeEditor.subcomponents.ExperienceForm import ExperienceForm
from src.gui.components.ResumeEditor.subcomponents.CertificationsForm import CertificationsForm


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
        self.spacing().pack()

        # Build fourth layer.
        layer_four = tk.Frame(self._frame)
        self._frm_experience = ExperienceForm(layer_four)
        self._frm_education = EducationForm(layer_four)
        self._frm_certifications = CertificationsForm(layer_four)
        self._frm_experience.grid(row=0, column=0, sticky="EW")
        self.spacing(layer_four).grid(row=0, column=1)
        self._frm_education.grid(row=0, column=2, sticky="EW")
        self.spacing(layer_four).grid(row=0, column=3)
        self._frm_certifications.grid(row=0, column=4, sticky="EW")
        layer_four.pack(fill=tk.BOTH)

    @property
    def frmMetaData(self):
        return self._frm_meta_data

    @property
    def frmHeader(self):
        return self._frm_header

    @property
    def frmSummary(self):
        return self._frm_summary

    @property
    def frmSkills(self):
        return self._frm_skills

    @property
    def frmExperience(self):
        return self._frm_experience

    @property
    def frmEducation(self):
        return self._frm_education

    @property
    def frmCertifications(self):
        return self._frm_certifications
