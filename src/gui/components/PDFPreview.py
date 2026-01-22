import tkinter as tk
from src.gui.base.BaseComponent import BaseComponent


class PDFPreview(BaseComponent):
    def __init__(self, master):
        self._frame = tk.Frame(master, padx=5, pady=5, borderwidth=1, relief="solid")
