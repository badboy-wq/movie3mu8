import win32con
import win32gui
import win32api
import win32ui

import time
import win32gui

hwnd_title = {}

def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


# win32gui.EnumWindows(get_all_hwnd, 0)
# for h, t in hwnd_title.items():
#     print(t)
#     if t :
#         print (h, t.decode("gbk"))
def handl():

    hand1=win32gui.FindWindow('WeGame')
    print(hand1)

if __name__ == '__main__':
    handl()
