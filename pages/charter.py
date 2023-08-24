import pandas as pd #import streamlit as st 
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from visual_functions import load_csv, generate_response, other_inputs
import visual_functions as mf # The file and or its path has to be changed but the abbreviation will remain constant.
from tempfile import NamedTemporaryFile
import statistics
import plotly 
import plotly.express as px
from sklearn.linear_model import LinearRegression
import random, string
from pathlib import Path
import os
import sys #df = pd.read_csv(df)
from streamlit_folium import folium_static
from pages.z_import import df_export2
 #fig = "I am here"
df = pd.read_csv(r"pages/dataset.csv") #df = pd.read_csv(r"writable_files\dataset.csv")
# Need to Assign the df2 to df because that is the default dataframe that GPT deals with 
#Can use a downloaded file to obtain the CSV  # Tries to import the uploaded file if possible, if it is possible it is overwritten
if df_export2:
    df = pd.read_csv(df_export2)
else:
    df = df = pd.read_csv(r"pages/dataset.csv")
    