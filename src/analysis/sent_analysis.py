from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from src.analysis.processing_data import get_news_df

analyzer = SentimentIntensityAnalyzer()


def get_sentiment_score(sentence):
    if sentence is None or sentence == "":
        return 0
    scores = analyzer.polarity_scores(sentence)
    return scores["compound"]


def get_sentiment_df():
    df = get_news_df()
    df["sentiment_score"] = df["content"].apply(get_sentiment_score)
    return df
    

def score_zero():
    df = get_sentiment_df()
    nil_df = df[df['sentiment_score'] == 0]
    print('Number of articles with sentiment score 0: ', len(nil_df))
    return df
