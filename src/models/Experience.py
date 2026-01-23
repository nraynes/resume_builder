from src.utils.DateUtils import DateUtils
from datetime import datetime


class Experience:
    def __init__(self, data: dict = {}):
        self._job_title = data["job_title"] if "job_title" in data else ""
        self._company = data["company"] if "company" in data else ""
        self._company_location = data["company_location"] if "company_location" in data else ""
        self._started_on = DateUtils.datetime(data["started_on"]) if "started_on" in data else DateUtils.epoch()
        self._ended_on = DateUtils.datetime(data["ended_on"]) if "ended_on" in data else DateUtils.epoch()
        self._current_position = data["current_position"] if "current_position" in data else False
        self._bullets = []
        if "bullets" in data:
            for bullet in data["bullets"]:
                self._bullets.append(bullet)

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
    def bullets(self) -> list[str]:
        return self._bullets

    def to_dict(self) -> dict:
        return {
            "job_title": self._job_title,
            "company": self._company,
            "company_location": self._company_location,
            "started_on": DateUtils.string(self._started_on),
            "ended_on": DateUtils.string(self._ended_on),
            "current_position": self._current_position,
            "bullets": self._bullets,
        }
