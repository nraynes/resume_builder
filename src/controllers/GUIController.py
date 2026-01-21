import tkinter as tk
from src.gui.windows.MainWindow import MainWindow

class GUIController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Resume Builder")
        self.active_window = MainWindow(self.root)

    def startGUI(self):
        self.root.mainloop()
