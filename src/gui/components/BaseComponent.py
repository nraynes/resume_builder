from src.gui.components.BaseFrame import BaseFrame


class BaseComponent(BaseFrame):
    def pack(self, *args, **kwargs):
        self._frame.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        self._frame.grid(*args, **kwargs)

    def place(self, *args, **kwargs):
        self._frame.place(*args, **kwargs)
