class Retriever:
    def __init__(self,embedder,vectorstore):
        self.embedder=embedder
        self.vectorstore=vectorstore
    
    def retrieve(self,query,top_k=4):
        query_embedding=self.embedder.embed([query])
        return self.vectorstore.search(query_embedding,top_k)
        
     
            
         