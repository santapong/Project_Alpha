import os
from dotenv import load_dotenv

from langchain_community.cache import SQLAlchemyCache
from langchain.globals import set_llm_cache
from sqlalchemy import create_engine


load_dotenv()

# Setup Cache for postgresql.
connection = os.getenv("LLM_CACHE")
engine = create_engine(url=connection)
set_llm_cache(SQLAlchemyCache(engine=engine))


# Find Cache Design.
class CacheManager:
    pass