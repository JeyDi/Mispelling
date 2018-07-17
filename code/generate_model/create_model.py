import os
import sys
import numpy as np
import pandas as pd
from configparser import ConfigParser
from generate_model import transition_matrix
from generate_model import normalize_matrix
from generate_model import emission_matrix
from generate_model import model
from models_IO import io_model
import hidden_markov
 
pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/config.ini')
 
# Compute elements of model and create HMM
def generate_model(input_dict, input_layout):
 
    resource_path = config['config']['resources']
    layout_file = resource_path + input_layout + '.json'
    
    #transition_out_file = library_path + 'model/transition/' +  input_dict + '.csv'
    #emission_out_file = library_path + 'model/emission/' + input_dict + '.csv'
 
    print("Generating Transition Matrix...")
    transitionMatrix = transition_matrix.create_transition_matrix(input_dict)
 
    # Normalizing transition matrix
    header, normalized_transition_matrix = normalize_matrix.normalize_dataframe(transitionMatrix,1) # 1 for normalizing with sklearn method, 0 for the other implementation
 
    transition_dataframe = pd.DataFrame(normalized_transition_matrix, index=header, columns=header)
    
    print("Generating Emission Matrix...")
 
    obs, emissionMatrix = emission_matrix.generate_emission_matrix(layout_file)
    emission_dataframe = pd.DataFrame(emissionMatrix, index=obs, columns=obs)
 
    # Print model elements
    start_prob = np.asmatrix(transition_dataframe.values[0])
    #print("Start Probabilities: {}".format(start_prob))
 
    states =  list(transition_dataframe.index.values)
    #print("States: {}".format(states))
 
    observation = list(transition_dataframe.index.values)
    #print("Observation: {}".format(observation))
 
    transition = np.asmatrix(transition_dataframe.values)
    #print("Transition: {}".format(transition))
 
    emission = np.asmatrix(emission_dataframe.values)
    #print("Emission: {}".format(emission))
 
    #Generate the HMM model using Start prob, Transaction, States, Emissions and Observations
    model = hidden_markov.hmm(states,observation,start_prob,transition,emission)
 
    return model, states, observation, start_prob, transition_dataframe, emission_dataframe
 
 
# Generate model with given elements
def generate_model_with_input(states, observation, start_prob, transition, emission):
 
    # Convert elements format to HMM library
    start_prob =  np.asmatrix(start_prob)
    emission = np.asmatrix(emission.values)
    transition = np.asmatrix(transition.values)
 
    #Generate the HMM model using Start prob, Transaction, States, Emissions and Observations
    model = hidden_markov.hmm(states,observation,start_prob,transition,emission)
 
    return model
 
 
# Build a merged dictionary from input file and returns the path to it
def compute_dictionary(input_dicts):
 
    path_to_dictionaries = config['config']['cleaned_tweets_folder']
    path_to_final_dictionary = config['config']['dictionaries_folder']
 
    # mkdir to dictionary if not exists
    if(not(os.path.exists(path_to_final_dictionary))):
        os.makedirs(path_to_final_dictionary)
 
    # build path to merged dictionary
    for dict in input_dicts:
        path_to_final_dictionary += dict
    
    path_to_final_dictionary += ".txt"
 
    # remove if already existing
    try:
        os.remove(path_to_final_dictionary)
    except OSError:
        pass
 
    # concatenate input_dicts in the final dictionary
    with open(path_to_final_dictionary, "a", encoding="utf8") as output_dict:
 
        for dict in input_dicts:
            dict_path = path_to_dictionaries + dict + ".txt"
 
            with open(dict_path, "rt", encoding="utf-8") as input_dict:
 
                if(not(os.path.exists(dict_path))):
                    print("Dizionario non presente!")
 
                output_dict.write(input_dict.read())
    
    return path_to_final_dictionary
 
 
# Launch the model creation with a custom user message
def generate_model_from_dictionary(input_dicts,input_layout,message):
    
    # Build the dictionary name
    input_dict_name = "".join(input_dicts)
 
    print(message)
 
    #Build a merged dictionary to train the model
    input_dict_path = compute_dictionary(input_dicts)
 
    #Train the model
    model, states, observation, start_prob, transition, emission = generate_model(
            input_dict_path,input_layout)
            
    # Output the model
    io_model.save_model(input_dict_name, states, observation, start_prob, transition, emission)
 
    return model
 
#############################################################################
##################### MAIN MODEL CREATION FUNCTION ##########################
  
def create_model(input_dict,input_layout,force_model_computing = False):
    
    # Build the dictionary name
    input_dict_name = "".join(input_dict)
    print("##################### " + input_dict_name)
    if not force_model_computing:
    # Check if the model already exists
        if io_model.check_model(input_dict_name):
 
            print("Model already existing, retrieving the elements...")
 
            # Import model elements
            states, observation, start_prob, transition, emission = io_model.import_model(
                input_dict_name)
 
            # Rebuild the model
            model = generate_model_with_input(
                states, observation, start_prob, transition, emission)
 
            print("Model restored!")
 
        else:
            message = "Model not existing, ready to compute it!"
            model = generate_model_from_dictionary(input_dict,input_layout,message)
    else:
        message = "Force recomputing enable, computing the model..."
        model = generate_model_from_dictionary(input_dict,input_layout,message)
 
    return model