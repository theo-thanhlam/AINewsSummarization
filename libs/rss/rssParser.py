import feedparser
from configs import headers
from abc import ABC, abstractmethod
from typing import List
from .rss_item import RSSItem
import requests

class RSSParser(ABC):
    def __init__(self, rssUrl):

        self.data = feedparser.parse(rssUrl, request_headers=headers)
        
    @abstractmethod
    def getItems(self) -> List[RSSItem]:
        """Return a list of items from rss feed """
        pass