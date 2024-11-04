from langchain.document_loaders import PyPDFLoader
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
import os
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain

# Define prompt
prompt_template = """Write a concise summary of the following in french language :
"{text}"
CONCISE SUMMARY:"""
prompt = PromptTemplate.from_template(prompt_template)

# Define LLM chain
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=0.5, token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
)
llm_chain = LLMChain(llm=llm, prompt=prompt)
loader = PyPDFLoader('./docs/testdoc.pdf')
docs = loader.load()

# Define StuffDocumentsChain
stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
print("StuffDocumentsChain : \n"+stuff_chain.run(docs))
