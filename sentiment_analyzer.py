from nltk.sentiment.vader import SentimentIntensityAnalyzer

def find_sentiment(tweet):
    '''return various sentiment scores for a tweet;
    including a calculated-by-us "overall" sentiment ranging from -1 to 1'''
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(tweet)
    sentiment['overall'] = sentiment['pos'] - sentiment['neg']
    return sentiment
