class Header:
    def __init__(
        self,
        data: dict = {}
    ):
        self._name = data["name"] if "name" in data.keys() else ""
        self._profession = data["profession"] if "profession" in data.keys() else ""
        self._email = data["email"] if "email" in data.keys() else ""
        self._phone_number = data["phone_number"] if "phone_number" in data.keys() else ""
        self._city = data["city"] if "city" in data.keys() else ""
        self._state = data["state"] if "state" in data.keys() else ""
        self._country = data["country"] if "country" in data.keys() else ""
        self._website = data["website"] if "website" in data.keys() else ""
        self._alt_website = data["alt_website"] if "alt_website" in data.keys() else ""

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
