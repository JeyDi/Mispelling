import csv
import re
import os
import sys
import string
import nltk
from nltk.tokenize import word_tokenize
from configparser import ConfigParser
 
#Some usefull regexp
MENTIONS = re.compile(r'@[^\s]*')
URL = re.compile(r'htt[^\s]*')
SYMBOLS = re.compile(r'[^A-Za-z ]')
RT = re.compile(r'RT ')
SPACE = re.compile(r'\s+')

pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/../config.ini')
 
#result folder with the downloaded tweets
input_folder = config['twitter']['twitter_raw_tweets_folder']
output_folder = config['twitter']['twitter_cleaned_tweets_folder']
 
#Load the file and launch the preprocessing
def loadFile(inputfile):
    
    text = ""

    try:
        file = open(inputfile, 'rt',encoding='UTF-8')
        text = file.read()
        file.close()
    except FileNotFoundError:
        print("File not found, please insert a valid one")
 
    return(text)
 
 
#TODO: need to implement a csv and a txt outfile
def writeFile(outfile,text,file_type):
    print("Final file generated")
    #Output the file to csv
    if(file_type == "csv"):
        outfile = outfile + ".csv"
        with open(outfile, "wt", encoding="utf8", newline="") as out_file:
            writer = csv.writer(out_file, delimiter="\t")
            for tweet_id in text:
                writer.writerow([tweet_id, text[tweet_id]])
    #Output the file to txt
    elif(file_type == "txt"):
        outfile = outfile + ".txt"
        with open(outfile, 'a', encoding='utf8') as text_file:
            text_file.write(text + "\n")
    #error if the extension is not valid            
    else:
        print("No file extension valid")
    
    print("File successfully writed")
 
#Standard preprocessing with regexp
def cleanTweets(text):
 
    #Text preprocessing using the REGEXP
    text = MENTIONS.sub(' ', text)  # Mentions
    text = URL.sub(' ', text)  # URLs
    text = SYMBOLS.sub(' ', text)  # Symbols
    text = RT.sub(' ', text)  # RT
    text = SPACE.sub(' ', text)
    final_text = text.strip()  # spaces at head or tail
 
    return(final_text)
 
 
#Another way to do the preprocessing using nltk and some others library
def cleanTweetsNLTK(text):
    
    #Tokenize the words
    tokens = word_tokenize(text)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    
    return(words)
    
    
def preprocessing(profile):
    
    print("Start preprocessing")
 
    input_file = os.path.join(input_folder, "raw_%s.txt" % profile)
 
    text = loadFile(input_file)
 
    #call the text preprocessing
    result_text = cleanTweets(text)
 
    #write the outfile
    outfile = os.path.join(output_folder, "clean_%s" % profile)
    file_type = "txt"
    writeFile(outfile,result_text,file_type)
 
    print("Finish preprocessing tweets")