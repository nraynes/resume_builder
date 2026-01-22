from src.gui.base.BaseEditorListForm import BaseEditorListForm


class ExperienceForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Work Experience"
        super().__init__(*args, **kwargs)
