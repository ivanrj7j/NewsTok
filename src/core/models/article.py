from src.components import client
from bson import ObjectId

articlesCollection = client["NewsTok"]["articles"]
# connecting to collection 

class Article:
    """
    A model for an article, contains essential details and methods related to an article
    """
    def __init__(self, url:str, title:str, content:str, author:str=None, summary:str=None) -> None:
        self.url = url
        self.title = title
        self.content = content
        self.author = author
        self.summary = summary

    @classmethod
    def fromUUID(self, uuid:str):
        """
        Fetches an article from the database using the uuid
        """

        articleData = articlesCollection.find_one({
            "_id": ObjectId(uuid)
        })

        if articleData is None:
            raise ModuleNotFoundError("The given article doesnt exist in the db")
        
        return self(articleData["url"], articleData["title"], articleData["content"], articleData["author"], articleData["summary"])
    
    def register(self):
        """
        Registers the article to the database
        """
        if articlesCollection.find_one({"url": self.url}) is None:
            articlesCollection.insert_one({
                "url": self.url,
                "title": self.title,
                "content": self.content,
                "author": self.author,
                "summary": self.summary
            })  

    def getSummary(self):
        """
        Returns the summary of the article, if it does not already exist, 
        """
        
        if self.summary is None or self.summary == "":
            raise NotImplementedError("Summarizing text method is not implemented yet")
        
        return self.summary
        