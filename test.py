from libs.articles.cbcArticle import CBCArticle
from libs.rss.cbcParser import CBCParser
import json




def main():
    cbcRSSTopStoriesUrl ="https://www.cbc.ca/webfeed/rss/rss-canada"
    parser = CBCParser(cbcRSSTopStoriesUrl)
    items = parser.getItems()
    
    articles = []
    for item in items:
        cbcNews = CBCArticle(item['url'])
        news_data = {
            "published": item["published"],
            "url":item['url'],
            "headline": cbcNews.getHeadline(),
            "author":cbcNews.getAuthor(),
            "story":cbcNews.getStory(),
            "relatedStories":cbcNews.getRelatedStories()
        } 
        articles.append(news_data)
    print(json.dumps(articles, ensure_ascii=False))
    
    
    
    
    

if __name__ == "__main__":
    main()