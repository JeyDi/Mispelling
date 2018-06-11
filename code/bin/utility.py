import csv
import numpy as np
import pandas as pd
import math as mh
import logging
import re
from nltk.util import ngrams
from collections import Counter


def normalize_list(v):
    norm = np.linalg.norm(v, ord=1)
    if norm == 0:
        norm = np.finfo(v.dtype).eps
    return v / norm


def normalize_matrix(matrix):
    # Set frequencies in 0:1 interval
    result = np.matrix(np.apply_along_axis(normalize_list, 1, matrix))  
    return result


#Load a dataframe (with Pandas) and apply a normalization
def import_dataframe(file, func=normalize_matrix):

    dataframe = pd.read_csv(file)
    dataframe = dataframe.drop(dataframe.columns[0], 1)
    matrix = np.matrix(dataframe.as_matrix())
    header = dataframe.columns.values.tolist()

    if func:
        matrix = func(matrix)

    return header, matrix


#TODO !!!!!!
###################
#Copied...don't know what is it
def create_emission_matrix(errors_distributions):
    size = len(errors_distributions)
    epsilon=''
    emission_matrix = np.full((size, size), epsilon, dtype=float)
    key_list = []
    keys_list = list(errors_distributions.keys())
    keys_list.sort()
    map_to_zero = list(zip(keys_list, range(0, size)))
    map_to_zero = dict(map_to_zero)

    for key in errors_distributions:
        key_list += [key]
        for letter, probability in errors_distributions[key]:
            i = map_to_zero[key]
            j = map_to_zero[letter]
            emission_matrix[i, j] = probability

    for i in range(0, size):
        emission_matrix[i] = emission_matrix[i] / sum(emission_matrix[i])

    result = np.matrix(emission_matrix)

    observations = list(errors_distributions.keys())
    observations.sort()

    return observations, result


######## CREATE TRANSACTION MATRIX FROM BAG OF WORDS
def is_ascii_char(char):
    char_code = ord(char)
    if (65 <= char_code <= 90) or (97 <= char_code <= 122) or char_code == 32:
        return True

    return False


def split_text_chars(text):
    chars = list(text)
    logging.info("Num of chars {}".format(len(chars)))
    filtered_chars = [char for char in chars if is_ascii_char(char)]
    return filtered_chars

spaces_re = re.compile(r"\s+|\r\n|\r|\n|\t+")


def letters_ngams(files, out_file, n=2):
    chars_count = Counter()

    for file in files:
        with open(file, "rt", encoding="utf8") as inf:
            text = " ".join(inf.readlines())
            text = spaces_re.sub(" ", text)
            chars = split_text_chars(text)
            logging.info("Splitted chars")
            chars_ngram = ngrams(chars, n)
            chars_ngram = [(x, y) for x, y in chars_ngram if not x == y == " "]
            logging.info("Computed n-grams")
            chars_count.update(chars_ngram)
            logging.info("Counted n-grams")

    header, matrix_count = count2matrix(chars_count)

    frequencies = pd.DataFrame(matrix_count, columns=header, index=header)
    frequencies.to_csv(path_or_buf=out_file, encoding="utf8")


def count2matrix(chars_counter):
    logging.info("Number of elements in counter: {}".format(len(chars_counter)))
    logging.info("Number of elements in counter.elements: {}".format(len(list(chars_counter.elements()))))
    # unpacked_elements = sum(chars_counter.elements(), ())
    unpacked_elements = [char for char, out in chars_counter.elements()]
    logging.info("Unpacked elements: {}".format(len(unpacked_elements)))
    header = sorted(set(unpacked_elements))
    logging.info("Sorted header")
    size = len(header)
    values = dict(zip(header, list(range(size))))
    logging.info("Values computed, length {}".format(len(values)))
    matrix = np.ones(shape=(size, size), dtype=int)

    for ngram, value in chars_counter.items():
        source, dest = ngram
        i = values[source]
        j = values[dest]
        matrix[i, j] = value

    return header, matrix


#Method to generate frequency matrix using a given alphabet and a file
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
