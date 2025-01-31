import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")

app_window = sg.Window('My To Do App', layout = [[label],[input_box,add_button]])
app_window.read()
app_window.close()









