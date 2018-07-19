import csv
import numpy as np
import pandas as pd
import math as mh
import logging
import json
import re
import os
import sys
from nltk.util import ngrams
from collections import Counter
from configparser import ConfigParser
 
 
pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/config.ini')
 
layout_file = config['config']['layout_file']
 
 
######## CREATE TRANSITION MATRIX FROM BAG OF WORDS
 
#Check if the char is ascii and return only the ascii chars
def is_ascii_char(char):
    char_code = ord(char)
    if (65 <= char_code <= 90) or (97 <= char_code <= 122) or char_code == 32:
        return True
 
    return False
 
#Split the text (corpus) in a list of chars
def split_text_chars(text):
    #Split all the char in the corpus (long list with character and spaces)
    chars = list(text)
    logging.info("Num of chars {}".format(len(chars)))
    #Keep only the Ascii text chars
    filtered_chars = [char for char in chars if is_ascii_char(char)]
 
    return filtered_chars
 
spaces_re = re.compile(r"\s+|\r\n|\r|\n|\t+")
 
# Function to add columns and rows for letters not met in training
def complete_matrix(frequencies, dict):
 
    # Get letters already met
    rows = list(frequencies.index)
 
    # For each letter in the dictionary check if met already met
    for key in dict:
        found = False
        for row in rows:
            if (key == row):
                found = True
                break
 
        # If not found add a 1-row and 1-column with the letter as key
        if (not(found)):
            frequencies[key] = 1
            frequencies.loc[key] = [1 for x in range(0, frequencies.shape[1])]
 
    # Sort the DF by rows
    sorted_rows = frequencies.sort_index(axis=0)
    # Sort the DF by columns
    sorted = sorted_rows.sort_index(axis=1)
 
    return sorted
 

 ###MAIN FUNCTIONS TO CREATE TRANSITION LETTERS NGRAM MATRIX
def create_transition_matrix(file, out_file=None, n=2):
    chars_count = Counter()
 
    with open(file, "rt", encoding="utf8") as inf:
        text = " ".join(inf.readlines())
 
        #Clear \n characters
        text = spaces_re.sub(" ", text)
 
        #Split text in char
        chars = split_text_chars(text)
        logging.info("Splitted chars")
 
        #Split with ngrams the text into subarray with dimension = n
        chars_ngram = ngrams(chars, n)
        chars_ngram = [(x, y) for x, y in chars_ngram if not x == y == " "]
        logging.info("Computed n-grams")
            
        #Start counting
        chars_count.update(chars_ngram)
        logging.info("Counted n-grams")
 
    header, matrix_count = count2matrix(chars_count)
 
    frequencies = pd.DataFrame(matrix_count, columns=header, index=header)
 
    #Read the json file
    with open(layout_file) as data_file:    
        layout_json = json.load(data_file)
 
    number_of_key_in_dict = 0
 
    for key in layout_json:
        number_of_key_in_dict =+ 1    
 
    if(number_of_key_in_dict != frequencies.shape[0]):
        frequencies = complete_matrix(frequencies, layout_json)
 
    if (not(out_file == None)):
        frequencies.to_csv(out_file, sep=";", encoding="utf-8")
 
    return frequencies
 
 
#Count the elements in the array of character
def count2matrix(chars_counter):
    logging.info("Number of elements in counter: {}".format(len(chars_counter)))
    logging.info("Number of elements in counter.elements: {}".format(len(list(chars_counter.elements()))))
 
    #Get all the elements in the counter
    unpacked_elements = [char for char, out in chars_counter.elements()]
    logging.info("Unpacked elements: {}".format(len(unpacked_elements)))
 
    #Get the list of elements (characters)
    header = sorted(set(unpacked_elements))
    logging.info("Sorted header")
 
    #Get the size
    size = len(header)
 
    #Create an array of values (indexes) based on the header array (character)
    #For exampe: A = 1
    values = dict(zip(header, list(range(size))))
    logging.info("Values computed, length {}".format(len(values)))
 
    #Create the final int matrix of ones with nrows and ncols equals to the size (character array length)
    matrix = np.ones(shape=(size, size), dtype=int)
 

    for ngram, value in chars_counter.items():
        source, dest = ngram
        i = values[source]
        j = values[dest]
        # filling up the matrix with weights                                                
        matrix[i, j] = value
 
    return header, matrix