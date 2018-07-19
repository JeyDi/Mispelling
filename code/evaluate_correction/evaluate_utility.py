import csv
import re
import os.path as path


mentions_re = re.compile(r'@[^\s]*')
url_re = re.compile(r'htt[^\s]*')
symbols_re = re.compile(r'[^A-Za-z ]')
rt_re = re.compile(r'RT ')
space_re = re.compile(r'\s+')


def load_file(path, cleaned = False):
    dict_tweets = {}

    with open(path, 'rt', encoding="utf-8") as file:
        reader = file.read()

        reader = reader.split(" ")

        dict_tweets = []

        for tweet in reader:
            tweet_clean = clean(tweet) if cleaned else tweet
            dict_tweets.append(tweet_clean)        
    return dict_tweets


def write_tweets(file, tweets):
    with open(file, "wt", encoding="utf8", newline="") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        for tweet_id in tweets:
            writer.writerow([tweet_id, tweets[tweet_id]])

def clean(tweet):
    tweet = mentions_re.sub(' ', tweet)  # Mentions
    tweet = url_re.sub(' ', tweet)  # URLs
    tweet = symbols_re.sub(' ', tweet)  # Symbols
    tweet = rt_re.sub(' ', tweet)  # RT
    tweet = space_re.sub(' ', tweet)
    tweet = tweet.strip()  # spaces at head or tail

    return tweet