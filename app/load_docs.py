# Script to load the documents to apply RAG
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.vectorstores import Chroma


def load_docs(embeddings, doc_directory, chunk_size = 1024, chunk_overlap= 64):
    """
    Load PDF documents from a directory and store embeddings in a vector database.
    
    Parameters:
        embeddings: The embedding model object to use
        doc_directory (str): Directory containing the PDF documents
        
    Returns:
        Chroma: A Chroma vector store instance with documents embeddings.
    """
    if not os.path.exists(doc_directory):
        raise FileNotFoundError(f"Directory not found: {doc_directory}")
    
    loader = PyPDFLoader(doc_directory)
    
    try:
        docs = loader.load()
    except Exception as e:
        raise RuntimeError(f"Error loading documents: {e}")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
    texts = text_splitter.split_documents(docs)
    
    db = Chroma.from_documents(texts, embeddings, persist_directory='db')
    return db

    
    
