import tkinter as tk
from tkinter import filedialog
from src.models.Cv import Cv
from src.models.Resume import Resume
from src.controllers.BaseController import BaseController
from src.gui.windows.MainWindow import MainWindow
from src.gui.windows.EditorWindow import EditorWindow
from typing import Optional

class GUIController(BaseController):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Resume Builder")
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

    def generateResumePDF(self, title: str):
        resume = self.resume(title)
        if resume is not None:
            output_path = filedialog.asksaveasfilename(title="Select where you would like to save this PDF to")
            if output_path[-4:] != ".pdf":
                output_path = f"{output_path.split(".")[0]}.pdf"
            self.pdf_service.generatePDFFromResume(resume, output_path)

    def deleteSelectedResume(self, title: str):
        self.deleteResume(title)
        self.populateMainWindowData()

    def saveActiveResume(self, resume: Cv):
        is_resume = isinstance(resume, Resume)
        if is_resume:
            self.overwriteResume(resume.title, resume)
        else:
            self.overwriteCv(resume)

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

    def setActiveResume(self, title: Optional[str] = None):
        if title is None:
            self._active_resume = self.cv
        else:
            self._active_resume = self.resume(title)

    def openMainWindow(self):
        self.editorWindow.hide()
        self.root.after(0, lambda: self.mainWindow.show())
        self.root.geometry("")
        self.populateMainWindowData()

    def openEditorWindow(self, title: Optional[str] = None):
        self.setActiveResume(title)
        self.mainWindow.hide()
        self.root.after(0, lambda: self.editorWindow.show())
        self.root.geometry("")
        self.populateEditorWindowData()

    def startGUI(self):
        self.root.mainloop()
