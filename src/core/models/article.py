from src.components import client
from bson import ObjectId
from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser

articlesCollection = client["NewsTok"]["articles"]
# connecting to collection 

class Article:
    """
    A model for an article, contains essential details and methods related to an article
    """
    def __init__(self, url:str, title:str, content:str, author:str=None, summary:str=None, cover:str=None) -> None:
        self.url = url
        self.title = title
        self.content = content
        self.author = author
        self.summary = summary
        self.cover = cover

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
        
        return self(articleData["url"], articleData["title"], articleData["content"], articleData["author"], articleData["summary"], articleData["cover"])
    
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
                "summary": self.summary,
                "cover": self.cover
            })  

    def getSummary(self, sentences=4, language="english"):
        """
        Returns the summary of the article, if it does not already exist, 
        """
        
        if self.summary is None or self.summary == "":
            parser = PlaintextParser.from_string(self.content, Tokenizer(language))
            stemmer = Stemmer(language)
            summarizer = Summarizer(stemmer)

            self.summary = ""

            for sentence in summarizer(parser.document, sentences):
                self.summary += str(sentence) + " "
        
        return self.summary
        