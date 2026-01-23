import tkinter as tk
from typing import Optional


class Listbox(tk.Listbox):
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
