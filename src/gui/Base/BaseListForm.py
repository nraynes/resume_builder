import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseComponent import BaseComponent
from src.gui.base.BaseListItem import BaseListItem
from src.gui.lib.Listbox import Listbox
from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseListForm(BaseComponent, ABC):
    _heading: str
    _items: list[BaseListItem]

    def __init__(self, master: tk.Frame):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=0)
        self._frame.columnconfigure(2, weight=1)
        self._frame.columnconfigure(3, weight=0)
        self._frame.columnconfigure(4, weight=1)
        lbl_heading = tk.Label(
            self._frame, text=self._heading, font=("Helvetica", 18, "bold")
        )
        self._items = []
        self._lst_items = Listbox(self._frame)
        self._btn_delete = ttk.Button(self._frame, text="Delete", command=self.cmdDelete)
        self._btn_add = ttk.Button(self._frame, text="Add", command=self.cmdAdd)

        lbl_heading.grid(row=0, column=0, sticky="W")
        self.spacing().grid(row=1, column=0)
        self._lst_items.grid(row=2, column=0, columnspan=5, sticky="NSEW")
        self.spacing().grid(row=3, column=0)
        self._btn_delete.grid(row=4, column=0, sticky="EW")
        self.spacing().grid(row=4, column=1)
        self.spacing().grid(row=4, column=3)
        self._btn_add.grid(row=4, column=4, sticky="EW")

    @property
    def lstItems(self) -> Listbox:
        return self._lst_items

    @property
    def btnDelete(self) -> ttk.Button:
        return self._btn_delete

    @property
    def btnAdd(self) -> ttk.Button:
        return self._btn_add
    
    @property
    def heading(self) -> str:
        return self._heading

    @abstractmethod
    def cmdAdd(self):
        pass

    @abstractmethod
    def cmdDelete(self):
        pass

    def clear(self):
        self._items = []
        self.updateList()

    def item(self, index: int) -> Optional[BaseListItem]:
        for item in self._items:
            if item.id == index:
                return item
        return None
    
    def items(self) -> list[Any]:
        return [item.item for item in self._items]

    def delete(self, index: int):
        refreshed_items = []
        for item in self._items:
            if item.id != index:
                refreshed_items.append(item)
        self._items = refreshed_items
        self.updateList()

    def selectedItem(self) -> Optional[BaseListItem]:
        selected_index = self._lst_items.selected_index()
        if selected_index is not None:
            item = self.item(selected_index)
            if item is not None:
                return item
        return None

    def addItem(self, item: Any, text: str = ""):
        self._items.append(BaseListItem(item, text=text))
        self.updateList()

    def replaceItem(self, replacement: BaseListItem):
        refreshed_items = []
        for item in self._items:
            if item.id == replacement.id:
                refreshed_items.append(replacement)
            else:
                refreshed_items.append(item)
        self._items = refreshed_items
        self.updateList()

    def updateList(self):
        self._lst_items.clear()
        for item in self._items:
            item.id = self._lst_items.add(item.text)

    def lastItem(self) -> BaseListItem:
        return self._items[-1]
