from typing import Any


class BaseListItem:
    def __init__(self, item: Any, id: int = 0, text: str = ""):
        self._id = id
        self._text = text
        self._item = item

    @property
    def id(self) -> int:
        return self._id

    @property
    def text(self) -> str:
        return self._text

    @property
    def item(self) -> str:
        return self._item

    @id.setter
    def id(self, x: int):
        self._id = x

    @text.setter
    def text(self, x: str):
        self._text = x

    @item.setter
    def item(self, x: str):
        self._item = x
