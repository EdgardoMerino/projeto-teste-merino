#https://api.whatsapp.com/send?phone=
import webbrowser
from time import sleep
import pyautogui

telefones=[]
with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

#telefones = [5545991026470,5545991026470,5545991026470]
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(654,1011)
    sleep(10)
    pyautogui.typewrite('Teste')
    sleep(5)
    pyautogui.press('enter')
    sleep(10)