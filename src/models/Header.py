from src.models.BaseModel import BaseModel


class Header(BaseModel):
    def __init__(
        self,
        data: dict = {}
    ):
        self._name = self.extract(data, "name", "")
        self._profession = self.extract(data, "profession", "")
        self._email = self.extract(data, "email", "")
        self._phone_number = self.extract(data, "phone_number", "")
        self._city = self.extract(data, "city", "")
        self._state = self.extract(data, "state", "")
        self._country = self.extract(data, "country", "")
        self._website = self.extract(data, "website", "")
        self._alt_website = self.extract(data, "alt_website", "")

    @property
    def name(self) -> str:
        return self._name

    @property
    def profession(self) -> str:
        return self._profession

    @property
    def email(self) -> str:
        return self._email

    @property
    def phoneNumber(self) -> str:
        return self._phone_number

    @property
    def city(self) -> str:
        return self._city

    @property
    def state(self) -> str:
        return self._state

    @property
    def country(self) -> str:
        return self._country

    @property
    def website(self) -> str:
        return self._website

    @property
    def altWebsite(self) -> str:
        return self._alt_website

    def to_dict(self) -> dict:
        return {
            "name": self._name,
            "profession": self._profession,
            "email": self._email,
            "phone_number": self._phone_number,
            "city": self._city,
            "state": self._state,
            "country": self._country,
            "website": self._website,
            "alt_website": self._alt_website
        }
