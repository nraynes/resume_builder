from src.utils.DateUtils import DateUtils
from src.gui.base.BaseModel import BaseModel
from datetime import datetime


class Certificate(BaseModel):
    def __init__(self, data: dict = {}):
        self._certificate_name = self.extract(data, "certificate_name", "")
        self._issuer = self.extract(data, "issuer", "")
        self._issue_date = self.extract(data, "issue_date", datetime.now(), DateUtils.datetime)
        self._exp_date = self.extract(data, "exp_date", datetime.now(), DateUtils.datetime)
        self._does_not_expire = self.extract(data, "does_not_expire", False)

    @property
    def certificateName(self) -> str:
        return self._certificate_name

    @property
    def issuer(self) -> str:
        return self._issuer

    @property
    def issueDate(self) -> datetime:
        return self._issue_date

    @property
    def expDate(self) -> datetime:
        return self._exp_date

    @property
    def doesNotExpire(self) -> bool:
        return self._does_not_expire

    def to_dict(self) -> dict:
        return {
            "certificate_name": self._certificate_name,
            "issuer": self._issuer,
            "issue_date": DateUtils.string(self._issue_date),
            "exp_date": DateUtils.string(self._exp_date),
            "does_not_expire": self._does_not_expire,
        }
