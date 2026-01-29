import tkinter as tk
from tkinter import ttk
from src.models.Experience import Experience
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.LabeledInput import LabeledInput
from src.gui.lib.LabeledDateInput import LabeledDateInput
from src.gui.components.BulletsForm import BulletsForm
from src.gui.components.BulletEditor import BulletEditor
from src.gui.base.BaseListItem import BaseListItem
from typing import Callable, Optional


class ExperienceEditor(BaseComponent):
    def __init__(self, master: tk.Toplevel, save_experience_cb: Callable, skills: list[str]):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self._left_container = tk.Frame(self._frame, padx=10, pady=10)
        self._left_container.columnconfigure(0, weight=1)
        self._left_container.columnconfigure(1, weight=1)
        self._inp_job_title = LabeledInput(self._left_container, "Job Title:")
        self._inp_company = LabeledInput(self._left_container, "Company:")
        self._inp_company_location = LabeledInput(self._left_container, "Company Location:")
        self._dat_started_on = LabeledDateInput(self._left_container, "Started On:")
        self._dat_ended_on = LabeledDateInput(self._left_container, "Ended On:")
        lbl_current_position = tk.Label(self._left_container, text="Current Position:")
        self._checked = tk.IntVar(value=0)
        self._checked.trace_add("write", self.onCheck)
        self._chk_current_position = tk.Checkbutton(self._left_container, variable=self._checked, onvalue=1, offvalue=0)
        self._frm_bullets = BulletsForm(
            self._left_container,
            edit_bullet_cb=self.showBulletEditor,
            close_bullet_cb=self.hideBulletEditor,
        )
        self._btn_submit = ttk.Button(self._left_container, text="Save", command=save_experience_cb)
        self._edt_bullet = BulletEditor(self._frame, save_bullet_cb=self.hideBulletEditor, skills=skills)

        self._inp_job_title.grid(row=0, column=0, columnspan=4, sticky="EW")
        self._inp_company.grid(row=1, column=0, columnspan=4, sticky="EW")
        self._inp_company_location.grid(row=2, column=0, columnspan=4, sticky="EW")
        self._dat_started_on.grid(row=3, column=0, sticky="EW")
        self.onCheck()
        lbl_current_position.grid(row=3, column=2, sticky="E")
        self._chk_current_position.grid(row=3, column=3, sticky="EW")
        self.spacing().grid(row=4)
        self._frm_bullets.grid(row=5, column=0, columnspan=4, sticky="EW")
        self.spacing().grid(row=6)
        self._btn_submit.grid(row=7, column=0, sticky="W")
        
        self._left_container.grid(row=0, column=0, sticky="N")

    @property
    def inpJobTitle(self) -> LabeledInput:
        return self._inp_job_title

    @property
    def inpCompany(self) -> LabeledInput:
        return self._inp_company

    @property
    def inpCompanyLocation(self) -> LabeledInput:
        return self._inp_company_location

    @property
    def datStartedOn(self) -> LabeledDateInput:
        return self._dat_started_on

    @property
    def datEndedOn(self) -> LabeledDateInput:
        return self._dat_ended_on

    @property
    def chkCurrentPosition(self) -> tk.Checkbutton:
        return self._chk_current_position

    @property
    def frmBullets(self) -> BulletsForm:
        return self._frm_bullets

    @property
    def edtBullet(self) -> BulletEditor:
        return self._edt_bullet

    @property
    def btnSubmit(self) -> ttk.Button:
        return self._btn_submit

    def showEndDate(self):
        self._dat_ended_on.grid(row=3, column=1, sticky="EW")

    def hideEndDate(self):
        self._dat_ended_on.grid_forget()

    def getObject(self) -> Experience:
        return Experience(
            {
                "job_title": self._inp_job_title.get(),
                "company": self._inp_company.get(),
                "company_location": self._inp_company_location.get(),
                "started_on": self._dat_started_on.getString(),
                "ended_on": self._dat_ended_on.getString(),
                "current_position": bool(self._checked.get()),
                "bullets": [bullet.to_dict() for bullet in self._frm_bullets.items()],
            }
        )

    def onCheck(self, *args):
        if self._checked.get() == 0:
            self.showEndDate()
        else:
            self.hideEndDate()

    def populateData(self, experience: Experience):
        self._frm_bullets.populateData(experience.bullets)
        self._inp_job_title.setValue(experience.jobTitle)
        self._inp_company.setValue(experience.company)
        self._inp_company_location.setValue(experience.companyLocation)
        self._dat_started_on.setValue(experience.startedOn)
        self._dat_ended_on.setValue(experience.endedOn)
        if experience.currentPosition:
            self._chk_current_position.select()
        else:
            self._chk_current_position.deselect()

    def showBulletEditor(self, bullet: BaseListItem):
        self._edt_bullet.populateData(bullet)
        self._edt_bullet.grid(row=0, column=1, sticky="N")

    def hideBulletEditor(self, bullet: Optional[BaseListItem] = None):
        if bullet is not None:
            self._frm_bullets.replaceItem(bullet)
        self._edt_bullet.grid_forget()
