from collections import defaultdict
from typing import List

'''
With extra space:
    TC: O(n),
    SC: O(n)

    Store the count of consecutive 1's and return the max count
'''
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    findingIndexOfFirstOne = 0
    oneCounts = defaultdict(int)

    for i in range(0, len(nums)):
        if nums[i] == 1:
            findingIndexOfFirstOne = i
            break

    randomKeys = ord("a")
    for i in range(findingIndexOfFirstOne, len(nums)):
        if nums[i] == 1:
            oneCounts[randomKeys] += 1
        else:
            randomKeys += 1

    maxValue = 0
    for value in oneCounts.values():
        maxValue = max(value, maxValue)

    return maxValue


'''
Without extra space:
    TC: O(n),
    SC: O(1)

    Use 2 variables instead of a dictionary - maxCount and currCount. Reset the currCount to 0 every time
    you come at a 0. When you come to a 1, set maxCount to the max of itself and currCount. maxCount should 
    have the count of max consecutive 1s.
'''
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    maxCount = 0
    currCount = 0

    for num in nums:
        if num == 1:
            currCount += 1
            maxCount = max(currCount, maxCount)
        else:
            currCount = 0

    return maxCount