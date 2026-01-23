from src.models.Header import Header
from src.models.Experience import Experience
from src.models.Education import Education
from src.models.Certificate import Certificate


class Cv:
    def __init__(self, data = {}):
        self._header = Header(data["header"] if "header" in data.keys() else {})
        self._summary = data["summary"] if "summary" in data.keys() else ""
        self._education = []
        self._skills = data["skills"] if "skills" in data.keys() else []
        self._certificates = []
        self._work_experience = []
        if "education" in data.keys():
            for edu in data["education"]:
                self._education.append(Education(edu))
        if "certificates" in data.keys():
            for cert in data["certificates"]:
                self._certificates.append(Certificate(cert))
        if "work_experience" in data.keys():
            for work in data["work_experience"]:
                self._work_experience.append(Experience(work))

    @property
    def header(self):
        return self._header

    @property
    def summary(self):
        return self._summary

    @property
    def education(self):
        return self._education

    @property
    def skills(self):
        return self._skills

    @property
    def certificates(self):
        return self._certificates

    @property
    def workExperience(self):
        return self._work_experience

    def to_dict(self):
        return {
            "header": self._header.to_dict(),
            "summary": self._summary,
            "work_experience": [work.to_dict() for work in self._work_experience],
            "education": [edu.to_dict() for edu in self._education],
            "certificates": [cert.to_dict() for cert in self._certificates],
            "skills": self._skills,
        }
