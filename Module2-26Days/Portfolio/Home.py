import streamlit as st
from dateutil.utils import within_delta
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    test=st.image("./Images/profile.jpeg", width = 400)
    print(test)
with col2:
    st.title("Kajal Chaudhary")
    content = """I am Kajal, a skilled software tester with 7 years of experience in ensuring high-quality software solutions. "
               "My expertise lies in test automation, functional testing, and performance testing, 
               ensuring seamless user experiences and robust application performance. 
               With a keen eye for detail and a passion for quality assurance, 
               I have successfully contributed to multiple projects across various domains."""
    st.info(content)

content2 = """Below you can find some of the apps, I have built in python. Feel free to contact me."""

st.write(content2  )

col3, col4 = st.columns(2)

df  = pandas.read_csv("data.csv", sep = ";")
with col3:
    for index, row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("./Images/" + row["image"],width=250)
        #st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[2:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("./Images/" + row["image"],width=400)



