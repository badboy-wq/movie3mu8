import win32gui
from pymouse import PyMouse
class gameassist:
    def __init__(self,wdname):
        self.hwnd=win32gui.FindWindow(0,wdname)
        if not self.hwnd:
            print("窗口找不到，请确认窗口句柄名称：【%s】" % wdname)
            exit()
        win32gui.SetForegroundWindow(self.hwnd)
        # self.im2num_arr = []
        #
        # # 主截图的左上角坐标和右下角坐标
        # self.scree_left_and_right_point = (299, 251, 768, 564)
        # # 小图标宽高
        # self.im_width = 39
        #
        # # PyMouse对象，鼠标点击
        # self.mouse = PyMouse()
if __name__ == '__main__':
    wdname='WeGame'
    demo = gameassist(wdname)



# import win32con
# import win32gui
# import win32api
#
# import time
# time.sleep(1)
# # 父窗口句柄, 参数1是类名，参数2是标题
# fileDialog = win32gui.FindWindow('#32770','炉石传说')
# # 子窗口句柄，是一个按钮控件，其中参数3是子窗口的类名
# bu = win32gui.FindWindowEx(fileDialog,None,'Button',None)
# # 鼠标左键按下
# win32gui.SendMessage(bu, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
# # 鼠标左键抬起
# win32gui.SendMessage(bu, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)
# print('11111111')