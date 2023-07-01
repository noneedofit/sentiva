import pandas as pd

def get_top_headlines_df(sorted_news):
    df = pd.DataFrame(sorted_news, columns=["title", "content"])
    return df


def get_categorised_news_df(categorised_news):
    df = pd.DataFrame(categorised_news, columns=["title", "content", "topic"])
    return df