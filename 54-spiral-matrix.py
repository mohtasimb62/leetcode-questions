'''
No brute-better-optimal approach for this problem. Just have to implement it in the most cleanest way.
    TC: O(n*m),
    SC: O(n*m) for the result list
'''
from typing import List

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    n = len(matrix)
    m = len(matrix[0])
    ans = []

    # 4 pointers - they are determined by the "edges" or "border" of the matrix
    left = 0
    right = m - 1
    top = 0
    bottom = n - 1

    while (left <= right and top <= bottom):
        # right
        for i in range(left, right+1):
            ans.append(matrix[top][i])
        
        top += 1

        # bottom
        for i in range(top, bottom+1):
            ans.append(matrix[i][right])

        right -= 1
    
        # left
        if top <= bottom:
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])

            bottom -= 1

        # top
        if left <= right:
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])

            left += 1

    return ans