from tkinter import Frame


class BaseFrame:
    _frame: Frame

    @property
    def frame(self):
        return self._frame
