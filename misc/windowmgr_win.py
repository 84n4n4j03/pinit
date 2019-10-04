import os
import time
import hashlib
import ctypes

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow
GetActiveWindow = ctypes.windll.user32.GetActiveWindow

title_handle_map = {}
def found_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        title_handle_map[buff.value] = hwnd
    return True

class WindowMgr(object):
    cmd_window_handle = None
    def __init__(self):
        if not WindowMgr.cmd_window_handle:
            title_hash = hashlib.sha224(bytes(str(time.time()), 'utf-8')).hexdigest()
            os.system("title " + title_hash)
            EnumWindows(EnumWindowsProc(found_window), 0)
            WindowMgr.cmd_window_handle = title_handle_map.get(title_hash)
        #print(WindowMgr.cmd_window_handle)

    def set_cmd_window_to_foreground(self):
        if(WindowMgr.cmd_window_handle):
            #current_handle = GetActiveWindow()
            SetForegroundWindow(WindowMgr.cmd_window_handle)
            #time.sleep(1)
            #SetForegroundWindow(current_handle)
