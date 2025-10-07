
from . import getSession
from models import *
from sqlalchemy import func
from pydantic import BaseModel
from typing import List
from datetime import datetime
from zoneinfo import ZoneInfo



class SingleNewsSummary(BaseModel):
    article_id:int
    article_title:str
    article_url:str
    # article_published_parsed:datetime
    article_published:str
    author_id:int
    author_name:str
    author_url:str
    summary:str
    takeaways:List[str]


def getNewsSnapshot(limit=5):
    with getSession() as db:
        query = (
         db.query(
            Article.id.label("article_id"),
            Article.title.label("article_title"),
            Article.url.label("article_url"),
            Article.published.label("article_published"),
            Author.id.label("author_id"),
            Author.name.label("author_name"),
            Author.url.label("author_url"),
            Summary.summary.label("summary"),
            func.array_agg(Takeaway.takeaway).label("takeaways")
         )
         .join(Author, Article.author_id == Author.id,isouter=True)
         .join(Summary, Article.id == Summary.article_id)
         .join(Takeaway, Takeaway.summary_id == Summary.id)
         .group_by(
            Article.id,
            Article.title,
            Article.url,
            Article.published,
            Author.id,
            Author.name,
            Author.url,
            Summary.summary
         ).order_by(Article.published.desc()).limit(limit)
      )
        results = query.all()
        data = [
            # SingleNewsSummary(
            #     article_id=row.article_id,
            #     article_title=row.article_title,
            #     article_url=row.article_url,
            # #    article_published_parsed=row.article_published.astimezone(ZoneInfo("America/New_York")),
            #     article_published=row.article_published.astimezone(ZoneInfo("America/New_York")).isoformat(),
            #     author_id = row.author_id,
            #     author_name=row.author_name,
            #     author_url = row.author_url,
            #     summary=row.summary,
            #     takeaways = row.takeaways
            #     ).model_dump_json(indent=4,)
           {
        "article_id": row.article_id,
        "article_title": row.article_title,
        "article_url": row.article_url,
        "article_published": row.article_published.astimezone(ZoneInfo("America/New_York")).isoformat() if row.article_published else None,
        "author_id": row.author_id,
        "author_name": row.author_name,
        "author_url": row.author_url,
        "summary": row.summary,
        "takeaways": row.takeaways  # already a list from array_agg
    }
            for row in results
        ]
        return {
            "date":datetime.now(ZoneInfo("America/New_York")).date().isoformat(),
            "data":data
        }

def getSubscribers():
    with getSession() as db:
        query = db.query(Subscriber.email)
        data = [subscriber.email for subscriber in query.all()]
        return {
            "data":data
        }