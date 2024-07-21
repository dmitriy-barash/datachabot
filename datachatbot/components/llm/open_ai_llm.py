from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from components.llm.llm import Llm
import os

class OpenAILlM(Llm):
    def __init__(self):
        self.llm = ChatOpenAI(
            #model="text-davinci-003",
            model="gpt-3.5-turbo",
            openai_api_key=os.environ['OPEN_AI_API_TOKEN'],
            temperature=0)

    def get(self):
        return self.llm