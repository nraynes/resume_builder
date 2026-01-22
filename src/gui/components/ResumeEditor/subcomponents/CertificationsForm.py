from src.gui.base.BaseEditorListForm import BaseEditorListForm


class CertificationsForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Certifications"
        super().__init__(*args, **kwargs)
