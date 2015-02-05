from basebutton import BaseButton
from configmenu import ConfigMenu

class ConfigButton(BaseButton):
    def __init__(self, pinMenuToConfigure, color="yellow"):
        BaseButton.__init__(self, "config", color)
        self.__configMenu = ConfigMenu(pinMenuToConfigure)

    def on_clicked(self):
        self.__configMenu.open_as_window()
