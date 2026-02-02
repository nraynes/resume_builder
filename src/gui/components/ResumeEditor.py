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
from src.gui.components.AwardsForm import AwardsForm
from typing import Callable
from src.gui.lib.Frame import Frame
from src.gui.lib.Label import Label


class ResumeEditor(BaseComponent):

    def __init__(
        self,
        master: tk.Frame,
        open_main_cb: Callable,
        save_resume_cb: Callable,
        generate_pdf_cb: Callable,
        resize_canvas_cb: Callable
    ):
        self._frame = Frame(master, padx=5, pady=5)
        self._is_cv = False
        self.resize_canvas_cb = resize_canvas_cb

        # Labels showing which skills have direct experience tied to them in the document.
        self._covered_skills = set()
        self._lbl_covered_skills = Label(self._frame, text="Covered Skills: ")
        self._lbl_missing_skills = Label(self._frame, text="Missing Skills: ")
        self._top_spacing = self.spacing()

        # Build first layer.
        self._layer_one = Frame(self._frame)
        self._frm_meta_data = ResumeMetaDataForm(self._layer_one)
        self._pnl_commands = ButtonPanel(
            self._layer_one,
            open_main_cb=open_main_cb,
            save_resume_cb=save_resume_cb,
            generate_pdf_cb=generate_pdf_cb,
        )
        self._layer_one.columnconfigure(0, weight=1)
        self._frm_meta_data.grid(row=0, column=0, sticky="EW")
        self.spacing(self._layer_one).grid(row=0, column=1)
        self._pnl_commands.grid(row=0, column=2, sticky="E")
        self._layer_one.grid(row=3, sticky="EW")
        self.spacing().grid(row=4)

        # Build second layer.
        self._frm_header = HeaderForm(self._frame)
        self._frm_header.grid(row=5, sticky="EW")
        self.spacing().grid(row=6)

        # Build third layer.
        self._layer_three = Frame(self._frame)
        self._layer_three.columnconfigure(2, weight=1)
        self._layer_three.columnconfigure(4, weight=1)
        self._frm_summary = SummaryForm(self._layer_three)
        self._frm_awards = AwardsForm(self._layer_three)
        self._frm_skills = SkillsForm(self._layer_three, update_skills_reference_cb=self.updateSkillsReferenceInExperience)
        self._frm_summary.grid(row=0, column=0, sticky="EW")
        self.spacing(self._layer_three).grid(row=0, column=1)
        self._frm_awards.grid(row=0, column=2, sticky="NSEW")
        self.spacing(self._layer_three).grid(row=0, column=3)
        self._frm_skills.grid(row=0, column=4, sticky="NSEW")
        self._layer_three.grid(row=7, sticky="EW")
        self.spacing().grid(row=8)

        # Build fourth layer.
        self._layer_four = Frame(self._frame)
        self._frm_experience = ExperienceForm(
            self._layer_four, update_covered_skills_cb=self.updateCoveredSkills
        )
        self._frm_education = EducationForm(self._layer_four)
        self._frm_certifications = CertificationsForm(self._layer_four)
        self._frm_experience.grid(row=0, column=0, sticky="EW")
        self.spacing(self._layer_four).grid(row=0, column=1)
        self._frm_education.grid(row=0, column=2, sticky="EW")
        self.spacing(self._layer_four).grid(row=0, column=3)
        self._frm_certifications.grid(row=0, column=4, sticky="EW")
        self._layer_four.grid(row=9, sticky="EW")

    @property
    def layerOne(self) -> tk.Frame:
        return self._layer_one

    @property
    def layerThree(self) -> tk.Frame:
        return self._layer_three

    @property
    def layerFour(self) -> tk.Frame:
        return self._layer_four

    @property
    def coveredSkills(self) -> set[str]:
        return self._covered_skills

    @property
    def lblCoveredSkills(self) -> tk.Label:
        return self._lbl_covered_skills

    @property
    def lblMissingSkills(self) -> tk.Label:
        return self._lbl_missing_skills

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
    def frmAwards(self) -> AwardsForm:
        return self._frm_awards

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

    def showCoveredSkills(self):
        self._lbl_covered_skills.grid(row=0, sticky="W")
        self._lbl_missing_skills.grid(row=1, sticky="W")
        self._top_spacing.grid(row=2)

    def hideCoveredSkills(self):
        self._lbl_covered_skills.grid_forget()
        self._lbl_missing_skills.grid_forget()
        self._top_spacing.grid_forget()    

    def updateCoveredSkills(self):
        self._covered_skills = set()
        for work in self._frm_experience.items():
            for bullet in work.bullets:
                for skill in bullet.associatedSkills:
                    self._covered_skills.add(skill)
        str_covered_skills = ""
        for skill in self._covered_skills:
            str_covered_skills += f"{skill}, "
        str_covered_skills = str_covered_skills[0:-2]
        str_missing_skills = ""
        for skill in self._frm_skills.items():
            if skill not in self._covered_skills:
                str_missing_skills += f"{skill}, "
        str_missing_skills = str_missing_skills[0:-2]
        self._lbl_covered_skills.config(text=f"Covered Skills: {str_covered_skills}")
        self._lbl_missing_skills.config(text=f"Missing Skills: {str_missing_skills}")

    def updateSkillsReferenceInExperience(self):
        self._frm_experience.skills = self._frm_skills.items()
        self.updateCoveredSkills()

    def populateData(self, resume: Cv):
        self._is_cv = not isinstance(resume, Resume)
        title = resume.title if not self._is_cv else "Curriculum Vitae"
        author = resume.author if not self._is_cv else "N/A"
        self._frm_meta_data.populateData(title, author)
        self._frm_header.populateData(resume.header)
        self._frm_summary.populateData(resume.summary)
        self._frm_skills.populateData(resume.skills)
        self._frm_experience.populateData(resume.workExperience)
        self._frm_education.populateData(resume.education)
        self._frm_certifications.populateData(resume.certificates)
        self._frm_awards.populateData(resume.awards)
        self.updateCoveredSkills()
        if self._is_cv:
            self.hideCoveredSkills()
        else:
            self.showCoveredSkills()
        self.resize_canvas_cb()

    def getObject(self) -> Cv:
        data_object = {
            "header": self._frm_header.to_dict(),
            "summary": self._frm_summary.get(),
            "work_experience": [work.to_dict() for work in self._frm_experience.items()],
            "education": [edu.to_dict() for edu in self._frm_education.items()],
            "certificates": [cert.to_dict() for cert in self._frm_certifications.items()],
            "awards": [award.to_dict() for award in self._frm_awards.items()],
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
