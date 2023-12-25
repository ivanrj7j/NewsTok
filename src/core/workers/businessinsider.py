from aiohttp import ClientSession
from src.core.workers.fetcher import Fetcher
from bs4 import BeautifulSoup
import json
from src.core.models.article import Article

class BusinessInsiderFetcher(Fetcher):
    def __init__(self, userAgent: str, url: str, client: ClientSession) -> None:
        super().__init__(userAgent, url, client)

    async def getArticle(self):
        page = await self.getPageData()

        soup = BeautifulSoup(page, "html.parser")

        article = json.loads(soup.select_one("#__NEXT_DATA__").text)
        
        title = article["props"]["pageProps"]["articleShowData"]["title"]
        content = article["props"]["pageProps"]["articleShowData"]["body"]
        date = article["props"]["pageProps"]["articleShowData"]["insertedTime"]
        author = article["props"]["pageProps"]["articleShowData"]["authorDetail"][0]["author_name"]
        cover = "https://www.businessinsider.in" + article["props"]["pageProps"]["articleShowData"]["img_Path"]

        article = Article(self.url, title, content, author, cover=cover, date=date)

        article.getSummary()
        article.register()

        return article



        
