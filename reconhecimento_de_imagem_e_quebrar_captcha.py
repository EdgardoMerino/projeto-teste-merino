import pyautogui
print(pyautogui.locateOnScreen('Capturar.PNG'))
print(pyautogui.locateCenterOnScreen('Capturar.PNG'))
pyautogui.click(x=1475, y=581,duration=1)

#captcha
captcha = pyautogui.locateCenterOnScreen('Captcha.PNG')
pyautogui.click(captcha[0],captcha[1])