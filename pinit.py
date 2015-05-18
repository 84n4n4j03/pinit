from menus.pinmenu import PinMenu
from buttons.basebutton import BaseButton
from buttons.actionbutton import ActionButton
from buttons.menubutton import MenuButton
from menus.mainmenu import MainMenu
from buttons.savebutton import SaveButton
import json
from misc.storagemanager import StorageManager
from misc.windowmgr import WindowMgr



class PinIt(object):
    def __init__(self):
        self.__mainMenu = StorageManager().load()
        if not self.__mainMenu:
            print("create new")
            self.__mainMenu = MainMenu("mainMenu")
        self.__mainMenu.open_as_window()
        self.__windowMgr = WindowMgr()


    def run(self):
        print("PinIt by Johannes Vogel")
        print("visit https://github.com/84n4n4j03/pinit")
        self.__mainMenu.run()

def run():
    pinIt = PinIt()
    pinIt.run()

if __name__ == "__main__":
    run()