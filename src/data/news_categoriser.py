from src.data.word_lists import politics, sports, entertainment, technology, science, health, business, environment, education, weather

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