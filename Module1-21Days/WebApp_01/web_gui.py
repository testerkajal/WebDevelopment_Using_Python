# Import required libraries
import streamlit as st

import functions



# Function to add a new todo
def add_todo():
    input_todo = st.session_state["new_todo"].strip()
    if input_todo:  # Avoid empty todos
        todos.append(input_todo + "\n")
        functions.modify_todos(todos)
        st.session_state["new_todo"] = ""  # Clear input field


# Streamlit App UI
st.title("My Todo App")
st.write("This app is to boost your <b>productivity.</b>",unsafe_allow_html=True)
st.text_input(label="", placeholder="Add new Todos...", on_change=add_todo, key="new_todo")

# Load existing todos
todos = functions.get_todos()

# Track completed todos
completed_todos = [] 

# Display todos with checkboxes
for todo in todos:
    if st.checkbox(todo, key=todo):  # Use todo as the key (ensures uniqueness)
        completed_todos.append(todo)

# Remove completed todos
if completed_todos:
    todos = [todo for todo in todos if todo not in completed_todos]  # Remove completed items
    functions.modify_todos(todos)  # Update stored todos
    st.rerun()  # Refresh the app to reflect changes


