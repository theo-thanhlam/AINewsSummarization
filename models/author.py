from .base import BaseModel, BaseMetadataModel
from sqlalchemy import Column, Text
from sqlalchemy.orm import relationship



class Author(BaseModel, BaseMetadataModel):
    __tablename__ = 'authors'
    url = Column(Text)
    articles = relationship("Article", back_populates="author")

    def __repr__(self):
        return f"<Author(id={self.id}, name='{self.name}')>"