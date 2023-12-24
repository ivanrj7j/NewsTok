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

        raise NotImplementedError("Method not implemented yet")
    
    def getSummary(self):
        if self.summary is not None and self.summary != "":
            return self.summary
        else:
            raise NotImplementedError("Summarizing text method is not implemented yet")
        