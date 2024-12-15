import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time
from langchain_community.document_loaders import PyPDFDirectoryLoader


from dotenv import load_dotenv
load_dotenv()

## load the Groq API key
groq_api_key=os.environ['GROQ_API_KEY']
api_key = os.getenv("GOOGLE_API_KEY")


embeddings = GoogleGenerativeAIEmbeddings(api_key=api_key, model="models/embedding-001")

if "vector" not in st.session_state:
    st.session_state.embeddings=embeddings
    st.session_state.loader=PyPDFDirectoryLoader("./documents")
    st.session_state.docs=st.session_state.loader.load()

    st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
    st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
    st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)

st.title("Chat with Documents")
llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="mixtral-8x7b-32768")



prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)
document_chain = create_stuff_documents_chain(llm, prompt)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

prompt=st.text_input("Input you prompt here")

if prompt:
    start=time.process_time()
    response=retrieval_chain.invoke({"input":prompt})
    print("Response time :",time.process_time()-start)
    st.write(response['answer'])

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")
    