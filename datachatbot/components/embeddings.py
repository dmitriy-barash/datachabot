from langchain.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
import os

#MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
MODEL_NAME = "text-embedding-ada-002"
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

class Embeddings:
    def __init__(self):
        #self.embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)        
        self.embeddings = OpenAIEmbeddings(model=MODEL_NAME, api_key=os.environ['OPEN_AI_API_TOKEN'])

    def get(self):
        return self.embeddings
