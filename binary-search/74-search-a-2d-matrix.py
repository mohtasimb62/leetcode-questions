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
            if target >= matrix[i][0] and target <= matrix[i][col-1]:
                return self.binarySearch(matrix[i], target)

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
    TC: O(log(n*m))
    SC: O(1)

'''


'''
My solution:
    TC: O(log(n) + log(m))
    SC: O(1)

    First locate in which row the target is in using binary search. After location which row, perform
    a binary search on that row to find the target.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        low = 0
        high = row - 1

        while low <= high:
            mid = (low + high) // 2
            
            # check if the target is in the current row
            if target >= matrix[mid][0] and target <= matrix[mid][col-1]:
                return self.binarySearch(matrix[mid], target)
            
            # if the target is less than the first element of the current row, then the target is in the 
            # previous rows
            elif target < matrix[mid][0]:
                high = mid - 1
            
            # if the target is greater than the last element of the current row, then the target is in the rows
            # after the current row.
            else:
                low = mid + 1

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