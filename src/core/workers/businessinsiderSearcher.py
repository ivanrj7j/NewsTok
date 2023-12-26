from src.core.workers.searcher import Searcher
from bs4 import BeautifulSoup
from aiohttp import ClientSession
from src.core.workers.businessinsider import BusinessInsiderFetcher
from src.core.workers.scheduler import FetcherScheduler

class BusinessInsiderSearcher(Searcher):
    def __init__(self, userAgent: str, batchSize: int = 50) -> None:
        super().__init__(userAgent, "https://www.businessinsider.in", "searchresult.cms?query=", batchSize)

    def createSearchURL(self, query: str, page:int=1) -> str:
        base = super().createSearchURL(query)
        return f"{base}&sortorder=effectivedate&curpg={page}"
    
    def getData(self, response: str) -> list[str]:
        soup = BeautifulSoup(response, "html.parser")
        linkTags = soup.select(".list-title-link")

        return list(map(lambda x: x.get("href"), linkTags))
    
    async def getArticles(self, query: str, topN:int=10):
        searchURLS = [self.createSearchURL(query, x) for x in range(1, topN+1)]
        articles = []
        async with ClientSession() as client:
            for searchURL in searchURLS:
                articles += await self.getArticlesFromPage(searchURL, client)

        return articles
    
    def getScheduler(self, urls: list[str]):
        return FetcherScheduler(BusinessInsiderFetcher, self.userAgent, urls)