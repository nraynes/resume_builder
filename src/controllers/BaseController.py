from src.models.Cv import Cv
from src.models.Resume import Resume


class BaseController:
    _active_resume: Cv
    cv: Cv
    resumes: dict[str, Resume]

    def resume(self):
        pass

    def newResume(self):
        pass

    def resumeFromCv(self):
        pass

    def overwriteCv(self, cv: Cv):
        pass

    def overwriteResume(self, title: str, new_resume: Resume):
        pass
    
    def deleteResume(self, title: str):
        pass
