from src.models.Header import Header
from src.gui.base.BaseModel import BaseModel
from src.models.Experience import Experience
from src.models.Education import Education
from src.models.Certificate import Certificate
from src.models.Award import Award


class Cv(BaseModel):
    def __init__(self, data: dict = {}):
        self._header = self.extract(data, "header", Header(), Header)
        self._summary = self.extract(data, "summary", "")
        self._education = [Education(edu) for edu in self.extract(data, "education", [])]
        self._skills = self.extract(data, "skills", [])
        self._certificates = [Certificate(cert) for cert in self.extract(data, "certificates", [])]
        self._awards = [Award(award) for award in self.extract(data, "awards", [])]
        self._work_experience = [Experience(work) for work in self.extract(data, "work_experience", [])]

    @property
    def header(self) -> Header:
        return self._header

    @property
    def summary(self) -> str:
        return self._summary

    @property
    def education(self) -> list[Education]:
        return self._education

    @property
    def skills(self) -> list[str]:
        return self._skills

    @property
    def certificates(self) -> list[Certificate]:
        return self._certificates

    @property
    def awards(self) -> list[Award]:
        return self._awards

    @property
    def workExperience(self) -> list[Experience]:
        return self._work_experience

    def to_dict(self) -> dict:
        return {
            "header": self._header.to_dict(),
            "summary": self._summary,
            "work_experience": [work.to_dict() for work in self._work_experience],
            "education": [edu.to_dict() for edu in self._education],
            "certificates": [cert.to_dict() for cert in self._certificates],
            "awards": [award.to_dict() for award in self._awards],
            "skills": self._skills,
        }
