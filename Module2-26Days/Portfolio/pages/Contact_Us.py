import streamlit as st
from email_sender import send_email

st.set_page_config(layout="wide")
st.header("Contact-US")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your suggestions")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}"

{raw_message}
"""

    submit_button = st.form_submit_button("Submit")

if submit_button:
    send_email(message)
    st.info("Your message was sent successfully!")
