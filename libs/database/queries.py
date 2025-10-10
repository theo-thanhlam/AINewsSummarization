
from . import getSession
from models import *
from sqlalchemy import func

from datetime import datetime
from zoneinfo import ZoneInfo

def getNewsSnapshot(limit=5,topic:str="Top Stories"):
    with getSession() as db:
        query = (
         db.query(
            Article.id.label("article_id"),
            Article.title.label("article_title"),
            Article.url.label("article_url"),
            Article.published.label("article_published"),
            
            Author.name.label("author_name"),
            Author.url.label("author_url"),
            Broadcaster.name.label("broadcaster_name"),
            Topic.name.label("topic_name"),
            Summary.summary,
            func.array_agg(Takeaway.takeaway).label("takeaways"),
         )
         .join(Author, Article.author_id == Author.id, isouter=True)
        .join(Broadcaster, Article.broadcaster_id == Broadcaster.id)
        .join(Topic, Article.topic_id == Topic.id)
        .join(Summary, Summary.article_id == Article.id)
        .join(Takeaway, Takeaway.article_id == Article.id)
        .filter(Topic.name==topic)
         .group_by(
            Article.id,
            Article.title,
            Article.url,
            Article.published,
            Author.name,
            Author.url,
            Summary.summary,
            Broadcaster.name,
            Topic.name,
         ).order_by(Article.published.desc()).limit(limit)
      )
        results = query.all()
        data = [
           
           {
        "article_id": row.article_id,
        "article_title": row.article_title,
        "article_url": row.article_url,
        "broadcaster_name":row.broadcaster_name,
        "topic_name":row.topic_name,
        "article_published": row.article_published.astimezone(ZoneInfo("America/New_York")).isoformat() if row.article_published else None,
        "author_name": row.author_name,
        "author_url": row.author_url,
        "summary": row.summary,
        "takeaways": row.takeaways  # already a list from array_agg
    }
            for row in results
        ]
        return {
            "date":datetime.now(ZoneInfo("America/New_York")).strftime("%A, %b %d %I%p"),
            "data":data
        }

def getSubscribers():
    with getSession() as db:
        query = db.query(Subscriber.email)
        data = [subscriber.email for subscriber in query.all()]
        return {
            "data":data
        }