from typing import List

'''
Brute force:
    TC: O(n),
    SC: O(1)

    Do a linear search and find the index of the element that has is greater than both its left and right
    elements. Handle the edge cases carefully.
'''


def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    if nums[0] > nums[1]:
        return 0

    if nums[len(nums)-1] > nums[len(nums)-2]:
        return len(nums)-1

    for i in range(1, len(nums)-1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i

    return -1


'''
Optimal approach (using binary search):
    TC: O(logn),
    SC: O(1)
'''