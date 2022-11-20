from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of brown: (209, 150,  74)
#Color of yellow: (251, 188,  16)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot (region = (920,200,450,450))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range (0,height,5):

            r,g,b = pic.getpixel((x,y))

            if (r == 253 and b == 22):
                click(x+920, y+240)
                time.sleep(1)
                break

            if (r == 209 and b ==74):
                click(x+920, y+240)
                time.sleep(1)
                break
