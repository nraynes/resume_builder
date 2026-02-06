from src.utils.DateUtils import DateUtils
from src.gui.base.BaseModel import BaseModel
from src.models.Bullet import Bullet
from datetime import datetime


class Experience(BaseModel):
    def __init__(self, data: dict = {}):
        self._job_title = self.extract(data, "job_title", "")
        self._company = self.extract(data, "company", "")
        self._company_location = self.extract(data, "company_location", "")
        self._started_on = self.extract(data, "started_on", datetime.now(), DateUtils.datetime)
        self._ended_on = self.extract(data, "ended_on", datetime.now(), DateUtils.datetime)
        self._current_position = self.extract(data, "current_position", False)
        self._bullets = [Bullet(bullet) for bullet in self.extract(data, "bullets", [])]

    @property
    def jobTitle(self) -> str:
        return self._job_title

    @property
    def company(self) -> str:
        return self._company

    @property
    def companyLocation(self) -> str:
        return self._company_location

    @property
    def startedOn(self) -> datetime:
        return self._started_on

    @property
    def endedOn(self) -> datetime:
        return self._ended_on

    @property
    def currentPosition(self) -> bool:
        return self._current_position

    @property
    def bullets(self) -> list[Bullet]:
        return self._bullets

    def to_dict(self) -> dict:
        return {
            "job_title": self._job_title,
            "company": self._company,
            "company_location": self._company_location,
            "started_on": DateUtils.string(self._started_on),
            "ended_on": DateUtils.string(self._ended_on),
            "current_position": self._current_position,
            "bullets": [bullet.to_dict() for bullet in self._bullets],
        }
