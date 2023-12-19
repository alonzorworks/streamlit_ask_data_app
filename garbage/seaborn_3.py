import pandas as pd 
import streamlit as st 
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from my_functions import load_csv, generate_response, other_inputs
import my_functions as mf 
from tempfile import NamedTemporaryFile
import statistics
import plotly 
import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
import bokeh
import altair
import seaborn as sns


# Functions: will be having the files here for this page because it is easier to manage and Seaborn is more simplistic ===========================================================
# User Uploads a CSV File in the other page
# For new functions we must run this function again to obtain a usable dataframe 
def load_csv(input_csv):
    df = pd.read_csv(input_csv)
    
    

    # Now we need to have the user be able to preview the dataframe 
    with st.expander("See the Dataframe"):
        st.write(df)
        
    df2 = df
    
    return df2

# Generate LLM Responses 
def generate_response(csv_file, input_query, ai_key): #input_question, question_list):
    llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2, openai_api_key= ai_key)
    
    df = csv_file
    
    # Create Pandas Dataframe Agent 
    agent = create_pandas_dataframe_agent(llm, df, verbose= True, agent_type = AgentType.OPENAI_FUNCTIONS)
    
    # Perform Queries with the agent 
    response = agent.run(input_query)
    
    return st.success(response)
    


# Other Inputs 
def other_inputs(list_of_questions, input_file_csv):
    """Add an additional question etc."""
    question_list = list_of_questions
    input_file = input_file_csv
    
    #Select the question.
    #query_text = st.selectbox("Select an example query:", question_list, disabled= not input_file)
    query_text = st.selectbox("Select an example query:", question_list, disabled= input_file.empty)
    
    # openai_api_key = st.text_input("OpenAI API Key", type = "password", disabled = not (input_file and query_text))
    openai_api_key = st.text_input("OpenAI API Key", type = "password", disabled = not (query_text) and input_file.empty)
    
    # Dealing with other questions and verifying API key
    if query_text is "Other":
        # query_text = st.text_input("Enter your query", placeholder= "Enter your query...", disabled = not input_file)
        st.info("Enter in your custom question below. Leavng the line blank will result in the LLM interpreting your dataset's columns." ,icon = "ℹ")
        query_text_custom = st.text_area("Enter your query", placeholder= "Enter your query...", disabled = input_file.empty)
        st.header("Output")
        return generate_response(input_file, query_text_custom, openai_api_key)
    
    # Instead we need to call the function provided by the SeabornAI plugin that we had to put in here manually:
    #return generate_graph(data = input_file, prompt = query_text_custom , style= chosen_theme, size=(x_number, y_number))
    
        
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key to enable functionality!", icon = "⚠")
    if openai_api_key.startswith("sk-") and (input_file is not None):
        st.header("Output")
        return generate_response(input_file, query_text, openai_api_key)

# ====================================================================================================================================================================

# EXTERNAL Functions +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Code provided by a package called seabornai 
# Pasting and modifying the code manually because importing it does not seem to work 
# See original code: https://github.com/aditya0072001/seabornai/blob/main/seabornai/seabornai.py

def set_openai_api_key(api_key):
    openai.api_key = api_key

def generate_graph(data = input_file, prompt = query_text_custom , style= chosen_theme, size=(x_number, y_number)):
    """A modified version of the provided SeabornAI code. The modifications will make the plugin play nicely with Streamlit and our code. Will replace default values from generate responses for consistency."""
    # We already have an OpenAI key verified in our own function 
    # if not openai.api_key:
    #     raise ValueError("OpenAI API key not set. Please use `set_openai_api_key` function to set the API key.")
    
    # Use the OpenAI ChatGPT API to generate a response based on the prompt/question
    response = openai.Completion.create(
        engine="davinci",  # Choose the appropriate GPT-3 model
        prompt=prompt,
        max_tokens=100,  # Adjust this based on the desired response length
        n=1,  # Number of responses to generate
        stop=None,  # Stop generating responses at a custom token
    )
    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()

    # Generate a Seaborn graph based on the supplied data and the generated text
    sns.set(style=style)
    sns.set(rc={"figure.figsize": size})
    # Use Seaborn plotting functions here to create the desired graph
    # For example:
    sns.barplot(data=data, x="x_column", y="y_column")
    sns.despine()

    # Show the graph
    sns.plt.show()
    return st.pyplot(sns.plt)
    
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Variables 
# Will only have other be a choice to generate custom 
question_list = ["Other"]

seaborn_themes = [
    "darkgrid",
    "whitegrid",
    "dark",
    "white",
    "ticks"
]




st.title("Seaborn Visualization 🌊")
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
    
    # Choose the size of the visualization 
    st.subheader("Chose Your Visual's Dimensions 📏")
    col_x, col_y = st.columns(2)
    with col_x:
        x_number = st.number_input("Insert size for the X-axis.", value= 5, step= 1)
    with col_y:
        y_number = st.number_input("Insert size for the y-axis.", value = 5, step= 1)


    dimension_announce = "Dimensions"

    st.write(f"Your X size in inches is: :green[{x_number}].", f"Your Y size in inches is: :green[{y_number}]", f":blue[{dimension_announce}](:green[{x_number}],:green[{y_number}])")

    chosen_theme = st.selectbox("What Seaborn Theme would you like to use?", options = seaborn_themes)

    
 
    # NOTE testing to see if we can get rid of these two lines of code
    input_file.seek(0)
    df = pd.read_csv(input_file, low_memory= False)
    df2 = df
    
    generator_ready = True
elif input_file is None: 
    st.info("Please upload a file on the above line to get started.")
    

# NOTE the necessary function is embedded in the previous if statement and is triggered once the file is uploaded.
# The uploading the file modifies the boolean and renders it true, allowing the next code to proceed without throwing an error.

if generator_ready is True:
    other_inputs(question_list, df2)
#other_inputs(question_list, f.name)














# Choose the size of the visualization 
# st.subheader("Chose Your Visual's Dimensions 📏")
# col_x, col_y = st.columns(2)
# with col_x:
#     x_number = st.number_input("Insert size for the X-axis.", value= 5, step= 1)
# with col_y:
#     y_number = st.number_input("Insert size for the y-axis.", value = 5, step= 1)


# dimension_announce = "Dimensions"

# st.write(f"Your X size in inches is: :green[{x_number}].", f"Your Y size in inches is: :green[{y_number}]", f":blue[{dimension_announce}](:green[{x_number}],:green[{y_number}])")

# chosen_theme = st.selectbox("What Seaborn Theme would you like to use?", options = seaborn_themes)
