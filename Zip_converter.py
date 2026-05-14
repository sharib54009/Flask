import PySimpleGUI as sg
from sqlalchemy import values
from zip_creator_func import make_archive


label1 = sg.Text("Select files to compress : ")
input_box1 = sg.Input(tooltip="Select a zip file")
choose_button1 = sg.FileBrowse("Choose", key="file")


label2 = sg.Text("select destination folder")
input_box2 = sg.Input(tooltip="Select a zip file")
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("compress")
output = sg.Text(size=(40,1), key="output")

window = sg.Window("Zip Converter", layout=[[label1], [input_box1, choose_button1], [label2], [input_box2, choose_button2], [compress_button], [output]])


while True:

    event, values = window.read()
    filepath = values["file"].split(";")
    folder_path = values["folder"]
    make_archive(filepath, folder_path)
    window["output"].update("Files compressed successfully!")

    if event == sg.WIN_CLOSED:
        break
    if event == "compress":
        # Handle compression logic here
        pass
window.close()