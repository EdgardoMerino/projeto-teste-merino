import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1')==False:
    if pyautogui.pixelMatchesColor(612,501,(33,177,77)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(688,498,(230,47,54)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(764,499,(232,231,31)):
        pyautogui.press('j')
        sleep(0.05)