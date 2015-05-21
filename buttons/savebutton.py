from buttons.basebutton import BaseButton
from misc.storagemanager import StorageManager


class SaveButton(BaseButton):
    def __init__(self, mainMenu, color="thistle"):
        BaseButton.__init__(self, "save", color)
        self.__mainMenu = mainMenu
        self.__storageManager = StorageManager()

    def on_clicked(self):
        self.__storageManager.save(self.__mainMenu)

