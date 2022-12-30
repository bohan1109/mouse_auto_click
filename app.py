import win32api 
import win32con
import time
import random

def move_click(x,y):
    win32api.SetCursorPos((x, y))
    try:
        while(True):
            if win32api.GetKeyState(ord('H')) < 0 : # H Key pressed
                print('interrupted!')
                break
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) 
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('interrupted!')


move_click(400,600)