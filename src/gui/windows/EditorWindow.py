import tkinter as tk
import platform
from src.gui.base.BaseWindow import BaseWindow
from src.gui.components.ResumeEditor import ResumeEditor
from src.models.Cv import Cv
from typing import Callable, Optional
from src.gui.lib.Frame import Frame
from src.gui.lib.Canvas import Canvas
from src.gui.lib.Scrollbar import Scrollbar


class EditorWindow(BaseWindow):

    def __init__(
        self,
        master: tk.Tk,
        open_main_cb: Callable,
        save_resume_cb: Callable,
        generate_pdf_cb: Callable,
    ):
        self._canvas = Canvas(master)
        self.save_resume_cb = save_resume_cb
        self.generate_pdf_cb = generate_pdf_cb
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self._scroll_bar = Scrollbar(master, orient="vertical", command=self._canvas.yview)
        self._frame = Frame(self._canvas, padx=10, pady=10)
        self._frame.bind("<Configure>", self.onFrameConfigure)
        self._canvas.bind("<Configure>", self.onCanvasConfigure)
        self._win_id = self._canvas.create_window((0, 0), window=self._frame, anchor="nw")
        self._canvas.configure(yscrollcommand=self._scroll_bar.set)
        self._edt_resume = ResumeEditor(
            self._frame,
            open_main_cb=open_main_cb,
            save_resume_cb=self.saveResume,
            generate_pdf_cb=self.generatePDF,
            resize_canvas_cb=self.resizeCanvas,
        )

        self._edt_resume.pack()
        self._canvas.update_idletasks()
        self._canvas.bind_all("<MouseWheel>", self.onMousewheel)
        self._canvas.bind_all("<Button-4>", self.onMousewheel)
        self._canvas.bind_all("<Button-5>", self.onMousewheel)

    @property
    def edtResume(self) -> ResumeEditor:
        return self._edt_resume

    def show(self):
        self._canvas.pack(side="left", fill="both", expand=True)
        self._scroll_bar.pack(side="right", fill="y")
        self._canvas.after_idle(self.refreshCanvas)

    def hide(self):
        self._scroll_bar.pack_forget()
        self._canvas.pack_forget()

    def generatePDF(self):
        self.saveResume()
        self.generate_pdf_cb(None if self._edt_resume.isCv else self._edt_resume.frmMetaData.inpTitle.get())

    def saveResume(self):
        self.save_resume_cb(self._edt_resume.getObject())

    def populateData(self, resume: Cv):
        self._edt_resume.populateData(resume)

    def onMousewheel(self, event: tk.Event):
        """Handles vertical scrolling across different platforms."""
        os_name = platform.system()
        if os_name == "Windows":
            # Windows uses <MouseWheel> and event.delta is +/- 120
            self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif os_name == "Darwin":
            # macOS uses <MouseWheel> with dynamic delta values
            self._canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            # X11 (Linux) uses <Button-4> for up and <Button-5> for down
            if event.num == 4:
                self._canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self._canvas.yview_scroll(1, "units")

    def resizeCanvas(self):
        x1, y1, x2, y2 = self._canvas.bbox("all")
        max_canvas_width = int(self.screen_width * 0.9)
        self.canvas_width = min(x2 - x1, max_canvas_width)
        max_canvas_height = int(self.screen_height * 0.8)
        self.canvas_height = min(y2 - y1, max_canvas_height)
        self._canvas.configure(width=self.canvas_width, height=self.canvas_height)

    def onCanvasConfigure(self, event: tk.Event):
        self._canvas.itemconfigure(self._win_id, width=event.width)
        self.onFrameConfigure()

    def onFrameConfigure(self, event: Optional[tk.Event] = None):
        bbox = self._canvas.bbox("all")
        if bbox is not None:
            self._canvas.configure(scrollregion=bbox)

    def refreshCanvas(self):
        self._canvas.update_idletasks()
        self.onFrameConfigure()
