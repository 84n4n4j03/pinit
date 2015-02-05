from pinmenu import PinMenu
from basebutton import BaseButton
from actionbutton import ActionButton
from menubutton import MenuButton
from mainmenu import MainMenu
from savebutton import SaveButton
import json
from storagemanager import StorageManager



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