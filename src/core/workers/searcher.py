from aiohttp import ClientSession

class Searcher:
    """
    Searches the given website for new articles.
    """
    def __init__(self, userAgent:str, baseURL:str, searchInterface:str) -> None:
        self.userAgent = userAgent
        self.baseURL = baseURL
        self.searchInterface = searchInterface

    def createSearchURL(self, query:str):
        raise NotImplementedError("This method should be implemented by the child")
    
    async def getPage(self, url:str, client:ClientSession):
        response = await client.get(url, headers={"user-agent":self.userAgent})
        return await response.text()
        
    async def getData(self, url:str, client:ClientSession):
        raise NotImplementedError("This method should be implemented by the child")
