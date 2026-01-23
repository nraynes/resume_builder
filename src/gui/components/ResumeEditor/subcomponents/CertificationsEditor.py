import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.LabeledInput import LabeledInput
from src.gui.lib.LabeledDateInput import LabeledDateInput
from src.models.Certificate import Certificate


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
        self._checked = tk.IntVar(value=0)
        self._checked.trace_add("write", self.onCheck)
        self._chk_does_not_expire = tk.Checkbutton(self._frame, variable=self._checked, onvalue=1, offvalue=0)
        self._btn_submit = ttk.Button(self._frame, text="Save", command=self.save)

        self._inp_certification_name.grid(row=0, column=0, columnspan=4, sticky="EW")
        self._inp_issuer.grid(row=1, column=0, columnspan=4, sticky="EW")
        self.onCheck()
        self._btn_submit.grid(row=3, column=0, columnspan=2, sticky="EW")
        lbl_does_not_expire.grid(row=3, column=2, sticky="E")
        self._chk_does_not_expire.grid(row=3, column=3, sticky="EW")

    def showExpDate(self):
        self._dat_exp.undefault()
        self._dat_exp.grid(row=2, column=2, columnspan=2, sticky="EW")
        self._dat_issued.grid(row=2, column=0, columnspan=2,  sticky="EW")

    def hideExpDate(self):
        self._dat_exp.default()
        self._dat_exp.grid_forget()
        self._dat_issued.grid(row=2, column=0, columnspan=4, sticky="EW")

    def onCheck(self, *args):
        if self._checked.get() == 0:
            self.showExpDate()
        else:
            self.hideExpDate()

    def populateData(self, certification: Certificate):
        self._inp_certification_name.setValue(certification.certificateName)
        self._inp_issuer.setValue(certification.issuer)
        self._dat_issued.setValue(certification.issueDate)
        self._dat_exp.setValue(certification.expDate)
        if certification.doesNotExpire:
            self._chk_does_not_expire.select()
        else:
            self._chk_does_not_expire.deselect()

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
