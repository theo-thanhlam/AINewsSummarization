from .article import Article
from .types import *
from typing import List


class CBCArticle(Article):
    cbcBaseUrl = "https://cbc.ca"
    def getStory(self) -> str:
        storyDiv = self.soup.find("div",class_="story")
        pTags = storyDiv.find_all("p")
        return "".join(tag.get_text() for tag in pTags)
    
    def getAuthor(self)->ArticleAuthor:
        authorSpan = self.soup.find("span", class_="authorText")
        try:
            authorName = authorSpan.get_text()
            authorHref = authorSpan.find("a")['href']
            
            authorData = {
                "name":authorName,
                "url":self.cbcBaseUrl+authorHref
            }
            return authorData
        except:
            return None
    
    def getRelatedStories(self) -> List[RelatedStories]:
        relatedStories = []
        relatedLinksa = self.soup.find_all("a",class_="relatedLink")
        for a_tag in relatedLinksa:
            relatedStory = {
                "url": self.cbcBaseUrl+a_tag['href'],
                "text":a_tag.get_text()
            }
            relatedStories.append(relatedStory)
        return relatedStories
    
    def getHeadline(self) -> str:
        headlineH1 = self.soup.find("h1", class_="detailHeadline")
        return headlineH1.text