from asyncio import events
import random
import PySimpleGUI as sg
import os
from playsound import playsound
class PassGen:
    def __init__(self):
        # Layout
        sg.theme('Black')
        playsound('Amber.mp3', block=False)
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
            sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usaário', size=(10, 1)),
            sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]            
        ]
        # Declarar janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            if event == 'Gerar Senha':
                nova_senha = self.gerar_senha(values)
                print(nova_senha)
                self.salvar_senha(nova_senha.values)

    def gerar_senha(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(values['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, values):
        with open('senhas.txt', 'a', newline='') as file:
            file.write(
                f"site: {values['site']}, usuario: {values['usuario']}, nova senha: {nova_senha}, {os.linesep}")

        print('Senha salva para o arquivo "Senhas.txt"')


gen = PassGen()
gen.Iniciar()