import tweets_downloader
import tweets_cleaner
import os
import sys
from configparser import ConfigParser

pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/../config.ini')
 
#result folder with the downloaded tweets
result_folder = config['twitter']['twitter_raw_tweets_folder']
 
#tweeter profile from where you want to download data
profiles = ["realDonaldTrump","rogerfederer","MercedesAMG", "Forbes"]
 
tweets_downloader.downloadTweets(profiles,result_folder)
 
for profile in profiles:
    tweets_cleaner.preprocessing(profile) 