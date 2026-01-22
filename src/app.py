from src.controllers.AppController import AppController
from src.controllers.GUIController import GUIController


class App(AppController, GUIController):
    def __init__(self):
        AppController.__init__(self)
        GUIController.__init__(self)


app = App()
app.startGUI()
