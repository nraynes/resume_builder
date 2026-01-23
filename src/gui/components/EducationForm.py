from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.modals.EducationModal import EducationModal
from src.models.Education import Education
from src.gui.base.BaseListItem import BaseListItem


class EducationForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Education"
        self._sub_window = None
        self._active_list_item = None
        super().__init__(*args, **kwargs)

    def cmdAdd(self):
        self.addItem(Education())
        self.openModal(self.lastItem())

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)

    def cmdEdit(self):
        selected_education = self.selectedItem()
        if selected_education:
            self.openModal(selected_education)

    def getTextName(self, edu: Education) -> str:
        return f"{edu.degreeType.name} - {edu.major}"

    def populateData(self, education: list[Education]):
        self.clear()
        for edu in education:
            self.addItem(edu, self.getTextName(edu))

    def saveActiveListItem(self, new_education: Education):
        if self._active_list_item is not None:
            self._active_list_item.item = new_education
            self._active_list_item.text = self.getTextName(new_education)
            self.replaceItem(self._active_list_item)
            self._sub_window.close()
            self._sub_window = None
            self._active_list_item = None

    def openModal(self, list_item: BaseListItem):
        self._active_list_item = list_item
        self._sub_window = EducationModal(
            self._frame,
            education=self._active_list_item.item,
            save_education_cb=self.saveActiveListItem,
        )
