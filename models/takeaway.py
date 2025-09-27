# your_project/models/takeaway.py
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class Takeaway(BaseModel):
    __tablename__ = 'takeaways'  # Renamed from ai_summary_takeaways

    summary_id = Column(Integer, ForeignKey('summaries.id')) # Updated foreign key column name and table

    takeaway = Column(Text)

    summary = relationship("Summary", back_populates="takeaways") # Updated relationship name

    def __repr__(self):
        return f"<Takeaway(id={self.id}, summary_id={self.summary_id})>"