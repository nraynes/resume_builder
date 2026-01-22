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
