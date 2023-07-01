from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(sentence):
    if sentence is None:
        return 0 
    scores = analyzer.polarity_scores(sentence)
    return scores["compound"]


def get_sentiment_df(df):
    df["sentiment_score"] = df["content"].apply(get_sentiment_score)
    return df
    

def count_zero_sentiment(df):
    # Count the number of articles with a sentiment score of 0.
    zero_sentiment_df = df[df['sentiment_score'] == 0]
    return zero_sentiment_df