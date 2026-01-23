from src.gui.base.BaseEditorListForm import BaseEditorListForm


class BulletsForm(BaseEditorListForm):
    def __init__(self, *args, cmd_edit, cmd_close, **kwargs):
        self._heading = "Bullets"
        super().__init__(*args, **kwargs)
        self.cmd_edit = cmd_edit
        self.cmd_close = cmd_close

    def populateData(self, bullets: list[dict[str, str]]):
        for bullet in bullets:
            self.addItem(bullet["text"], bullet["text"])

    def cmdAdd(self):
        self.addItem("", "")
        self.cmd_edit(self.lastItem())

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.cmd_close()
            self.delete(self.selectedItem().id)

    def cmdEdit(self):
        if self.selectedItem() is not None:
            self.cmd_edit(self.selectedItem())
