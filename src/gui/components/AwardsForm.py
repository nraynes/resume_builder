from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.gui.modals.AwardsModal import AwardsModal
from src.models.Award import Award
from src.gui.base.BaseListItem import BaseListItem
from copy import deepcopy


class AwardsForm(BaseEditorListForm):
    def __init__(self, *args, **kwargs):
        self._heading = "Awards"
        self._sub_window = None
        self._active_list_item = None
        super().__init__(*args, **kwargs)
        self._frame.rowconfigure(2, weight=1)

    def cmdAdd(self):
        self.addItem(Award())
        self.openModal(self.lastItem())

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.delete(self.selectedItem().id)

    def cmdEdit(self):
        selected_award = self.selectedItem()
        if selected_award:
            self.openModal(selected_award)

    def cmdCopy(self):
        selected_award = self.selectedItem()
        if selected_award:
            self.addItem(deepcopy(selected_award.item), selected_award.text)

    def populateData(self, awards: list[Award]):
        self.clear()
        for award in awards:
            self.addItem(award, award.awardName)

    def saveActiveListItem(self, new_award: Award):
        if self._active_list_item is not None:
            self._active_list_item.item = new_award
            self._active_list_item.text = new_award.awardName
            self.replaceItem(self._active_list_item)
            self._sub_window.close()
            self._sub_window = None
            self._active_list_item = None

    def openModal(self, list_item: BaseListItem):
        self._active_list_item = list_item
        self._sub_window = AwardsModal(
            self._frame,
            award=self._active_list_item.item,
            save_award_cb=self.saveActiveListItem,
        )
