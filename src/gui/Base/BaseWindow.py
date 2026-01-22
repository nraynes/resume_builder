from src.gui.base.BaseFrame import BaseFrame
from abc import ABC, abstractmethod


class BaseWindow(BaseFrame, ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass
