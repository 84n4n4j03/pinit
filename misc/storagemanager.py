import menus.mainmenu
import menus.pinmenu
import buttons.configbutton
import buttons.savebutton
import buttons.actionbutton
import buttons.dirbutton
import buttons.menubutton
import json

class StorageManager(object):
    FILENAME = None

    def __init__(self, layout_file=None):
        if layout_file:
            StorageManager.FILENAME = layout_file
        if not StorageManager.FILENAME:
            raise StorageManagerException("no layout file specified")


    def load(self):
        try:
            with open(StorageManager.FILENAME, "r") as f:
                js = f.read()
        except:
            print("unable to load saved layout")
            return None
        d = json.loads(js)
        if not "mainmenu.MainMenu" in d["type"]:
            raise StorageManagerException("no MainMenu found in toplevel")
        mainMenu = menus.mainmenu.MainMenu(d["name"], create_empty=True)
        for button in d["buttons"]:
            self.__add_button(mainMenu, button)
        return mainMenu

    def save(self, mainMenu):
        print("store to: " + StorageManager.FILENAME)
        s = json.dumps(mainMenu.get_storage_description(), sort_keys=True, indent=4)
        with open(StorageManager.FILENAME, "w") as f:
            f.write(s)

    def __add_button(self, menu, button):
        if "configbutton.ConfigButton" in button["type"]:
            menu.add_button(buttons.configbutton.ConfigButton(menu, button["color"]))
        elif "savebutton.SaveButton" in button["type"]:
            menu.add_button(buttons.savebutton.SaveButton(menu, button["color"]))
        elif "actionbutton.ActionButton" in button["type"]:
            menu.add_button(buttons.actionbutton.ActionButton(button["name"],
                                                button["cmd"], button["color"]))
        elif "dirbutton.DirButton" in button["type"]:
            menu.add_button(buttons.dirbutton.DirButton(button["name"],
                                        button["directory"], button["color"]))
        elif "menubutton.MenuButton" in button["type"]:
            menu.add_button(buttons.menubutton.MenuButton(button["name"],
                    self.__create_submenu(button["submenu"]), button["color"]))
        else:
            raise StorageManagerException("unknown buttontype")
        menu.get_buttons()[-1].add_description(button["description"])

    def __create_submenu(self, submenu):
        if not "pinmenu.PinMenu" in submenu["type"]:
            raise StorageManagerException("no PinMenu found as submenu")
        pinMenu = menus.pinmenu.PinMenu(submenu["name"], create_empty=True)
        for button in submenu["buttons"]:
            self.__add_button(pinMenu, button)
        return pinMenu


class StorageManagerException(Exception):
    def __init__(self, reason):
        self.reason = reason
    def __str__(self):
        return "Error reason: " + self.reason
