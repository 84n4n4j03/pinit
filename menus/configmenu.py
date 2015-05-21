import tkinter as tk
from menus.basemenu import BaseMenu
from buttons.menubutton import MenuButton
from buttons.actionbutton import ActionButton
from buttons.dirbutton import DirButton
import menus.pinmenu
import tkinter.colorchooser as cc

class ConfigMenu(BaseMenu):
    def __init__(self, pinMenuToConfigure):
        BaseMenu.__init__(self,
                    "config: " + pinMenuToConfigure.get_name())
        self.__pinMenu = pinMenuToConfigure
        self.__entries = {}

    def __paint_menu_panel(self):
        lf = tk.LabelFrame(self._frame, text="Create new Menu Button")
        lf.pack(side="top")
        tk.Label(lf, text="name:").grid(row=0, column=0)
        entry = tk.Entry(lf, width=50)
        entry.grid(row=0, column=1)
        self.__entries["menu_name_entry"] = entry
        btn_color = tk.Button(lf, text="choose color", command=self.__open_menu_color_chooser)
        btn_color.grid(row=1, column=0)
        self.__entries["menu_color_btn"] = btn_color
        btn = tk.Button(lf, text="create new menu button",
                                        command=self.__create_new_menu_button)
        btn.grid(row=1, column=1)

    def __paint_action_panel(self):
        lf = tk.LabelFrame(self._frame, text="Create new Action Button  (use '$name' as placeholders)")
        lf.pack(side="top")
        tk.Label(lf, text="name:").grid(row=0, column=0)
        entry = tk.Entry(lf, width=50)
        entry.grid(row=0, column=1)
        self.__entries["action_name_entry"] = entry
        tk.Label(lf, text="cmd:").grid(row=1, column=0)
        cmd_entry = tk.Entry(lf, width=50)
        cmd_entry.grid(row=1, column=1)
        self.__entries["action_cmd_entry"] = cmd_entry
        btn_color = tk.Button(lf, text="choose color", command=self.__open_action_color_chooser)
        btn_color.grid(row=2, column=0)
        self.__entries["action_color_btn"] = btn_color
        btn = tk.Button(lf, text="create new action button",
                                        command=self.__create_new_action_button)
        btn.grid(row=2, column=1)

    def __paint_dir_panel(self):
        lf = tk.LabelFrame(self._frame, text="Create new Directory Button  ('$xxx' as placeholders, §pinit is root dir)")
        lf.pack(side="top")
        tk.Label(lf, text="name:").grid(row=0, column=0)
        entry = tk.Entry(lf, width=50)
        entry.grid(row=0, column=1)
        self.__entries["dir_name_entry"] = entry
        tk.Label(lf, text="directory:").grid(row=1, column=0)
        cmd_entry = tk.Entry(lf, width=50)
        cmd_entry.grid(row=1, column=1)
        self.__entries["dir_cmd_entry"] = cmd_entry
        btn_color = tk.Button(lf, text="choose color", command=self.__open_dir_color_chooser)
        btn_color.grid(row=2, column=0)
        self.__entries["dir_color_btn"] = btn_color
        btn = tk.Button(lf, text="create new dir button",
                                        command=self.__create_new_dir_button)
        btn.grid(row=2, column=1)


    def __open_action_color_chooser(self):
        self.__entries["action_color_btn"]["bg"] = cc.askcolor()[1]

    def __open_menu_color_chooser(self):
        self.__entries["menu_color_btn"]["bg"] = cc.askcolor()[1]

    def __open_dir_color_chooser(self):
        self.__entries["dir_color_btn"]["bg"] = cc.askcolor()[1]


    def __paint(self):
        self.__paint_menu_panel()
        self.__paint_action_panel()
        self.__paint_dir_panel()

    def __create_new_menu_button(self):
        name = self.__entries["menu_name_entry"].get()
        color = self.__entries["menu_color_btn"]["bg"]
        self.__pinMenu.add_button(MenuButton(name, menus.pinmenu.PinMenu(name), color))

    def __create_new_action_button(self):
        name = self.__entries["action_name_entry"].get()
        cmd = self.__entries["action_cmd_entry"].get()
        color = self.__entries["action_color_btn"]["bg"]
        self.__pinMenu.add_button(ActionButton(name, cmd, color))

    def __create_new_dir_button(self):
        name = self.__entries["dir_name_entry"].get()
        directory = self.__entries["dir_cmd_entry"].get()
        color = self.__entries["dir_color_btn"]["bg"]
        self.__pinMenu.add_button(DirButton(name, directory, color))

    def open_as_window(self):
        if self.is_opened():
            return
        self._open(True)
        self.__paint()

    def _on_mouse_entered(self, event):
        pass # override action from basemenu

    def _on_mouse_left(self, event):
        pass # override action from basemenu