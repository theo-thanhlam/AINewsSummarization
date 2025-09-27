from libs.articles.cbcArticle import CBCArticle
from libs.rss.cbcParser import CBCParser
import json
import time
from datetime import datetime
from agents import SummarizeAgent
import feedparser
from configs import headers
from concurrent.futures import ThreadPoolExecutor
from libs.database import getSession
from models import Author



def parseRssFeed(url):
    parser = CBCParser(url)
    items = parser.getItems()
    return items
    
def parseItem(item):
    article= CBCArticle(item['url'])
    return{
                "id":item['id'],
                "published": item['published'],
                "url":item['url'],
                "title":item['title'],
                # "headline": cbcNews.getHeadline(),
                "author":article.getAuthor(),
                "story":article.getStory(),
                "relatedStories":article.getRelatedStories(),
    } 

def parseArticleData(item):
    return {
        "article_id":item['id'],
        "published": item['published'],
        "url":item['url'],
        "title":item['title'],
        "story":item['story']
        
    }
def parseAuthor(item):
    return item['author']

def summerize(item, summerizeAgent=None):
    if not summerizeAgent: 
        summerizeAgent = SummarizeAgent()
    
    title, story = item['title'],item['story']
    summerizeAgent.summerize(title, story)
    ai_response = summerizeAgent.getSummerization()
    return ai_response

def parseAiSummary(ai_response):
    return ai_response.summary

def parseAiKeyTakeaways(ai_response):
    return ai_response.key_takeaways





def main():
    with getSession() as session:
   
        new_author = Author(name="Test", description="descrioption",url="https://")
        session.add(new_author)
    
    

if __name__ == "__main__":
    main()