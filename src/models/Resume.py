from src.models.Cv import Cv


class Resume(Cv):
    def __init__(self, title: str = "", author: str = "", *args, **kwargs):
        self._title = title
        self._author = author
        super().__init__(*args, **kwargs)

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    def to_dict(self) -> dict:
        cv = super().to_dict()
        cv["title"] = self._title
        cv["author"] = self._author
        return cv
