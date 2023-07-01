# lists of words that are associated with each category

politics = ['politics', 'government', 'election', 'policy']
sports = ['sports', 'athletics', 'competition']
entertainment = ['entertainment', 'celebrities', 'movies', 'music']
technology = ['technology', 'computers', 'innovation']
health = ['health', 'medical', 'medicine']
business = ['business', 'economy', 'finance']
environment = ['environment', 'climate', 'nature']
science = ['science', 'research', 'discovery', 'study', 'scientists', 'scientist', 'space', 'physics', 'chemistry', 'biology', 'astronomy', 'astronomers', 'astronomer', 'mathematics', 'mathematicians', 'mathematician', 'geology', 'geologists', 'geologist', 'geography', 'geographers', 'geographer', 'engineering', 'engineers', 'engineer', 'technology', 'technologists', 'technologist', 'astrophysics']
education = ['education', 'school', 'learning']
weather = ['weather', 'forecast', 'climate']


# a dictionary mapping each category to its list of words

categories = {
    'politics': politics, 'sports': sports, 'entertainment': entertainment, 'technology': technology, 'science': science,
    'health': health, 'business': business, 'environment': environment, 'education': education, 'weather': weather,
}

def categorise_news(article):

    # if the article field is empty, return None to avoid errors

    if article is None:
        return None

    # create a dictionary with the same keys as categories, with all values initialized to zero
    word_counts = {category: 0 for category in categories}

    # count the occurrences of words in the article
    for word in article.split():
        for category, words in categories.items():
            if word.lower() in words:
                word_counts[category] += 1

    # find the category with the highest count
    max_count = 0
    best_category = None
    for category, count in word_counts.items():
        if count > max_count:
            max_count = count
            best_category = category

    return best_category


'''
article = ''' '''

category = categorise_news(article)
print("Category:", category)
'''