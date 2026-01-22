import tkinter as tk
from src.models.Cv import Cv
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
                openEditorCb=self.openEditorWindow,
                newResumeCb=self.createNewResume,
                newCvResumeCb=self.createNewResumeFromCv,
            ),
            "editor": EditorWindow(self.root, self.openMainWindow),
        }
        self.openMainWindow()

    @property
    def mainWindow(self) -> MainWindow:
        return self.windows["main"]

    @property
    def editorWindow(self) -> EditorWindow:
        return self.windows["editor"]

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
