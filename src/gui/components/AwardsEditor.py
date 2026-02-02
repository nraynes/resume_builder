import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.lib.LabeledInput import LabeledInput
from src.gui.lib.LabeledDateInput import LabeledDateInput
from src.models.Award import Award
from typing import Callable
from src.gui.lib.Frame import Frame
from src.gui.lib.Button import Button


class AwardsEditor(BaseComponent):
    def __init__(self, master: tk.Toplevel, save_award_cb: Callable):
        self._frame = Frame(master, padx=10, pady=10)
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)
        self._frame.columnconfigure(2, weight=1)
        self._inp_award_name = LabeledInput(self._frame, "Award Name:")
        self._inp_issuer = LabeledInput(self._frame, "Issued By:")
        self._dat_issued = LabeledDateInput(self._frame, "Issued On:")
        self._btn_submit = Button(self._frame, text="Save", command=save_award_cb)

        self._inp_award_name.pack(fill=tk.BOTH)
        self._inp_issuer.pack(fill=tk.BOTH)
        self._dat_issued.pack(fill=tk.BOTH)
        self._btn_submit.pack(fill=tk.BOTH)

    @property
    def inpAwardName(self) -> LabeledInput:
        return self._inp_award_name

    @property
    def inpIssuer(self) -> LabeledInput:
        return self._inp_issuer

    @property
    def datIssued(self) -> LabeledDateInput:
        return self._dat_issued

    @property
    def btnSubmit(self) -> ttk.Button:
        return self._btn_submit

    def getObject(self) -> Award:
        return Award(
            {
                "award_name": self._inp_award_name.get(),
                "issuer": self._inp_issuer.get(),
                "issue_date": self._dat_issued.getString(),
            }
        )

    def populateData(self, award: Award):
        self._inp_award_name.setValue(award.awardName)
        self._inp_issuer.setValue(award.issuer)
        self._dat_issued.setValue(award.issueDate)
