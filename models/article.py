from .base import BaseModel
from sqlalchemy import Column, Text, Date, Integer,ForeignKey
from sqlalchemy.orm import relationship


class Article(BaseModel):
    __tablename__ = "articles"
    article_id = Column(Text, unique=True, nullable=False) # ID given by broadcasters
    title = Column(Text, nullable=False)
    story = Column(Text)
    url = Column(Text)
    published = Column(Date)
    author_id = Column(Integer, ForeignKey('authors.id'))
    broadcaster_id = Column(Integer, ForeignKey('broadcasters.id'))

    author = relationship("Author", back_populates="articles")
    broadcaster = relationship("Broadcaster", back_populates="articles")
    summaries = relationship("Summary", back_populates="article", uselist=True, cascade="all, delete-orphan") 


    def __repr__(self):
        return f"<Article(id={self.id}, title='{self.title}', broadcaster_id={self.broadcaster_id})>"