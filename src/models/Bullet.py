from src.gui.base.BaseModel import BaseModel

class Bullet(BaseModel):
    def __init__(self, data: dict = {}):
        self._associated_skills = self.extract(data, "associated_skills", [])
        self._text = self.extract(data, "text", "")

    @property
    def associatedSkills(self) -> list[str]:
        return self._associated_skills

    @property
    def text(self) -> str:
        return self._text
    
    @associatedSkills.setter
    def associatedSkills(self, value: list[str]):
        self._associated_skills = value
    
    def to_dict(self) -> dict:
        return {
            "associated_skills": self._associated_skills,
            "text": self._text
        }
