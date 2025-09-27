# your_project/models/summary.py
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Summary(BaseModel):
    __tablename__ = 'summaries'  # Renamed from ai_summaries
    article_id = Column(Integer, ForeignKey('articles.id'))
    summary = Column(Text)
    
    article = relationship("Article", back_populates="summaries") # Updated back_populates
    takeaways = relationship("Takeaway", back_populates="summary", uselist=True, cascade="all, delete-orphan") # Updated relationship name

    def __repr__(self):
        return f"<Summary(id={self.id}, article_id={self.article_id})>"