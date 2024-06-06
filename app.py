# Qual biblioteca python PysimpleGUI
# pip install pysimplegui

#Fazer toda configuração PysimpleGUI
#import PySimpleGUI as sg

#sg.popup('ok')

import PySimpleGUI as sg

sg.theme('reddit')

layout = [
    [sg.Text('E-mail'),sg.Input(key='email')],
    [],
    [],
    [],
    []  
]