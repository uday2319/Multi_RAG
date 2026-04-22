from fastapi import FastAPI
from fastapi import UploadFile , File
from pydantic import BaseModel
import os
import time
from rag_builder import build_rag
import logging
import uuid
from LLM.generator import generate_answer
from retriver.retreiver import Retriever
from logger_config import setup_logger
from embeddings.embedder import Embedder
from configure import *
from vectorestore.faiss import Faissstore


logger=setup_logger()

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_pdf(file:UploadFile=File(...)):
    try:
        os.makedirs("uploads", exist_ok=True)

        file_path = f"uploads/{file.filename}"

        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)

        build_rag(file_path)  

        return {"message": "File processed successfully"}

    except Exception as e:
        return {"error": str(e)}
        
        

@app.post("/ask")
def ask_question(request: QueryRequest):
    try:
        start = time.time()

        query = request.question
        logger.info(f"API Query: {request.question}")
        Embedder_instance=Embedder(EMBED_MODEL)
        store = Faissstore(384)

        store.load(f"vectorstore/")
        import json

        with open("vectorstore/metadata.json") as f:
            metadata = json.load(f)

        retriever = Retriever(Embedder_instance, store)
        retrieved = retriever.retrieve(query)

        for i,chunk in enumerate(retrieved):
            logger.info(f" retrived chunk {i+1} : {chunk}")
        answer = generate_answer(query, retrieved)

        latency = time.time() - start
        logger.info(f"Latency: {latency:.2f}s")
        logger.info(f"final answer:{answer}")

        return {
        "question": query,
        "answer": answer,
        "latency_seconds": round(latency, 2)
       }
    except Exception as e:
        print("REAL ERROR:", str(e)) 
        return {"error": str(e)}

    