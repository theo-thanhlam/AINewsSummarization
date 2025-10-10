from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel, BaseMetadataModel

class Feed(BaseModel, BaseMetadataModel):
    __tablename__ = "feeds"
    url = Column(Text)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    broadcaster_id = Column(Integer, ForeignKey("broadcasters.id"))
    topic = relationship("Topic", back_populates="feeds")
    broadcaster = relationship("Broadcaster", back_populates="feeds")
    
    def __repr__(self):
        return f"<Feed(id={self.id}, name='{self.name}', url='{self.url}', topic_id='{self.topic_id}', broadcaster_id='{self.broadcaster_id}')>"
    
    