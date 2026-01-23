import tkinter as tk
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.ResumeEditor.subcomponents.CertificationsEditor import CertificationsEditor
from src.models.Certificate import Certificate


class CertificationsWindow(BaseWindow):
    def __init__(self, master, certificate: Certificate, cmd_save):
        self._frame = tk.Toplevel(master)
        self._frame.title("Certification Editor")
        self._cmd_save = cmd_save
        self._edt_certifications = CertificationsEditor(self._frame, cmd_close=self.save)
        self._edt_certifications.pack()
        self.populateData(certificate)

    def populateData(self, certification: Certificate):
        self._edt_certifications.populateData(certification)

    def save(self) -> Certificate:
        self._cmd_save(self._edt_certifications.getObject())

    def show(self):
        pass

    def hide(self):
        self._frame.destroy()
