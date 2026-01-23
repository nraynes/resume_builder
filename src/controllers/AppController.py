from src.models.Cv import Cv
from src.models.Resume import Resume
from src.services.PDFService import PDFService
from src.controllers.BaseController import BaseController
import json
import os
from typing import Optional


class AppController(BaseController):
    resumes: dict[str, Resume]
    def __init__(self):
        self.cv_path = "./data/cv.json"
        self.resumes_path = "./data/resumes"
        self.cv = Cv(self.loadCv())
        self.pdf_service = PDFService()
        self.resumes = {}
        self.populateResumeList()

    def loadCv(self) -> dict:
        if not os.path.exists(self.cv_path):
            with open(self.cv_path, "w") as file:
                file.write(json.dumps(Cv().to_dict()))
        with open(self.cv_path, "r") as file:
            return json.loads(file.read())

    def saveCv(self):
        content = json.dumps(self.cv.to_dict())
        with open(self.cv_path, "w") as file:
            file.write(content)

    def overwriteCv(self, cv: Cv):
        self.cv = cv
        self.saveCv()

    def resumeFromCv(self, title: str = "", author: str = "") -> Resume:
        self.resumes[title] = Resume(title, author, self.cv.to_dict())
        self.saveResume(title)
        return self.resumes[title]

    def newResume(self, title: str = "", author: str = "") -> Resume:
        self.resumes[title] = Resume(title, author)
        self.saveResume(title)
        return self.resumes[title]

    def resume(self, title: str) -> Optional[Resume]:
        if title in self.resumes.keys():
            return self.resumes[title]
        return None

    def deleteResume(self, title: str):
        if title in self.resumes.keys():
            del self.resumes[title]
        file_path = f"{self.resumes_path}/{title}.json"
        if os.path.exists(file_path):
            os.remove(file_path)

    def overwriteResume(self, title: str, new_resume: Resume):
        self.resumes[title] = new_resume
        self.saveResume(title)

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

    def populateResumeList(self):
        files = self.getFilesInDir(self.resumes_path)
        for file in files:
            self.loadResume(file.split(".")[0])

    def getFilesInDir(cls, dir_path: str) -> list[str]:
        all_entries = os.listdir(dir_path)
        files = []
        for entry in all_entries:
            full_path = os.path.join(dir_path, entry)
            if os.path.isfile(full_path):
                files.append(entry)
        return files
