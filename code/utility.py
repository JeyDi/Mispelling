import csv
import numpy as np
import pandas as pd
import math as mh
import logging
import re
import os
from nltk.util import ngrams
from collections import Counter

# Build a merged dictionary from input file and returns the path to it
def compute_dictionary(input_dicts):

    path_to_dictionaries = "../tweet_library/"
    path_to_final_dictionary = "../dictionaries/"

    # mkdir to dictionary if not exists
    if(not(os.path.exists(path_to_final_dictionary))):
        os.makedirs(path_to_final_dictionary)

    # build path to merged dictionary
    for dict in input_dicts:
        path_to_final_dictionary += dict
    
    path_to_final_dictionary += ".txt"

    # remove if already existing
    try:
        os.remove(path_to_final_dictionary)
    except OSError:
        pass

    # concatenate input_dicts in the final dictionary
    with open(path_to_final_dictionary, "a", encoding="utf8") as output_dict:

        for dict in input_dicts:
            dict_path = path_to_dictionaries + dict + ".txt"

            with open(dict_path, "rt", encoding="utf-8") as input_dict:

                if(not(os.path.exists(dict_path))):
                    print("Dizionario non presente!")

                output_dict.write(input_dict.read())
    
    return path_to_final_dictionary


##########-----TEMP-----#########
#My Method to generate frequency matrix using a given alphabet and a file
def createFrequencyMatrix(file):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    finalList = []
    with open(file, "rt", encoding="utf8") as myFile:
        for char in alphabet: 
            text = myFile.read()
            text = text.lower()
            curstring = text
            letters = []

            while len(curstring) > 0:
                arr = curstring.split(char, 1)
                if len(arr) == 1:
                    break
                letters.append(arr[1][0])
                curstring = arr[1]

            #Remove the space
            while ' ' in letters:
                letters.remove(' ')

            freq = {}
            
            for l in letters:
                if l in freq.keys():
                    continue  
                freq[l] = letters.count(l) / len(letters)

            finalList.append(freq)

        #Create the final dataframe with the letters
        myDict = pd.DataFrame(finalList)
        print(myDict)

    return myDict
