from src.gui.base.BaseFrame import BaseFrame


class BaseComponent(BaseFrame):
    def pack(self, *args, **kwargs):
        self._frame.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self._frame.grid(*args, **kwargs)

    def place(self, *args, **kwargs):
        self._frame.place(*args, **kwargs)

    def pack_forget(self):
        self._frame.pack_forget()

    def grid_forget(self):
        self._frame.grid_forget()

    def place_forget(self):
        self._frame.place_forget()
