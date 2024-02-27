# langchain-samples
A collection of langchain sample scripts

## Samples using Ollama

* Install and run Ollama : https://ollama.com
* Install python requirements and pull mistral llm :
```
pip3 install -r requirements
ollama pull mistral
```
### langtest-basic-local
Run a python script with a simple question to mistral :
```
python3 ollama/langtest-basic-local.py
```

### langtest-streamlit-simple
Ask questions to mistral using streamlit ui.
```
streamlit run ollama/langtest-streamlit-simple.py
```

### langtest-conversationchain.py
Ask questions to llm using a ConversationChain.
```
streamlit run ollama/langtest-conversationchain.py
```

### langtest-app-youtube
From the example of Nicholas Renotte : https://www.youtube.com/watch?v=MlK6SIjcjE8 \
Uses LLMChain, PromptTemplate, ConversationMemoryBuffer and WikipediaAPIWrapper to build an app generating a YouTube video title and script
```
streamlit run ollama/langtest-app-youtube.py
```

## Samples using HuggingFace
Create a .env file with huggingface api token generated on https://huggingface.co
```
cat << EOF > .env
HUGGINGFACEHUB_API_TOKEN="<TOKEN>"
EOF
```

### langtest-wikipedia-agent
