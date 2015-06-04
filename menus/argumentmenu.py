import tkinter as tk
from menus.basemenu import BaseMenu
import subprocess as sp
from misc.windowmgr import WindowMgr

class ArgumentMenu(BaseMenu):
    def __init__(self, argumentString, button):
        BaseMenu.__init__(self, "specify arguments")
        self.__argumentString = argumentString
        self.__button = button
        self.__argument_names = [argument.split(")")[0] for argument in argumentString.split("$(")
                                            if ")" in argument]
        self.__arguments = {}
        #print("self.__argument_names", self.__argument_names)

    def __paint_argument_row(self, lf, argument, row_number):
        tk.Label(lf, text=argument).grid(row=row_number, column=0)
        entry = tk.Entry(lf, width=50)
        entry.grid(row=row_number, column=1)
        self.__arguments[argument] = entry

    def __paint_execute_button(self, lf, row_number):
        btn = tk.Button(lf, text="execute (or hit Enter)", command=self.__execute)
        btn.grid(row=row_number, column=0, columnspan=2)

    def __paint(self):
        lf = tk.LabelFrame(self._frame, text=self.__argumentString)
        self._parent.bind('<Return>', self.__execute)
        lf.pack(side="top")
        row_number = 0
        for argument in self.__argument_names:
            self.__paint_argument_row(lf, argument, row_number)
            row_number += 1
        self.__paint_execute_button(lf, row_number)

    def __execute(self, event=None):
        argString = self.__argumentString
        for argument, entry in self.__arguments.items():
            argString = argString.replace("$("+argument+")", entry.get())
        self.__button.execute(argString)

    def open_as_window(self):
        if self.is_opened():
            return
        self._open(True)
        self.__paint()

    def _on_mouse_entered(self, event):
        pass # override action from basemenu

    def _on_mouse_left(self, event):
        pass # override action from basemenu