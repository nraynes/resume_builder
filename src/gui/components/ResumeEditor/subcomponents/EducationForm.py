from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.windows.EducationWindow import EducationWindow
from src.models.Education import Education
from src.gui.base.BaseListItem import BaseListItem


class EducationForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Education"
        self._sub_window = None
        self._active_list_item = None
        super().__init__(*args, **kwargs)

    def getTextName(self, edu: Education):
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
            self._sub_window.hide()
            self._sub_window = None
            self._active_list_item = None

    def openModal(self, list_item: BaseListItem):
        self._active_list_item = list_item
        self._sub_window = EducationWindow(
            self._frame,
            education=self._active_list_item.item,
            cmd_save=self.saveActiveListItem,
        )

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
