import functions
import FreeSimpleGUI as sg  # ✅ Corrected import

# GUI Layout
label = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip="Enter Todo", key="Todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values=functions.get_todos() or [], key='todos',
                      enable_events=True, size=(45, 10))

app_window = sg.Window('My To Do App', layout=[[label], [input_box, add_button], [list_box, edit_button],[complete_button,exit_button]],
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
                app_window["todos"].update(values=todos)  # ✅ Update Listbox

        case "Edit":
            if not value["todos"]:  # ✅ Prevent IndexError
                continue

            todo_to_edit = value["todos"][0]  # ✅ Fix undefined values
            new_todo = value["Todo"].strip()  # ✅ Use correct input key

            if new_todo:
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.modify_todos(todos)
                app_window["todos"].update(values=todos) # ✅ Update Listbox
                app_window['Todo'].update('') # ✅ Update Input box
        case "Complete":
                if not value["todos"]:  # ✅ Prevent IndexError
                    continue

                todo_to_complete = value["todos"][0]# ✅ Fix undefined values
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.modify_todos(todos)
                app_window['todos'].update(values = todos)
                app_window['Todo'].update('')
        case "Exit":
              break



app_window.close()  # ✅ Close window after exiting loop
