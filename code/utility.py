import csv
import numpy as np
import pandas as pd
import math as mh
import logging
import re
from nltk.util import ngrams
from collections import Counter


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
