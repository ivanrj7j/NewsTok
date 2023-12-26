"""
Backend for the website
"""
from flask import Blueprint
from src.core import Article
from src.components import client


db = client["NewsTok"]
articleCollection = db["articles"]

backend = Blueprint("backend", __name__)

@backend.route('/getNext')
def getNext():
    postID = articleCollection.aggregate([{ "$sample": { "size": 1 } }]).next()["_id"]
    article = Article.fromUUID(postID)

    return article.json