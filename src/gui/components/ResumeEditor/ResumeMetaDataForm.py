import tkinter as tk
from src.gui.components.LabeledInput import LabeledInput
from src.gui.Base.BaseComponent import BaseComponent


class ResumeMetaDataForm(BaseComponent):
    def __init__(self, master, header: bool = True):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        self._inp_title = LabeledInput(self._frame, "Title:")
        self._inp_author = LabeledInput(self._frame, "Author:")
        if header:
            lbl_heading = tk.Label(self._frame, text="Meta Data", font=("Helvetica", 18, "bold"))
            lbl_heading.pack()
            self.spacing().pack()
        self._inp_title.pack(anchor="e", fill=tk.BOTH)
        self._inp_author.pack(anchor="e", fill=tk.BOTH)

    @property
    def inpTitle(self):
        return self._inp_title

    @property
    def inpAuthor(self):
        return self._inp_author
