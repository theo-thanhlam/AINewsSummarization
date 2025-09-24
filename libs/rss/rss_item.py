from dataclasses import dataclass
from datetime import datetime

@dataclass
class RSSItem:
    id:str
    title:str
    url:str
    published:datetime