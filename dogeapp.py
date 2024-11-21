import pyautogui
from time import sleep

#posicao algo
#faz\er algo com essa posição
pyautogui.moveTo(-1141,456,duration=0.5)
for i in range(100):
    sleep(0.1)
    pyautogui.click()