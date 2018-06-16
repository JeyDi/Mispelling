import os
from configparser import ConfigParser
from generateModel import transition_matrix
from generateModel import normalize_matrix

#Path to this file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


config = ConfigParser()
config.read('../config.ini')

inputFile = '../tweet_library/tweet_result_rogerfederer.txt'
outFile = '../tweet_library/tweet_result_transition_matrix.txt'

#resultMatrix = createFrequencyMatrix(inputFile)


#Create transition matrix
n = 2
fileList = [inputFile]
transition_matrix.letters_ngams(fileList, outFile, n)

#TODO: Need to normalize the output file
normalizeMatrix = normalize_matrix.import_dataframe_normalize(outFile)
print(normalizeMatrix)
#TODO: Save the matrix normalized

#TODO: Create emission matrix


#TODO: Generate the HMM model
#Using Transaction, States, Emissions and Observations

