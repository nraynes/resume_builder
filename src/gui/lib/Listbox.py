import tkinter as tk


class Listbox(tk.Listbox):
    def clear(self):
        self.delete(0, tk.END)

    def add(self, x: str):
        self.insert(tk.END, x)
        return self.index(tk.END)-1

    def selected_index(self):
        selected_indices = self.curselection()
        return selected_indices[0] if selected_indices else None

    def selected(self):
        selected_index = self.selected_index()
        return self.get(selected_index) if selected_index else None

    def index_of(self, x: str):
        for i in self.size():
            item = self.get(i)
            if x == item:
                return i
        return None
