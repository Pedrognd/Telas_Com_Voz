import PySimpleGUI as sg
from gtts import gTTS
from playsound import playsound


layout = [
    [
        sg.Input(key = 'cod', s=(30,1)),
        sg.Button('Enviar')
    ]
]

window = sg.Window('Chamada de Pedido', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Enviar':
        Cod = values['cod']
        audio = '(Cod).mp3'
        language = 'pt-br'

        sp = gTTS(
            text = Cod,
            lang = language
        )

        sp.save(audio)
        playsound(audio)
        break
window.close()