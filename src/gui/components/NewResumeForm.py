import tkinter as tk
from src.gui.components.BaseComponent import BaseComponent


class NewResumeForm(BaseComponent):
    def __init__(self, master):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
        lbl_title_entry = tk.Label(self._frame, text="Title:")
        lbl_author_entry = tk.Label(self._frame, text="Author:")
        self._inp_title = tk.Entry(self._frame)
        self._inp_author = tk.Entry(self._frame)
        self._btn_new_resume = tk.Button(self._frame, text="New Resume")

        lbl_title_entry.grid(row=0, sticky="E")
        self._inp_title.grid(row=0, column=1)
        lbl_author_entry.grid(row=1, sticky="E")
        self._inp_author.grid(row=1, column=1)
        self._btn_new_resume.grid(row=2, columnspan=2)

    @property
    def inpTitle(self):
        return self._inp_title
    
    @property
    def inpAuthor(self):
        return self._inp_author
    
    @property
    def btnNewResume(self):
        return self._btn_new_resume
