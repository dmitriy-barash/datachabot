# pip install streamlit streamlit-chat
# pip install python-dotenv
# pip install langchain_community
# pip install "unstructured[pdf]"
# pip uninstall python-magic
# pip uninstall python-magic-bin
# pip install python-magic-bin==0.4.14
# pip install numpy --upgrade
# pip install faiss-cpu

import streamlit as st

from chat import create_application
from chat_view_model import ChatViewModel

def main():
    chat_view_model = ChatViewModel()
    create_application(view_model=chat_view_model)

if __name__ == "__main__":
    main()