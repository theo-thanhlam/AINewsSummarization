
from .base import BaseModel, BaseMetadataModel
from sqlalchemy import Column, Integer, Text, ForeignKey


class Subscriber(BaseModel):
    __tablename__ = 'subscribers'
    email = Column(Text, unique=True)
    
    def __repr__(self):
        return f"<Subscriber(id={self.id}, email={self.email})>"