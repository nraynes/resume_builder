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
        """Loads the current CV from the stored json file.
        Creates a blank one if it does not exist.

        Returns:
            dict: The CV json file contents converted to a python dictionary.
        """
        if not os.path.exists(self.cv_path):
            with open(self.cv_path, "w") as file:
                file.write(json.dumps(Cv().to_dict()))
        with open(self.cv_path, "r") as file:
            return json.loads(file.read())

    def saveCv(self):
        """Saves the current CV to the designated json file.
        """
        content = json.dumps(self.cv.to_dict())
        with open(self.cv_path, "w") as file:
            file.write(content)

    def overwriteCv(self, cv: Cv):
        """Overwrites the current CV file with a new CV.

        Args:
            cv (Cv): The new CV.
        """
        self.cv = cv
        self.saveCv()

    def resumeFromCv(self, title: str = "", author: str = "") -> Resume:
        """Creates and saves a new resume file copied from the current CV.

        Args:
            title (str, optional): Resume Title. Defaults to "".
            author (str, optional): Resume Author. Defaults to "".

        Returns:
            Resume: The new Resume object.
        """
        self.resumes[title] = Resume(title, author, self.cv.to_dict())
        self.saveResume(title)
        return self.resumes[title]

    def newResume(self, title: str = "", author: str = "") -> Resume:
        """Creates and saves a new blank resume file.

        Args:
            title (str, optional): Resume title. Defaults to "".
            author (str, optional): Resume Author. Defaults to "".

        Returns:
            Resume: The new Resume object.
        """
        self.resumes[title] = Resume(title, author)
        self.saveResume(title)
        return self.resumes[title]

    def resume(self, title: str) -> Optional[Resume]:
        """Gets a resume with the supplied title if it exists.

        Args:
            title (str): The title of the resume to get.

        Returns:
            Optional[Resume]: The Resume object if it exists.
        """
        if title in self.resumes.keys():
            return self.resumes[title]
        return None

    def deleteResume(self, title: str):
        """Deletes a resume file with the supplied title if it exists.

        Args:
            title (str): The title of the resume to delete.
        """
        if title in self.resumes.keys():
            del self.resumes[title]
        file_path = f"{self.resumes_path}/{title}.json"
        if os.path.exists(file_path):
            os.remove(file_path)

    def overwriteResume(self, title: str, new_resume: Resume):
        """Overwrites a resume file with the supplied title with a new resume object.

        Args:
            title (str): The title of the resume to replace.
            new_resume (Resume): The new resume object.
        """
        self.resumes[title] = new_resume
        self.saveResume(title)

    def saveResume(self, title: str):
        """Saves a resume with the supplied title to a file.
        Will overwrite the current resume file.

        Args:
            title (str): The title of the resume to save.
        """
        resume = self.resumes[title]
        content = json.dumps(resume.to_dict())
        with open(f"{self.resumes_path}/{resume.title}.json", "w") as file:
            file.write(content)

    def loadResume(self, title: str):
        """Loads a resume with the supplied title into memory from a file.

        Args:
            title (str): The title of the resume to load.
        """
        with open(f"{self.resumes_path}/{title}.json", "r") as file:
            resume_data = json.loads(file.read())
            self.resumes[title] = Resume(
                resume_data["title"], resume_data["author"], resume_data
            )

    def populateResumeList(self):
        """Loads all of the stored resume files into memory.
        """
        files = self.getFilesInDir(self.resumes_path)
        for file in files:
            self.loadResume(file.split(".")[0])

    def getFilesInDir(cls, dir_path: str) -> list[str]:
        """Gets a list of all the files in a directory.

        Args:
            dir_path (str): The directory path.

        Returns:
            list[str]: A list of file names excluding file extension.
        """
        all_entries = os.listdir(dir_path)
        files = []
        for entry in all_entries:
            full_path = os.path.join(dir_path, entry)
            if os.path.isfile(full_path):
                files.append(entry)
        return files
