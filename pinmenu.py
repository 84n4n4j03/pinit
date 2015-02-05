from basemenu import BaseMenu
from configbutton import ConfigButton

class PinMenu(BaseMenu):
    def __init__(self, name, create_empty=False):
        BaseMenu.__init__(self, name, parent=None)
        if not create_empty:
            self.add_button(ConfigButton(self));


