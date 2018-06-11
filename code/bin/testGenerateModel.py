from utility import createFrequencyMatrix, letters_ngams
import os
from configparser import ConfigParser

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


config = ConfigParser()
config.read('../config.ini')

inputFile = '../../tweet_library/tweet_result_rogerfederer.txt'
outFile = '../../tweet_library/tweet_result.txt'

#resultMatrix = createFrequencyMatrix(inputFile)

n = 2
fileList = [inputFile]
letters_ngams(fileList, outFile, n)


