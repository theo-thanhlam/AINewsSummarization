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
    topic_id = Column(Integer, ForeignKey('topics.id'))

    author = relationship("Author", back_populates="articles")
    broadcaster = relationship("Broadcaster", back_populates="articles")
    topic = relationship("Topic", back_populates="articles")

    summary = relationship("Summary", back_populates="article", cascade="all, delete-orphan") 
    takeaways = relationship("Takeaway",back_populates="article", cascade='all, delete-orphan', uselist=True)


    def __repr__(self):
        return f"<Article(id={self.id}, title='{self.title}', broadcaster_id={self.broadcaster_id})>"