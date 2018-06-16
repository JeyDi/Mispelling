
import numpy as np
import pandas as pd

#### FUNCTIONS TO NORMALIZE MATRIX (Stochastic matrix of characters Markov Chain )

#Normalize a list of a matrix
def normalize_list(v):
    norm = np.linalg.norm(v, ord=1)
    if norm == 0:
        norm = np.finfo(v.dtype).eps
    return v / norm

#Normalize Matrix
def normalize_matrix(matrix):
    # Set frequencies in 0:1 interval
    result = np.matrix(np.apply_along_axis(normalize_list, 1, matrix))  
    return result

#Load a dataframe (with Pandas) and apply a normalization
def import_dataframe_normalize(file, func=normalize_matrix):

    dataframe = pd.read_csv(file)
    dataframe = dataframe.drop(dataframe.columns[0], 1)
    matrix = np.matrix(dataframe.as_matrix())
    header = dataframe.columns.values.tolist()

    if func:
        matrix = func(matrix)

    return header, matrix