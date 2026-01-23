from src.utils.DateUtils import DateUtils
from datetime import datetime
import uuid


class Certificate:
    def __init__(self, data = {}):
        self._id = data["id"] if "id" in data else str(uuid.uuid4())
        self._certificate_name = data["certificate_name"] if "certificate_name" in data else ""
        self._issuer = data["issuer"] if "issuer" in data else ""
        self._issue_date = DateUtils.datetime(data["issue_date"]) if "issue_date" in data else DateUtils.epoch()
        self._exp_date = DateUtils.datetime(data["exp_date"]) if "exp_date" in data else DateUtils.epoch()
        self._does_not_expire = data["does_not_expire"] if "does_not_expire" in data else False

    @property
    def id(self):
        return self._id

    @property
    def certificateName(self):
        return self._certificate_name

    @property
    def issuer(self):
        return self._issuer

    @property
    def issueDate(self):
        return self._issue_date

    @property
    def expDate(self):
        return self._exp_date

    @property
    def doesNotExpire(self):
        return self._does_not_expire

    def to_dict(self):
        return {
            "id": self._id,
            "certificate_name": self._certificate_name,
            "issuer": self._issuer,
            "issue_date": DateUtils.string(self._issue_date),
            "exp_date": DateUtils.string(self._exp_date),
            "does_not_expire": self._does_not_expire,
        }
