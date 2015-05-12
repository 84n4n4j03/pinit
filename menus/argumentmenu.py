import tkinter as tk
from menus.basemenu import BaseMenu
import subprocess as sp

class ArgumentMenu(BaseMenu):
    def __init__(self, cmd):
        BaseMenu.__init__(self, "specify arguments")
        self.__cmd = cmd
        self.__argument_names = [argument for argument in cmd.split()
                                            if argument.startswith("$")]
        self.__arguments = {}
        #print("self.__arguments", self.__arguments)

    def __paint_argument_row(self, lf, argument, row_number):
        tk.Label(lf, text=argument).grid(row=row_number, column=0)
        entry = tk.Entry(lf, width=50)
        entry.grid(row=row_number, column=1)
        self.__arguments[argument] = entry

    def __paint_execute_button(self, lf, row_number):
        btn = tk.Button(lf, text="execute (or hit Enter)", command=self.__execute)
        btn.grid(row=row_number, column=0, columnspan=2)

    def __paint(self):
        lf = tk.LabelFrame(self._frame, text=self.__cmd)
        self._parent.bind('<Return>', self.__execute)
        lf.pack(side="top")
        row_number = 0
        for argument in self.__argument_names:
            self.__paint_argument_row(lf, argument, row_number)
            row_number += 1
        self.__paint_execute_button(lf, row_number)

    def __execute(self, event=None):
        cmd = self.__cmd
        for argument, entry in self.__arguments.items():
            cmd = cmd.replace(argument, entry.get())
        print("\ncmd: " + cmd + "\n>>>>>>>>>>>>>>>>>>")
        sp.call(cmd, shell=True)

    def open_as_window(self):
        if self.is_opened():
            return
        self._open(True)
        self.__paint()

    def _on_mouse_entered(self, event):
        pass # override action from basemenu

    def _on_mouse_left(self, event):
        pass # override action from basemenu