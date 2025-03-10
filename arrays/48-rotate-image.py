'''
Brute force solution:
    TC: O(n^2),
    SC: O(n^2)

    Create a new matrix that stores the rotated matrix and do the shiftings there. Iterate over the rotated
    matrix and put the elements in the original matrix.
'''
from typing import List

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    rotatedMatrix = []

    for _ in range(n):
        rotatedMatrix.append([0] * n)

    for i in range(0, n):
        for j in range(0, n):
            rotatedMatrix[j][n-1-i] = matrix[i][j]
    
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = rotatedMatrix[i][j]


'''
Optimal approach:
    TC: O(n^2) + O(n^2),
    SC: O(1)

    First transpose the matrix then reverse each row in the matrix
'''
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for i in range(0, n):
        for j in range(i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(0, n):
        matrix[i].reverse()
