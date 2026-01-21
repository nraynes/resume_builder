import tkinter as tk
from src.gui.components.BaseFrame import BaseFrame


class EditorWindow(BaseFrame):
    def __init__(self, master):
        self._frame = tk.Frame(master, padx=10, pady=10)
        self._frame.pack(anchor="center", expand=True)

    def addSpacing(self):
        spacing = tk.Frame(self._frame, height=5)
        spacing.pack()
