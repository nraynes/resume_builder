from src.models.Cv import Cv


class Resume(Cv):
    def __init__(self, title = "", author = "", *args, **kwargs):
        self._title = title
        self._author = author
        super().__init__(*args, **kwargs)
        
    def to_dict(self):
        cv = super().to_dict()
        cv["title"] = self._title
        cv["author"] = self._author
        return cv

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
