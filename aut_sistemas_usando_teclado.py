import pyautogui
from time import sleep
pyautogui.click(518,283,duration=1)
pyautogui.typewrite('admin@hotmail.com')
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.typewrite('123456')
sleep(1)
pyautogui.press('tab')
sleep(1)
pyautogui.press('space')

#dicas:
print(pyautogui.KEYBOARD_KEYS)

#copiar texto e colar
pyautogui.click(518,283,duration=1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl','c')
pyautogui.click(428,183,duration=1)
pyautogui.hold('ctrl', 'v')
