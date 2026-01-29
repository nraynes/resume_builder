import tkinter as tk
from src.gui.base.BaseMetaDataForm import BaseMetaDataForm
from src.gui.lib.Label import Label


class ResumeMetaDataForm(BaseMetaDataForm):
    def __init__(self, master: tk.Frame):
        super().__init__(master)
        lbl_heading = Label(
            self._frame, text="Meta Data", font=("Helvetica", 18, "bold")
        )
        
        lbl_heading.pack()
        self.spacing().pack()
        self.packBase()
        
    def populateData(self, title: str, author: str):
        self._inp_title.setValue(title)
        self._inp_author.setValue(author)
