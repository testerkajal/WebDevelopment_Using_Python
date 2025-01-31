import functions
import FreeSimpleGUI as sg  # ✅ Corrected import

# GUI Layout
label = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip="Enter Todo", key="Todo")
add_button = sg.Button("Add")

app_window = sg.Window('My To Do App', layout=[[label], [input_box, add_button]],
                       font=("Helvetica", 16), background_color="black")

# Event Loop
while True:
    event, value = app_window.read()
    print(event, value)

    if event == sg.WIN_CLOSED:  # ✅ Proper exit condition
        break

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value.get("Todo", "").strip()  # ✅ Prevent KeyError and remove extra spaces
            if new_todo:  # ✅ Only add if input is not empty
                todos.append(new_todo + "\n")
                functions.modify_todos(todos)

app_window.close()  # ✅ Close window after exiting loop
