import streamlit as st 
import openai
import os 
from PIL import Image
import requests
from io import BytesIO
from streamlit_lottie import st_lottie
from streamlit_folium import folium_static
import json

# Page Configuration 
st.set_page_config(
    page_title= "Art Generator",
    page_icon= "🎨"
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


st.title("Automatic Image Generation")

col1, col2 = st.columns(2)

with col1:
    ai_brain_scan = import_json(r"lottie_files/robo_brain.json")
    st_lottie(ai_brain_scan, height = 400, key = "brain_scan")

with col2:
    pot_sculptor = import_json(r"lottie_files/pot_sculpter.json")
    st_lottie(pot_sculptor, height = 400, key = "sculptor")

st.write("Artificial intelligence can be used to generate images that derive from conventionally created art by artists. Use this page to turn your prompt into (potentially) beautiful art that you can right click and download.")

image_sizes = ["256x256", "512x512", "1024x1024"]

key = st.text_input("Enter your API key here to enable functionality.", type = "password")
openai_api_key = key


if not key:
    #st.warning("Please enter a valid OpenAI API key to start chatting.", icon = "⚠")
    pass
if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key to enable functionality!", icon = "⚠")

    


chosen_size = st.selectbox("Choose image dimensions.", image_sizes)

    
    
query_text_custom = st.text_area("Describe your ideal image.", placeholder= "An image will be generated to your liking...", disabled = not openai_api_key)


# response = openai.Image.create(
#     prompt = query_text_custom,
#     n = 1, 
#     size = chosen_size
# )

def image_generation(prompt = query_text_custom, size = chosen_size):
    res = openai.Image.create(
        # Only one image will be generated to keep it simple
        prompt = prompt,
        n = 1,
        size = size
    )
    
    final_image = res["data"][0]["url"]
    
    render_image = requests.get(final_image)
    
    #return Image.open(render_image.raw)
    return Image.open(BytesIO(render_image.content))

st.warning("If you see an image that you like save it immediately. Even with the same prompt you will likely not get the same image again.", icon = "⚠")

if st.button("Generate Image"):
    #image_generation()
    generated_image = image_generation(query_text_custom, chosen_size)
    st.image(generated_image, caption= query_text_custom, use_column_width=True)



# image_formatted = response["data"][0]["url"]

# st.image(response)