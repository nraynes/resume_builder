from src.validation.Validate import Validate
from src.enums.Degree import Degree
from datetime import datetime
import uuid


class Education:
    def __init__(self, data):
        self._id = data["id"] if "id" in data else str(uuid.uuid4())
        self._school_name = data["school_name"] if "school_name" in data else ""
        self._degree_type = Degree[data["degree_type"]] if "degree_type" in data else Degree.NONE
        self._major = data["major"] if "major" in data else ""
        self._graduation_date = datetime.strptime(data["graduation_date"], Validate.isodateformat) if "graduation_date" in data else Validate.epoch  # Or expected.
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
    def major(self):
        return self._school_name

    @property
    def graduationDate(self):
        return self._graduation_date

    @property
    def stillAttending(self):
        return self._still_attending

    def setSchoolName(self, value):
        validation = Validate.string(value)
        if validation.passed:
            self._school_name = value
        return validation

    def setDegreeType(self, value):
        validation = Validate.degree(value)
        if validation.passed:
            self._degree_type = Degree[value]
        return validation

    def setMajor(self, value):
        validation = Validate.string(value)
        if validation.passed:
            self._major = value
        return validation

    def setGraduationDate(self, value):
        validation = Validate.date(value)
        if validation.passed:
            self._graduation_date = datetime.strptime(value, Validate.isodateformat)
        return validation

    def setStillAttending(self, value):
        validation = Validate.bool(value)
        if validation.passed:
            self._still_attending = bool(value)
        return validation

    def to_dict(self):
        return {
            "id": self._id,
            "school_name": self._school_name,
            "degree_type": self._degree_type.name,
            "major": self._major,
            "graduation_date": datetime.strftime(self._graduation_date, Validate.isodateformat),
            "still_attending": self._still_attending
        }
