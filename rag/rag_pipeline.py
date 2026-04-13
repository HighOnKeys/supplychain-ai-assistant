# ENV SETUP

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os

load_dotenv()


# 1. LOAD DOCUMENTS


def load_documents(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

    return documents

# 2. SPLIT DOCUMENTS


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)
    return chunks

# 3. CREATE VECTOR STORE (FREE)


def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)
    return db

# 4. RETRIEVE DOCUMENTS


def retrieve_documents(query, db):
    results = db.similarity_search_with_score(query, k=5)
    #filtered = [doc for doc, score in results if score < 1.0]
    return results
