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