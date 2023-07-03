from src.data.top_headlines import get_sorted_top_headlines
from src.data.category_news import get_categorised_news
from src.data.news_dataframe import get_top_headlines_df, get_categorised_news_df
from src.analysis.sent_analysis import get_sentiment_df, count_zero_sentiment, update_zero_sentiment
import time

def print_status(text, status):
    print(f"{text.ljust(45)} {status}")

def print_error(text, error):
    print(f"{text.ljust(45)} ERROR: {error}")

def main(df_stats=False, updated_stats=False):
   try:
        # get data from API
        print_status('Getting articles from the API..', '🟡')
        time.sleep(1)
        sorted_news = get_sorted_top_headlines()
        categorised_news = get_categorised_news()
        print_status('Fetching DONE', '✅')

        # get dataframes from data 
        print_status('Making dataframes for the articles..', '🟡')
        time.sleep(1)
        top_headlines_df = get_top_headlines_df(sorted_news)
        categorised_news_df = get_categorised_news_df(categorised_news)
        print_status('Dataframes MADE', '✅')

        # get sentiment scores for each article 
        print_status('Applying sentiment analysis on the articles..', '🟡')
        time.sleep(1)
        top_headlines_df = get_sentiment_df(top_headlines_df)
        categorised_news_df = get_sentiment_df(categorised_news_df)
        print_status('Analysis DONE', '✅')

        # update sentiment scores for articles with 0 sentiment score
        print_status('Records with ZERO score information..', '🟡')
        time.sleep(1)
        top_headlines_df = update_zero_sentiment(top_headlines_df)
        categorised_news_df = update_zero_sentiment(categorised_news_df)
        print_status('Records UPDATED', '✅')

        # plot sentiment scores
        print_status('Visualising our data..', '🟡')
        time.sleep(1)
        '''
        plot_sentiment(top_headlines_df, "Trending News")
        plot_sentiment(categorised_news_df, "Categorised News")
        '''
        print_status('Visualisation DONE', '✅')

   except Exception as e:
        print_error('An error occurred:', str(e))

        if df_stats:
           # dataframes sizes
           print('Number of articles in TOP HEADLINES dataframe: ', top_headlines_df.size)
           print('Number of articles in CATEGORISED news dataframe: ', categorised_news_df.size)
        
           print('Number of TRENDING articles with ZERO in sentiment score: ', count_zero_sentiment(top_headlines_df).size)
           print('Number of CATEGORISED articles with ZERO in sentiment score: ', count_zero_sentiment(categorised_news_df).size)

           # print dataframes
           print('TOP HEADLINES dataframe: ')
           print(top_headlines_df.head(10))

           print('CATEGORISED news dataframe: ')
           print(categorised_news_df.head(10))

        elif updated_stats:
           # updated 0 -> non zero scores df and also retrieve the no. of records updated in each df
           updated_top_headlines_df, updated_top_count = update_zero_sentiment(top_headlines_df, True, True)
           updated_categorised_news_df, updated_categorised_count = update_zero_sentiment(categorised_news_df, True, True)

           # print no. of updated records 
           print('No. of records updated in TOP HEADLINES dataframe: ', updated_top_count)
           print('No. of records updated in CATEGORISED news dataframe: ', updated_categorised_count)
           print('TOTAL NO. OF RECORDS UPDATED with ZERO score: ', updated_top_count + updated_categorised_count)

           print('UPDATED TOP HEADLINES dataframe: ')
           print(updated_top_headlines_df.head(15))

           print('UPDATED CATEGORISED news dataframe: ')
           print(updated_categorised_news_df.head(15))

if __name__ == "__main__":
    main()
