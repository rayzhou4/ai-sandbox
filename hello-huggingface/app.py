from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.callbacks.tracers import ConsoleCallbackHandler
import requests
import os
import streamlit as st

load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# img2text (used Huggingface through transformers)
def img2text(url):
  image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
  
  text = image_to_text(url)[0]['generated_text']
  
  print(text)
  return text

# llm (used LangChain)
def generate_story(scenario):
  template="""
  You are a story teller;
  You can generate a short story based on a simple narrative, the story should be no more than 50 words;
  
  CONTEXT: {scenario}
  STORY:
  """
  
  prompt = PromptTemplate(template=template, input_variables=["scenario"])
  model = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=1)
  output_parser = StrOutputParser()
  
  chain = prompt | model | output_parser
  
  story = chain.invoke({"scenario": scenario}, config={'callbacks': [ConsoleCallbackHandler()]}) # ConsoleCallbackHandler() for verbosity (you can see what happens in the chain!!)
  
  print(story)
  return story

# text to speech (used Huggingface's inference API)
def text2speech(message):
  API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
  headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
  payloads = {
    "inputs": message
  }
  
  response = requests.post(API_URL, headers=headers, json=payloads)
    
  with open('audio.flac', 'wb') as file:
    file.write(response.content)

# main function
def main():    
  st.set_page_config(page_title='img 2 audio story', page_icon="🦆")

  st.header("Turn an image into an audio story!")
  uploaded_file = st.file_uploader("choose an image...", type=["jpg","png"])
  
  if uploaded_file is not None:
    print(uploaded_file)
    bytes_data = uploaded_file.getvalue()
    with open(uploaded_file.name, 'wb') as file:
      file.write(bytes_data)
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    scenario = img2text(uploaded_file.name)
    story = generate_story(scenario)
    text2speech(story)
    
    with st.expander("scenario"):
      st.write(scenario)
    with st.expander("story"):
      st.write(story)
      
    st.audio("audio.flac")

if __name__ == '__main__':
  main()