# your_project/models/broadcaster.py
from sqlalchemy.orm import relationship
from .base import BaseModel, BaseMetadataModel

class Broadcaster(BaseModel, BaseMetadataModel):
    __tablename__ = 'broadcasters'
    articles = relationship("Article", back_populates="broadcaster")
    
    feeds = relationship("Feed", back_populates="broadcaster")

    def __repr__(self):
        return f"<Broadcaster(id={self.id}, name='{self.name}')>"