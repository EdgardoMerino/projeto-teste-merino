import pyautogui
from time import sleep
import webbrowser

nome = pyautogui.prompt('Digite seu nome')
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(5)
pyautogui.scroll(-500)
sleep(1)
nome_alerta = pyautogui.locateCenterOnScreen('digite_nome.PNG')
pyautogui.click(nome_alerta[0],nome_alerta[1],duration=1)
pyautogui.typewrite(nome)
sleep(1)
alerta = pyautogui.locateCenterOnScreen('alerta.PNG')
pyautogui.click(alerta[0],alerta[1],duration=1)
sleep(2)
ok = pyautogui.locateCenterOnScreen('ok.PNG')
pyautogui.click(ok[0],ok[1],duration=1)
sleep(1)
pyautogui.scroll(10000)
sleep(1)
pyautogui.scroll(-2000)
pyautogui.click(482,312,duration=1)
pyautogui.click(660,322,duration=1)
pyautogui.click(854,312,duration=1)
pyautogui.click(1035,342,duration=1)
pyautogui.click(1223,312,duration=1)
pyautogui.click(1425,343,duration=1)
pyautogui.alert('Terminou!')