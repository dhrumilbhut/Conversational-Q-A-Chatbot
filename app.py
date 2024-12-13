import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader, PyPDFLoader

## Load the Environment Variables
from dotenv import load_dotenv
load_dotenv()

## Load the GROQ API Kye
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

groq_api_key = os.getenv("GROQ_API_KEY")

llm=ChatGroq(groq_api_key=groq_api_key, model_name='Gemma-7b-It')

prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    <context>
    Question: {input}
    """
)



def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

        if uploaded_file is not None:
            temp_file_path = os.path.join(os.getcwd(), uploaded_file.name)
            
            with open(uploaded_file.name, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.session_state.loader = PyPDFLoader(temp_file_path)
        else: 
            st.write("Please upload a file")
        # st.session_state.loader = PyPDFDirectoryLoader("research_papers")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=20000, chunk_overlap=1000),
        st.session_state.final_documents = st.session_state.text_splitter[0].split_documents(st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)


uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector Database is ready")
    

user_prompt = st.text_input("Enter the query from the document")

import time
if user_prompt:
    document_chain=create_stuff_documents_chain(llm, prompt)
    retriever=st.session_state.vectors.as_retriever()
    retriever_chain=create_retrieval_chain(retriever, document_chain)

    start=time.process_time()
    response=retriever_chain.invoke({"input": user_prompt})
    print(f"Response time : {time.process_time()-start}")

    st.write(response["answer"])

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write('---------------------------------')