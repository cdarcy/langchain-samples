from langchain_community.llms import Ollama

# App UI
import streamlit as st

st.title('LLM prompt UI')
prompt = st.text_input('Put your prompt here')

# LLM
llm = Ollama(model="mistral")
if prompt:
    st.markdown(llm.invoke(prompt))
