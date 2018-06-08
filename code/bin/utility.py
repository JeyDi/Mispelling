import csv
import numpy as np
import pandas
import math as mh


def normalize_list(v):
    norm = np.linalg.norm(v, ord=1)
    if norm == 0:
        norm = np.finfo(v.dtype).eps
    return v / norm

def normalize_matrix(matrix):
    # Set frequencies in 0:1 interval
    result = np.matrix(np.apply_along_axis(normalize_list, 1, matrix))  
    return result

#Load a dataframe (with Pandas) and apply a normalization
def import_dataframe(file, func=normalize_matrix):

    dataframe = pandas.read_csv(file)
    dataframe = dataframe.drop(dataframe.columns[0], 1)
    matrix = np.matrix(dataframe.as_matrix())
    header = dataframe.columns.values.tolist()

    if func:
        matrix = func(matrix)

    return header, matrix


#TODO !!!!!!
###################
#Copied...don't know what is it
def create_emission_matrix(errors_distributions):
    size = len(errors_distributions)

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