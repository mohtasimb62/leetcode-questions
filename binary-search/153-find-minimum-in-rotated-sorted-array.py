'''
Brute force approach:
    TC: O(n),
    SC: O(1)

    Do a linear search and return the index of the smallest element if found.
'''

'''
Optimal approach:
    TC: O(logn),
    SC: O(1)

    This is a modified version of binary search. Find mid and search for the minimum in the sorted area.
    Realize that nums[low] is the minimum in the sorted area. 
'''
import sys
from typing import List


def findMin(self, nums: List[int]) -> int:
    low = 0
    high = len(nums) - 1

    minimum = sys.maxsize

    while low <= high:
        mid = (low + high) // 2

        # this ensures that if the whole list is sorted (possible as it is rotated), nums[low] is the
        # minimum and end the algorithm right here (just a slight optimization).
        if nums[low] <= nums[high]:
            minimum = min(minimum, nums[low])
            break

        if nums[low] <= nums[mid]:
            minimum = min(minimum, nums[low])
            low = mid + 1
        else:
            minimum = min(minimum, nums[mid])
            high = mid - 1

    return minimum