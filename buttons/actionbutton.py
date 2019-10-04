from buttons.basebutton import BaseButton
import subprocess as sp
import menus.argumentmenu
from misc.windowmgr_gtk import WindowMgr


class ActionButton(BaseButton):

    def __init__(self, name, cmd=None, color="thistle"):
        BaseButton.__init__(self, name, color)
        self.__cmd = cmd

    def on_clicked(self):
        if not self.__cmd:
            print("no cmd set for:", self._name)
            return
        if "$(" in self.__cmd:
            am = menus.argumentmenu.ArgumentMenu(self.__cmd, self)
            am.open_as_window()
        else:
            self.execute(self.__cmd)

    def get_storage_description(self):
        d = BaseButton.get_storage_description(self)
        d["cmd"] = self.__cmd
        return d

    def execute(self, cmd):
        WindowMgr().set_cmd_window_to_foreground()
        print("\ncmd: " + cmd + "\n>>>>>>>>>>>>>>>>>>")
        sp.call(cmd, shell=True)
