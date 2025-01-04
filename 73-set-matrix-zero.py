'''
Brute force approach:
    TC: O(n*m) + O(n+m) + O(n*m) => O(n^3)
    SC: O(1)

    Iterate the matrix and mark the rows and cols with an "X". Iterate the matrix again and mark every "X"
    with 0s
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    self.markRow(i, matrix)
                    self.markCol(j, matrix)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == "X":
                    matrix[i][j] = 0

        print(matrix)

    def markRow(self, ithRow, matrix):
        for i in range(0, len(matrix[0])):
            if matrix[ithRow][i] != 0:
                matrix[ithRow][i] = "X"

    def markCol(self, jthCol, matrix):
        for i in range(0, len(matrix)):
            if matrix[i][jthCol] != 0:
                matrix[i][jthCol] = "X"



'''
Better approach:
    TC: O(n^2),
    SC: O(n) + O(m)

    Instead of iterating the matrix 3 times, we reduce that to 2 by using extra space. We create 2 extra lists
    which keep track of the 0s (just like the brute force approach). Finally, in the second iteration, if either
    of the lists is marked, we put a 0 in that position in the matrix.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowMarks = [0] * len(matrix)
        colMarks = [0] * len(matrix[0])

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    rowMarks[i] = 1
                    colMarks[j] = 1

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if rowMarks[i] == 1 or colMarks[j] == 1:
                    matrix[i][j] = 0