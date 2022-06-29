import PySimpleGUI as sg
from gtts import gTTS
from playsound import playsound

layout = [
    [
        sg.Input(key = 'cod', s=(30,1)),
        sg.Button('Enviar'), sg.Button('Nova Chamada')
        ]
]
TelaCod = sg.Window('Codigo Pedido', layout)

while True:
    event, values = TelaCod.read()
    if event == sg.WIN_CLOSED:
        break 
    if event == 'Enviar':
        Cod = values['cod']
        layout2 = [
            [
                sg.Listbox(values=[Cod], no_scrollbar=True, size=(100,30))
            ]
        ]
        TelaChamada = sg.Window('Chamada Pedido', layout2)

        audio = '(Cod).mp3'
        language = 'pt-br'

        sp = gTTS(
            text = Cod,
            lang = language
        )

        sp.save(audio)
        playsound(audio)

        event, values = TelaChamada.read()

        
        break
    teste = values['cod']
TelaCod.close()