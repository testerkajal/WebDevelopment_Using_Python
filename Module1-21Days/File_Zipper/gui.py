import FreeSimpleGUI as sg
from zip_creator import file_compressor
import streamlit as st



label1=sg.Text("Select file to compress:")
textbox1 = sg.InputText()
button1 = sg.FilesBrowse("Choose", key = "files")

label2=sg.Text("Select destination folder:")
textbox2 = sg.InputText()
button2 = sg.FolderBrowse("Choose", key = "folder")

button3 = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")


app_window = sg.Window("File Compres sor",layout=[[label1,textbox1,button1],[label2,textbox2,button2],[button3,output_label]])

while True:
    event, values = app_window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    print(filepaths)
    file_compressor(filepaths,folder)
    app_window["output"].update("File compression is completed")






app_window.close()
