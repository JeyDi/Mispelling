import os
import numpy as np
import pandas as pd
from configparser import ConfigParser
from generate_model import transition_matrix
from generate_model import normalize_matrix
from generate_model import emission_matrix
from generate_model import model
from models_IO import io_model
import hidden_markov

# Compute elements of model and create HMM
def generate_model(input_dict, input_layout):

    resource_path = './resources/'
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