import PySimpleGUI as sg
import requests
import json
sg.theme('Default1')
layout = [
    [sg.Text("Digite seu CEP sem hífens ou pontos: "), sg.Input(key='cep', size=(8,1)), sg.Submit('Enviar')],
    [sg.Text("Logradouro: ")],
    [sg.Text("Bairro: ")],
    [sg.Text("Cidade: ")],
    [sg.Text("UF: ")],
    [sg.Text("DDD: ")]
]
window = sg.Window("CEP Finder", layout, icon="images/CEPFinder.ico")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    c = values['cep']
    r = requests.get('https://viacep.com.br/ws/%s/json/' % (c))
    resultado = (json.loads(r.content))
    if event == 'Enviar':
        layout = [
            [sg.Text("Digite seu CEP sem hífens ou pontos: "), sg.Input(key='cep', size=(8,1)), sg.Submit('Enviar')],
            [sg.Text("Logradouro:"),sg.InputText(resultado["logradouro"], use_readonly_for_disable=True, disabled=True)],
            [sg.Text("Bairro:"),sg.InputText(resultado["bairro"], use_readonly_for_disable=True, disabled=True)],
            [sg.Text("Cidade:"),sg.InputText(resultado["localidade"], use_readonly_for_disable=True, disabled=True)],
            [sg.Text("UF:"),sg.InputText(resultado["uf"], use_readonly_for_disable=True, disabled=True)],
            [sg.Text("DDD:"),sg.InputText(resultado["ddd"], use_readonly_for_disable=True, disabled=True)]
        ]
        window.close()
        window = sg.Window('CEP Finder', layout, icon="images/CEPFinder.ico")