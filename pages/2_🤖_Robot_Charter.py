import pandas as pd 
import streamlit as st 
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from visual_functions import load_csv, generate_response, other_inputs
import visual_functions as mf # The file and or its path has to be changed but the abbreviation will remain constant.
from tempfile import NamedTemporaryFile
import statistics
import plotly 
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
import bokeh
import altair
from streamlit_ace import st_ace
import random, string
from pathlib import Path
import os
import sys 
from streamlit_folium import folium_static
import seaborn as sns
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_folium import folium_static
import json

# Page Configuration 
st.set_page_config(
    page_title= "GPT Data Visualizer",
    page_icon= "📈"
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



# Here we get the system ready to take in the file where the code instructions will be written
# No more need for writable files folder 
#sys.path.insert(0, r"writable_files")



# Original Name 
# 2_🐼_Robo_Charter

# Here we get the system ready to take in the file where the code instructions will be written
# sys.path.insert(0, "writable_files")

# From Writab


#import charter

# Documentation  https://platform.openai.com/docs/api-reference/fine-tunes/create?lang=python

# Todo list
# See how he gets more outputs for llms
# Create a plotting page for charts 
# Create a mapping page 
# Create an illustration page



# We will use this to satiate the other inputs function.
question_list = ["Other"]

# question_list = [
#     "How many rows are in this dataset?",
#     "How many columns are in this dataset?",
#     "Other"
# ]



st.title("Robo-Visualizer Assistant 🤖📈")

col1, col2 = st.columns(2)

with col1:
    powerful_bot = import_json(r"lottie_files/powerful_robot.json")
    st_lottie(powerful_bot, height = 400, key = "power_bot")
with col2:
    analytics_bot = import_json(r"lottie_files/robo_analytics.json")
    st_lottie(analytics_bot, height = 400, key = "analytics_bot")

st.caption("In this page we use Language Learning Models to help us create visualizations.")


st.write("""This page is dedicated to enabling people to make visualizations in a Python application named Plotly. ChatGPT is very good at creating robust code as long as the prompt is clearly defined. In order to ensure that the output has the maximum chance of running successfully follow these steps.
         """)


st.markdown(
"""
Tips for making a successful query:
- Make sure that you mention that you want Python Plotly Code!
- Familiarize yourself with the dataset and use specific column names verbatim if possible.
- Give clear instructions. Only make one view at a time. 
- If you make a visual that you like go to the upper right hand corner of it and save it.
- Follow other instructions and tips that are given below.
"""
)

st.write("")
st.write("")

# ====================================================================================================================
# # Collect CSV From User Here
# input_file = st.file_uploader("Browse for a CSV file:", type = ["csv"])



# # This Boolean stops the generate_response line from breaking.
# # We will see that the llm generator will only become ready when the df is both loaded and configured.
# generator_ready = False


# # Loading the file for analytics 
# # Note streamlit allows users to upload files however once they are utilized once the dataframe is deleted 
# # This is why it is best to make a copy of the dataframe and to utilize the copy instead to prevent errors in this case it is df2.

# if input_file is not None:
#     dataframe = load_csv(input_file)
    
 
#     # NOTE testing to see if we can get rid of these two lines of code
#     input_file.seek(0)
#     df = pd.read_csv(input_file, low_memory= False)
#     df2 = df

#     generator_ready = True
# elif input_file is None: 
#     st.info("Please upload a file on the above line to get started.")
    

# # NOTE the necessary function is embedded in the previous if statement and is triggered once the file is uploaded.
# # The uploading the file modifies the boolean and renders it true, allowing the next code to proceed without throwing an error.

# if generator_ready is True:
#     other_inputs(question_list, df2)
# #other_inputs(question_list, f.name)
#=====================================================================================================================

# Collect CSV From User Here
input_file = st.file_uploader("Browse for a CSV file:", type = ["csv"])





# This Boolean stops the generate_response line from breaking.
# We will see that the llm generator will only become ready when the df is both loaded and configured.
generator_ready = False


# Loading the file for analytics 
# Note streamlit allows users to upload files however once they are utilized once the dataframe is deleted 
# This is why it is best to make a copy of the dataframe and to utilize the copy instead to prevent errors in this case it is df2.

if input_file is not None:
    dataframe = load_csv(input_file)
    
 
    # NOTE testing to see if we can get rid of these two lines of code
    input_file.seek(0)
    df = pd.read_csv(input_file, low_memory= False)
    df2 = df
    
    # Will save the df file to the external folder 
    #filepath = Path(r"writable_files/dataset.csv")
    #filepath = Path(r"dataset.csv")
    filepath = Path(r"pages\dataset.csv")
    df2.to_csv(filepath, index= False)
    
    

    generator_ready = True
elif input_file is None: 
    st.info("Please upload a file on the above line to get started.")
    

# NOTE the necessary function is embedded in the previous if statement and is triggered once the file is uploaded.
# The uploading the file modifies the boolean and renders it true, allowing the next code to proceed without throwing an error.

if generator_ready is True:
    other_inputs(question_list, df2)
#other_inputs(question_list, f.name)





# Coding in Streamlit to make visualizations ===========================================================================================

# Add a temporary file for the code that is inputted 
# First we need a file name this will be randomized so the user won't have to name the file

# def generate_file(code_viz):
#     # file_name = "".join(random.choices(string.ascii_letters + strings.digits, k = 8))
#     path = "writable_files/charter.py"
#     with open(path, "w",) as f:
        
#         #f = open(path, "rU")
        
#         # Delete the file's contents before we get started.
#         f.truncate(0)
        
#         f.write(code_viz)
        
        
    # Now we can load in the file 

# ======================================================================================================================================

def generate_file(code_viz, start_line):
    #path = r"writable_files/charter.py"
    #path = r"charter.py"
    path = r"pages/charter.py"
    with open(path, "r") as f:
        lines = f.readlines()

    with open(path, "w") as f:
        for line_number, line in enumerate(lines, start=1):
            if line_number < start_line:
                f.write(line)
        
        f.write(code_viz)
    
    
    



col1, col2, col3 = st.tabs(["Edit Code", "See Formatted Code", "Preview File"])

with col1:
    st.subheader("Paste Plotly Code from GPT code here.")
    st.warning("Need a CSV file AND a valid OpenAI key in order to function.", icon = "⚠")
    code_viz = st.text_area("Enter in code. Make sure the final plot that you want to display is stored in a variable called 'fig'.")
    
with col2:
    st.subheader("See formatted code")
    st.write("Remember you will have to go to the previous tab to edit the code. You can edit this code but the streamlit text area takes precedent.")
    ace_code = st_ace(code_viz)
    #ace_code
with col3:
    st.info("Previews the actual remote file. Nothing will show if nothing is submitted via the button.", icon = "ℹ")
    st.info("Big text is normal. Python comments indicated by '#' tells Markdown to make text bigger. There is no issue.", icon = "✅")
    # Test 
    # First let us see if we can read the file
    #test_path = r"writable_files/charter.py"
    #test_path = r"charter.py" 
    test_path = r"pages/charter.py"
    with open(test_path, "r") as file:
        file_contents = file.read()
        st.write(file_contents)

st.button("Click Here to Write Code", on_click= generate_file(code_viz, 30))

st.info("Plotly has a lot of functionality. Familiarizing yourself with documentation is always prudent.", icon = "ℹ")
#st.info("Note that for mapmaking packages Folium and Pydeck you will need latitude and longitude. Familiarizing yourself with documentation is advised.", icon = "ℹ")
#st.warning("For the map making packages you will have to tell GPT that you will need the final map to be labeled as fig in order to make the code work.", icon = "🚨")

# package_library = st.radio("Pick which package to run your code.",
#                            ("Plotly"))        #("Plotly", "Matplotlib", "Altair", "Bokeh", "sklearn", "Folium", "PyDeck", "Seaborn"))

package_library = "Plotly"

# KEEP: Having Import Outside of the function =================================================
# Below are the old set: we are phasing these out 
#from writable_files.charter import fig
# from charter import fig # This line was already commented out the real two usable lines are the ones above and below
#from writable_files import charter as ch

# =============================================================================================

# Need New Sets of Imports These are the local files that are in pages and NOT in writable files
import charter as ch
from charter import fig
#import charter as ch
    
#fig2 = charter.fig
fig2 = ch.fig
# =================================================================


# from writable_files import charter

def plot_chart(package_library = package_library):
    """Let's users select which Python package they want to use. Unfortunately only plotly will be supported either because
    the other packages don't work. Or they do not work often enough."""
    # try:
    #     from charter import fig
    # except ImportError:
    #     st.error("Make sure that your code has a variable of your desired graph called 'fig'.")
    # finally:
    
    #from writable_files.charter import fig
    # from charter import fig
    #from writable_files import charter as ch
    
    #fig2 = charter.fig
    #fig = ch.fig
        
    if package_library == "Plotly":
        #plotly_plot = st.plotly_chart(fig, use_container_width= True)
        #st.title("Oh yeah")
        return st.plotly_chart(fig, use_container_width= True)
    # if package_library == "Matplotlib":
    #     matlib_plot =  st.pyplot(fig, use_container_width= True)
    #     return matlib_plot
    # if package_library == "Altair":
    #     altair_chart = st.altair_chart(fig, use_container_width= True)
    #     return altair_chart
    # if package_library == "Bokeh":
    #     bokeh_chart = st.bokeh_chart(fig, use_container_width= True)
        #return bokeh_chart
    # if package_library == "Folium":
    #     folium_chart = folium_static(fig)
    #     return folium_chart
    # if package_library == "PyDeck":
    #     py_deck_map = st.pydeck_chart(fig)
    #     return py_deck_map
    # if package_library == "Seaborn":
    #     sns_chart = st.pyplot(fig.get_figure())
    #     return st.pyplot (sns_chart)
        
        
        
        
        
        # try:
        #     st.plotly_chart(fig, use_container_width= True)
        # except NameError:
        #     df = input_file


    
# NOTE Need a way to import the dataframe df2 into the charter file, overwrite everything except the first line that imports the df

#st.button("Click Here to Write Code", on_click= generate_file(code_viz))

# Streamlit has a particulate way to call a function on click. You must name the function and provide the arguments separately using onclick and args
#st.button("Click to visualize.", on_click= plot_chart)

# Retrying the code to make the button work.
# This does work. Streamlit buttons do not directly call functions. So we use an if statement. 
# if st.button("Click to Visualize"):
#     plot_chart(package_library)


if st.button("Make Plot Visualization"):
    plot_chart(package_library)



#plot_chart(package_library= package_library)


# Now with the code entered we need to do several things 
# Write a file with the content from the code_viz instructions after pressing a button (the button comes later)
# Import the file into this project 
# Allow users to pick a package of choice to display the visualization 
# The button press will show the figure in Streamlit 
# In the function that is called when the button is pressed it should return fig which can be assigned a variable, with fig we should be able to combine it with the radio button and use st_plotly or whatever to graph it 


 


#st.plotly_chart(plotly_code , use_container_width= True)


   
   

# Already Implemented 

# Test 
# First let us see if we can read the file
# test_path = "writable_files/charter.py"
# with open(test_path, "r") as file:
#     file_contents = file.read()

# st.write(file_contents)
