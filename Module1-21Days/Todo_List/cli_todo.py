import functions


while True:
     user_prompt = input("Enter add, exit,edit  or show: ").strip()

     if user_prompt.startswith("add"):
        #using slicing to remove add part from the user prompt
        todo = user_prompt[4:]

        #to prevent the overwrite of old todos with new todos, first we are reading the existing todos in the file
        todos = functions.get_todos()

        #here we are appending new todos in the same list
        todos.append(todo + '\n')

        #open file and write the content
        functions.modify_todos(todos)

     elif  user_prompt.startswith("show"):

         todos = functions.get_todos()

         # now iterate over the new_todos list to show the items
         for index, item in enumerate(todos): #enumerate iterate over the list and keeps item with its index
             item = item.strip('\n')
             print(f"{index+1}-{item}")

     elif  user_prompt.startswith("edit"):
         try:
             number  =  int(user_prompt[5:])
             number = number-1

             todos = functions.get_todos()

             new_todo = input("Enter new Todo: ")
             todos[number] = new_todo + '\n'

             functions.modify_todos(todos)
         except ValueError:
             print("You entered an invalid command")
             continue

     elif  user_prompt.startswith("complete"):
         try:
             number = int(user_prompt[9:])
             number = number-1

             todos = functions.get_todos()

             item_to_remove = todos.pop(number - 1)

             functions.modify_todos(todos)

             message  = f"Todo {item_to_remove}is remove from the todos list"
             print(message)
         except IndexError:
             print("There is no item with this number")
             continue

     elif "exit"in user_prompt:
         break
     else:
         print("Entered wrong input")


