import pandas as pd

from src.data.news_trends import get_sorted_news


def get_news_df():
    sorted_news = get_sorted_news()
    df = pd.DataFrame(sorted_news.items(), columns=["title", "content"])
    return df