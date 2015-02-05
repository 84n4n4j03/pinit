import tkinter as tk

class BaseMenu(object):
    def __init__(self, name, parent=None):
        self._name = name
        self._parent = parent
        self._is_opened = False
        self._frame = None
        self.__is_pinned = False
        self.__is_mouse_over = False
        self.__buttons = []

    def _open(self, isDecorated):
        if self._is_opened: #if opened just set decoration
            self._parent.overrideredirect(not isDecorated)
            return
        if self._parent == None:
            self._parent = tk.Toplevel()
        self._parent.overrideredirect(not isDecorated)
        self._parent.wm_attributes('-topmost', 1)
        self._parent.protocol("WM_DELETE_WINDOW", self.close)
        self._parent.wm_title(self._name)
        self._parent.configure(background='black')
        self._frame = tk.Frame(self._parent)
        self._frame.pack()
        self._frame.bind("<Enter>", self._on_mouse_entered)
        self._frame.bind("<Leave>", self._on_mouse_left)
        x = self._parent.winfo_pointerx()
        y = self._parent.winfo_pointery()
        self._parent.geometry("%+d%+d" % (x-10, y+10))
        self._is_opened = True

    def close(self):
        if self._is_opened:
            self._parent.destroy()
            self._parent = None
            self._is_opened = False
            self.__is_pinned = False

    def __paint(self, isDecorated):
        if self.is_opened():
            self._open(isDecorated) #just set decoration
            return
        self._open(isDecorated)
        for button in self.__buttons:
            button.paint(self._frame)

    def open_as_window(self):
        self.__is_pinned = True
        self.__paint(True)

    def open_as_panel(self):
        if self.__is_pinned:
            return
        self.__paint(False)

    def add_button(self, button):
        self.__buttons.append(button)
        if self._is_opened:
            button.paint(self._frame)

    def get_name(self):
        return self._name

    def is_opened(self):
        return self._is_opened

    def _on_mouse_entered(self, event):
        self.__is_mouse_over = True

    def _on_mouse_left(self, event):
        self.__is_mouse_over = False
        if not self.__is_pinned:
            self.close()

    def is_pinned(self):
        return self.__is_pinned

    def is_mouse_over(self):
        return self.__is_mouse_over

    def get_storage_description(self):
        d = {}
        d["type"] = str(type(self))
        d["name"] = self._name
        d["buttons"] = []
        for button in self.__buttons:
            d["buttons"].append(button.get_storage_description())
        return d
