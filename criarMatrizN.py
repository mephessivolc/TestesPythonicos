"""
    Este programa resolve o problema de em uma matriz NxN encontrar N casas não
    alinhadas
"""

import numpy as np
import random

def create_matrix(n):
    """
        Constroi uma matriz NxN de zeros
    """
    random_first_line_place = random.randint(0,n-1)
    random_first_colunm_place = random.randint(0,n-1)
    matrix = np.zeros((n,n))
    matrix[random_first_line_place][random_first_colunm_place] = 1

    print(matrix)

    return matrix

# def search_place(n):
#     matrix = create_matrix(n)
#
#     for i in range(matrix):
#         for j in range(matrix[i]):

create_matrix(8)
