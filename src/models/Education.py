from src.utils.DateUtils import DateUtils
from src.enums.Degree import Degree
from datetime import datetime


class Education:
    def __init__(self, data: dict = {}):
        self._school_name = data["school_name"] if "school_name" in data else ""
        self._degree_type = Degree[data["degree_type"]] if "degree_type" in data else Degree.NONE
        self._major = data["major"] if "major" in data else ""
        self._graduation_date = DateUtils.datetime(data["graduation_date"]) if "graduation_date" in data else DateUtils.epoch()
        self._still_attending = data["still_attending"] if "still_attending" in data else False

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
