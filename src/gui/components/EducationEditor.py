import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.LabeledInput import LabeledInput
from src.gui.lib.LabeledDateInput import LabeledDateInput
from src.gui.lib.LabeledCombo import LabeledCombo
from src.enums.Degree import Degree
from src.models.Education import Education
from typing import Callable
from src.gui.lib.Frame import Frame
from src.gui.lib.Label import Label
from src.gui.lib.Checkbutton import Checkbutton
from src.gui.lib.Button import Button


class EducationEditor(BaseComponent):

    def __init__(self, master: tk.Toplevel, save_education_cb: Callable):
        self._frame = Frame(master, padx=10, pady=10)
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)
        self._inp_school_name = LabeledInput(self._frame, "School Name:")
        self._cmb_degree_type = LabeledCombo(self._frame, "Degree Type:", values=[degree.name for degree in Degree])
        self._inp_major = LabeledInput(self._frame, "Major:")
        self._dat_grad = LabeledDateInput(self._frame, "Graduation Date:")
        lbl_still_attending = Label(self._frame, text="Still Attending:")
        self._checked = tk.IntVar(value=0)
        self._chk_still_attending = Checkbutton(self._frame, variable=self._checked, onvalue=1, offvalue=0)
        self._btn_submit = Button(self._frame, text="Save", command=save_education_cb)

        self._inp_school_name.grid(row=0, column=0, columnspan=3, sticky="EW")
        self._inp_major.grid(row=1, column=0, columnspan=3, sticky="EW")
        self._cmb_degree_type.grid(row=2, column=0, columnspan=3, sticky="EW")
        self._dat_grad.grid(row=3, column=0, sticky="EW")
        lbl_still_attending.grid(row=3, column=1, sticky="E")
        self._chk_still_attending.grid(row=3, column=2, sticky="EW")
        self._btn_submit.grid(row=4, column=0, columnspan=3, sticky="EW")

    @property
    def inpSchoolName(self) -> LabeledInput:
        return self._inp_school_name

    @property
    def cmbDegreeType(self) -> LabeledCombo:
        return self._cmb_degree_type

    @property
    def inpMajor(self) -> LabeledInput:
        return self._inp_major

    @property
    def datGrad(self) -> LabeledDateInput:
        return self._dat_grad

    @property
    def chkStillAttending(self) -> tk.Checkbutton:
        return self._chk_still_attending

    @property
    def btnSubmit(self) -> ttk.Button:
        return self._btn_submit

    def getObject(self) -> Education:
        return Education(
            {
                "school_name": self._inp_school_name.get(),
                "degree_type": self._cmb_degree_type.get(),
                "major": self._inp_major.get(),
                "graduation_date": self._dat_grad.getString(),
                "still_attending": bool(self._checked.get()),
            }
        )

    def populateData(self, education: Education):
        self._inp_school_name.setValue(education.schoolName)
        self._inp_major.setValue(education.major)
        self._cmb_degree_type.setValue(education.degreeType.name)
        self._dat_grad.setValue(education.graduationDate)
        if education.stillAttending:
            self._chk_still_attending.select()
        else:
            self._chk_still_attending.deselect()
