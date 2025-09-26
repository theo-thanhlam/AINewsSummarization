from libs.articles.cbcArticle import CBCArticle
from libs.rss.cbcParser import CBCParser
import json
import time
from datetime import datetime
from libs.llm.agents import SummarizeAgent
import feedparser
from configs import headers



def cbcNewsFetch():
    cbcRSSTopStoriesUrl ="https://www.cbc.ca/webfeed/rss/rss-topstories"
    parser = CBCParser(cbcRSSTopStoriesUrl)
    items = parser.getItems()
    summarizeAgent = SummarizeAgent()
    
    
    articles = []
    for item in items:
        try:
            article = CBCArticle(item['url'])
            summarizeAgent.summerize(item['title'], article.getStory())
            ai_response = summarizeAgent.getSummerization()
           
            news_data = {
                "id":item['id'],
                "published": item['published'],
                "url":item['url'],
                "title":item['title'],
                # "headline": cbcNews.getHeadline(),
                "author":article.getAuthor(),
                "story":article.getStory(),
                "relatedStories":article.getRelatedStories(),
                "summary":ai_response.summary,
                "key_takeaways":ai_response.key_takeaways
            } 
            articles.append(news_data)
        except:
            continue
            
    # return json.dumps(articles, ensure_ascii=False, indent=4)
    return articles



def main():
    pass
    
    
    
    
    
    
    

if __name__ == "__main__":
    main()