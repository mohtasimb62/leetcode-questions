from typing import List

'''
Brute force:
    TC: O(n*m) -> O(n^2) where n is the number of rows and m is the number of columns,
    SC: O(1)

    This is a brute force approach where we are iterating over each element in the matrix and checking 
    if the target is present in the matrix.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == target:
                    return True

        return False