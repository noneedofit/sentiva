from newsapi import NewsApiClient
from src.env.creds import news_api_key

newsapi = NewsApiClient(news_api_key)

def get_sorted_news():
    newsapi = NewsApiClient(news_api_key) 
    
    top_headlines = newsapi.get_top_headlines(category='general', language='en', country='in')
    articles = top_headlines['articles']
    sorted_news = {}

    for article in articles:
        title = article['title']
        content = article['content']
        sorted_news[title] = content

    return sorted_news

get_sorted_news()