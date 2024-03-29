# -*- coding: utf-8 -*-
"""GaussJordanElimination.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E9dBo_JdJ_fRdT-8DlbBFK36q3h-ibGH
"""

print("i am going to start google colab")
# shortcut key is ctrl + enter to run a single cell

print("this is a new cell which can be accessed by shift+enter")

# Doing Gauss-jordan elimination
# The outline of the algorithm.
# we will have a loop from 0 to n-1 to index the pivot rows and columns
# store the pivot element and run the j loop from index k to n-1 for the columns of pivot row
# i loop from 0 to n-1 to index the subtracted rows
# there will be some edge cases
# if the pivot element a(k,k) is 0 then

def gauss_jordan_elimination(a, b):
    # Combine matrices A and B to form augmented matrix [A|B]
    aug_matrix = [row_a + row_b for row_a, row_b in zip(a, b)]

    N = len(aug_matrix)
    M = len(aug_matrix[0])

    for i in range(N):
        # Check if the pivot element is zero and swap rows if necessary
        if aug_matrix[i][i] == 0:
            for j in range(i + 1, N):
                if aug_matrix[j][i] != 0:
                    aug_matrix[i], aug_matrix[j] = aug_matrix[j], aug_matrix[i]
                    break
            else:
                # If no non-zero pivot is found, the matrix might be singular
                raise ValueError("Matrix is singular, cannot proceed with elimination.")

        # row operations for the pivot elements
        for j in range(N):
            if i != j:
                ratio = aug_matrix[j][i] / aug_matrix[i][i]
                for k in range(M):
                    aug_matrix[j][k] -= ratio * aug_matrix[i][k]

    # Now we have to normailize each row.
    for i in range(N):
        divisor = aug_matrix[i][i]
        for j in range(M):
            aug_matrix[i][j] /= divisor

    # return the augmented_matrix and the answer will be stored on the last
    return aug_matrix





# writing a print matrix function just to check the output.
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(f'{element:10}', end=' ')
        print()


# Example usage
matrix_a = [
    [0,2,0,1],
    [2,2,3,2],
    [4,-3,0,1],
    [6,1,-6,-5]
]

matrix_b = [
    [0],
    [-2],
    [-7],
    [6]
]

print("Matrix A:")
print_matrix(matrix_a)

print("\nMatrix B:")
print_matrix(matrix_b)

result = gauss_jordan_elimination(matrix_a, matrix_b)

print("\nAugmented Matrix [A|B] after Gauss-Jordan Elimination:")
print_matrix(result)

"""

> Indented block

"""