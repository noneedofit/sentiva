from src.data.top_headlines import get_sorted_top_headlines
from src.data.category_news import get_categorised_news
from src.data.news_dataframe import get_top_headlines_df, get_categorised_news_df
from src.analysis.sent_analysis import get_sentiment_df, count_zero_sentiment, update_zero_sentiment
from src.analysis.sent_plots import scatter_plot, heatmap_plot
import time

def print_status(text, status):
    print(f"{text.ljust(45)} {status}")

def print_error(text, error):
    print(f"{text.ljust(45)} ERROR: {error}")

def fetch_analyse():
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

        return top_headlines_df, categorised_news_df

    except Exception as e:
        print_error('An error occurred:', str(e))


def visualize(*dataframes):
    try:
        print_status('Visualising our data..', '🟡')
        time.sleep(1)
        scatter_plot(*dataframes)
        heatmap_plot(*dataframes)
        print_status('Visualisation DONE', '✅')
    except Exception as e:
        print_error('An error occurred while visualizing data:', str(e))


def stats(*dataframes):
    try:
        for df in dataframes:
            df_name = df.__class__.__name__.split("_")[0]
            df, count = update_zero_sentiment(df, True)
            print(f"{df_name.capitalize()} stats:")
            print('Number of articles in the dataframe:', df.size)
            print('Number of articles with ZERO sentiment score:', count_zero_sentiment(df).size)
            print('Number of articles with UPDATED (from 0) sentiment score:', count)
            print()
    except Exception as e:
        print_error('An error occurred while printing dataframe stats:', str(e))


def print_dataframe_records(df, n_head):
    if df is not None:
        df_name = df.__class__.__name__.split("_")[0]
        print(f"{df_name.capitalize()} ({n_head} articles):")
        print(df.head(n_head))

if __name__ == "__main__":
    print('Running main.py.. ✨')
    print()

    fetch_analyse_choice = input('Do you want to fetch and analyze data? (Y/N): ')
    fetch_analyse_choice = fetch_analyse_choice.lower() == 'y'

    visualize_choice = input('Do you want to visualize data? (Y/N): ')
    visualize_choice = visualize_choice.lower() == 'y'

    stats_choice = input('Do you want to print dataframe stats? (Y/N): ')
    stats_choice = stats_choice.lower() == 'y'

    n_head = None
    print_articles_choice = input('Do you want to print the articles? (Y/N): ')
    print_articles_choice = print_articles_choice.lower() == 'y'
    if print_articles_choice:
        n_head = int(input('Enter the number of articles to print: '))

    if fetch_analyse_choice:
        top_headlines_df, categorised_news_df = fetch_analyse()
    else:
        top_headlines_df, categorised_news_df = None, None

    if visualize_choice:
        if top_headlines_df is not None or categorised_news_df is not None:
            visualize(top_headlines_df, categorised_news_df)
        else:
            print_error('Dataframes not available for visualization.', '')
    
    if stats_choice:
        if top_headlines_df is not None or categorised_news_df is not None:
            stats(top_headlines_df, categorised_news_df)
        else:
            print_error('Dataframes not available for printing stats.', '')

    if print_articles_choice:
        print_dataframe_records(top_headlines_df, n_head)
        print_dataframe_records(categorised_news_df, n_head)