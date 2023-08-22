import streamlit as st 
import openai 
import pandas as pd 
from streamlit_lottie import st_lottie
from streamlit_folium import folium_static
import json
from PIL import Image


# Page Configuration 
st.set_page_config(
    page_title= "GPT Chatbot",
    page_icon= "😃"
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

    
st.title("Private GPT Space")

hi_robot = import_json(r"lottie_files\hi_robot.json")
st_lottie(hi_robot, height= 400, key = "hey_robot")

st.write("Users can use this page to ask ChatGPT general questions. This can be a viable space to use when the ChatGPT is unavailable but someone has a OpenAI key to use.")

key = st.text_input("Enter your API key here to enable functionality.", type = "password")
openai.api_key = key
#openai.api_key = st.text_input("Enter your API key here to enable functionality.", type = "password")


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo-0613"

# Start the Chat History 
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
if not key:
    st.warning("Please enter a valid OpenAI API key to start chatting.", icon = "⚠")
# React to user input
prompt = st.chat_input("What is up?", disabled = not key)
if prompt:
    # Display user message in chat message container 
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history 
    st.session_state.messages.append({"role": "user", "content": prompt}) 
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model = st.session_state["openai_model"],
            messages = [
                {"role": m["role"], "content" : m["content"]}
                for m in st.session_state.messages
            ],
            stream = True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content" : full_response})
        
    
    
    