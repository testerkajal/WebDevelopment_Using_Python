#streamlit lib is used to create webapps
import streamlit as st
import functions

st.title("My Todo App ")
st.subheader("This is  My Todo App ")
todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label = "", placeholder="Add new Todos..")

