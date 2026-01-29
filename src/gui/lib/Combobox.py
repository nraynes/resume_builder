from tkinter import ttk


class Combobox(ttk.Combobox):
    def grid(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Combobox.grid(self, *args, **kwargs))

    def pack(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Combobox.pack(self, *args, **kwargs))

    def place(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Combobox.place(self, *args, **kwargs))

    def grid_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Combobox.grid_forget(self, *args, **kwargs))

    def pack_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Combobox.pack_forget(self, *args, **kwargs))

    def place_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Combobox.place_forget(self, *args, **kwargs))
