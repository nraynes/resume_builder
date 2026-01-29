import tkinter as tk


class Frame(tk.Frame):
    def grid(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Frame.grid(self, *args, **kwargs))

    def pack(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Frame.pack(self, *args, **kwargs))

    def place(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Frame.place(self, *args, **kwargs))

    def grid_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Frame.grid_forget(self, *args, **kwargs))

    def pack_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Frame.pack_forget(self, *args, **kwargs))

    def place_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Frame.place_forget(self, *args, **kwargs))
