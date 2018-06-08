import tweepy
import re

consumer_key = "P5wTozEUuNOAJCXMajGnRcDs2"
consumer_secret = "RB7p2JVEZxbodmRT3eaA32caonxpo5fS5DOKXcoTxEKJelTZys"
access_token = "997065391644917761-mSZZ6gkTdLEOdDSOAFfu7clvJO4vQPq"
access_token_secret = "MoAMNPZeAmYMwtjaopDrAs1njCwmx9pdCmC7JBP0A1uxF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline(count=200)

#per riazzerare ogni volta il file
text_file = open("tweet.txt","w")
text_file.close

for tweet in public_tweets:
    strNoUrl = re.sub(r"http\S+", "", tweet.text)
    with open("tweet.txt", 'a', encoding='utf8') as text_file:
        text_file.write(strNoUrl + "\n")
    print(strNoUrl)
