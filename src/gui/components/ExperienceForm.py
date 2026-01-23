from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.modals.ExperienceModal import ExperienceModal
from src.models.Experience import Experience
from src.gui.base.BaseListItem import BaseListItem


class ExperienceForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Work Experience"
        self._sub_window = None
        self._active_list_item = None
        super().__init__(*args, **kwargs)

    def cmdAdd(self):
        self.addItem(Experience())
        self.openModal(self.lastItem())

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)

    def cmdEdit(self):
        selected_experience = self.selectedItem()
        if selected_experience:
            self.openModal(selected_experience)

    def getTextName(self, work: Experience) -> str:
        return f"{work.company} - {work.jobTitle}"

    def populateData(self, experience_list: list[Experience]):
        self.clear()
        for work in experience_list:
            self.addItem(work, self.getTextName(work))

    def saveActiveListItem(self, new_experience: Experience):
        if self._active_list_item is not None:
            self._active_list_item.item = new_experience
            self._active_list_item.text = self.getTextName(new_experience)
            self.replaceItem(self._active_list_item)
            self._sub_window.close()
            self._sub_window = None
            self._active_list_item = None

    def openModal(self, list_item: BaseListItem):
        self._active_list_item = list_item
        self._sub_window = ExperienceModal(
            self._frame,
            experience=self._active_list_item.item,
            save_experience_cb=self.saveActiveListItem,
        )
