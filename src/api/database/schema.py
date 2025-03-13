from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Boolean, DATETIME, func

# This is Class for create table.

# Create DDL of Table.
BASE = declarative_base()

# User Table
class User(BASE):
    
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    nickname = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    state = Column(Boolean, default=False)
    login_at = Column(DATETIME(timezone=True), default=func.now())