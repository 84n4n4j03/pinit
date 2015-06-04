import tkinter as tk
from misc.windowmgr import WindowMgr

class BaseButton(object):
    def __init__(self, name, color=None):
        self._name = name
        self.__description = ""
        self.__image = None
        self._tk_button = None
        self._color = color

    def get_name(self):
        return self._name

    def add_description(self, description):
        self.__description = description

    def paint(self, parent):
        self._tk_button = tk.Button(parent)
        if self._color != None:
            self._tk_button['bg'] = self._color
        else:
            self._color = self._tk_button['bg']
        self._tk_button["text"] = self._name
        self._tk_button["command"] = self.on_clicked
        self._tk_button.pack(side="left")
        self._tk_button.bind("<Enter>", self.on_mouse_entered)
        self._tk_button.bind("<Leave>", self.on_mouse_left)
        self._tk_button.bind("<Button-3>", self.on_right_clicked)


    def add_image(self, image):
        pass

    def on_clicked(self):
        pass

    def on_right_clicked(self, event):
        WindowMgr().set_cmd_window_to_foreground()
        print("\nbutton '" + self._name + "':")
        if not self.__description:
            print("no description found (add it to your layout.js file)\n")
        else:
            print(self.__description + "\n")

    def on_mouse_entered(self, event):
        pass

    def on_mouse_left(self, event):
        pass

    def get_storage_description(self):
        d = {}
        d["type"] = str(type(self))
        d["name"] = self._name
        d["description"] = self.__description
        d["color"] = self._color
        return d

