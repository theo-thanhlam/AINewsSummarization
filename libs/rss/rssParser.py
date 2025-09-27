import feedparser
from configs import headers
from typing import List
from .rss_item import RSSItem
import requests
from datetime import datetime,timedelta

class RSSParser:
    def __init__(self, rssUrl):

        self.data = feedparser.parse(rssUrl, request_headers=headers)
        self.items = []
        self.parseItems()
        
        
    
    def parseItems(self):
        for entry in self.data.entries: 
            published = datetime.strptime(entry.published,"%a, %d %b %Y %H:%M:%S %Z")
            today = datetime.now().replace(hour=0, minute=0,second=0,microsecond=0)
            tomorrow = today + timedelta(days=1)
            if not (today <= published < tomorrow):
                continue
            
            id = entry.id
            title = entry.title
            link = entry.link
            
            
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