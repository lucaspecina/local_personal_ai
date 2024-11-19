from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

class Orchestrator:
    def __init__(self, model_name='llama3.2:latest'):
        self.embeddings_model = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
        self.vectorstore = Chroma(
            embedding_function=self.embeddings_model,
            persist_directory='./vectorstore'
        )
        self.retriever = self.vectorstore.as_retriever(search_kwargs={'k': 3})
        self.llm = Ollama(model=model_name)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=False
        )
        self.base_prompt = """
You are my personal assistant AI. Your goal is to help me with my personal tasks, provide information from my personal notes, and assist me in organizing my thoughts. Be concise, friendly, and helpful in your responses.

Use the following context from my personal data to answer the question.

"""

    # def get_answer(self, query):
    #     full_query = f"{self.base_prompt}\n\nUser: {query}"
    #     answer = self.qa_chain.invoke(full_query)
    #     return answer['result']
    

    def get_answer(self, query):
        # Retrieve relevant documents
        retrieved_docs = self.retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        
        # Create the full query with context
        full_query = f"{self.base_prompt}\n\nContext: {context}\n\nUser: {query}"
        
        # Get the answer from the QA chain
        answer = self.qa_chain.invoke(full_query)
        return answer['result']