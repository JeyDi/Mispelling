import csv
import os
import model
import utility

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



def train(input_tweet_path,input_frequency_path):

    #Load using the letters frequency
    states, transition = utility.import_dataframe(input_frequency_path)




#TODO:Generate a global normalized frequencies matrix
#input_frequency_path = "../../resources/Hybrid_en_US_letters_frequencies.txt"
