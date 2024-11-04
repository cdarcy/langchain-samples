from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
import os
from PyPDF2 import PdfReader


repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=0.5, token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
)
loader = PyPDFLoader('./docs/test.pdf')
documents = loader.load()

# Get your splitter ready
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)

# Split your docs into texts
texts = text_splitter.split_documents(documents)

# There is a lot of complexity hidden in this one line. I encourage you to check out the video above for more detail
chain = load_summarize_chain(llm, chain_type="stuff", verbose=True)
response = chain.run(texts)
print(response)