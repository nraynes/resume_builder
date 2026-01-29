import tkinter as tk


class Entry(tk.Entry):
    def grid(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Entry.grid(self, *args, **kwargs))

    def pack(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Entry.pack(self, *args, **kwargs))

    def place(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Entry.place(self, *args, **kwargs))

    def grid_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Entry.grid_forget(self, *args, **kwargs))

    def pack_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Entry.pack_forget(self, *args, **kwargs))

    def place_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Entry.place_forget(self, *args, **kwargs))
