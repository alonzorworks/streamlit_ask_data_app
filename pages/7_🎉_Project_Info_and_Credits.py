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
st.header("Our Partner Snowflake 🌨🧊❄")

snow_bear = Image.open(r"images/snowflake_bear.png")  
st.image(snow_bear, use_column_width=True)
    
    
st.write("AHEAD is a proud partner of Snowflake a premier cloud data warehousing platform. This project was made possible by Snowflake's Streamlit a free Python library that enables interactive data web applications.")
if st.button("Celebrate Snowflake"):
    st.snow()

st.write("")
st.write("")


st.subheader("About The Project")
project_manager = import_json(r"lottie_files/project_manager.json")
st_lottie(project_manager, height = 400, key = "adv_chat")


st.write("This project was made to showcase the power of Language Learning Models and Generative Pre-Trained Transformers. ")

st.write("""
This project can be very useful to anyone who is curious about Data Analysis. Python is considered to be one of the easiest programming languages to learn. However, many people around the world find coding to be very difficult and intimidating. Indeed, learning to code can be a daunting task. Even some skilled data analysts try to avoid coding for as long as they can.
         
         """)



st.write("""
         This project helps level the playing field. While knowing how to code is always a boon, this app enables people to gain insights into data with simply a well-phrased prompt and OpenAI API key. This app also enables users to create interactive data visualizations that are as aesthetically pleasing as they are edifying. This application also enables its users to converse with a “Robo-Analyst” who is apt to respond to further questioning in a chat-like interface.
         
         """)

st.write("""
         From expediting a data analyst’s workflow to enabling a non-Python user to explore its functionality, this application has something for everyone. 
         
         """)


st.header("About AHEAD")
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