import os
import sys
from os import path, listdir
from configparser import ConfigParser
from models_IO import io_model
from generate_model import create_model
from generate_model import model
from generate_model import viterbi_compute
from words_perturbation import perturbation
from evaluate_correction import evaluate

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
# input_dicts.append('clean_MercedesAMG')
# input_dicts.append('clean_rogerfederer')
input_dicts.append('clean_realDonaldTrump')

input_layout = "qwerty_simple"

#Compute the dictionary
# input_dicts = create_model.compute_dictionary(input_dicts)

#Create the model
model = create_model.create_model(input_dicts,input_layout)

input_dicts = "".join(input_dicts)
input_path = "..\\tweets\\cleaned"
cleaned_input_dicts = os.path.join(input_path,input_dicts+".txt")

##TODO: 2. PERTURB THE FILE
print("### PERTURB THE FILE ###")
# input_path = "../tweets/cleaned" 
# filename = "clean_realDonaldTrump.txt" 
# input_path = path.join(input_path,filename) 
# print(input_path) 
 
perturbation_path = perturbation.word_perturbation(input_file=cleaned_input_dicts,string=None,clean=0,words_percentage=10,string_percentage=10) 


##TODO: 3. CORRECT THE FILE
print("### START CORRECTING THE FILE ###")
#Check the input with viterbi
# perturbed_file_path = "../tweets/perturbed"
# perturbed_file_path = path.join(perturbed_file_path,filename)

# ATTENTION: use this only if you want to calculate a new correction!!!!! otherwise use the path directly (more fast)!!!!
# correction_path = viterbi_compute.file_correction(model,perturbation_path)[1]
correction_path = "../tweets/corrected/clean_realDonaldTrump.txt"


##TODO: 4. EVALUATE THE FILE
# dict_file = "../tweets/"
print("### START EVALUATING THE FILE ###")
print("input: " + cleaned_input_dicts)
print("perturbation: " + perturbation_path)
print("correction: " + correction_path )
evaluate.evaluate(cleaned_input_dicts,perturbation_path,correction_path)