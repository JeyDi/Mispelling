import os
from configparser import ConfigParser
from models_IO import io_model
from generate_model import create_model
from generate_model import model
from generate_model import viterbi_compute

# Path to this file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

config = ConfigParser()
config.read('../config.ini')

# # Set to true for recomputing the model even if it exists
# force_model_computing = False

input_dicts = []
# Choose the dicts to append as input
input_dicts.append('clean_MercedesAMG')
input_dicts.append('clean_rogerfederer')
input_dicts.append('clean_realDonaldTrump')

#Create the model
model = create_model.create_model(input_dicts)

#Check the input with viterbi
viterbi_compute.viterbi_check(model)
