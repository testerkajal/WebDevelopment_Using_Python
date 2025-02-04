def get_todos(filepath="Todos.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # this will return a list
    return todos_local

def modify_todos(todos_arg, filepath="Todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # this will return a list

def modify_todos(todos_arg, filepath="Todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # this will return a list
