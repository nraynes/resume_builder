from tkinter import ttk


class Button(ttk.Button):
    def grid(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Button.grid(self, *args, **kwargs))

    def pack(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Button.pack(self, *args, **kwargs))

    def place(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Button.place(self, *args, **kwargs))

    def grid_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Button.grid_forget(self, *args, **kwargs))

    def pack_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Button.pack_forget(self, *args, **kwargs))

    def place_forget(self, *args, **kwargs):
        self.master.after(0, lambda: ttk.Button.place_forget(self, *args, **kwargs))
