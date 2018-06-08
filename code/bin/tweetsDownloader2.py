import tweepy
import re
import string
import os

#Check the working directory, go inside the file wd and launch
#TODO: when the solution is complete, don't need this :)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Consumer keys and access tokens, used for OAuth
#TODO: need to insert the configuration in a json config file
consumer_key = "P5wTozEUuNOAJCXMajGnRcDs2"
consumer_secret = "RB7p2JVEZxbodmRT3eaA32caonxpo5fS5DOKXcoTxEKJelTZys"
access_token = "997065391644917761-mSZZ6gkTdLEOdDSOAFfu7clvJO4vQPq"
access_token_secret = "MoAMNPZeAmYMwtjaopDrAs1njCwmx9pdCmC7JBP0A1uxF"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def downloadTweets(profiles,result_folder):
    #Inizialize the file when you want to save informations
    for index, item in enumerate(profiles):
        filename = result_folder + "/tweet_" + profiles[index] + ".txt"
        try:
            text_file = open(filename, "r")
            text_file.close
        except FileNotFoundError:
            text_file = open(filename, "w")
            text_file.close

    print("Files inizialized")

    #Download the tweets and save into files
    for index, item in enumerate(profiles):
        screen_name = "@" + profiles[index]
        print("Start downloading: " + screen_name)
        #Warning: if you put a number inside the items you can limit the max tweets download
        try:
            for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name).items():
                filename = result_folder + "tweet_" + profiles[index] + ".txt"
                with open(filename, 'a', encoding='utf8') as text_file:
                    text_file.write(status.text + "\n")
        except Exception as e:
            print("Error downloading tweets: " + str(e))
        
        print("Tweet for " + profiles[index] + " downloaded!")