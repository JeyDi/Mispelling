import os
import sys
from configparser import ConfigParser
from models_IO import io_model
from generate_model import create_model
from generate_model import model
 
def launch_model_creation(input_dicts,input_layout,input_dict_name):
    
    #Build a merged dictionary to train the model
    input_dict_path = create_model.compute_dictionary(input_dicts)
 
    #Train the model
    model, states, observation, start_prob, transition, emission = create_model.generate_model(
            input_dict_path,input_layout)
            
    # Output the model
    io_model.save_model(input_dict_name, states, observation, start_prob, transition, emission)
 
    return model