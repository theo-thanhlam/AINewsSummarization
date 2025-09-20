from dataclasses import dataclass

@dataclass
class ArticleAuthor:
    name:str
    url:str

@dataclass
class RelatedStories:
    url:str
    text:str