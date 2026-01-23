from src.utils.DateUtils import DateUtils
from src.enums.Degree import Degree
from datetime import datetime
import uuid


class Education:
    def __init__(self, data = {}):
        self._id = data["id"] if "id" in data else str(uuid.uuid4())
        self._school_name = data["school_name"] if "school_name" in data else ""
        self._degree_type = Degree[data["degree_type"]] if "degree_type" in data else Degree.NONE
        self._major = data["major"] if "major" in data else ""
        self._graduation_date = DateUtils.datetime(data["graduation_date"]) if "graduation_date" in data else DateUtils.epoch()
        self._still_attending = data["still_attending"] if "still_attending" in data else False

    @property
    def id(self):
        return self._id

    @property
    def schoolName(self):
        return self._school_name

    @property
    def degreeType(self):
        return self._degree_type

    @property
    def major(self):
        return self._major

    @property
    def graduationDate(self):
        return self._graduation_date

    @property
    def stillAttending(self):
        return self._still_attending

    def to_dict(self):
        return {
            "id": self._id,
            "school_name": self._school_name,
            "degree_type": self._degree_type.name,
            "major": self._major,
            "graduation_date": DateUtils.string(self._graduation_date),
            "still_attending": self._still_attending
        }
