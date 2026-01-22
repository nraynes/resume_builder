import tkinter as tk
from src.gui.lib.LabeledInput import LabeledInput
from src.gui.base.BaseComponent import BaseComponent
from src.gui.base.BaseMetaDataForm import BaseMetaDataForm


class ResumeMetaDataForm(BaseMetaDataForm):
    def __init__(self, master):
        super().__init__(master)
        lbl_heading = tk.Label(
            self._frame, text="Meta Data", font=("Helvetica", 18, "bold")
        )
        lbl_heading.pack()
        self.spacing().pack()
        self.packBase()
        
    def populateData(self, title: str, author: str):
        self._inp_title.setValue(title)
        self._inp_author.setValue(author)
