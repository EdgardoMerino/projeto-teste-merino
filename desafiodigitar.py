import pyautogui
import pyperclip

def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.click(-861,213,duration=2, button='left')
escrever('Automação é incrível')