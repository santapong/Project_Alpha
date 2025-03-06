import os
from dotenv import load_dotenv

from langchain_ollama import OllamaEmbeddings
from langchain_postgres import PGVector

from sqlalchemy import create_engine

load_dotenv()

# Class for database model
class VectorDBModel:
    
    # Constucter
    def __init__(
        self,
        model=os.getenv("EMBEDDING_MODEL"),
        collection_name=os.getenv("COLLECTION_NAME"),
                 ):
        self.vector_store = PGVector(
            connection=self.__engine(),
            collection_name=collection_name,
            embeddings=OllamaEmbeddings(model=model),
            use_jsonb=True
        )
        
    # Connect to PGvector Datbase
    def __engine(
        self, 
        connection=os.getenv("VECTORDB_CONNECTION")
        ):
        return create_engine(url=connection)
    
    def load_document(self):
        pass
    
    
if __name__ == "__main__":
    test = VectorDBModel()        