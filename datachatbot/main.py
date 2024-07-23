# pip install streamlit streamlit-chat
# pip install python-dotenv
# pip install langchain_community
# pip install "unstructured[pdf]"
# pip uninstall python-magic
# pip uninstall python-magic-bin
# pip install python-magic-bin==0.4.14
# pip install numpy --upgrade
# pip install faiss-cpu

# pip install python-dotenv==1.0.0 langchain==0.0.302 unstructured==0.10.12 sentence_transformers==2.2.2 tqdm==4.66.1 faiss-cpu==1.7.4
# pip install python-dotenv langchain unstructured sentence_transformers tqdm faiss-cpu
# pip install python-dotenv -U langchain -U unstructured -U sentence_transformers -U tqdm -U faiss-cpu -U 
# pip uninstall python-magic
# pip install python-magic-bin==0.4.14

import streamlit as st

from chat import create_application
from chat_view_model import ChatViewModel

def main():
    chat_view_model = ChatViewModel()
    create_application(view_model=chat_view_model)

if __name__ == "__main__":
    main()