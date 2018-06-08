import csv
import re

import os.path as path


def clean_tweets(in_file, out_file=None):
    dict_tweets = load_tweets(in_file, True)
    if not out_file:
        base_path = path.dirname(in_file)
        file_name, extension = path.splitext(path.basename(in_file))

        out_file = path.join(base_path, file_name + "_cleaned" + extension)

    write_tweets(out_file, dict_tweets)


def load_tweets(file, not_cleaned=False):
    dict_tweets = {}

    with open(file, 'rt', encoding="utf8") as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')

        for tweet_id, tweet in reader:
            tweet_clean = clean(tweet) if not_cleaned else tweet
            if tweet_clean:
                dict_tweets[tweet_id] = tweet_clean

    return dict_tweets


def write_tweets(file, tweets):
    with open(file, "wt", encoding="utf8", newline="") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        for tweet_id in tweets:
            writer.writerow([tweet_id, tweets[tweet_id]])


mentions_re = re.compile(r'@[^\s]*')
url_re = re.compile(r'htt[^\s]*')
symbols_re = re.compile(r'[^A-Za-z ]')
rt_re = re.compile(r'RT ')
space_re = re.compile(r'\s+')


def clean(tweet):
    tweet = mentions_re.sub(' ', tweet)  # Mentions
    tweet = url_re.sub(' ', tweet)  # URLs
    tweet = symbols_re.sub(' ', tweet)  # Symbols
    tweet = rt_re.sub(' ', tweet)  # RT
    tweet = space_re.sub(' ', tweet)
    tweet = tweet.strip()  # spaces at head or tail

    return tweet
