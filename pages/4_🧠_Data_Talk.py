import pandas as pd 
import streamlit as st 
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import plotly
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
import bokeh
import altair
import openai
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.chat.base import ChatAgent
from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from langchain.tools.python.tool import PythonAstREPLTool
from langchain.agents.chat.output_parser import ChatOutputParser
from langchain.agents.agent import AgentExecutor
from langchain.callbacks import StdOutCallbackHandler
from langchain.callbacks.base import BaseCallbackManager
from langchain.schema import SystemMessage
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_folium import folium_static
import json

# Page Configuration 
st.set_page_config(
    page_title= "Chat About Data",
    page_icon= "🧠"
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


st.title("Chat About Your Data 👨🏿‍💻🧠💻🤖")

robo_chat = import_json(r"lottie_files\robo_adv_chat.json")
st_lottie(robo_chat, height = 400, key = "adv_chat")
st.write("On this page, you can chat about your data with the help of GPT technology. This page combines the functionality of the chatbot and the main page. This page allows you to converse with the Language Learning Model enabling you to gain deeper data insights.")

# User Uploads a CSV File in the other page
# For new functions we must run this function again to obtain a usable dataframe 
def load_csv(input_csv):
    df = pd.read_csv(input_csv)
    
    

    # Now we need to have the user be able to preview the dataframe 
    with st.expander("See the Dataframe"):
        st.write(df)
        
    df2 = df
    
    return df2

# Collect CSV From User Here
input_file = st.file_uploader("Browse for a CSV file:", type = ["csv"])


# Loading the file for analytics 
# Note streamlit allows users to upload files however once they are utilized once the dataframe is deleted 
# This is why it is best to make a copy of the dataframe and to utilize the copy instead to prevent errors in this case it is df2.

if input_file is not None:
    dataframe = load_csv(input_file)
    
 
    # NOTE testing to see if we can get rid of these two lines of code
    input_file.seek(0)
    df = pd.read_csv(input_file, low_memory= False)
    df2 = df

    generator_ready = True
elif input_file is None: 
    st.info("Please upload a file on the above line to get started.")
    
    

key = st.text_input("Enter your API key here to enable functionality.", type = "password")


openai.api_key = key
#openai.api_key = st.text_input("Enter your API key here to enable functionality.", type = "password")


if "openai_model" not in st.session_state:
     # Test adding in Agent functionality that responds to df
    # llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key= key)
    # agent = create_pandas_dataframe_agent(llm, df, verbose= True, agent_type = AgentType.OPENAI_FUNCTIONS)
    #response = agent.run(prompt)
    
    
    
    st.session_state["openai_model"] = "gpt-3.5-turbo-0613"

# Start the Chat History 
if "messages" not in st.session_state:
    st.session_state.messages = []

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Display chat messages from history on app rerun 
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
    
#     # Test adding in Agent functionality that responds to df
#     llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key= key)
#     agent = create_pandas_dataframe_agent(llm, df, verbose= True, agent_type = AgentType.OPENAI_FUNCTIONS)
#     # Response comes later
#     #response = agent.run(prompt)
    
# if not key or not input_file:
#     st.warning("Please enter a valid OpenAI API key and a CSV to start chatting.", icon = "⚠")
# # React to user input
# prompt = st.chat_input("What is up?", disabled = not key or not input_file)
# if prompt:
#     # Display user message in chat message container 
#     response = agent.run(prompt)
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     # Add user message to chat history 
#     st.session_state.messages.append({"role": "user", "content": prompt}) 
#     # Test adding in Agent functionality that responds to df
#     llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key= key)
#     agent = create_pandas_dataframe_agent(llm, df, verbose= True, agent_type = AgentType.OPENAI_FUNCTIONS)
#     response = agent.run(prompt)
    
    
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         #full_response = ""
#         full_response = response
#         for response in openai.ChatCompletion.create(
#             model = st.session_state["openai_model"], 
            
#             messages = [
#                 {"role": m["role"], "content" : m["content"]}
#                 #{"role": m["role"], "content" : m[response]}
#                 for m in st.session_state.messages
#             ],
#             stream = True,
#         ):
#             full_response += response.choices[0].delta.get("content", "")
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     # st.session_state.messages.append({"role": "assistant", "content" : full_response})
#     # Utilize GPT That Has Access to the Dataframe
#     st.session_state.messages.append({"role": "assistant", "content" : full_response})
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# New code test 
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Test adding in Agent functionality that responds to df
# Moving these lines to be only activated if the pre-reqs are met 
# llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key=key)
# agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)


if not key or not input_file:
    st.warning("Please enter a valid OpenAI API key and a CSV to start chatting.", icon="⚠")
else:
    # Initiate Language Learning Model 
    llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key=key)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)

    # React to user input
    prompt = st.chat_input("What is up?", disabled=not key or not input_file)
    if prompt:
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get the agent's response using your agent
        response = agent.run(prompt)
        
        # Display agent response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = response
            message_placeholder.markdown(full_response + "▌")
            
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": str(m["content"])}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
                
            message_placeholder.markdown(full_response)
        
        # Add agent response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
