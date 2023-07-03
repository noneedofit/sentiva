from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np

analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(sentence):
    if sentence is None or sentence == "":
        return 0 
    scores = analyzer.polarity_scores(sentence)
    return scores["compound"]


def get_sentiment_df(df):
    df["sentiment_score"] = df["content"].apply(get_sentiment_score)
    return df
    

def update_zero_sentiment(df, return_updated_records=False, zero_sentiment_updated=False):
    updated_df = df.copy()  # create a new DataFrame to store the updated records
    zero_sentiment_count = df[df['sentiment_score'] == 0].shape[0]  # number of records with 0 sentiment score
    updated_count = 0  # variable to track the number of records updated

    while True:
        zero_sentiment_df = updated_df[updated_df['sentiment_score'] == 0]
        
        if zero_sentiment_df.empty:
            break
        
        for index, row in zero_sentiment_df.iterrows():
            original_sentiment_score = row["sentiment_score"]
            new_sentiment_score = get_sentiment_score(row["content"])
            updated_df.at[index, "sentiment_score"] = new_sentiment_score
            updated_df.at[index, "original_sentiment_score"] = original_sentiment_score
            updated_count += 1
        
        new_zero_sentiment_count = updated_df[updated_df['sentiment_score'] == 0].shape[0]
        
        if new_zero_sentiment_count == zero_sentiment_count:
            break
        
        zero_sentiment_count = new_zero_sentiment_count
    
    if return_updated_records:
        if zero_sentiment_updated:
            return updated_df, updated_count
        else:
            return updated_df
    else:
        if zero_sentiment_updated:
            return df, updated_count
        else:
            return df
        
    
def count_zero_sentiment(df):
    # count the number of articles with a sentiment score of 0, NaN, or None.
    zero_sentiment_df = df[df['sentiment_score'].isin([0, np.nan, None])]
    return zero_sentiment_df