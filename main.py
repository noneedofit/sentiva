from src.data.news_trends import get_sorted_news
from src.analysis.processing_data import get_news_df
from src.analysis.sent_analysis import get_sentiment_df

def main():
    sorted_news = get_sorted_news()
    df = get_news_df()
    df = get_sentiment_df()
    print(df.head(3))

main()