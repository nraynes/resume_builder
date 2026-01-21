from src.gui.Base.BaseFrame import BaseFrame


class BaseWindow(BaseFrame):
    def show(self):
        self._frame.pack(anchor="center", expand=True)

    def hide(self):
        self._frame.pack_forget()
