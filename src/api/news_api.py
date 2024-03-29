from os import getenv

from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

news_api_key = getenv("NEWS_API_KEY")

api = NewsApiClient(news_api_key)