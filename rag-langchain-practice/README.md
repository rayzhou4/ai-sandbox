# 🦆 RAG + LangChain Chatbot
STILL A WORK IN PROGRESS (need to build UI + improve RAG capabilites) \
Click [here]() for deployment link. (link currently doesn't work) \
If out of credits, it will stop working.
### Learning Objectives
I created a simple AI application to learn more about utilizing basic AI tools including:
- Chroma, 
- LangChain and its OpenAI package.

### Purpose
Simple AI chatbot with RAG

### How it works
You give it some documents in markdown that are going to be related to what you want to chatbot to know (as context). The first script,
`create_database.py`, will create a Chroma DB to store your documents with vectorized embedding as the key, making it retrieval.
Then, after your Chroma DB has been initialized, the second script executes, `query_data.py`. It is here where you will pass a query
(that is hopefully related to your documents that you've inputted) which will be answered by the chatbot which utilizes LangChain's OpenAI
package. You can repeat this process as if you are on chatgpt, but make sure you are wary of OpenAI's API costs 👀.

### To get it set up
1. Install `onnxruntime` first
```bash
pip install onnxruntime
```
If you're still experiencing issues, see this [thread](https://github.com/microsoft/onnxruntime/issues/11037)
- For Windows users, you must also follow this [guide](https://github.com/bycloudai/InstallVSBuildToolsWindows?tab=readme-ov-file) to install Microsoft C++ Build Tools.

2. Install all the dependencies in `requirements.txt`
```bash
pip install -r requirements.txt
```

3. Install markdown dependencies
```bash
pip install "unstructured[md]"
```

4. Add an `.env` file with your OpenAI API key
```bash
OPENAI_API_KEY=this-is-where-you-insert-your-api-key
```

### To run the scripts
1. Initialize the Chroma DB
```bash
python create_database.py
```

2. Query the Chroma DB
```bash
python query_data.py "What is the purpose of life?"
```