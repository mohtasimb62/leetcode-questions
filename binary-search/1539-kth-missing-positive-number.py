from typing import List

'''
Brute Force:
    TC: O(n),
    SC: O(1)
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1  # shifting k
            else:
                break
        return k