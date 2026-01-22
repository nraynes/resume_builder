import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.components.LabeledInput import LabeledInput
from src.gui.components.LabeledDateInput import LabeledDateInput


class CertificationsEditor(BaseComponent):
    def __init__(self, master, cmd_close):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self.cmd_close = cmd_close
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)
        self._frame.columnconfigure(2, weight=1)
        self._inp_certification_name = LabeledInput(self._frame, "Certification Name:")
        self._inp_issuer = LabeledInput(self._frame, "Issued By:")
        self._dat_issued = LabeledDateInput(self._frame, "Issued On:")
        self._dat_exp = LabeledDateInput(self._frame, "Expires On:")
        lbl_does_not_expire = tk.Label(self._frame, text="Does Not Expire:")
        self._chk_does_not_expire = tk.Checkbutton(self._frame)
        self._btn_submit = ttk.Button(self._frame, text="Save", command=self.save)

        self._inp_certification_name.grid(row=0, column=0, columnspan=4, sticky="EW")
        self._inp_issuer.grid(row=1, column=0, columnspan=4, sticky="EW")
        self._dat_issued.grid(row=2, column=0, columnspan=2,  sticky="EW")
        self._dat_exp.grid(row=2, column=2, columnspan=2, sticky="EW")
        self._btn_submit.grid(row=3, column=0, columnspan=2, sticky="EW")
        lbl_does_not_expire.grid(row=3, column=2, sticky="E")
        self._chk_does_not_expire.grid(row=3, column=3, sticky="EW")
        
    def save(self):
        self.cmd_close()

    @property
    def inpCertificationName(self):
        return self._inp_certification_name

    @property
    def inpIssuer(self):
        return self._inp_issuer

    @property
    def datIssued(self):
        return self._dat_issued

    @property
    def datExp(self):
        return self._dat_exp

    @property
    def chkDoesNotExpire(self):
        return self._chk_does_not_expire

    @property
    def btnSubmit(self):
        return self._btn_submit
