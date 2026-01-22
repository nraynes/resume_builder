import tkinter as tk
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.ResumeEditor.subcomponents.CertificationsEditor import CertificationsEditor


class CertificationsWindow(BaseWindow):
    def __init__(self, master):
        self._frame = tk.Toplevel(master)
        self._frame.title("Certification Editor")
        self._edt_certifications = CertificationsEditor(self._frame, self._frame.destroy)
        self._edt_certifications.pack()

    def show(self):
        pass

    def hide(self):
        pass
