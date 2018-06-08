import tweetsDownloader2
import tweetsCleaner2
import os

#Check the working directory, go inside the file wd and launch
#TODO: when the solution is complete, don't need this :)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#result folder with the downloaded tweets
result_folder = "../../tweet_library"

#tweeter profile from where you want to download data
profiles = ["realDonaldTrump","rogerfederer","MercedesAMG"]

tweetsDownloader2.downloadTweets(profiles,result_folder)

for profile in profiles:
    #textFileIn = tweetsCleaner2.loadFile(result_folder + "/tweet_" + profile + ".txt")
    #textFileClean = tweetsCleaner2.cleanTweets(textFileIn)
    tweetsCleaner2.preprocessing(profile)

