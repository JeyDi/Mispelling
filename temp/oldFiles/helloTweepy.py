import tweepy

consumer_key = "P5wTozEUuNOAJCXMajGnRcDs2"
consumer_secret = "RB7p2JVEZxbodmRT3eaA32caonxpo5fS5DOKXcoTxEKJelTZys"
access_token = "997065391644917761-mSZZ6gkTdLEOdDSOAFfu7clvJO4vQPq"
access_token_secret = "MoAMNPZeAmYMwtjaopDrAs1njCwmx9pdCmC7JBP0A1uxF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

