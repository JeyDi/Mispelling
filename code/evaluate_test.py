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

input_dicts = []
# Choose the dicts to append as input
# input_dicts.append('clean_MercedesAMG')
# input_dicts.append('clean_rogerfederer')
input_dicts.append('clean_realDonaldTrump')

input_layout = "qwerty:simple"

#Compute the dictionary
input_dicts = create_model.compute_dictionary(input_dicts)

#Create the model
model = create_model.create_model(input_dicts,input_layout)




##TODO: 2. PERTURB THE FILE

# input_path = "../tweets/cleaned" 
# filename = "clean_realDonaldTrump.txt" 
# input_path = path.join(input_path,filename) 
# print(input_path) 
 
perturbation_path = perturbation.word_perturbation(input_file=input_dicts,string=None,clean=0,words_percentage=50,string_percentage=50) 


##TODO: 3. CORRECT THE FILE

#Check the input with viterbi
# perturbed_file_path = "../tweets/perturbed"
# perturbed_file_path = path.join(perturbed_file_path,filename)
correction_path = viterbi_compute.file_correction(model,perturbation_path)



##TODO: 4. EVALUATE THE FILE
# dict_file = "../tweets/"
evaluate.evaluate(input_dicts,perturbation_path,correction_path)