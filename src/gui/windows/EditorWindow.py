import tkinter as tk
from tkinter import ttk
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.ResumeEditor.ResumeEditor import ResumeEditor


class EditorWindow(BaseWindow):
    def __init__(self, master: tk.Tk, openMainCb, show: bool = True):
        self._canvas = tk.Canvas(master)
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self._scroll_bar = ttk.Scrollbar(master, orient="vertical", command=self._canvas.yview)
        self._frame = ttk.Frame(self._canvas, padding=10)
        self._frame.bind("<Configure>", lambda e: self.on_frame_configure())
        self._canvas.bind("<Configure>", self._on_canvas_configure)
        self._win_id = self._canvas.create_window((0, 0), window=self._frame, anchor="nw")
        self._canvas.configure(yscrollcommand=self._scroll_bar.set)
        self._frm_resume = ResumeEditor(self._frame, openMainCb)
        self._frm_resume.pack()
        self._canvas.update_idletasks()
        self._resize_canvas()
        if show:
            self.show()

    def _resize_canvas(self):
        x1, y1, x2, y2 = self._canvas.bbox("all")
        max_canvas_width = int(self.screen_width * 0.9)
        self.canvas_width = min(x2 - x1, max_canvas_width)
        max_canvas_height = int(self.screen_height * 0.8)
        self.canvas_height = min(y2 - y1, max_canvas_height)
        self._canvas.configure(width=self.canvas_width, height=self.canvas_height)

    def _on_canvas_configure(self, event):
        self._canvas.itemconfigure(self._win_id, width=event.width)
        self.on_frame_configure()

    def on_frame_configure(self):
        bbox = self._canvas.bbox("all")
        if bbox is not None:
            self._canvas.configure(scrollregion=bbox)

    @property
    def frmResume(self):
        return self._frm_resume

    def hide(self):
        self._scroll_bar.pack_forget()
        self._canvas.pack_forget()

    def show(self):
        self._canvas.pack(side="left", fill="both", expand=True)
        self._scroll_bar.pack(side="right", fill="y")
        self._canvas.after_idle(self._refresh_canvas)

    def _refresh_canvas(self):
        self._canvas.update_idletasks()
        self.on_frame_configure()
