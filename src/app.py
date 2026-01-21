from src.controllers.AppController import AppController
from src.controllers.GUIController import GUIController


class App(AppController, GUIController):
    def __init__(self):
        super(AppController, self).__init__()
        super(GUIController, self).__init__()


app = App()
app.startGUI()
