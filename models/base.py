from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime,Text
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now())
    
class BaseMetadataModel(Base):
    __abstract__=True

    name = Column(Text, nullable=False)
    description = Column(Text)