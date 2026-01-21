from src.validation.Validate import Validate
from src.validation.ValidationResult import ValidationResult
from datetime import datetime
import uuid


class Experience:
    def __init__(self, data):
        self._id = data["id"] if "id" in data else str(uuid.uuid4())
        self._job_title = data["job_title"] if "job_title" in data else ""
        self._company = data["company"] if "company" in data else ""
        self._company_location = data["company_location"] if "company_location" in data else ""
        self._started_on = datetime.strptime(data["started_on"], Validate.isodateformat) if "started_on" in data else Validate.epoch
        self._ended_on = datetime.strptime(data["ended_on"], Validate.isodateformat) if "ended_on" in data else Validate.epoch
        self._current_position = data["current_position"] if "current_position" in data else False
        self._bullets = {}
        for bullet in data["bullets"]:
            self._bullets[bullet["id"]] = bullet

    @property
    def id(self):
        return self._id

    @property
    def jobTitle(self):
        return self._job_title

    @property
    def company(self):
        return self._company

    @property
    def companyLocation(self):
        return self._company_location

    @property
    def startedOn(self):
        return self._started_on

    @property
    def endedOn(self):
        return self._ended_on

    @property
    def currentPosition(self):
        return self._current_position

    @property
    def bullets(self):
        return self._bullets

    def setJobTitle(self, value):
        validation = Validate.string(value)
        if validation.passed:
            self._job_title = value
        return validation

    def setCompany(self, value):
        validation = Validate.string(value)
        if validation.passed:
            self._company = value
        return validation

    def setCompanyLocation(self, value):
        validation = Validate.string(value)
        if validation.passed:
            self._company_location = value
        return validation

    def setStartedOn(self, value):
        validation = Validate.date(value)
        if validation.passed:
            self._started_on = datetime.strptime(value, Validate.isodateformat)
        return validation

    def setEndedOn(self, value):
        validation = Validate.date(value)
        if validation.passed:
            self._ended_on = datetime.strptime(value, Validate.isodateformat)
        return validation

    def setCurrentPosition(self, value):
        validation = Validate.bool(value)
        if validation.passed:
            self._current_position = bool(value)
        return validation

    def _newBullet(self, text):
        return {
            "id": str(uuid.uuid4),
            "text": text
        }

    def addBullet(self, bullet: str):
        if bullet in [b["text"] for b in self._bullets.values()]:
            return ValidationResult(bullet, 0, "Bullet already present in Work Experience.")
        validation = Validate.string(bullet)
        if validation.passed:
            new_bullet = self._newBullet(bullet)
            self._bullets[new_bullet["id"]] = new_bullet
        return validation

    def removeBullet(self, id):
        if id in self._bullets.keys():
            del self._bullets[id]
            return ValidationResult(id, 1)
        return ValidationResult(id, 0, "Could not find bullet with ID.")

    def editBullet(self, id: str, new_text: str):
        if id in self._bullets.keys():
            self._bullets[id]["text"] = new_text
            return ValidationResult(id, 1)
        return ValidationResult(id, 0, "Could not find bullet with ID.")

    def to_dict(self):
        return {
            "id": self._id,
            "job_title": self._job_title,
            "company": self._company,
            "company_location": self._company_location,
            "started_on": datetime.strftime(self._started_on, Validate.isodateformat),
            "ended_on": datetime.strftime(self._ended_on, Validate.isodateformat),
            "current_position": self._current_position,
            "bullets": list(self._bullets.values()),
        }
