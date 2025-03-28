from dotenv import load_dotenv
load_dotenv() ##loading all the environment varibles 

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##fucntion to load Gemini Pro Model and to get responses
model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_responses(input,image):
    if input!="":
     response= model.generate_content([input,image])
    else:
       response=model.generate_content(image)
    return response.text

##initialize streamlit app
st.set_page_config(page_title="Image-Responses")

st.header("PLANT-CARE:CHATBOT")
input=st.text_input("Input Prompt: ",key="input")

uploaded_file=st.file_uploader("Choose an image...", type=["jpeg","jpg","png"])
image=""
if uploaded_file is not None:
   image=Image.open(uploaded_file)
   st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the image")

##if submit is clicked
if submit:
  response=get_gemini_responses(input,image)
  st.subheader("The Response is:")
  st.write(response)