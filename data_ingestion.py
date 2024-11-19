import os
import sys
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

import warnings
warnings.filterwarnings("ignore")

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def chunk_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_text(text)
    return chunks

def generate_embeddings(chunks):
    embeddings_model = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    # embeddings = embeddings_model.embed_documents(chunks)
    return embeddings_model

def store_embeddings(chunks, embeddings_model):
    persist_directory = './vectorstore'
    vectorstore = Chroma(
        embedding_function=embeddings_model,
        persist_directory=persist_directory
    )
    vectorstore.add_texts(texts=chunks)
    vectorstore.persist()
    print(f"Embeddings stored in {persist_directory}")

def main():
    data_directory = 'tmp_data'
    txt_files = [f for f in os.listdir(data_directory) if f.endswith('.txt')]

    if not txt_files:
        print(f"No .txt files found in {data_directory}.")
        sys.exit(1)

    for txt_file in txt_files:
        txt_path = os.path.join(data_directory, txt_file)
        print(f"Processing {txt_file}...")
        text = extract_text_from_txt(txt_path)
        chunks = chunk_text(text)
        embeddings_model = generate_embeddings(chunks)
        store_embeddings(chunks, embeddings_model)
        print(f"Finished processing {txt_file}.\n")

if __name__ == '__main__':
    main()
