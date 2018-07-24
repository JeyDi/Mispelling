import os
import sys
import math
from os import path, listdir
from configparser import ConfigParser
from models_IO import io_model
from generate_model import create_model
from generate_model import model
from generate_model import viterbi_compute
from words_perturbation import perturbation
from evaluate_correction import evaluate
from evaluate_correction import evaluate_utility

# Path to this file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/config.ini')


##TODO: 1. CREATE THE MODEL
print("### CREATE THE MODEL ###")
input_dicts = []
# Choose the dicts to append as input
input_dicts.append('clean_MercedesAMG')
input_dicts.append('clean_rogerfederer')
input_dicts.append('clean_realDonaldTrump')
input_dicts.append('clean_Forbes')

input_layout = "qwerty_simple"

#Create the model
model = create_model.create_model(input_dicts,input_layout)

###TODO: ASK THE PATH TO THE USER



##TODO: 2. PERTURB THE FILE
print("\n### PERTURB THE FILE ###")
input_path = "../tweets/cleaned"

#filename= "clean_test.txt"
# filename = "clean_movie_lines.txt" 
# cleaned_input_dicts = path.join(input_path,filename)

##### Uncomment this line to use n percent of dictionary######
cleaned_input_dicts = evaluate_utility.obtain_n_percent(path = "../tweets/dictionaries/" + "".join(input_dicts) + ".txt", percent = 30)

perturbation_path = perturbation.word_perturbation(input_file=cleaned_input_dicts,string=None,clean=0,words_percentage=10,string_percentage=10) 

##TODO: 3. CORRECT THE FILE
print("\n### START CORRECTING THE FILE ###")
#Check the input with viterbi
#perturbed_file_path = "../tweets/perturbed"
#perturbation_path = path.join(perturbed_file_path,filename)

# ATTENTION: use this only if you want to calculate a new correction!!!!! otherwise use the path directly (more fast)!!!!
correction_path = viterbi_compute.file_correction(model,perturbation_path)[1]
#correction_path = "../tweets/corrected/clean_realDonaldTrump.txt"

##TODO: 4. EVALUATE THE FILE
# dict_file = "../tweets/"
print("\n### START EVALUATING THE FILE ###")
result=evaluate.evaluate(cleaned_input_dicts,perturbation_path,correction_path)
print("Triple results: " + str(result))
print("Perturbed corrected ratio: " + str(evaluate.perturbed_corrected_ratio(result)))
precision = evaluate.precision(result)
print("Precision: " + str(precision))
print("Not perturbed not corrected ratio: " + str(evaluate.not_perturbed_not_corrected_ratio(result)))
print("Accuracy: " + str(evaluate.accuracy(result)))
recall = evaluate.recall(result)
print("Recall: " + str(recall))
print("F1-measure: " + str(evaluate.F1_measure(result, precision, recall)))