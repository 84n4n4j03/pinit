from buttons.basebutton import BaseButton
import subprocess as sp

class ActionButton(BaseButton):

    def __init__(self, name, cmd=None, color="thistle"):
        BaseButton.__init__(self, name, color)
        self.__cmd = cmd

    def on_clicked(self):
        if not self.__cmd:
            print("no cmd set for:", self._name)
            return
        sp.call(self.__cmd, shell=True)

    def get_storage_description(self):
        d = BaseButton.get_storage_description(self)
        d["cmd"] = self.__cmd
        return d

