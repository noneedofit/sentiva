# collect data from API and get news dataframes 

from src.data.top_headlines import get_sorted_top_headlines
from src.data.category_news import get_categorised_news
from src.data.news_dataframe import get_top_headlines_df, get_categorised_news_df

# get sentiment scores and plot sentiment scores

from src.analysis.sent_analysis import get_sentiment_df
from src.analysis.sent_analysis import count_zero_sentiment
from src.analysis.sent_analysis import update_zero_sentiment
from src.analysis.sent_plots import plot_sentiment


def main():

    # get data from API
    print('Getting articles from the API..')
    sorted_news = get_sorted_top_headlines()
    categorised_news = get_categorised_news()
    print('Fetching DONE.')

    # get dataframes from data 
    print('Making dataframes for the articles..')
    top_headlines_df = get_top_headlines_df(sorted_news)
    categorised_news_df = get_categorised_news_df(categorised_news)
    print('Dataframes MADE.')

    # get sentiment scores for each article 
    print('Applying sentiment analysis on the articles..')
    top_headlines_df = get_sentiment_df(top_headlines_df)
    categorised_news_df = get_sentiment_df(categorised_news_df)
    print('Analysis DONE.')

    # update sentiment scores for articles with 0 sentiment score
    print('Records with ZERO score information..')
    top_headlines_df = update_zero_sentiment(top_headlines_df)
    categorised_news_df = update_zero_sentiment(categorised_news_df)
    print('Number of 0 -> non-zero sentiment score updates: ', top_headlines_df.size + categorised_news_df.size - 2*count_zero_sentiment(top_headlines_df).size - 2*count_zero_sentiment(categorised_news_df).size)

    # plot sentiment scores
    print('Visualising our data..')
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

    # updated 0 -> non zero scores df
    updated_top_headlines_df = update_zero_sentiment(top_headlines_df, True)
    updated_categorised_news_df = update_zero_sentiment(categorised_news_df, True)

    print('UPDATED TOP HEADLINES dataframe: ', updated_top_headlines_df.size)
    print(updated_top_headlines_df.head(50))

    print('UPDATED CATEGORISED news dataframe: ', updated_categorised_news_df.size)
    print(updated_categorised_news_df.head(50))


if __name__ == "__main__":
    main()