from src.analysis.processing_data import get_news_df
from src.analysis.sent_analysis import get_sentiment_df
from src.analysis.sent_analysis import score_zero
from src.analysis.matplot import plot_sentiment

def main():
    df = get_news_df()
    df = get_sentiment_df()
    # df = score_zero()
    df = plot_sentiment()
    print(df.head(10))

if __name__ == "__main__":
    main()