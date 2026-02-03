import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from src.models.Cv import Cv
from src.models.Resume import Resume
from src.controllers.BaseController import BaseController
from src.gui.windows.MainWindow import MainWindow
from src.gui.windows.EditorWindow import EditorWindow
from typing import Callable, Optional

class GUIController(BaseController):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Resume Builder")
        self._style = ttk.Style()
        self.configureStyle()
        self._active_resume = None
        self.windows = {
            "main": MainWindow(
                self.root,
                open_editor_cb=self.openEditorWindow,
                new_resume_cb=self.createNewResume,
                new_cv_resume_cb=self.createNewResumeFromCv,
                delete_resume_cb=self.deleteSelectedResume,
            ),
            "editor": EditorWindow(
                self.root,
                open_main_cb=self.openMainWindow,
                save_resume_cb=self.saveActiveResume,
                generate_pdf_cb=self.generateResumePDF,
            ),
        }
        self.openMainWindow()

    @property
    def mainWindow(self) -> MainWindow:
        return self.windows["main"]

    @property
    def editorWindow(self) -> EditorWindow:
        return self.windows["editor"]

    def configureStyle(self):
        self._style.configure("TButton", width=0)

    def addEvent(self, cb: Callable, *args, **kwargs):
        self.root.after(0, lambda: cb(*args, **kwargs))

    def generateResumePDF(self, title: Optional[str]):
        """Calls the GeneratePDF method with different arguments based on whether
        the CV or a Resume is being generated. If a title is supplied, then a resume
        is generated. If no title is supplied, the CV is generated.

        Args:
            title (Optional[str]): The title of a resume.
        """
        if title is None:
            self.generatePDF("Curriculum Vitae", "N/a", self.cv)
        else:
            resume = self.resume(title)
            if resume is not None:
                self.generatePDF(resume.title, resume.author, resume)

    def generatePDF(self, title: str, author: str, resume: Cv):
        """Asks the user where to save the pdf file, then generates and saves it.

        Args:
            title (str): The title of the resume.
            author (str): The author of the resume.
            resume (Cv): The Resume or Cv object to generate a pdf from.
        """
        output_path = filedialog.asksaveasfilename(title="Select where you would like to save this PDF to")
        if output_path[-4:] != ".pdf":
            output_path = f"{output_path.split(".")[0]}.pdf"
        self.pdf_service.generatePDFFromResume(title, author, resume, output_path)

    def deleteSelectedResume(self, title: str):
        self.deleteResume(title)
        self.populateMainWindowData()

    def saveActiveResume(self, resume: Cv):
        is_resume = isinstance(resume, Resume)
        if is_resume:
            self.overwriteResume(resume.title, resume)
        else:
            self.overwriteCv(resume)

    def setActiveResume(self, title: Optional[str] = None):
        if title is None:
            self._active_resume = self.cv
        else:
            self._active_resume = self.resume(title)

    def createNewResume(self, title: str, author: str):
        self.newResume(title, author)
        self.populateMainWindowData()

    def createNewResumeFromCv(self, title: str, author: str):
        self.resumeFromCv(title, author)
        self.populateMainWindowData()

    def populateMainWindowData(self):
        self.mainWindow.setResumeList(list(self.resumes.keys()))

    def populateEditorWindowData(self):
        if self._active_resume is not None:
            self.editorWindow.populateData(self._active_resume)

    def openMainWindow(self):
        self.editorWindow.hide()
        self.root.after(0, lambda: self.mainWindow.show())
        self.populateMainWindowData()
        self.root.after(0, lambda: self.root.geometry(""))

    def openEditorWindow(self, title: Optional[str] = None):
        self.setActiveResume(title)
        self.mainWindow.hide()
        self.root.after(0, lambda: self.editorWindow.show())
        self.populateEditorWindowData()
        self.root.after(0, lambda: self.root.geometry(""))

    def startGUI(self):
        self.root.mainloop()
