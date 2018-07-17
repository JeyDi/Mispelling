import os, sys
import re
from os import path
from configparser import ConfigParser
 
pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/config.ini')
 
mentions_re = re.compile(r'@[^\s]*')
url_re = re.compile(r'htt[^\s]*')
symbols_re = re.compile(r'[^A-Za-z ]')
rt_re = re.compile(r'RT ')
space_re = re.compile(r'\s+')
 
#Viterbi prompt single word check (FOR TEST)
def viterbi_check(model,repeat=True):
    while(repeat):
        try_word = input("\nViterbi correction check for test \nWrite 0 if you want to exit\nPlease enter a word to test the correction: ")
        if(try_word.strip() == "0"):
            repeat = False
        elif(try_word.isalpha()):
            repeat = True
            print("Viterbi results for " + try_word)
            print("".join(model.viterbi(list(try_word))))
        else:
            print("Error validating the input string\nPlease insert only characters\nPlease retry\n")
    
    return 0
 
#Word correction function for the GUI CALL
def word_correction(model,word):
    result = model.viterbi(word)
    return result
 
 
 #File correction function to correct a txt file
def file_correction(model,input_file):
    result = ""
    text = ""
    
    try:
        file = open(input_file, 'rt',encoding='UTF-8')
        text = file.read()
        file.close()
    except FileNotFoundError:
        print("File not found, please insert a valid one")
    
    text = clean(text)
    text = text.split(" ")
 
    for i in text:
        text_viterbi = ''.join(model.viterbi(i))
        result = result + text_viterbi + " "
 
    #Remove the first empty space
    result.strip()
 
    print("File corrected")
 
    file_name, _ = path.splitext(path.basename(input_file))
    result_path = export_result(file_name,result)
 
    return result_path
 
#Function to export the perturbation result into a file txt
def export_result(filename,result):
 
 
    result_path = config['config']['export_viterbi_folder']
    
    result_path = path.join(result_path,filename + ".txt")
 
    with open(result_path, "w") as text_file:
        # for i in result:
        #     text_file.write("%s " % i)
        text_file.write(result)
        text_file.close()
 
    print("File corrected with Viterbi saved and exported")
 
    return result_path
 
def clean(tweet):
    tweet = mentions_re.sub(' ', tweet)  # Mentions
    tweet = url_re.sub(' ', tweet)  # URLs
    tweet = symbols_re.sub(' ', tweet)  # Symbols
    tweet = rt_re.sub(' ', tweet)  # RT
    tweet = space_re.sub(' ', tweet)
    tweet = tweet.strip()  # spaces at head or tail
 
    return tweet
 