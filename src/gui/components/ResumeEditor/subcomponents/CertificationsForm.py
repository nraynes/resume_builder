from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.windows.CertificationsWindow import CertificationsWindow


class CertificationsForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Certifications"
        self._sub_window = None
        super().__init__(*args, **kwargs)

    def cmdAdd(self):
        pass

    def cmdDelete(self):
        pass

    def cmdEdit(self):
        self._sub_window = CertificationsWindow(self._frame)
