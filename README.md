# Local Personal AI

**Note:** This project is for educational purposes only and is intended as a toy project for experimenting with RAG systems and personal data. The goal is to gain insights into what features are useful for personal AI assistants, what kinds of data are beneficial, and which tasks are most effective for enhancing their capabilities.

## Components

### 1. `data_ingestion.py`

This script handles the ingestion of PDF documents, including text extraction, chunking, embeddings generation, and storage.

### 2. `orchestrator.py`

This module orchestrates the retrieval and question-answering process. It initializes the embeddings model, vector store, retriever, and language model.

### 3. `cli.py`

This script provides a command-line interface for interacting with the personal AI assistant. Users can input queries and receive answers in real-time.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/lucaspecina/local_personal_ai.git
    cd local_personal_ai
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Ingest TXT Data**:
    ```bash
    python data_ingestion.py <path_to_txt>
    ```

2. **Run the Assistant**:
    ```bash
    python cli.py <model_name>
    ```