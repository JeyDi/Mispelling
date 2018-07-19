 
import tweepy
import re
import os
import sys
from configparser import ConfigParser

# Consumer keys and access tokens, used for OAuth
pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/../config.ini')
 
consumer_key = config['twitter']['consumer_key']
consumer_secret = config['twitter']['consumer_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
 
print("\nconsumer_key: " + consumer_key)
print("consumer_secret: " + consumer_secret)
print("access_token: " + access_token)
print("access_token_secret: " + access_token_secret + "\n")
 
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
                filename = os.path.join(result_folder, "raw_%s.txt" % profiles[index])
                with open(filename, 'a', encoding='utf8') as text_file:
                    text_file.write(status.text + "\n")
        except Exception as e:
            print("Error downloading tweets: %s" % e)
        
        print("Tweet for %s downloaded!" % profiles[index])