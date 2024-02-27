from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
import streamlit as st
from langchain.llms import Ollama

import datetime

from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


def get_final_winner(sport, year):
    # Prompt
    prompt = PromptTemplate(
        input_variables=["sport_type", "year_of_final"],
        template="Who won the {sport_type} World Cup in the year {year_of_final} ?",
    )

    repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    llm = HuggingFaceEndpoint(
       repo_id=repo_id, temperature=0.5, token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
    )
    # Chain
    answer_chain = LLMChain(llm=llm, prompt=prompt, output_key='winner', verbose=True)

    return answer_chain.invoke({'year_of_final': year, 'sport_type': sport})


# UI
st.title("World Cups' winners")

sport_type = st.sidebar.selectbox("Which sport ?", ("Football", "Basketball", "Marathon"))

today = datetime.date.today()

if sport_type:
    year_of_finals = st.sidebar.number_input(
        value=int(today.year),
        label="Which year do you want to know the World Cup winner of " + sport_type + "?",
        min_value=1900,
        max_value=int(today.year))
    if year_of_finals:
        st.markdown(get_final_winner(sport_type, year_of_finals)['winner'])
