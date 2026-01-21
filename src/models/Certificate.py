from src.validation.Validate import Validate
from datetime import datetime
import uuid


class Certificate:
    def __init__(self, data):
        self._id = data["id"] if "id" in data else str(uuid.uuid4())
        self._certificate_name = data["certificate_name"] if "certificate_name" in data else ""
        self._issuer = data["issuer"] if "issuer" in data else ""
        self._issue_date = datetime.strptime(data["issue_date"], Validate.isodateformat) if "issue_date" in data else Validate.epoch
        self._exp_date = datetime.strptime(data["exp_date"], Validate.isodateformat) if "exp_date" in data else Validate.epoch
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

    def setCertificateName(self, value):
        validation = Validate.string(value)
        if validation.passed:
            self._certificate_name = value
        return validation

    def setIssuer(self, value):
        validation = Validate.string(value)
        if validation.passed:
            self._issuer = value
        return validation

    def setIssueDate(self, value):
        validation = Validate.date(value)
        if validation.passed:
            self._issue_date = datetime.strptime(value, Validate.isodateformat)
        return validation

    def setExpDate(self, value):
        validation = Validate.date(value)
        if validation.passed:
            self._exp_date = datetime.strptime(value, Validate.isodateformat)
        return validation

    def setDoesNotExpire(self, value):
        validation = Validate.bool(value)
        if validation.passed:
            self._does_not_expire = bool(value)
        return validation

    def to_dict(self):
        return {
            "id": self._id,
            "certificate_name": self._certificate_name,
            "issuer": self._issuer,
            "issue_date": datetime.strftime(self._issue_date, Validate.isodateformat),
            "exp_date": datetime.strftime(self._exp_date, Validate.isodateformat),
            "does_not_expire": self._does_not_expire,
        }
