import win32api 
import win32con
import time

def move_click():
    run = False
    try:
        while(True):
            if win32api.GetKeyState(ord('H')) < 0 :
                run = not run # H Key pressed
                print("click")
            if run:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) 
            time.sleep(0.2)
    except KeyboardInterrupt:
        print('interrupted!')
if __name__ == '__main__':
    move_click()