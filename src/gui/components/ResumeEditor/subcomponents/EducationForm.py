from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.windows.EducationWindow import EducationWindow
from src.models.Education import Education


class EducationForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Education"
        self._sub_window = None
        super().__init__(*args, **kwargs)

    def populateData(self, education: list[Education]):
        self.clear()
        for edu in education:
            self.addItem(edu, f"{edu.degreeType.name} - {edu.major}")

    def cmdAdd(self):
        pass

    def cmdDelete(self):
        pass

    def cmdEdit(self):
        self._sub_window = EducationWindow(self._frame)
