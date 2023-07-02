from src.api.news_api import api


def get_sorted_top_headlines():
    top_headlines = api.get_top_headlines(
        category="general", language="en", country="in", page_size=100
    )
    articles = top_headlines["articles"]
    sorted_news = []

    for article in articles:
        title = article["title"]
        content = article.get("content")
        if not content or len(content.split()) < 5:
           content = title

    
        sorted_news.append({
           "title": title,
           "content": content
        })

    return sorted_news