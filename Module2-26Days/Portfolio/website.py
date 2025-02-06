import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    test=st.image("./Images/profile.jpeg", width = 600)
    print(test)
with col2:
    st.title("Kajal Chaudhary")
    content = """I am Kajal, a skilled software tester with 7 years of experience in ensuring high-quality software solutions. "
               "My expertise lies in test automation, functional testing, and performance testing, ensuring seamless user experiences and robust application performance. With a keen eye for detail and a passion for quality assurance, I have successfully contributed to multiple projects across various domains."""
    st.info(content)

