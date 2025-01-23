import math
from typing import List

'''
Brute force:
    TC: O(max(n)) * O(n)
    SC: O(1)

    Similar to leetcode 875, find the starting and ending index which will act as the divisor. Note that
    the ending index here is the highest element in the list. Why? Because after the highest element, the
    result of the sum is the same, no matter how high you go.
    
    Calculate the sum for each divisor and as soon as you find the divisor which gives a sum that is less 
    than or equal to the threshold, return that divisor.
'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        highest = max(nums)
        ans = 0

        for i in range(1, highest+1):
            currSum = self.calculateSum(nums, i)

            if currSum <= threshold:
                ans = i
                return ans

        return -1

    def calculateSum(self, arr, divisor):
        res = 0
        for i in range(0, len(arr)):
            res += math.ceil(arr[i] / divisor)

        return res
    

'''
Optimal approach:
    TC: O(max(n)) * O(logn)
    SC: O(1)

    Just like the brute force, but instead of doing a linear iteration of calculating the sum for each
    divisor, do a binary search to trim down the search space. Return as soon as you find the divisor
    that is less than or equal to the threshold.
'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            currSum = self.calculateSum(nums, mid)
            
            if currSum <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def calculateSum(self, arr, divisor):
        res = 0
        for i in range(0, len(arr)):
            res += math.ceil(arr[i] / divisor)

        return res