import FreeSimpleGUI as sg

label1=sg.Text("Select file to compress:")
textbox1 = sg.InputText()
button1 = sg.FilesBrowse("Choose")

label2=sg.Text("Select destination folder:")
textbox2 = sg.InputText()
button2 = sg.FolderBrowse("Choose")

button3 = sg.Button("Compress")


app_window = sg.Window("File Compressor",layout=[[label1,textbox1,button1],[label2,textbox2,button2],[button3]])
app_window.read()
app_window.close()
