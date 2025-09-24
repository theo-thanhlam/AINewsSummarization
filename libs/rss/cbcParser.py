from .rssParser import RSSParser

class CBCParser(RSSParser):
    def getItems(self):
        items = []
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
            items.append(item)   
        return items
