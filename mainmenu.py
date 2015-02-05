from basemenu import BaseMenu
import tkinter as tk
from configbutton import ConfigButton
from savebutton import SaveButton

class MainMenu(BaseMenu):
    def __init__(self, name, create_empty=False):
        BaseMenu.__init__(self, name, parent=tk.Tk())
        if not create_empty:
            self.add_button(ConfigButton(self))
            self.add_button(SaveButton(self))

    def run(self):
        self._parent.mainloop()

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['view']
        return state
        #Todo:hier weiter: howto pickle/store
