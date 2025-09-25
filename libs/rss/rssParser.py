import feedparser
from configs import headers
from typing import List
from .rss_item import RSSItem
import requests

class RSSParser:
    def __init__(self, rssUrl):

        self.data = feedparser.parse(rssUrl, request_headers=headers)
        self.items = []
        self.parseItems()
        
        
    
    def parseItems(self):
        for entry in self.data.entries: 
            id = entry.id
            title = entry.title
            link = entry.link
            published = entry.published
            
            item = {
                "id":id,
                "title":title,
                "url":link,          
                "published":published,
                
            }
            self.items.append(item) 
        
    
    def getItems(self) -> List[RSSItem]:
        """Return a list of items from rss feed """
        return self.items