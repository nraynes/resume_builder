from src.utils.DateUtils import DateUtils
from src.gui.base.BaseModel import BaseModel
from datetime import datetime


class Award(BaseModel):
    def __init__(self, data: dict = {}):
        self._award_name = self.extract(data, "award_name", "")
        self._issuer = self.extract(data, "issuer", "")
        self._issue_date = self.extract(
            data, "issue_date", datetime.now(), DateUtils.datetime
        )

    @property
    def awardName(self) -> str:
        return self._award_name

    @property
    def issuer(self) -> str:
        return self._issuer

    @property
    def issueDate(self) -> datetime:
        return self._issue_date

    def to_dict(self) -> dict:
        return {
            "award_name": self._award_name,
            "issuer": self._issuer,
            "issue_date": DateUtils.string(self._issue_date),
        }
