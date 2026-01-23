import tkinter as tk
from src.gui.lib.LabeledInput import LabeledInput
from src.gui.base.BaseComponent import BaseComponent
from src.models.Header import Header


class HeaderForm(BaseComponent):
    def __init__(self, master: tk.Frame):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=1)
        self._frame.columnconfigure(2, weight=1)
        lbl_heading = tk.Label(self._frame, text="Header", font=("Helvetica", 18, "bold"))
        self._inp_name = LabeledInput(self._frame, "Name:")
        self._inp_profession = LabeledInput(self._frame, "Profession:")
        self._inp_email = LabeledInput(self._frame, "Email:")
        self._inp_phone_number = LabeledInput(self._frame, "Phone Number:")
        self._inp_city = LabeledInput(self._frame, "City:")
        self._inp_state = LabeledInput(self._frame, "State:")
        self._inp_country = LabeledInput(self._frame, "Country:")
        self._inp_website = LabeledInput(self._frame, "Website:")
        self._inp_alt_website = LabeledInput(self._frame, "Alternate Website:")

        lbl_heading.grid(row=0, column=0, sticky="W")
        self.spacing().grid(row=1, column=0)
        self._inp_name.grid(row=2, column=0, sticky="EW")
        self._inp_profession.grid(row=3, column=0, sticky="EW")
        self._inp_email.grid(row=4, column=0, sticky="EW")
        self._inp_phone_number.grid(row=5, column=0, sticky="EW")
        self._inp_city.grid(row=2, column=1, sticky="EW")
        self._inp_state.grid(row=3, column=1, sticky="EW")
        self._inp_country.grid(row=4, column=1, sticky="EW")
        self._inp_website.grid(row=2, column=2, sticky="EW")
        self._inp_alt_website.grid(row=3, column=2, sticky="EW")

    @property
    def inpName(self):
        return self._inp_name

    @property
    def inpProfession(self):
        return self._inp_profession

    @property
    def inpEmail(self):
        return self._inp_email

    @property
    def inpPhoneNumber(self):
        return self._inp_phone_number

    @property
    def inpCity(self):
        return self._inp_city

    @property
    def inpState(self):
        return self._inp_state

    @property
    def inpCountry(self):
        return self._inp_country

    @property
    def inpWebsite(self):
        return self._inp_website

    @property
    def inpAltWebsite(self):
        return self._inp_alt_website

    def populateData(self, header: Header):
        self._inp_name.setValue(header.name)
        self._inp_profession.setValue(header.profession)
        self._inp_email.setValue(header.email)
        self._inp_phone_number.setValue(header.phoneNumber)
        self._inp_city.setValue(header.city)
        self._inp_state.setValue(header.state)
        self._inp_country.setValue(header.country)
        self._inp_website.setValue(header.website)
        self._inp_alt_website.setValue(header.altWebsite)

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self._inp_name.get(),
            "profession": self._inp_profession.get(),
            "email": self._inp_email.get(),
            "phone_number": self._inp_phone_number.get(),
            "city": self._inp_city.get(),
            "state": self._inp_state.get(),
            "country": self._inp_country.get(),
            "website": self._inp_website.get(),
            "alt_website": self._inp_alt_website.get(),
        }
