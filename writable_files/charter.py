import pandas as pd 
import altair as alt #import streamlit as st 
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
import sys #df = pd.read_csv(df)
from streamlit_folium import folium_static
import streamlit as st
fig = ""
#df = pd.read_csv(r"writable_files\dataset.csv") #df = pd.read_csv(r"writable_files\dataset.csv")  # This file is being retired. It does not need anything.
# Need to Assign the df2 to df because that is the default dataframe that GPT deals with 

#Can use a downloaded file to obtain the CSV 

