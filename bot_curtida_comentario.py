import pyautogui
from time import sleep
import webbrowser

pagina = pyautogui.prompt('Qual página você deseja seguir?')
webbrowser.open('https://www.instagram.com/')
sleep(7)
pyautogui.click(84,269,duration=1)
sleep(1)
pyautogui.typewrite(pagina)
sleep(1)
pyautogui.hotkey('enter')
sleep(1)
pyautogui.click(209,254,duration=1)
sleep(1)
pyautogui.click(778,737,duration=1)
sleep(10)
botao_curtir = pyautogui.locateCenterOnScreen('curtida.PNG')
if botao_curtir is not None:
    sleep(86400)
elif botao_curtir == None:
    pyautogui.click(botao_curtir[0], botao_curtir[1])
    sleep(1)
    pyautogui.click(1222,991,duration=1)
    sleep(1)
    pyautogui.typewrite('Bora flusao')
    sleep(1)
    pyautogui.hotkey('enter')
    sleep(86400)