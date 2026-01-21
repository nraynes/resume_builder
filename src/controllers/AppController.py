from src.models.Cv import Cv
from src.models.Resume import Resume
from src.services.PDFService import PDFService
import json


class AppController:
    resumes: dict[str, Resume]
    def __init__(self):
        self.cv_path = "./data/cv.json"
        self.resumes_path = "./data/resumes"
        self.data = self._loadCv()
        self.cv = Cv(self.data)
        self.pdf_service = PDFService()
        self.resumes = {}

    def _loadCv(self):
        with open(self.cv_path, "r") as file:
            return json.loads(file.read())

    def saveCv(self):
        content = json.dumps(self.cv.to_dict())
        with open(self.cv_path, "w") as file:
            file.write(content)

    def resumeFromCv(self, title: str = "", author: str = ""):
        resume = Resume(title, author, self.data)
        self.save_resume(resume)
        self.resumes[title] = resume
        return resume

    def newResume(self, title: str = "", author: str = ""):
        resume = Resume(title, author)
        self.save_resume(resume)
        self.resumes[title] = resume
        return resume

    def saveResume(self, resume: Resume):
        content = json.dumps(resume.to_dict())
        with open(f"{self.resumes_path}/{resume.title}.json", "w") as file:
            file.write(content)

    def loadResume(self, title: str):
        with open(f"{self.resumes_path}/{title}.json", "r") as file:
            self.resumes[title] = json.loads(file.read())
        return self.resumes[title]
