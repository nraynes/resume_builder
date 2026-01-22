import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.components.LabeledInput import LabeledInput
from src.gui.components.LabeledDateInput import LabeledDateInput
from src.gui.components.ResumeEditor.subcomponents.BulletsForm import BulletsForm
from src.gui.components.ResumeEditor.subcomponents.BulletEditor import BulletEditor


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
        self._chk_current_position = tk.Checkbutton(self._frame)
        self._frm_bullets = BulletsForm(self._frame, cmd_edit=self.showBulletEditor)
        self._edt_bullet = BulletEditor(self._frame, cmd_close=self.hideBulletEditor)
        self._btn_submit = ttk.Button(self._frame, text="Save", command=self.save)

        self._inp_job_title.grid(row=0, column=0, columnspan=4, sticky="EW")
        self._inp_company.grid(row=1, column=0, columnspan=4, sticky="EW")
        self._inp_company_location.grid(row=2, column=0, columnspan=4, sticky="EW")
        self._dat_started_on.grid(row=3, column=0, sticky="EW")
        self._dat_ended_on.grid(row=3, column=1, sticky="EW")
        lbl_current_position.grid(row=3, column=2, sticky="E")
        self._chk_current_position.grid(row=3, column=3, sticky="EW")
        self.spacing().grid(row=4)
        self._frm_bullets.grid(row=5, column=0, columnspan=4, sticky="EW")
        self.spacing().grid(row=6)
        self.spacing().grid(row=7)
        self._btn_submit.grid(row=9, column=0, sticky="EW")

    def showBulletEditor(self):
        self._edt_bullet.grid(row=8, column=0, columnspan=4, sticky="EW")

    def hideBulletEditor(self):
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
