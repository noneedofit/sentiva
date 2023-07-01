# collect data from API and get news dataframes 

from src.data.top_headlines import get_sorted_top_headlines
from src.data.category_news import get_categorised_news
from src.data.news_dataframe import get_top_headlines_df, get_categorised_news_df

# get sentiment scores and plot sentiment scores

from src.analysis.sent_analysis import get_sentiment_df
from src.analysis.sent_analysis import count_zero_sentiment
from src.analysis.sent_plots import plot_sentiment


def main():

    # get data from API 
    sorted_news = get_sorted_top_headlines()
    categorised_news = get_categorised_news()
    
    # get dataframes from data 
    top_headlines_df = get_top_headlines_df(sorted_news)
    categorised_news_df = get_categorised_news_df(categorised_news)

    # get sentiment scores for each article 
    top_headlines_df = get_sentiment_df(top_headlines_df)
    categorised_news_df = get_sentiment_df(categorised_news_df)

    # plot sentiment scores
    '''
    plot_sentiment(top_headlines_df, "Trending News")
    plot_sentiment(categorised_news_df, "Categorised News")
    '''

    # dataframes sizes
    print('Number of articles in TOP HEADLINES dataframe: ', top_headlines_df.size)
    print('Number of articles in CATEGORISED news dataframe: ', categorised_news_df.size)
    
    print('Number of TRENDING articles with ZERO in sentiment score: ', count_zero_sentiment(top_headlines_df).size)
    print('Number of CATEGORISED articles with ZERO in sentiment score: ', count_zero_sentiment(categorised_news_df).size)

    # print dataframes
    print('TOP HEADLINES dataframe: ')
    print(top_headlines_df.head(50))

    print('CATEGORISED news dataframe: ')
    print(categorised_news_df.head(50))


if __name__ == "__main__":
    main()