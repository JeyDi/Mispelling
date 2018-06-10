import tweepy
import re
import os
from configparser import ConfigParser

#Check the working directory, go inside the file wd and launch
#TODO: when the solution istwitter, don't need this :)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Consumer keys and access tokens, used for OAuth
config = ConfigParser()
config.read('../config.ini')

consumer_key = config['twitter']['consumer_key']
consumer_secret = config['twitter']['consumer_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def downloadTweets(profiles,result_folder):
    #Download the tweets and save into files
    for index, _item in enumerate(profiles):
        screen_name = "@%s" % profiles[index]
        print("Start downloading: %s" % screen_name)
        #Warning: if you put a number inside the items you can limit the max tweets download
        try:
            for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name).items():
                filename = os.path.join(result_folder, "tweet_%s.txt" % profiles[index])
                with open(filename, 'a', encoding='utf8') as text_file:
                    text_file.write(status.text + "\n")
        except Exception as e:
            print("Error downloading tweets: %s" % e)
        
        print("Tweet for %s downloaded!" % profiles[index])