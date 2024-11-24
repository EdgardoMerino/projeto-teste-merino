import pyautogui
from time import sleep

email = pyautogui.prompt(text='Digite seu email', title='Dados de login')
senha = pyautogui.password(text='Digite sua senha',title='Dados de login',mask='*')
pyautogui.click(-566,312, duration=2)
pyautogui.typewrite(email)
sleep(1)
pyautogui.hotkey('enter')
pyautogui.typewrite(senha)