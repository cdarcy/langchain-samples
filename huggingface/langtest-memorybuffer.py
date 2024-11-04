from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from operator import itemgetter

import os
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=0.5, token=os.environ["HUGGINGFACEHUB_API_TOKEN"]
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful chatbot"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

memory = ConversationBufferMemory(return_messages=True)

memory.load_memory_variables({})

chain = (
        RunnablePassthrough.assign(
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
        )
        | prompt
        | llm
)

inputs = {"input": "hi im bob"}
response = chain.invoke(inputs)
print(response)

memory.save_context(inputs, {"output": response})

memory.load_memory_variables({})

inputs = {"input": "whats my name"}
response = chain.invoke(inputs)
print(response)