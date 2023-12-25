from aiohttp import ClientSession


class Fetcher:
    """
    Fetches article from any given website
    """
    def __init__(self, userAgent:str, url:str, client:ClientSession) -> None:
        self.userAgent = userAgent
        self.url = url
        self.client = client

    async def getPageData(self):
        response = await self.client.get(self.url, headers={"user-agent": self.userAgent})
        return await response.text()
    
    async def getArticle(self):
        raise NotImplementedError("This method should be implemented by the child")