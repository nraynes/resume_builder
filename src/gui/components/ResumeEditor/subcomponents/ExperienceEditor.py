import tkinter as tk
from tkinter import ttk
from src.models.Experience import Experience
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.LabeledInput import LabeledInput
from src.gui.lib.LabeledDateInput import LabeledDateInput
from src.gui.components.ResumeEditor.subcomponents.BulletsForm import BulletsForm
from src.gui.components.ResumeEditor.subcomponents.BulletEditor import BulletEditor
from src.gui.base.BaseListItem import BaseListItem
from typing import Optional


class ExperienceEditor(BaseComponent):
    def __init__(self, master, cmd_close):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)
        self.cmd_close = cmd_close
        self._inp_job_title = LabeledInput(self._frame, "Job Title:")
        self._inp_company = LabeledInput(self._frame, "Company:")
        self._inp_company_location = LabeledInput(self._frame, "Company Location:")
        self._dat_started_on = LabeledDateInput(self._frame, "Started On:")
        self._dat_ended_on = LabeledDateInput(self._frame, "Ended On:")
        lbl_current_position = tk.Label(self._frame, text="Current Position:")
        self._checked = tk.IntVar(value=0)
        self._checked.trace_add("write", self.onCheck)
        self._chk_current_position = tk.Checkbutton(self._frame, variable=self._checked, onvalue=1, offvalue=0)
        self._frm_bullets = BulletsForm(
            self._frame,
            cmd_edit=self.showBulletEditor,
            cmd_close=self.hideBulletEditor
        )
        self._edt_bullet = BulletEditor(self._frame, cmd_close=self.hideBulletEditor)
        self._btn_submit = ttk.Button(self._frame, text="Save", command=self.save)

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
        self.spacing().grid(row=7)
        self._btn_submit.grid(row=9, column=0, sticky="EW")

    def showEndDate(self):
        self._dat_ended_on.undefault()
        self._dat_ended_on.grid(row=3, column=1, sticky="EW")

    def hideEndDate(self):
        self._dat_ended_on.default()
        self._dat_ended_on.grid_forget()

    def onCheck(self, *args):
        if self._checked.get() == 0:
            self.showEndDate()
        else:
            self.hideEndDate()

    def populateData(self, experience: Experience):
        self._frm_bullets.populateData(experience.bullets.values())
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
        self._edt_bullet.grid(row=8, column=0, columnspan=4, sticky="EW")

    def hideBulletEditor(self, bullet: Optional[BaseListItem] = None):
        if bullet is not None:
            self._frm_bullets.replaceItem(bullet)
        self._edt_bullet.grid_forget()

    def save(self):
        self.cmd_close()

    @property
    def inpJobTitle(self):
        return self._inp_job_title

    @property
    def inpCompany(self):
        return self._inp_company

    @property
    def inpCompanyLocation(self):
        return self._inp_company_location

    @property
    def datStartedOn(self):
        return self._dat_started_on

    @property
    def datEndedOn(self):
        return self._dat_ended_on

    @property
    def chkCurrentPosition(self):
        return self._chk_current_position

    @property
    def frmBullets(self):
        return self._frm_bullets

    @property
    def edtBullet(self):
        return self._edt_bullet

    @property
    def btnSubmit(self):
        return self._btn_submit
