import os
import uuid
from configure import *
from embeddings.embedder import Embedder
from ingestion.pdf_loader import load_pdf,chunk_text
from ingestion.chart_processor import describe_chart
from vectorestore.faiss import Faissstore
from retriver.retreiver import Retriever
from LLM.generator import generate_answer
from rag_builder import build_rag

def main():
    file_path = r"D:\MultiRAG\data\document_page.pdf"
    my_retriever = build_rag(file_path)

    while True:
        q = input("\nAsk: ")
        retrieved=my_retriever.retrieve(q)
        answer=generate_answer(q,retrieved)
        print(answer)
        
if __name__=="__main__":
    main()
