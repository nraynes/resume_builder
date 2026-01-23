import tkinter as tk
from src.gui.base.BaseModal import BaseModal
from src.gui.components.CertificationsEditor import CertificationsEditor
from src.models.Certificate import Certificate
from typing import Callable


class CertificationsModal(BaseModal):
    def __init__(
        self,
        master: tk.Frame,
        certificate: Certificate,
        save_certification_cb: Callable
    ):
        self._frame = tk.Toplevel(master)
        self._frame.title("Certification Editor")
        self.save_certification_cb = save_certification_cb
        self._edt_certifications = CertificationsEditor(self._frame, save_certification_cb=self.save)

        self._edt_certifications.pack()
        self.populateData(certificate)
        
    @property
    def edtCertifications(self) -> CertificationsEditor:
        return self._edt_certifications

    def populateData(self, certification: Certificate):
        self._edt_certifications.populateData(certification)

    def save(self) -> Certificate:
        self.save_certification_cb(self._edt_certifications.getObject())
