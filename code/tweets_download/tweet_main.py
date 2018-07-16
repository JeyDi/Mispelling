import os
from tweets_download import tweets_cleaner
from tweets_download import tweets_downloader
from configparser import ConfigParser

#Check the working directory, go inside the file wd and launch
#TODO: when the solution is complete, don't need this :)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

config = ConfigParser()
config.read('config.ini')

#result folder with the downloaded tweets
result_folder = config['config']['raw_tweets_folder']

#tweeter profile from where you want to download data
profiles = ["realDonaldTrump","rogerfederer","MercedesAMG","Forbes"]

tweets_downloader.downloadTweets(profiles,result_folder)

for profile in profiles:
    tweets_cleaner.preprocessing(profile)