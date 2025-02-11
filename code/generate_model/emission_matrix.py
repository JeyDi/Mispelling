import numpy as np
import json
import math
import sys
import os
import pandas as pd
 
#Import a keyboard layout matrix
#parameter: layout is a .json file withthe layout defined
def import_layout(layout_file):
 
    layout_matrix = {}
 
    #Read the json file
    with open(layout_file) as data_file:    
        layout_json = json.load(data_file)
 
    #Get the list and calculate the gaussian distribution for every key or char of the matrix
    #1. Error_Model
    for key in layout_json:
            key_neighbors = layout_json[key]
            layout_matrix[key] = gaussian_matrix(key_neighbors)
    
    #2. Gaussian Distribution of the Gaussian 
    return layout_matrix
 

 #Calculate the gaussian matrix of error distribution based on a layout keyboard
def gaussian_matrix(neighbors,mean=0,variance=0.5):
 
    size = len(neighbors)
 
    result = []
 
    half_size = int(math.floor(size // 2))
 
    x = 0
    gaussian = [[0] * size for _ in range(0, size)]
    for i in range(-half_size, half_size + 1):
        y = 0
        for j in range(-half_size, half_size + 1):
            x_dist = (1 / (math.sqrt(2 * math.pi * variance))) * (
                        math.e ** ((-(i - mean) ** 2) / (2 * variance ** 2)))
            y_dist = (1 / (math.sqrt(2 * math.pi * variance))) * (
                        math.e ** ((-(j - mean) ** 2) / (2 * variance ** 2)))
            gaussian[x][y] = x_dist * y_dist
            y += 1
        x += 1
 
    probability = gaussian
    for i in range(0, size):
        for j in range(0, size):
            if neighbors[i][j] is not None:
                result += [(neighbors[i][j], probability[i][j])]
 
    total = sum(prob for neighbor, prob in result)
    normalized_result = [(neighbor, prob / total) for neighbor, prob in result]
 
    return normalized_result
 
#Check if this is correct and try to do some eperiments
def create_emission_matrix(errors_distributions):
    size = len(errors_distributions)
    epsilon=10*10**-5
    emission_matrix = np.full((size, size), epsilon, dtype=float)
    key_list = []
    keys_list = list(errors_distributions.keys())
    keys_list.sort()
    map_to_zero = list(zip(keys_list, range(0, size)))
    map_to_zero = dict(map_to_zero)
 
    for key in errors_distributions:
        key_list += [key]
        for letter, probability in errors_distributions[key]:
            i = map_to_zero[key]
            j = map_to_zero[letter]
            emission_matrix[i, j] = probability
 
    for i in range(0, size):
        emission_matrix[i] = emission_matrix[i] / sum(emission_matrix[i])
 
    result = np.matrix(emission_matrix)
 
    observations = list(errors_distributions.keys())
    observations.sort()
 
    return observations, result
 
 

def generate_emission_matrix(layout_file,out_file=None):
 
    result = import_layout(layout_file)
 
    for key in result:
        a = sum(n for _, n in result[key])
  
    observations, emission = create_emission_matrix(result)
 
    if(not(out_file == None)):
        np.savetxt(out_file, emission, delimiter=';')
 
    return observations, emission