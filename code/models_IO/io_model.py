import numpy
import os
import csv
import pandas as pd

main_directory = "../saved_models/"

# Export a model in a serie of CSV file
def save_model(dict, states, obs, start_prob, transition, emission):

    # Check if the directory for this dict already exists
    directory = main_directory + dict

    # Eventually create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_raw_directory = directory + "/" + dict + "_"

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


# Check if a model is have been already computed
def check_model(dict):
    return os.path.exists(main_directory + dict)


# Import already computed model elemetns
def import_model(dict):

    raw_dir = main_directory + dict + "/" + dict + "_"

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