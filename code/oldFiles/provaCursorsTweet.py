import tweepy
import re
import string

# Consumer keys and access tokens, used for OAuth
consumer_key = "P5wTozEUuNOAJCXMajGnRcDs2"
consumer_secret = "RB7p2JVEZxbodmRT3eaA32caonxpo5fS5DOKXcoTxEKJelTZys"
access_token = "997065391644917761-mSZZ6gkTdLEOdDSOAFfu7clvJO4vQPq"
access_token_secret = "MoAMNPZeAmYMwtjaopDrAs1njCwmx9pdCmC7JBP0A1uxF"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#per riazzerare ogni volta il file
text_file = open(".\\tweetTrumpComplete.txt","w")
text_file.close
text_file = open(".\\tweetTrumpClean.txt","w")
text_file.close
text_file = open(".\\tweetFedererComplete.txt","w")
text_file.close
text_file = open(".\\tweetFedererClean.txt","w")
text_file.close
text_file = open(".\\tweetMercedesComplete.txt","w")
text_file.close
text_file = open(".\\tweetMercedesClean.txt","w")
text_file.close

# for tweet in public_tweets:
#     with open("tweet.txt", 'a', encoding='utf8') as text_file:
#         text_file.write(tweet.text + "\n")
#     print(tweet.text)

string_punctuation =  ".#,_;"

def remove_punctuation(s):
    no_punct = ""
    for letter in s:
        if letter not in string_punctuation:
            no_punct += letter
    return no_punct

def get_user_mentions(tweet):
    return [m['screen_name'] for m in tweet['entities']['user_mentions']]


#se si mette un numero dentro ad items si limita il download a quel numero di tweet indicato
for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump').items():
    with open("tweetTrumpComplete.txt", 'a', encoding='utf8') as text_file:
        text_file.write(status.text + "\n")
    strNoUrl = re.sub(r"http\S+", "", status.text)
    strNoPunct = remove_punctuation(strNoUrl)
    with open("tweetTrumpClean.txt", 'a', encoding='utf8') as text_file:
        text_file.write(strNoPunct + "\n")
    
    # print(status._json['text'])
    
    #print(status.text)

for status in tweepy.Cursor(api.user_timeline, screen_name='@rogerfederer').items():
    with open("tweetFedererComplete.txt", 'a', encoding='utf8') as text_file:
        text_file.write(status.text + "\n")
    strNoUrl = re.sub(r"http\S+", "", status.text)
    strNoPunct = remove_punctuation(strNoUrl)
    with open("tweetFedererClean.txt", 'a', encoding='utf8') as text_file:
        text_file.write(strNoPunct + "\n")


for status in tweepy.Cursor(api.user_timeline, screen_name='@MercedesAMG').items(2000):
    with open("tweetMercedesComplete.txt", 'a', encoding='utf8') as text_file:
        text_file.write(status.text + "\n")
    strNoUrl = re.sub(r"http\S+", "", status.text)
    strNoPunct = remove_punctuation(strNoUrl)
    with open("tweetMercedesClean.txt", 'a', encoding='utf8') as text_file:
        text_file.write(strNoPunct + "\n")