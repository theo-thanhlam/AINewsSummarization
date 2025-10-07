from models import *
from libs.articles.cbcArticle import CBCArticle
from libs.rss.cbcParser import CBCParser
from agents import SummarizeAgent
from libs.database.crud import CRUD



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
    
def summerize(item, summerizeAgent=None):
    if not summerizeAgent: 
        summerizeAgent = SummarizeAgent()
    
    title, story = item['title'],item['story']
    summerizeAgent.summerize(title, story)
    ai_response = summerizeAgent.getSummerization()
    return ai_response

def fetchCBCTopStories():
    cbcTopNews = 'https://www.cbc.ca/webfeed/rss/rss-topstories'

    items = parseRssFeed(cbcTopNews)
    db = CRUD()
    summerizeAgent = SummarizeAgent()
    for item in items:
        try:
            data = parseItem(item)
            
            #Handle author operations
            authorDoc = data['author']
            if authorDoc:
                existing_author = db.getOneBy(Author, name=authorDoc['name'])
                if not existing_author:
                    new_author = Author(name=authorDoc['name'], url = authorDoc['url'])
                    db.create(new_author)
                    
        
            # Handle aricle operations
            articleDoc = data
            article_author=articleDoc['author']
            
            existing_article = db.getOneBy(Article, article_id=articleDoc['id'])
            if existing_article:
                continue
            
            
            author_id:int = None
            if article_author:
                author_id = db.getOneBy(Author, name=article_author['name']).id
            
            
            new_article = Article(article_id=articleDoc['id'], 
                                title=articleDoc['title'], 
                                story=articleDoc['story'],
                                url=articleDoc['url'], 
                                published=articleDoc['published'],
                                author_id=author_id,
                                broadcaster_id = 1
                                )
            db.create(new_article)
            
            #Handle AI Summaries
            ai_response = summerize(data,summerizeAgent=summerizeAgent)
            new_summary = Summary(article_id = new_article.id, summary = ai_response.summary)
            db.create(new_summary)
            
            for takeaway in ai_response.key_takeaways:
                new_takeaway = Takeaway(summary_id = new_summary.id, takeaway=takeaway)
                db.create(new_takeaway)
            
        except :
            print(f"Error fetching {item['url']}")
        print(f"ADDED {len(items)}")


if __name__ == "__main__":
    fetchCBCTopStories()