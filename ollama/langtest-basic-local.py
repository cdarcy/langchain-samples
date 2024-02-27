from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

llm = Ollama(
    model="mistral", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

llm.invoke("Can you describe the weather concept in 100 words maximum ?")