'''
With extra space:
    TC: O(n),
    SC: O(n)

    Store the 0's, 1's, and 2's (in that order) to a new list and for every i, nums[i] = newArr[i]
'''

from typing import List

def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    newArr = []

    # finding 0s
    for num in nums:
        if num == 0:
            newArr.append(num)

    # finding 1s
    for num in nums:
        if num == 1:
            newArr.append(num)

    # finding 2s
    for num in nums:
        if num == 2:
            newArr.append(num)
    

    for i in range(0, len(nums)):
        nums[i] = newArr[i]


'''
Optimal approach (Dutch National Flag):
    TC: O(n),
    SC: O(1)
'''

def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # swapping nums[low] and nums[mid]
            tmp = nums[low]
            nums[low] = nums[mid]
            nums[mid] = tmp

            # update pointers
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1
        else:
            # swapping nums[mid] and nums[high]
            tmp = nums[mid]
            nums[mid] = nums[high]
            nums[high] = tmp

            # update pointers
            high -= 1