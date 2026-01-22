from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.windows.EducationWindow import EducationWindow


class EducationForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Education"
        self._sub_window = None
        super().__init__(*args, **kwargs)

    def cmdAdd(self):
        pass

    def cmdDelete(self):
        pass

    def cmdEdit(self):
        self._sub_window = EducationWindow(self._frame)
