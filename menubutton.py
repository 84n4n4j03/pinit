from basebutton import BaseButton

class MenuButton(BaseButton):

    def __init__(self, name, submenu, color="sky blue"):
        BaseButton.__init__(self, name, color)
        self.__submenu = submenu

    def on_clicked(self):
        print("open menu:", self.__submenu)
        self.__submenu.open_as_window()

    def on_mouse_entered(self, event):
        self._tk_button.configure(background="grey")
        self.__submenu.open_as_panel()

    def on_mouse_left(self, event):
        self._tk_button.configure(background=self._color)
        self._tk_button.after(100, self.close_if_submenu_is_not_hoverered_or_pinned)

    def close_if_submenu_is_not_hoverered_or_pinned(self):
        if not (self.__submenu.is_mouse_over() or self.__submenu.is_pinned()):
            self.__submenu.close()

    def get_storage_description(self):
        d = BaseButton.get_storage_description(self)
        d["submenu"] = self.__submenu.get_storage_description()
        return d

