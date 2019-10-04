#! /usr/bin/env python3

from menus.pinmenu import PinMenu
from buttons.basebutton import BaseButton
from buttons.actionbutton import ActionButton
from buttons.menubutton import MenuButton
from menus.mainmenu import MainMenu
from buttons.savebutton import SaveButton
import json
from misc.storagemanager import StorageManager
from misc.windowmgr_gtk import WindowMgr
import argparse
import os


class PinIt(object):
    def __init__(self, layout_file):
        self.__mainMenu = StorageManager(layout_file).load()
        if not self.__mainMenu:
            print("create new")
            self.__mainMenu = MainMenu("mainMenu")
        self.__mainMenu.open_as_window()
        self.__windowMgr = WindowMgr()
        os.environ["PINIT_ROOT_DIR"] = os.path.dirname(os.path.realpath(__file__))
        os.environ["PINIT_LAYOUT_DIR"] = os.path.dirname(os.path.realpath(layout_file))


    def run(self):
        print("PinIt by Johannes Vogel")
        print("visit https://github.com/84n4n4j03/pinit")
        self.__mainMenu.run()

def run():
    description="""
Lightweight GUI to simply create buttons to fire
commands, programms, web-pages, ...
Easily organize these buttons in submenus and
pin them wherever needed on the screen.
They're always on top.
"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-l', '--layout', default='../layout.js',
                    help='specify a json layout file (default: ../layout.js)')
    args = parser.parse_args()
    pinIt = PinIt(args.layout)
    pinIt.run()

if __name__ == "__main__":
    run()
