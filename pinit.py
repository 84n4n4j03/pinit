from menus.pinmenu import PinMenu
from buttons.basebutton import BaseButton
from buttons.actionbutton import ActionButton
from buttons.menubutton import MenuButton
from menus.mainmenu import MainMenu
from buttons.savebutton import SaveButton
import json
from misc.storagemanager import StorageManager



class PinIt(object):
    def __init__(self):
        self.__mainMenu = StorageManager().load()
        if not self.__mainMenu:
            self.__mainMenu = MainMenu("mainMenu")
        self.__mainMenu.open_as_window()


    def run(self):
        self.__mainMenu.run()

def run():
    pinIt = PinIt()
    pinIt.run()

if __name__ == "__main__":
    run()