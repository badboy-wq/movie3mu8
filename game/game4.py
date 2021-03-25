import win32gui
import win32con
hand1 = win32gui.FindWindow(None,'WeGame')
text = win32gui.GetWindowText(hand1)
print(hand1)
print(text)
win32gui.SetWindowPos(hand1,win32con.HWND_TOPMOST,100,100,300,300,win32con.SWP_SHOWWINDOW)