from src.gui.base.BaseComponent import BaseComponent
from abc import ABC, abstractmethod
import tkinter as tk
from typing import Any


class BaseEntry(BaseComponent, ABC):
    _inp: tk.BaseWidget

    @property
    def inp(self) -> tk.BaseWidget:
        return self._inp

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def setValue(self, x: Any):
        pass
