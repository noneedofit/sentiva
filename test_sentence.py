from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


def get_sentiment_score(sentence):
    if sentence is None or sentence == "":
        return 0
    scores = analyzer.polarity_scores(sentence)
    return scores["compound"]

news = '''While Rohit Sharma failed to lead India to their first International Cricket Council (ICC) title in 10 years at the World Test Championship (WTC) final at the Oval in London against Australia, where the Men in Blue succumbed to a 209-run defeat, fresh reports suggest that the Indian opener could be rested for the part of the West Indies tour. Notably, India are set to tour the Caribbean for Two Test matches followed by three ODIs and five T20Is. The series will commence with the first Test beginning on July 12 and culminate with the final T20I on August 13.

The decision of handing Rohit a bit of a rest is being considered owing to his workload since taking over as captain. Moreover, he hasn't been at his best form either. While he did score an ODI century against New Zealand while also making a hundred in Test matches against Australia, he hasn't managed to come up significant contributions with the consistency that one has come to expect of him.

His form in the 2023 season of the Indian Premier League (IPL) wasn't much encouraging either as he scored 322 runs in 16 matches at a strike rate of 132.80. He then did get off to a start in both the innings of the WTC final, especially the second one where he was looking good on 43 off 59 balls before he went for the sweep against Nathan Lyon and missed to make any connection with the bat. When the ball hit his pads, he was caught right in front of the stumps and the ball would have gone on to hit the stumps.

"Rohit looked a bit jaded during the IPL and the World Test Championship final in England. The selectors want him to rest for some part of the West Indies tour. He’s likely to miss the Tests or the eight-match white-ball series (three ODIs and five T20Is) to follow. The selectors will'''

print(get_sentiment_score(news))