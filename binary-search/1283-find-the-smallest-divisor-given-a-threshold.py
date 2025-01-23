import math
from typing import List

'''
Brute force:
    TC: O(max(n)) * O(n)
    SC: O(1)

    Similar to leetcode 875, find the starting and ending index which will act as the divisor. Calculate
    the sum for each divisor and as soon as you find the divisor which gives a sum that is less than or
    equal to the threshold, return that divisor.
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