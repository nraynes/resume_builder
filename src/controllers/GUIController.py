import tkinter as tk
from tkinter import ttk
from src.gui.windows.MainWindow import MainWindow
from src.gui.windows.EditorWindow import EditorWindow
from src.gui.base.BaseWindow import BaseWindow

class GUIController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Resume Builder")
        self.windows = {
            "main": MainWindow(self.root, self.openEditorWindow),
            "editor": EditorWindow(self.root, self.openMainWindow, False)
        }

    def openMainWindow(self):
        self.windows["editor"].hide()
        self.root.after(0, lambda: self.windows["main"].show())
        self.root.geometry("")

    def openEditorWindow(self):
        self.windows["main"].hide()
        self.root.after(0, lambda: self.windows["editor"].show())
        self.root.geometry("")

    def startGUI(self):
        self.root.mainloop()
