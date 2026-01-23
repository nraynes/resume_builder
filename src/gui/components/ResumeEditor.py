import tkinter as tk
from src.models.Cv import Cv
from src.models.Resume import Resume
from src.gui.base.BaseComponent import BaseComponent
from src.gui.components.ResumeMetaDataForm import ResumeMetaDataForm
from src.gui.components.HeaderForm import HeaderForm
from src.gui.components.ButtonPanel import ButtonPanel
from src.gui.components.SummaryForm import SummaryForm
from src.gui.components.SkillsForm import SkillsForm
from src.gui.components.EducationForm import EducationForm
from src.gui.components.ExperienceForm import ExperienceForm
from src.gui.components.CertificationsForm import CertificationsForm
from typing import Callable


class ResumeEditor(BaseComponent):

    def __init__(
        self,
        master: tk.Frame,
        open_main_cb: Callable,
        save_resume_cb: Callable,
        generate_pdf_cb: Callable
    ):
        self._frame = tk.Frame(master, padx=5, pady=5)
        self._is_cv = False

        # Build first layer.
        layer_one = tk.Frame(self._frame)
        self._frm_meta_data = ResumeMetaDataForm(layer_one)
        self._pnl_commands = ButtonPanel(
            layer_one,
            open_main_cb=open_main_cb,
            save_resume_cb=save_resume_cb,
            generate_pdf_cb=generate_pdf_cb,
        )
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
    def frmMetaData(self) -> ResumeMetaDataForm:
        return self._frm_meta_data
    
    @property
    def pnlCommands(self) -> ButtonPanel:
        return self._pnl_commands

    @property
    def frmHeader(self) -> HeaderForm:
        return self._frm_header

    @property
    def frmSummary(self) -> SummaryForm:
        return self._frm_summary

    @property
    def frmSkills(self) -> SkillsForm:
        return self._frm_skills

    @property
    def frmExperience(self) -> ExperienceForm:
        return self._frm_experience

    @property
    def frmEducation(self) -> EducationForm:
        return self._frm_education

    @property
    def frmCertifications(self) -> CertificationsForm:
        return self._frm_certifications    
    
    @property
    def isCv(self) -> bool:
        return self._is_cv

    def populateData(self, resume: Cv):
        is_resume = isinstance(resume, Resume)
        self._is_cv = not is_resume
        title = resume.title if is_resume else "Curriculum Vitae"
        author = resume.author if is_resume else "N/A"
        self._frm_meta_data.populateData(title, author)
        self._frm_header.populateData(resume.header)
        self._frm_summary.populateData(resume.summary)
        self._frm_skills.populateData(resume.skills)
        self._frm_experience.populateData(resume.workExperience)
        self._frm_education.populateData(resume.education)
        self._frm_certifications.populateData(resume.certificates)

    def getObject(self) -> Cv:
        data_object = {
            "header": self._frm_header.to_dict(),
            "summary": self._frm_summary.get(),
            "work_experience": [work.to_dict() for work in self._frm_experience.items()],
            "education": [edu.to_dict() for edu in self._frm_education.items()],
            "certificates": [cert.to_dict() for cert in self._frm_certifications.items()],
            "skills": self._frm_skills.items(),
        }
        if self._is_cv:
            return Cv(data_object)
        else:
            return Resume(
                title=self._frm_meta_data.inpTitle.get(),
                author=self._frm_meta_data.inpAuthor.get(),
                data=data_object
            )
