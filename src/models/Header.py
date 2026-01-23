class Header:
    def __init__(
        self,
        data = {}
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
    def name(self):
        return self._name

    @property
    def profession(self):
        return self._profession

    @property
    def email(self):
        return self._email

    @property
    def phoneNumber(self):
        return self._phone_number

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def country(self):
        return self._country

    @property
    def website(self):
        return self._website

    @property
    def altWebsite(self):
        return self._alt_website

    def to_dict(self):
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
