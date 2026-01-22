import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.components.LabeledInput import LabeledInput
from src.gui.components.LabeledDateInput import LabeledDateInput
from src.gui.components.LabeledCombo import LabeledCombo
from src.enums.Degree import Degree


class EducationEditor(BaseComponent):
    def __init__(self, master, cmd_close):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)
        self.cmd_close = cmd_close
        self._inp_school_name = LabeledInput(self._frame, "School Name:")
        self._cmb_degree_type = LabeledCombo(self._frame, "Degree Type:", values=[degree.name for degree in Degree])
        self._inp_major = LabeledInput(self._frame, "Major:")
        self._dat_grad = LabeledDateInput(self._frame, "Graduation Date:")
        lbl_still_attending = tk.Label(self._frame, text="Still Attending:")
        self._chk_still_attending = tk.Checkbutton(self._frame)
        self._btn_submit = ttk.Button(self._frame, text="Save", command=self.save)

        self._inp_school_name.grid(row=0, column=0, columnspan=3, sticky="EW")
        self._inp_major.grid(row=1, column=0, columnspan=3, sticky="EW")
        self._cmb_degree_type.grid(row=2, column=0, columnspan=3, sticky="EW")
        self._dat_grad.grid(row=3, column=0, sticky="EW")
        lbl_still_attending.grid(row=3, column=1, sticky="E")
        self._chk_still_attending.grid(row=3, column=2, sticky="EW")
        self._btn_submit.grid(row=4, column=0, columnspan=3, sticky="EW")
        
    def save(self):
        self.cmd_close()

    @property
    def inpSchoolName(self):
        return self._inp_school_name

    @property
    def cmbDegreeType(self):
        return self._cmb_degree_type

    @property
    def inpMajor(self):
        return self._inp_major

    @property
    def datGrad(self):
        return self._dat_grad

    @property
    def chkStillAttending(self):
        return self._chk_still_attending
    
    @property
    def btnSubmit(self):
        return self._btn_submit
