import pprint
import mainmenu
import pinmenu
import configbutton
import savebutton
import actionbutton
import menubutton
import json

class StorageManager(object):
    FILENAME = "savedLayout.js"

    def __init__(self):
        pass

    def load(self):
        try:
            with open(StorageManager.FILENAME, "r") as f:
                js = f.read()
        except:
            print("unable to load saved layout")
            return None
        d = json.loads(js)
        #print(d)
        if not "mainmenu.MainMenu" in d["type"]:
            raise StorageManagerException("no MainMenu found in toplevel")
        mainMenu = mainmenu.MainMenu(d["name"], create_empty=True)
        for button in d["buttons"]:
            self.__add_button(mainMenu, button)
        return mainMenu

    def save(self, mainMenu):
        s = json.dumps(mainMenu.get_storage_description(), sort_keys=True, indent=4)
        with open(StorageManager.FILENAME, "w") as f:
            f.write(s)


    def __add_button(self, menu, button):
        if "configbutton.ConfigButton" in button["type"]:
            menu.add_button(configbutton.ConfigButton(menu, button["color"]))
        elif "savebutton.SaveButton" in button["type"]:
            menu.add_button(savebutton.SaveButton(menu, button["color"]))
        elif "actionbutton.ActionButton" in button["type"]:
            menu.add_button(actionbutton.ActionButton(button["name"],
                                                button["cmd"], button["color"]))
        elif "menubutton.MenuButton" in button["type"]:
            menu.add_button(menubutton.MenuButton(button["name"],
                    self.__create_submenu(button["submenu"]), button["color"]))

    def __create_submenu(self, submenu):
        if not "pinmenu.PinMenu" in submenu["type"]:
            raise StorageManagerException("no PinMenu found as submenu")
        pinMenu = pinmenu.PinMenu(submenu["name"], create_empty=True)
        for button in submenu["buttons"]:
            self.__add_button(pinMenu, button)
        return pinMenu


class StorageManagerException(Exception):
    def __init__(self, reason):
        self.reason = reason
    def __str__(self):
        return "Error reason: " + self.reason
