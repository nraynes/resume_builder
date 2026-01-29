from datetime import datetime


class DateUtils:
    iso_date_format = "%Y-%m-%dT%H:%M:%S.%f"
    epoch = "1970-01-01T00:00:00.000000"

    @classmethod
    def datetime(cls, x: str) -> datetime:
        """converts an ISO date string to a datetime object.

        Args:
            x (str): ISO date string.

        Returns:
            datetime: The resulting datetime object.
        """
        return datetime.strptime(x, cls.iso_date_format)

    @classmethod
    def string(cls, x: datetime) -> str:
        """Converts a datetime object to an ISO date string.

        Args:
            x (datetime): Input datetime object.

        Returns:
            str: ISO date string.
        """
        return datetime.strftime(x, cls.iso_date_format)
