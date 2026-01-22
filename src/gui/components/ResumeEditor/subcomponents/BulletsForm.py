from src.gui.base.BaseEditorListForm import BaseEditorListForm


class BulletsForm(BaseEditorListForm):
    def __init__(self, *args, cmd_edit, **kwargs):
        self._heading = "Bullets"
        super().__init__(*args, **kwargs)
        self.cmd_edit = cmd_edit

    def cmdAdd(self):
        pass

    def cmdDelete(self):
        pass
    
    def cmdEdit(self):
        self.cmd_edit()
