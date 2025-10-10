from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel, BaseMetadataModel

class Topic(BaseModel, BaseMetadataModel):
    __tablename__ = "topics"
    
    articles = relationship("Article", back_populates="topic")
    feeds = relationship("Feed", back_populates="topic")
    
    def __repr__(self):
        return f"<Topic(id={self.id}, name='{self.name}')>"