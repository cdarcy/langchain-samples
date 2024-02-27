# langchain-samples
A collection of langchain sample scripts

## Samples using Ollama

* Install and run Ollama : https://ollama.com
* Create a local virtualenv, install python requirements and pull mistral llm :
```
python -m venv .venv
source .venv/bin/activate
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
Create a .env file with huggingface API Token generated on https://huggingface.co and source it
```
echo -e "export HUGGINGFACEHUB_API_TOKEN=\"<TOKEN>\"" >> .venv/bin/activate && source .venv/bin/activate
```

### langtest-wikipedia-agent
Simple app to get information from wikipedia since how long do we know about a topic.
Demonstrates the use of a wikipedia langchain agent/tool.
```
streamlit run huggingface/langtest-wikipedia-agent.py
```

Demonstrates the use of a wikipedia langchain agent/tool.

### langtest-prompt-multi-inputs
Simple app to get the winner country of a world cup finals
Demonstrates the use of Prompt and LLMChain with multiple inputs
```
streamlit run huggingface/langtest-prompt-multi-inputs.py
```

