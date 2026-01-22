from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.windows.ExperienceWindow import ExperienceWindow


class ExperienceForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Work Experience"
        self._sub_window = None
        super().__init__(*args, **kwargs)

    def cmdAdd(self):
        pass

    def cmdDelete(self):
        pass

    def cmdEdit(self):
        self._sub_window = ExperienceWindow(self._frame)
