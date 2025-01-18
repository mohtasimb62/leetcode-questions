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

    Just like the brute force, handle the edge cases carefully. And instead of doing a linear search, do
    a binary search and just eliminate the opposite side where the peak may lie.
'''
def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return 0

    if nums[0] > nums[1]:
        return 0

    if nums[len(nums)-1] > nums[len(nums)-2]:
        return len(nums)-1

    low = 1
    high = len(nums) - 2

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] > nums[mid-1]:   # meaning you are on the left side of the peak
            low = mid + 1
        else:                           # and this means you are on the right side of the peak
            high = mid - 1

    return -1