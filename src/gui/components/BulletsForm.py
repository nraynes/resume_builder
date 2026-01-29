from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.models.Bullet import Bullet
from typing import Callable


class BulletsForm(BaseEditorListForm):

    def __init__(self, *args, edit_bullet_cb: Callable, close_bullet_cb: Callable, **kwargs):
        self._heading = "Bullets"
        super().__init__(*args, **kwargs)
        self.edit_bullet_cb = edit_bullet_cb
        self.close_bullet_cb = close_bullet_cb

    def cmdAdd(self):
        self.addItem(Bullet())
        self.edit_bullet_cb(self.lastItem())

    def cmdDelete(self):
        if self.selectedItem() is not None:
            self.close_bullet_cb()
            self.delete(self.selectedItem().id)

    def cmdEdit(self):
        if self.selectedItem() is not None:
            self.edit_bullet_cb(self.selectedItem())

    def populateData(self, bullets: list[Bullet]):
        for bullet in bullets:
            self.addItem(bullet, bullet.text)
