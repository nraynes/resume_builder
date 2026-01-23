from datetime import datetime


class DateUtils:
    iso_date_format = "%Y-%m-%dT%H:%M:%S.%f"
    str_epoch = "1970-01-01T00:00:00.000000"

    @classmethod
    def epoch(cls) -> datetime:
        return datetime.strptime(cls.str_epoch, cls.iso_date_format)

    @classmethod
    def datetime(cls, x: str) -> datetime:
        return datetime.strptime(x, cls.iso_date_format)

    @classmethod
    def string(cls, x: datetime) -> str:
        return datetime.strftime(x, cls.iso_date_format)
