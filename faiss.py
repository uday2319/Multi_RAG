import faiss
class Faissstore:
    def __init__(self,diemension):
        self.index=faiss.IndexFlatL2(diemension)
        self.metadata=[]

    def add(self,embeddings,meta_items):
        self.index.add(embeddings)
        self.metadata.extend(meta_items)
    
    def search(self,embeddings,top_k):
        D,I=self.index.search(embeddings,top_k)
        return [self.metadata[i] for i in I[0]]
    
    def save(self,path):
        import faiss
        faiss.write_index(self.index,f"{path}/index.faiss")
        
    def load(self,path):
        self.index = faiss.read_index(f"{path}/index.faiss")