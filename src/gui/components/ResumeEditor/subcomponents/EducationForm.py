from src.gui.base.BaseEditorListForm import BaseEditorListForm


class EducationForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Education"
        super().__init__(*args, **kwargs)
