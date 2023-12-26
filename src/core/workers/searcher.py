from aiohttp import ClientSession
from src.core.workers.scheduler import FetcherScheduler
from src.core.workers.fetcher import Fetcher
from itertools import islice

class Searcher:
    """
    Searches the given website for new articles. Prepares fetchers based on a batchsize
    """
    def __init__(self, userAgent:str, baseURL:str, searchInterface:str, batchSize:int=50) -> None:
        self.userAgent = userAgent
        self.baseURL = baseURL
        self.searchInterface = searchInterface
        self.batchSize = batchSize

    def createSearchURL(self, query:str) -> str:
        return f"{self.baseURL}/{self.searchInterface}{query}"
    
    async def getPage(self, url:str, client:ClientSession):
        response = await client.get(url, headers={"user-agent":self.userAgent})
        return await response.text()
        
    def getData(self, response:str) -> list[str]:
        raise NotImplementedError("This method should be implemented by the child")
    
    def getScheduler(self, urls:list[str]):
        return FetcherScheduler(Fetcher, self.userAgent, urls)
    
    def prepareSchedulers(self, urls:list[str]):
        it = iter(urls)
        batches = iter(lambda: list(islice(it, self.batchSize)), [])

        schedulers = list(map(lambda x: self.getScheduler(x), batches))
        return schedulers
    
    async def getArticles(self, query:str):
        searchPage = self.createSearchURL(query)
        async with ClientSession() as client:
            return await self.getArticlesFromPage(searchPage, client)
    
    async def getArticlesFromPage(self, url:str, client:ClientSession):
        page = await self.getPage(url, client)
        urls = self.getData(page)
        schedulers = self.prepareSchedulers(urls)

        articles = []
        for scheduler in schedulers:
            articles += await scheduler.fetch()

        return articles 

