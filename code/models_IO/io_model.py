import numpy
import os
import sys
import csv
import pandas as pd
import shutil
from configparser import ConfigParser
 
pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/config.ini')
 
# Folder with saved models
main_directory = config['config']['saved_model_folder']
 
# Export a model in a serie of CSV file
def save_model(dict, states, obs, start_prob, transition, emission):
 
    # Check if the directory for this dict already exists
    directory = os.path.join(main_directory, dict)
 
    # Eventually create it
    if not os.path.exists(directory):
        os.makedirs(directory)
 
    try:
 
        file_raw_directory = os.path.join(directory, dict + "_")
 
        # Dump states to CSV
        states_file = open(file_raw_directory + "states.csv", "w")
 
        for state in states:
            states_file.write(state + ";")
 
        states_file.close()
 
        # Dump observations to csv
        obs_file = open(file_raw_directory + "obs.csv", "w")
 
        for ob in obs:
            obs_file.write(ob + ";")
 
        obs_file.close()
 
        # Dump start probability to CSV
        numpy.savetxt(file_raw_directory + "start_prob.csv", start_prob, delimiter=";")
 
        # Dump transition matrix to CSV
        transition.to_csv(file_raw_directory + "transition.csv", index=True, header=True, sep=';')
 
        # Dump emission matrix to CSV
        emission.to_csv(file_raw_directory + "emission.csv", index=True, header=True, sep=';')

    except OSError:
        if os.path.exists(directory):
            shutil.rmtree(directory, ignore_errors=True)
            raise
 
 
# Check if a model is have been already computed
def check_model(dict):
    return os.path.exists(main_directory + dict)
 
 
# Import already computed model elemetns
def import_model(dict):
 
    # Check if the directory for this dict already exists
    directory = os.path.join(main_directory, dict)
 
    raw_dir = os.path.join(directory, dict + "_")
 
    # Import start_prob
    file = open(raw_dir + 'start_prob.csv', 'r')
    prob = file.readline()
    probs = prob.split(";")
    start_prob = []
 
    for prob in probs:
        start_prob.append(float(prob))
 
    # Import transition
    transition = pd.read_csv(raw_dir + 'transition.csv', ";", header=0, index_col=0)
 
    # Import emission
    emission = pd.read_csv(raw_dir + 'emission.csv', ";", header=0, index_col=0)
 
    # Import states
    states = list(transition.index.values)

    # Import obs
    observations = list(emission.index.values)
    
    return states, observations, start_prob, transition, emission