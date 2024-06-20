# Qual biblioteca python PysimpleGUI
# pip install pysimplegui

#Fazer toda configuração PysimpleGUI
#import PySimpleGUI as sg

#sg.popup('ok')

import PySimpleGUI as sg

sg.theme('reddit')

#ou janela_principal
janela_principal = [
    [sg.Text('E-mail'),sg.Input(key='email')],
    [sg.Text('senha'),sg.Input(key='senha',password_char='*')],
    [sg.FolderBrowse('Escolher pasta anexos',target='input_anexos'),sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher pasta planilha',target='input_planilha'),sg.Input(key='input_planilha')],
    [sg.Button('Salvar')]  
]
#aqui em Layout=janela_principal
janela = sg.Window('principal',layout=janela_principal)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values['email']
        senha = values['senha']
        caminho_pasta_anexos = values['input_anexos']
        caminho_pasta_planilha = values['input_planilha']
        print(f' o e-mail digitado foi {email}')
        print(f' a senha digitado foi {senha}')
        print(f' o caminho da pasta de anexo é {caminho_pasta_anexos}')
        print(f'o caminho da pasta da pllanilha é {caminho_pasta_planilha}')