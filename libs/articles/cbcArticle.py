from .article import Article
from .types import *
from typing import List


class CBCArticle(Article):
    cbcBaseUrl = "https://cbc.ca"
    def getStory(self) -> str:
        storyDiv = self.soup.find("div",class_="story")
        tags = storyDiv.select("p, h1, h2, h3, h4, h5, h6")
        story = ' '.join(tag.get_text(strip=True) for tag in tags)
        story = story.replace('\x00', " ")
        return story
    
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
            url = a_tag['href'] if "cbc.ca" in a_tag['href'] else self.cbcBaseUrl+a_tag['href']
            relatedStory = {
                "url": url,
                "title":a_tag.get_text()
            }
            relatedStories.append(relatedStory)
        return relatedStories
    
    def getHeadline(self) -> str:
        headlineH1 = self.soup.find("h1", class_=["detailHeadline","heading-element-h1"])
        return headlineH1.text