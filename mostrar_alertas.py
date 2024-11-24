import pyautogui

pyautogui.alert(text='Iniciando sua automação',title='Automação de Login', button='ok')
email = pyautogui.prompt(text='Digite seu e-mail', title='informações obrigatórias')
print(f'Você digitou {email}')

#confirmar se algo deve ou nao acontecer
resposta = pyautogui.confirm(text='Continuar rodando nossa automação?', title='Conformação', buttons=['sim', 'não', 'cancelar'])
if resposta == 'sim':
     print('continuando automação')
elif resposta == 'não':
     print('encerrando automação')
else:
     print('operação cancelada') 

#senha
senha = pyautogui.password(text='digite sua senha: ', title='dados de login', mask='*')
print(senha)