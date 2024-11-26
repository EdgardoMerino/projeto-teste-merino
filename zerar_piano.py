import pyautogui
from time import sleep
import keyboard
import win32api
import win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1')==False:
    if pyautogui.pixelMatchesColor(754,721,(0,0,0)):
        click(754,721)
    if pyautogui.pixelMatchesColor(842,718,(0,0,0)):
        click(842,718)
    if pyautogui.pixelMatchesColor(929,713,(0,0,0)):
        click(929,713)
    if pyautogui.pixelMatchesColor(1022,713,(0,0,0)):
        click(1022,713)