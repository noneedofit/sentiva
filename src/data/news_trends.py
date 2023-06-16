from src.api.news_api import api


def get_sorted_news():
    top_headlines = api.get_top_headlines(
        category="general", language="en", country="in"
    )
    articles = top_headlines["articles"]
    sorted_news = {}

    for article in articles:
        title = article["title"]
        content = article.get("content", article["title"])
        sorted_news[title] = content

    return sorted_news