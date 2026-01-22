import tkcalendar


class DateEntry(tkcalendar.DateEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.unbind("<ButtonPress-1>")
        self.bind("<ButtonRelease-1>", self._on_b1_press)
