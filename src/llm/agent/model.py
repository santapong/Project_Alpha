import os
import abc

from typing import Dict
from dotenv import load_dotenv

from sqlalchemy import create_engine

from langchain.chat_models import init_chat_model
from langchain_google_community.search import (
    GoogleSearchAPIWrapper, 
    GoogleSearchResults,
    )
from langchain_postgres import PGVector
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import (
    WebBaseLoader, 
    PyMuPDFLoader
    )

from langgraph.graph import START, StateGraph, END

from src.llm.utils import (
    register_tool,
    register_edge,
    register_node,
    )

load_dotenv()

# Create Agentic Model
class BaseAgentModel:
    
    # Setting up Model
    # def __init__(self):
        # self.__llm = self.__init_chat_model()
        # self.__graph = self.__init_graph_db()
        # self.__vector_store = self.__init_vector_db()
    
    # Internal Method #
    
    # Setting Model.
    @abc.abstractmethod
    def __init_chat_model(self):
        return init_chat_model(
            model=os.getenv("LLM_MODEL"),
            model_provider=os.getenv("MODEL_PROVIDER"),
            base_url=os.getenv("BASE_URL"),
            TEMPERATURE=os.getenv("TEMPERATURE"),
        )
        
    # Setting Vector Database.
    @abc.abstractmethod
    def __init_vector_db(self):
        return PGVector(
            embeddings=OllamaEmbeddings(model=os.getenv("EMBEDDING_MODEl")),
            connection=self.__init_engine,
            collection_name=os.getenv("COLLECTION_NAME")
        )
        
    # TODO: NEED more knowledge
    # Setting for Graph Database
    @abc.abstractmethod
    def __init_graph_db(self):
        pass
    
    # Internal Method #
    
    # Tools Method #
    @register_tool
    def search(self):
        
        print("Test")
        return
    
    
    # Get all tool.
    @abc.abstractmethod
    def get_tool_as_dict(self):
        # Getting Tool from @register_tool.
        self.__tool_methods = [
            method_name for method_name in dir(self)
            if callable(getattr(self, method_name)) and hasattr(getattr(self, method_name), "__is_tool")
        ]
        return {
                getattr(self, method_name).__name__: getattr(self, method_name)
                for method_name in self.__tool_methods
                }
    
    # Tools Method # 
    
    

    # Node Method # 
    @register_node
    def agent(
            self,
            State: StateGraph
        )-> dict[any]:
        
        pass
    
    # Make it get all node.
    @abc.abstractmethod
    def get_node_as_dict(self):
        # Getting Node from @register_node.
        self.__node_methods = [
            method_name for method_name in dir(self)
            if callable(getattr(self, method_name)) and hasattr(getattr(self, method_name), "__is_node")
        ]
        return {
                getattr(self, method_name).__name__: getattr(self, method_name)
                for method_name in self.__node_methods
                }
        
    # Node Method # 
    
    
    
    # Edge Method #
     
    # Make it to get all Edge
    @abc.abstractmethod
    def get_edge_as_dict(self):
        # Getting Edge from @register_edge.
        self.__edge_methods = [
            method_name for method_name in dir(self)
            if callable(getattr(self, method_name)) and hasattr(getattr(self, method_name), "__is_edge")
        ]
        return {
                getattr(self, method_name).__name__: getattr(self, method_name)
                for method_name in self.__edge_methods
                }
    # Edge Method #


    # NOTE: Maybe Deprecate
    # compile workflow
    def compile(self):
        self.workflow = StateGraph()
    
    # NOTE: It will useful.
    # Invoke
    def invoke(self):
        pass
    
    # Display Graph from compile.
    def display(self):
        pass
    
if __name__ == "__main__":
    test = BaseAgentModel()
    test = test.get_tool_as_dict()