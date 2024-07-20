#pip install python-dotenv==1.0.0 langchain==0.0.302 unstructured==0.10.12 sentence_transformers==2.2.2 tqdm==4.66.1 faiss-cpu==1.7.4
# openai pandas PyMuPDF 
#pip install python-dotenv -U langchain -U unstructured -U sentence_transformers -U tqdm -U faiss-cpu -U

from dotenv import load_dotenv
import os
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

if __name__ == '__main__':
    load_dotenv()
    #huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.load_local("faiss_vector_db", embeddings= embeddings)
    repo_id = "tiiuae/falcon-7b-instruct"
    llm = HuggingFaceHub(
        repo_id=repo_id,
        #huggingfacehub_api_token=huggingfacehub_api_token,
        model_kwargs={
            "temperature": 0.1,
            "max_new_tokens":100,
        },
    )
    llm.client.api_url = 'https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct'

    qa = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff",
        retriever=vector_store.as_retriever(), 
        return_source_documents = True
    )

    exit_conditions = (":q", "quit", "exit")
    while True:
        query = input("\nType your question\n")

        if query in exit_conditions:
            break
        else:
            #result = qa(query)
            result = qa({"query": query})
            print("-" * 60)
            for index, doc in enumerate(result["source_documents"], start=1):
                print(f"Document {index}:")
                print("Page Content:")
                print(doc.page_content)
                print("Metadata:", doc.metadata)
                print("-" * 40)

            print("\n")
            print("Result:", result["result"])