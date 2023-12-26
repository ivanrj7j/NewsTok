from typing import Type
from aiohttp import ClientSession
import asyncio

class FetcherScheduler:
    """
    Schedules Fetchers for many urls, calls them async
    """
    
    def __init__(self, fetcher:Type, userAgent:str, urls:list[str]=[]) -> None:
        self.fetcher = fetcher
        self.urls = urls
        self.userAgent = userAgent

    def addURL(self, url:str):
        self.urls.append(url)

    async def fetch(self):
        if len(self.urls) > 0:
            async with ClientSession() as client:
                jobs = []
                for url in self.urls:
                    fetcher = self.fetcher(self.userAgent, url, client)
                    jobs.append(asyncio.ensure_future(fetcher.getArticle()))

                await asyncio.gather(*jobs)

    @property
    def scheduledTasksLength(self):
        return len(self.urls)