from libs.articles.cbcArticle import CBCArticle
from libs.rss.cbcParser import CBCParser
import json
from datetime import datetime
def cbcNewsFetch():
    cbcRSSTopStoriesUrl ="https://www.cbc.ca/webfeed/rss/rss-topstories"
    parser = CBCParser(cbcRSSTopStoriesUrl)
    items = parser.getItems()
   
    
    
    articles = []
    for item in items:
        try:
            artcile = CBCArticle(item['url'])
           
            news_data = {
                "published": item['published'],
                "url":item['url'],
                "title":item['title'],
                # "headline": cbcNews.getHeadline(),
                "author":artcile.getAuthor(),
                "story":artcile.getStory(),
                "relatedStories":artcile.getRelatedStories()
            } 
            articles.append(news_data)
        except:
            print(f'Failed to fetch {item['url']}')
            
    return json.dumps(articles, ensure_ascii=False, indent=4)



def main():
    cbcTopStories = cbcNewsFetch()
    print(cbcTopStories)
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    main()