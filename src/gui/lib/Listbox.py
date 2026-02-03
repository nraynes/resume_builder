import tkinter as tk
from typing import Callable, Optional


class Listbox(tk.Listbox):

    def __init__(self, *args, shift_item_cb: Callable = lambda x, i: None, **kwargs):
        kwargs["selectmode"] = tk.SINGLE
        tk.Listbox.__init__(self, *args, **kwargs)
        self.bind("<Button-1>", self.setIndexOne)
        self.bind("<B1-Motion>", self.setIndexTwo)
        self.bind("<ButtonRelease-1>", self.shiftSelection)
        self.index_one = None
        self.index_two = None
        self.shift_item_cb = shift_item_cb

    def setIndexOne(self, event):
        self.index_one = self.nearest(event.y)

    def setIndexTwo(self, event):
        self.index_two = self.nearest(event.y)

    def shiftSelection(self, event):
        if (
            self.index_one is not None
            and self.index_two is not None
            and self.index_one != self.index_two
        ):
            self.shift_item_cb(self.index_one, self.index_two)
            self.index_one = None
            self.index_two = None

    def grid(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Listbox.grid(self, *args, **kwargs))

    def pack(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Listbox.pack(self, *args, **kwargs))

    def place(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Listbox.place(self, *args, **kwargs))

    def grid_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Listbox.grid_forget(self, *args, **kwargs))

    def pack_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Listbox.pack_forget(self, *args, **kwargs))

    def place_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Listbox.place_forget(self, *args, **kwargs))

    def clear(self):
        self.delete(0, tk.END)

    def add(self, x: str) -> int:
        self.insert(tk.END, x)
        return self.index(tk.END)-1

    def selected_index(self) -> Optional[int]:
        """Gets the index of the currently selected item.

        Returns:
            int: Index of currently selected item.
        """
        selected_indices = self.curselection()
        return selected_indices[0] if selected_indices else None

    def selected(self) -> Optional[str]:
        """Gets the currently selected item.

        Returns:
            Optional[str]: The currently selected item.
        """
        selected_index = self.selected_index()
        return self.get(selected_index) if selected_index is not None else None

    def index_of(self, x: str) -> Optional[int]:
        """Gets the item at the supplied index.

        Args:
            x (str): The index of the item to get.

        Returns:
            Optional[int]: The item at the supplied index.
        """
        for i in self.size():
            item = self.get(i)
            if x == item:
                return i
        return None
