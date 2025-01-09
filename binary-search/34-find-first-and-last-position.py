'''
Brute force approach:
    TC: O(n),
    SC: O(1)

    Just do a linear search and find the first and last occurance of target in nums array.
'''

def searchRange(self, nums: List[int], target: int) -> List[int]:
    result = [-1, -1]

    for i in range(0, len(nums)):
        if nums[i] == target:
            if result[0] == -1:
                result[0] = i
            result[1] = i

    return result