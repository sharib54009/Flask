import PySimpleGUI as sg

label1 = sg.Text("Select files to compress : ")
input_box1 = sg.Input(tooltip="Select a zip file")
choose_button1 = sg.FileBrowse("Choose")


label2 = sg.Text("select destination folder")
input_box2 = sg.Input(tooltip="Select a zip file")
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("compress")

window = sg.Window("Zip Converter", layout=[[label1], [input_box1, choose_button1], [label2], [input_box2, choose_button2], [compress_button]])

window.read()
window.close()