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
    

'''
Better approach:
    TC: O(n*log(m))
    SC: O(1)

    Instead of iterating over each element in the matrix, we can iterate over each row and perform a
    binary search.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(0, row):
            if self.binarySearch(matrix[i], target):
                return True

        return False


    def binarySearch(self, arr, target):
        low = 0
        high = len(arr)

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False
    

'''
Optimal approach:
    TC: O(n+m)
    SC: O(1)

    We have to first figure out where we can start from. Notice that the top right corner and the bottom
    left corner have a property where it's ascending from left to right and continues it from top to 
    bottom. In this case, we start from the top right. If the target is greater than the current element,
    we move down for that property. Else, we move left.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        row = 0
        col = m - 1

        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
            
