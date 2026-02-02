import tkinter as tk
from src.gui.base.BaseModal import BaseModal
from src.gui.components.AwardsEditor import AwardsEditor
from src.models.Award import Award
from typing import Callable
from src.gui.lib.Toplevel import Toplevel


class AwardsModal(BaseModal):
    def __init__(
        self,
        master: tk.Frame,
        award: Award,
        save_award_cb: Callable
    ):
        self._frame = Toplevel(master)
        self._frame.title("Award Editor")
        self.save_award_cb = save_award_cb
        self._edt_awards = AwardsEditor(self._frame, save_award_cb=self.save)

        self._edt_awards.pack()
        self.populateData(award)
        self.setLocationTopLeft()

    @property
    def edtAwards(self) -> AwardsEditor:
        return self._edt_awards

    def populateData(self, award: Award):
        self._edt_awards.populateData(award)

    def save(self) -> Award:
        self.save_award_cb(self._edt_awards.getObject())
