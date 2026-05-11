import PySimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")


window = sg.Window("My TO-DO App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
