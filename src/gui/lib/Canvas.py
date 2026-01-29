import tkinter as tk


class Canvas(tk.Canvas):
    def grid(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Canvas.grid(self, *args, **kwargs))

    def pack(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Canvas.pack(self, *args, **kwargs))

    def place(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Canvas.place(self, *args, **kwargs))

    def grid_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Canvas.grid_forget(self, *args, **kwargs))

    def pack_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Canvas.pack_forget(self, *args, **kwargs))

    def place_forget(self, *args, **kwargs):
        self.master.after(0, lambda: tk.Canvas.place_forget(self, *args, **kwargs))
