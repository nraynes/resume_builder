from src.models.Header import Header
from src.models.Experience import Experience
from src.models.Education import Education
from src.models.Certificate import Certificate
from src.validation.Validate import Validate
from src.validation.ValidationResult import ValidationResult


class Cv:
    def __init__(self, data = {}):
        self._header = Header(data["header"] if "header" in data.keys() else {})
        self._summary = data["summary"] if "summary" in data.keys() else ""
        self._education = {}
        self._skills = data["skills"] if "skills" in data.keys() else []
        self._certificates = {}
        self._work_experience = {}
        if "education" in data.keys():
            for edu in data["education"]:
                self._education[edu["id"]] = Education(edu)
        if "certificates" in data.keys():
            for cert in data["certificates"]:
                self._certificates[cert["id"]] = Certificate(cert)
        if "work_experience" in data.keys():
            for work in data["work_experience"]:
                self._work_experience[work["id"]] = Experience(work)

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

    def setSummary(self, value):
        validation = Validate.string(value)
        if validation.passed:
            self._summary = value
        return validation

    def addEducation(self, edu: Education):
        self._education[edu.id] = edu

    def removeEducation(self, id: int):
        if id in self._education.keys():
            del self._education[id]
            return ValidationResult(id, 1)
        return ValidationResult(id, 0, "Could not find education with ID.")

    def addCertificate(self, cert: Certificate):
        self._certificates[cert.id] = cert

    def removeCertificate(self, id: int):
        if id in self._certificates.keys():
            del self._certificates[id]
            return ValidationResult(id, 1)
        return ValidationResult(id, 0, "Could not find certificate with ID.")

    def addExperience(self, work: Experience):
        self._work_experience[work.id] = work

    def removeExperience(self, id: int):
        if id in self._work_experience.keys():
            del self._work_experience[id]
            return ValidationResult(id, 1)
        return ValidationResult(id, 0, "Could not find work experience with ID.")

    def addSkill(self, skill: str):
        if skill in self._skills:
            return ValidationResult(skill, 0, "Skill already present in CV.")
        validation = Validate.string(skill)
        if validation.passed:
            self._skills.append(skill)
        return validation

    def removeSkill(self, skill: str):
        try:
            self._skills.remove(skill)
            return ValidationResult(skill, 1)
        except ValueError:
            return ValidationResult(skill, 0, "Skill not found.")

    def editSkill(self, current_skill: str, new_skill: str):
        removal_validation = self.removeSkill(current_skill)
        if removal_validation.failed:
            return removal_validation
        return self.addSkill(new_skill)

    def to_dict(self):
        return {
            "header": self._header.to_dict(),
            "summary": self._summary,
            "work_experience": [work.to_dict() for work in self._work_experience.values()],
            "education": [edu.to_dict() for edu in self._education.values()],
            "certificates": [cert.to_dict() for cert in self._certificates.values()],
            "skills": self._skills,
        }
