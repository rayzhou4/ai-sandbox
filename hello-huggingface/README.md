# 🦆 Hello-Huggingface (Img2AudioStory)
Click [here](https://img-to-audiostory.streamlit.app/) for deployment link
### Learning Objectives
I created a simple AI application to learn more about utilizing basic AI tools including:
- HuggingFace's Transformers and Inference API methods, 
- LangChain and,
- Streamlit.

### Purpose
It converts and image into an audio story!

### How it works
You can simply drag and drop an image into the image dropbox. The first model, Salesforce's BLIP image captioning model 
(https://huggingface.co/Salesforce/blip-image-captioning-base), will infer what is happening inside the image. 
I used HuggingFace's Transformers method to import this model. Next, I used another model, the GPT-3.5-turbo model, 
to generate a story from the image's caption. This was done through LangChain, which was used to import the model, provide
instructions for the model, and parse its output. Finally, the last model, ESPnet2 TTS pretrained model 
(https://huggingface.co/espnet/kan-bayashi_ljspeech_vits), converts the text story into an audio story. This was done through
HuggingFace's Inference API method, which was just as simple as the Transformers method. After all that, it was deployed through
Streamlit, a very developer-friendly UI!
