from src.models.Cv import Cv
from src.models.Resume import Resume
from src.services.PDFService import PDFService
from src.controllers.BaseController import BaseController
import json
import os


class AppController(BaseController):
    resumes: dict[str, Resume]
    def __init__(self):
        self.cv_path = "./data/cv.json"
        self.resumes_path = "./data/resumes"
        self.cv_raw = self._loadCv()
        self.cv = Cv(self.cv_raw)
        self.pdf_service = PDFService()
        self.resumes = {}
        self.populateResumeList()

    def _loadCv(self):
        with open(self.cv_path, "r") as file:
            return json.loads(file.read())

    def saveCv(self):
        content = json.dumps(self.cv.to_dict())
        with open(self.cv_path, "w") as file:
            file.write(content)

    def resume(self, title: str):
        if title in self.resumes.keys():
            return self.resumes[title]
        else:
            return None

    def resumeFromCv(self, title: str = "", author: str = ""):
        self.resumes[title] = Resume(title, author, self.cv_raw)
        self.saveResume(title)
        return self.resumes[title]

    def newResume(self, title: str = "", author: str = ""):
        self.resumes[title] = Resume(title, author)
        self.saveResume(title)
        return self.resumes[title]

    def saveResume(self, title: str):
        resume = self.resumes[title]
        content = json.dumps(resume.to_dict())
        with open(f"{self.resumes_path}/{resume.title}.json", "w") as file:
            file.write(content)

    def loadResume(self, title: str):
        with open(f"{self.resumes_path}/{title}.json", "r") as file:
            resume_data = json.loads(file.read())
            self.resumes[title] = Resume(
                resume_data["title"], resume_data["author"], resume_data
            )
        return self.resumes[title]

    def populateResumeList(self):
        files = self.getFilesInDir(self.resumes_path)
        for file in files:
            self.loadResume(file.split(".")[0])

    def getFilesInDir(cls, dir_path: str):
        all_entries = os.listdir(dir_path)
        files = []
        for entry in all_entries:
            full_path = os.path.join(dir_path, entry)
            if os.path.isfile(full_path):
                files.append(entry)
        return files
