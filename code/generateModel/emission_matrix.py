import numpy as np

#Import a keyboard layout matrix
#parameter: layout is a .json file withthe layout defined
def import_layout(layout):

    layout_matrix = {}

    #TODO: layout_matrix as a dataframe
    return layout_matrix


#Calculate the gaussian matrix of error distribution based on a layout keyboard
def gaussian_matrix(matrix):
    mean = 0
    variance = 0,5

    #TODO: _distribution_
    #TODO: _single_dist_
    #TODO: _2d_gaussian_distribution_

    return matrix


#Check if this is correct and try to do some eperiments
def create_emission_matrix(errors_distributions):
    size = len(errors_distributions)
    epsilon=''
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
