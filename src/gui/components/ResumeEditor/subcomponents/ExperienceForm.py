from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.windows.ExperienceWindow import ExperienceWindow
from src.models.Experience import Experience


class ExperienceForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Work Experience"
        self._sub_window = None
        super().__init__(*args, **kwargs)

    def populateData(self, experience: list[Experience]):
        self.clear()
        for work in experience:
            self.addItem(work, f"{work.company} - {work.jobTitle}")

    def cmdAdd(self):
        self.addItem(Experience())
        self._sub_window = ExperienceWindow(
            self._frame, experience=self.lastItem().item
        )

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)

    def cmdEdit(self):
        selected_experience = self.selectedItem()
        if selected_experience:
            self._sub_window = ExperienceWindow(
                self._frame, experience=selected_experience.item
            )
