import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.click(-984,993,duration=2, button='left')
escrever_frase('Olá bom dia')
pyautogui.click(-187,986, duration=2, button='left')