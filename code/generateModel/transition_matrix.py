import csv
import numpy as np
import pandas as pd
import math as mh
import logging
import re
from nltk.util import ngrams
from collections import Counter


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

###MAIN FUNCTIONS TO CREATE TRANSITION LETTERS NGRAM MATRIX
def letters_ngams(files, out_file, n=2):
    chars_count = Counter()

    for file in files:
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
    frequencies.to_csv(path_or_buf=out_file, encoding="utf8")


#Count the elements in the array of character
def count2matrix(chars_counter):
    logging.info("Number of elements in counter: {}".format(len(chars_counter)))
    logging.info("Number of elements in counter.elements: {}".format(len(list(chars_counter.elements()))))
    # unpacked_elements = sum(chars_counter.elements(), ())

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