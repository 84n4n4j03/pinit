from buttons.basebutton import BaseButton
from menus.configmenu import ConfigMenu

class ConfigButton(BaseButton):
    def __init__(self, pinMenuToConfigure, color="yellow"):
        BaseButton.__init__(self, "config", color)
        self.__configMenu = ConfigMenu(pinMenuToConfigure)
        self.add_description(
                "Opens a configuration menu to add a new button. Types:\n" +
                "   1. MenuButton: Container for further buttons\n" +
                "   2. ActionButton: executes a command in the associated terminal as supprocess\n" +
                "   3. DirectoryButton: Jumps to directories in the associated terminal\n" +
                "2+3: * you can specify placeholders, e.g.: $(aName)\n" +
                "       will open an additional dialog that asks for 'aName'\n" +
                "     * you can use environment variables (windows: %VARIABLE%)\n" +
                "       there are a couple of environment variables available:\n" +
                "       PINIT_ROOT_DIR:   root directory of your pinit instance\n" +
                "       PINIT_LAYOUT_DIR: directory of of the associated layout file")

    def on_clicked(self):
        self.__configMenu.open_as_window()
