import pandas as pd 
import streamlit as st 
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import statistics
import plotly 
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
import bokeh


st.title("Robo-Analytical Assistant 🤖📈")
st.write("This project will show the power of utilizing Language Learning Models (LLMs) in jumpstarting data analytics.")

# Collect CSV From User Here
input_file = st.file_uploader("Browse for a file:")



# User Uploads a CSV File Here
def load_csv(input_csv):
    df = pd.read_csv(input_csv)

    # Now we need to have the user be able to preview the dataframe 
    with st.expander("See the Dataframe"):
        st.write(df)
    
    return df 


# Loading the file for analytics 
if input_file is not None:
    load_csv(input_file)
elif input_file is None: 
    st.info("Please upload a file to get started.")
    

# Generate LLM Responses 
def generate_response(csv_file, input_question):
    llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key= openai_api_key)
    
    df = load_csv(input_file)
    
    # Create a Pandas Dataframe Agent
    agent = create_pandas_dataframe_agent(llm, df, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
    
    # Perform Query using the Agent
    response = agent.run(input_query)
    return st.success(response)
    


    
    
