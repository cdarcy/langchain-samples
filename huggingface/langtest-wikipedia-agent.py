import os
import streamlit as st
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


def get_agent(topic):
    repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    llm = HuggingFaceEndpoint(
        repo_id=repo_id, temperature=0.5, token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
    )
    tools = load_tools(["wikipedia"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    return agent.run("How long do we know about " + topic)


# UI
st.title("How long do we know about... ?")

topic = st.text_input(label="Which topic ?")
if topic:
    st.markdown(get_agent(topic))
