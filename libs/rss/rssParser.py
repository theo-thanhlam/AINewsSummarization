import feedparser
from configs import headers
from typing import List
from .rss_item import RSSItem
import requests
from datetime import datetime,timedelta
from dateutil import parser,tz
class RSSParser:
    def __init__(self, rssUrl):

        self.data = feedparser.parse(rssUrl, request_headers=headers)
        self.items = []
        self.parseItems()
        
        
    
    def parseItems(self):
        
        tzinfos = {
            "EDT": tz.tzoffset("EDT", -4 * 3600),  # UTC-4
            "EST": tz.tzoffset("EST", -5 * 3600),  # UTC-5
        }
        for entry in self.data.entries: 
            published = parser.parse(entry.published, tzinfos=tzinfos)  # parse the string with dateutil
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            tomorrow = today + timedelta(days=1)

            
            
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