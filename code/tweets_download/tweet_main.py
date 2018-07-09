from tweets_download import tweets_downloader
from tweets_download import tweets_cleaner
import os
from configparser import ConfigParser

#Check the working directory, go inside the file wd and launch
#TODO: when the solution is complete, don't need this :)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

config = ConfigParser()
config.read('../config.ini')

#result folder with the downloaded tweets
result_folder = config['config']['result_folder']
print(result_folder)

#tweeter profile from where you want to download data
profiles = ["realDonaldTrump","rogerfederer","MercedesAMG"]

tweets_downloader.downloadTweets(profiles,result_folder)

for profile in profiles:
    #textFileIn = tweetsCleaner2.loadFile(result_folder + "/tweet_" + profile + ".txt")
    #textFileClean = tweetsCleaner2.cleanTweets(textFileIn)
    tweets_cleaner.preprocessing(profile)

