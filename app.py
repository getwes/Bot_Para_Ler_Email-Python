# Qual biblioteca python PysimpleGUI
# pip install pysimplegui

#Fazer toda configuração PysimpleGUI
#import PySimpleGUI as sg

#sg.popup('ok')

import PySimpleGUI as sg

sg.theme('reddit')

layout = [
    [sg.Text('E-mail'),sg.Input(key='email')],
    [sg.Text('senha'),sg.Input(key='senha', password_char='*')],
    [sg.FolderBrowse('Escolher pasta anexos' , targuet='input_anexos'),sg.Input(key='input_anexos')],
    [sg.FolderBrowse('Escolher pasta planilha' , targuet='input_planilha'),sg.Input(key='input_planilha')],
    [sg.button('Salvar')]  
]

