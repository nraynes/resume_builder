from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.windows.CertificationsWindow import CertificationsWindow
from src.models.Certificate import Certificate


class CertificationsForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Certifications"
        self._sub_window = None
        super().__init__(*args, **kwargs)

    def populateData(self, certifications: list[Certificate]):
        self.clear()
        for cert in certifications:
            self.addItem(cert, f"{cert.issuer} - {cert.certificateName}")

    def cmdAdd(self):
        self.addItem(Certificate())
        self._sub_window = CertificationsWindow(
            self._frame, certificate=self.lastItem().item
        )

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)

    def cmdEdit(self):
        selected_certificate = self.selectedItem()
        if selected_certificate:
            self._sub_window = CertificationsWindow(
                self._frame, certificate=selected_certificate.item
            )
