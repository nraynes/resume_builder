from tkinter import ttk


class Scrollbar(ttk.Scrollbar):
    def grid(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Scrollbar.grid(self, *args, **kwargs))

    def pack(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Scrollbar.pack(self, *args, **kwargs))

    def place(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Scrollbar.place(self, *args, **kwargs))

    def grid_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Scrollbar.grid_forget(self, *args, **kwargs))

    def pack_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Scrollbar.pack_forget(self, *args, **kwargs))

    def place_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Scrollbar.place_forget(self, *args, **kwargs))
