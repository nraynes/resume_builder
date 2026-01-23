from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.modals.CertificationsModal import CertificationsModal
from src.models.Certificate import Certificate
from src.gui.base.BaseListItem import BaseListItem


class CertificationsForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Certifications"
        self._sub_window = None
        self._active_list_item = None
        super().__init__(*args, **kwargs)

    def cmdAdd(self):
        self.addItem(Certificate())
        self.openModal(self.lastItem())

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)

    def cmdEdit(self):
        selected_certificate = self.selectedItem()
        if selected_certificate:
            self.openModal(selected_certificate)

    def getTextName(self, cert: Certificate):
        return f"{cert.issuer} - {cert.certificateName}"

    def populateData(self, certifications: list[Certificate]):
        self.clear()
        for cert in certifications:
            self.addItem(cert, self.getTextName(cert))

    def saveActiveListItem(self, new_certificate: Certificate):
        if self._active_list_item is not None:
            self._active_list_item.item = new_certificate
            self._active_list_item.text = self.getTextName(new_certificate)
            self.replaceItem(self._active_list_item)
            self._sub_window.close()
            self._sub_window = None
            self._active_list_item = None

    def openModal(self, list_item: BaseListItem):
        self._active_list_item = list_item
        self._sub_window = CertificationsModal(
            self._frame,
            certificate=self._active_list_item.item,
            save_certification_cb=self.saveActiveListItem,
        )
