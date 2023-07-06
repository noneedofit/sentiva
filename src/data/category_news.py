import time
from src.api.news_api import api
from src.data.news_categoriser import categorise_news


def get_categorised_news():

    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    sorted_categorised_news = []

    for category in categories:
        top_headlines = api.get_top_headlines(
            category=category, language='en', country='in'
            )

        articles = top_headlines["articles"]

        for article in articles:
            title = article["title"]
            content = article.get("content")
            if not content or len(content.split()) < 5:
               content = title
            category = categorise_news(content)

            # temporary fix for articles with no category
            import numpy as np
            if category is None or category == np.nan or category == "":
                category = np.random.choice(categories)

            sorted_categorised_news.append({
               "title": title,
               "content": content,
               "category": category
            })

    return sorted_categorised_news