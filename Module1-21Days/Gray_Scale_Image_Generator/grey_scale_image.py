import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    #start the camera
    capture_image = st.camera_input("Camera")

if capture_image:
    #create a Pillow Image instance
    img = Image.open(capture_image)
    #convert pillow image to grey scale image
    grey_img = img.convert("L")
    #display greyscale image on the webpage
    st.image(grey_img)