from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


def get_sentiment_score(sentence):
    if sentence is None or sentence == "":
        return 0
    scores = analyzer.polarity_scores(sentence)
    return scores["compound"]

# the count of no. of words in the csv file
word_count = 0

# count each word in the csv file, for each field row column or record, basically no. of wordds in the csv
csv_file = open('/Users/dhruv/Desktop/quaterLife/programming/projects/sentiva ip/sentiva/src/data/categorised_news.csv', 'r')
for row in csv_file:
    for column in row.split(','):
        for word in column.split():
            word_count += 1
csv_file.close()

print("Word count:", word_count)
