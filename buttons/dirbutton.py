from buttons.basebutton import BaseButton
import subprocess as sp
import menus.argumentmenu
from misc.windowmgr import WindowMgr
import os


class DirButton(BaseButton):

    def __init__(self, name, directory=None, color="thistle"):
        BaseButton.__init__(self, name, color)
        self.__directory = directory
        self.__pinit_root_dir = os.path.dirname(os.path.realpath(__file__+"/.."))

    def on_clicked(self):
        if not self.__directory:
            print("no directory set for:", self._name)
            return
        if "$(" in self.__directory:
            am = menus.argumentmenu.ArgumentMenu(self.__directory, self)
            am.open_as_window()
        else:
            self.execute(self.__directory)

    def get_storage_description(self):
        d = BaseButton.get_storage_description(self)
        d["directory"] = self.__directory
        return d

    def execute(self, directory):
        WindowMgr().set_cmd_window_to_foreground()
        directory = os.path.expandvars(directory)
        print("\ndirectory: " + directory + "\n>>>>>>>>>>>>>>>>>>")
        os.chdir(directory)
        print("currentDir: " + os.getcwd())
        print()
