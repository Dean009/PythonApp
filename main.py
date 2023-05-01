import PySimpleGUI as sg
import sys


import PySimpleGUI as psg
menu_def = [['File', ['New', 'Open', 'Save', 'Exit', ]], ['Edit', ['Cut', 'Copy', 'Paste', 'Undo'], ],  ['Help', 'About...'], ]
layout = [[psg.Menu(menu_def)],
   [psg.Multiline("", key='-IN-',
   expand_x=True, expand_y=True)],
   [psg.Multiline("", key='-OUT-',
   expand_x=True, expand_y=True)],
   [psg.Text("", key='-TXT-',
   expand_x=True, font=("Arial Bold", 14))]
]
window = psg.Window("Menu", layout, size=(715, 300))
while True:
   event, values = window.read()
   print(event, values)

   if event != psg.WIN_CLOSED:
      window['-TXT-'].update(values[0] + "Menu Button Clicked")
   if event == 'Copy':
      txt = window['-IN-'].get()
   if event == 'Paste':
      window['-OUT-'].update(value=txt)
   if event == psg.WIN_CLOSED:
      break
      
window.close()


