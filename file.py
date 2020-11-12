import PySimpleGUI as sg
from utils import get_meaning,get_synonyms,get_antonyms

words="Enter the word to get details\n"

layout=[
    [sg.Multiline(words, font=("Arial", 14), size=(70,15),key='output')],
    [sg.InputText("",font=("Arial",14),size=(50,1),key='input')],
    [sg.Button("Meaning",font=("Arial",14),key='meaning'),
    sg.Button("Synonyms",font=("Arial",14),key='synonyms'),
    sg.Button("Antonyms",font=("Arial",14),key='antonyms'),
    sg.Button("Clear",font=("Arial",14),key='clear')
    ]
]

def display_meaning(word):
    meaning=get_meaning(word)
    window['output'].print("WORD:",word)
    if meaning:
        window['output'].print("MEANING: ",meaning)
    else:
        display_error("Word is not found in corpus")

def display_error(message):
    window['output'].print("ERROR: "+message,text_color='red')

def display_synonyms(word):
    synonyms=get_synonyms(word)
    window['output'].print("WORD:",word)
    if synonyms:
        window['output'].print("SYNONYMS: ",synonyms)
    else:
        display_error("Word is not found in corpus")

def display_antonyms(word):
    antonyms=get_antonyms(word)
    window['output'].print("WORD:",word)
    if antonyms:
        window['output'].print("SYNONYMS: ",antonyms)
    else:
        display_error("Word is not found in corpus")

def clear_windows():
    window['output'].Update(words)
    window['input'].Update('')

window=sg.Window("week1",layout)


while True:
    event,values=window.Read()
    if event==sg.WINDOW_CLOSED:
        break
    elif event=="meaning":
        display_meaning(values['input'])
    elif event=="synonyms":
        display_synonyms(values['input'])
    elif event=="antonyms":
        display_antonyms(values['input'])
    elif event=="clear":
        clear_windows()

window.Close()
