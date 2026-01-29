from src.utils.DateUtils import DateUtils
from src.models.BaseModel import BaseModel
from src.enums.Degree import Degree
from datetime import datetime


class Education(BaseModel):
    def __init__(self, data: dict = {}):
        self._school_name = self.extract(data, "school_name", "")
        self._degree_type = Degree[self.extract(data, "degree_type", "NONE")]
        self._major = self.extract(data, "major", "")
        self._graduation_date = self.extract(data, "graduation_date", datetime.now(), DateUtils.datetime)
        self._still_attending = self.extract(data, "still_attending", False)

    @property
    def schoolName(self) -> str:
        return self._school_name

    @property
    def degreeType(self) -> Degree:
        return self._degree_type

    @property
    def major(self) -> str:
        return self._major

    @property
    def graduationDate(self) -> datetime:
        return self._graduation_date

    @property
    def stillAttending(self) -> bool:
        return self._still_attending

    def to_dict(self) -> dict:
        return {
            "school_name": self._school_name,
            "degree_type": self._degree_type.name,
            "major": self._major,
            "graduation_date": DateUtils.string(self._graduation_date),
            "still_attending": self._still_attending
        }
