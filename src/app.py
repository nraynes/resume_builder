from src.controllers.AppController import AppController
from src.controllers.GUIController import GUIController

class App:
    def __init__(self):
        self.app_controller = AppController()
        self.gui_controller = GUIController()

app = App()

app.gui_controller.startGUI()
