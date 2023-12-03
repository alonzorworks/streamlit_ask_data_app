import streamlit as st 
import pandas as pd 
from PIL import Image

from streamlit_lottie import st_lottie
from streamlit_folium import folium_static
import json
from PIL import Image


# Page Configuration 
st.set_page_config(
    page_title= "Project Info and Credits",
    page_icon= "ℹ"
)




#Image In Sidebar 
with st.sidebar.container():
    image = Image.open(r"images/pictures/ahead_transparent_edit2.png")  
    st.image(image, use_column_width=True)


# Import Downloaded JSON
def import_json(path):
    with open(path, "r", encoding="utf8", errors="ignore") as file:
        url = json.load(file)
        return url


st.subheader("Project Info and Credits")
st.header("Our Partner Finderr.com🧊")

snow_bear = Image.open(r"images/snowflake_bear.png")  
st.image(snow_bear, use_column_width=True)
    
    
st.write("Welcome to our project")
if st.button("Celebrate Finderr.com"):
    st.snow()

st.write("")
st.write("")


st.subheader("About The Project")
project_manager = import_json(r"lottie_files/project_manager.json")
st_lottie(project_manager, height = 400, key = "adv_chat")


import streamlit as st

# Introduction
st.write("## Project Overview")
st.write("This project showcases the power of Language Learning Models and Generative Pre-Trained Transformers.")

# Benefits of the Project
st.write("## Benefits of the Project")
st.write("This project is valuable for individuals interested in data analysis, especially those who find coding intimidating.")
st.write("### Key Benefits:")
st.write("- Simplifies data analysis without extensive coding knowledge.")
st.write("- Provides insights using well-phrased prompts and the OpenAI API key.")
st.write("- Enables users to create interactive and aesthetically pleasing data visualizations.")
st.write("- Offers the ability to interact with a 'Robo-Analyst' in a chat-like interface.")
st.write("- Enhances workflow for data analysts and empowers non-Python users to explore its functionality.")


st.header("About this app")
ahead_logo = Image.open(r"images/pictures/ahead_logo.jpg")  
st.image(ahead_logo, use_column_width=True)
    
st.write("AHEAD builds platforms for digital business. By stitching together advances in Cloud, Automation, Operations, Security and DevOps, we help clients deliver on the promise of digital transformation.")


image_credit = """
Art Generation Page =========

Technology isometric ai robot brain
Abdul Latif
https://lottiefiles.com/animations/technology-isometric-ai-robot-brain-2vX5SyCjFX


Artist
Suhayra Sarwar
https://lottiefiles.com/animations/artist-kkZHgVVmks



Robo Analytical Assistant Page ==============

Robot
KamalZeynallı
https://lottiefiles.com/animations/robot-mQU24wKXKT

Regular Chatbot Page ============

Robot Says Hi!
Irby Pace
https://lottiefiles.com/animations/robot-says-hi-4KNeuRqlcw

Data Chatbot Page ==========

Man and robot with computers sitting together in workplace
Abdul Latif
https://lottiefiles.com/animations/man-and-robot-with-computers-sitting-together-in-workplace-QnbODCGAFt


Visualizer Assistant Page ========

Artificial intelligence digital technology
Abdul Latif
https://lottiefiles.com/animations/artificial-intelligence-digital-technology-qysxvjzSuE


Web analytics
Roman
https://lottiefiles.com/animations/web-analytics-dRNRNfByqS



Credit Page ===============================================
Project Manager Stats
Usama Liaquat
https://lottiefiles.com/animations/project-manager-stats-wGHFv6Jjuy





"""

st.write("")
st.write("")

st.subheader("Image Credits")
with st.expander("Click to See Image Credits"):
    st.write(image_credit)