from src.analysis.processing_data import get_news_df
from src.analysis.sent_analysis import get_sentiment_df


def main():
    df = get_news_df()
    df = get_sentiment_df()
    print(df.head(3))


if __name__ == "__main__":
    main()
