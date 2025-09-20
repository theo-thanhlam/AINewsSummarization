import requests
from bs4 import BeautifulSoup
from configs import headers
from abc import ABC, abstractmethod
from configs.request_headers import headers

class Article(ABC):
    def __init__(self,url):
        article = requests.get( url,headers=headers)
        self.soup = BeautifulSoup(article.content,"html.parser")
    
    @abstractmethod
    def getStory(self):
        pass
    @abstractmethod
    def getAuthor(self):
        pass
    @abstractmethod
    def getRelatedStories(self):
        pass
    @abstractmethod
    def getHeadline(self):
        pass