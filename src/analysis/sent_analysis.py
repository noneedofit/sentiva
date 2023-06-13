from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from processing_data import get_news_df
import pandas as pd
import matplotlib.pyplot as plt

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(sentence):
    if sentence is None or sentence == '':
        return 0
    scores = analyzer.polarity_scores(sentence)
    return scores['compound']

def get_sentiment_df():
    df = get_news_df()
    df['sentiment_score'] = df['content'].fillna(df['title']).apply(get_sentiment_score)
    print(df.head(5))
    return df

get_sentiment_df()