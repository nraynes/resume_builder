from src.gui.base.BaseEditorListForm import BaseEditorListForm
from src.models.Bullet import Bullet
from typing import Callable
from copy import deepcopy


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
        selected_bullet = self.selectedItem()
        if selected_bullet:
            self.edit_bullet_cb(selected_bullet)

    def cmdCopy(self):
        selected_bullet = self.selectedItem()
        if selected_bullet:
            self.addItem(deepcopy(selected_bullet.item), selected_bullet.text)

    def populateData(self, bullets: list[Bullet]):
        for bullet in bullets:
            self.addItem(bullet, bullet.text)
