import PySimpleGUI as sg  # sg para facilitar na chamada do PySimpleGUI

# Layout


def janela_inicial():
    sg.theme('reddit')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Limpar Tudo')]
    ]
    return sg.Window('Todo List', layout=layout, finalize=True)

# Criar janela


janela = janela_inicial()


# criar regras dessa janela

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],
                             [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Limpar Tudo':
        janela.close()
        janela = janela_inicial()
