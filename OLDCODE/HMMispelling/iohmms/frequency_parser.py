import csv
import numpy as np
import math as mh
import pandas


def normalize_matrix(matrix):
    result = np.matrix(np.apply_along_axis(normalize_list, 1, matrix))  # Set frequencies in 0:1 interval
    return result


def load_dataframe(file, func=normalize_matrix):

    dataframe = pandas.read_csv(file)
    dataframe = dataframe.drop(dataframe.columns[0], 1)
    matrix = np.matrix(dataframe.as_matrix())
    header = dataframe.columns.values.tolist()

    if func:
        matrix = func(matrix)

    return header, matrix


def load_probabilities(file):
    i = 0
    probability = np.matrix([])

    with open(file, 'r', encoding="utf8") as csv_file:

        reader = csv.reader(csv_file)
        header = next(reader)[1:]  # Skip of header row

        for row in reader:
            row_values = row[1:]  # Remove first column
            row_float = [float(k) for k in row_values]  # Casting to float
            probability = np.matrix(row_float) if i == 0 else np.vstack([probability, row_float])
            i += 1

        if probability[0, :].sum != 1:
            probability = normalize_distribution(probability)

    return header, probability


def normalize_distribution(matrix):
    r = matrix.shape[0]
    c = matrix.size
    result = np.matrix([])

    if r == 1:  # Case First letter frequency
        for i in np.nditer(matrix):
            element = i / 100  # Apply the function
            result = np.hstack((result, [[element]]))  # Append the new element
    else:  # Other cases, nxn frequency matrix
        for i in np.nditer(matrix):
            if i == 0:
                element = 0  # To avoid e^0 = 1 the frequency equal to 0 should not be transformed
            else:
                element = round(mh.exp(i), 0)  # Apply the function if the element in matrix is not 0
            result = np.hstack((result, [[element]]))  # Append the new element

        slicer = int(c / r)
        result = result.reshape(1, r, slicer)  # reshape frequencies in original shape

        result = np.matrix(np.apply_along_axis(normalize_list, 1, result))  # Set frequencies in 0:1 interval
        # matrix_norm = matrix_norm.round(3)

    return result


def normalize_list(v):
    norm = np.linalg.norm(v, ord=1)
    if norm == 0:
        norm = np.finfo(v.dtype).eps
    return v / norm
