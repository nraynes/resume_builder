from src.models.Cv import Cv


class Resume(Cv):
    def __init__(self, title = "", author = "", *args, **kwargs):
        self._title = title
        self._author = author
        super().__init__(*args, **kwargs)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
