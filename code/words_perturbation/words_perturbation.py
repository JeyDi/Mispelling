import os
import re
import math
import random
from random import randint
from string import ascii_letters
from os import path, listdir
from configparser import ConfigParser
 
config = ConfigParser()
config.read('./Code/config.ini')
 
#Function to basic clean and preprocess input string or text
def clean_text(text):
    
    #Some usefull regexp
    MENTIONS = re.compile(r'@[^\s]*')
    URL = re.compile(r'htt[^\s]*')
    SYMBOLS = re.compile(r'[^A-Za-z ]')
    RT = re.compile(r'RT ')
    SPACE = re.compile(r'\s+')
 
    #Text preprocessing using the REGEXP
    text = MENTIONS.sub(' ', text)  # Mentions
    text = URL.sub(' ', text)  # URLs
    text = SYMBOLS.sub(' ', text)  # Symbols
    text = RT.sub(' ', text)  # RT
    text = SPACE.sub(' ', text)
    result_text = text.strip()  # spaces at head or tail
 
    return result_text
 
 
#Perturb the word by a certain percentage
def perturb_word(word,percentage):
    
    string_list = list(word)
    string_count = len(string_list)
    string_to_perturb = int(math.floor(string_count*percentage/100))
 
    for s in range(string_to_perturb):
        string_index = randint(0,string_count-1)
        string_list[string_index] = random.choice(ascii_letters)
    
    #Re assemble the string
    word = "".join(string_list)
 
    return word
 
 
 
#Main function for the perturbation algorithm
def perturb(input_words,words_percentage=10,string_percentage=10):