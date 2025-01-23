from typing import List

# This problem NEEDS extra space - i.e. it is not possible to achieve O(1) SC.

'''
Brute force approach:
    TC: O(n),
    SC: O(n)

    Store the positive and negative elements in a separate list and add the positive first and then negative
    element to the result list.
'''

def rearrangeArray(self, nums: List[int]) -> List[int]:
    positiveElements = []
    negativeElements = []

    result = []

    for i in range(0, len(nums)):
        if nums[i] > 0:
            positiveElements.append(nums[i])
        else:
            negativeElements.append(nums[i])

    for i in range(0, len(positiveElements)):
        result.append(positiveElements[i])
        result.append(negativeElements[i])


    return result


'''
One-pass approach:
    TC: O(n),
    SC: O(n)

    Notice that the positive numbers are in the even indexes and the negative numbers are in the odd indexes.
    Use 2 pointers to keep track of the indexes (odd and even) and place the elements accordingly.
'''
def rearrangeArray(self, nums: List[int]) -> List[int]:
    pos = 0
    neg = 1
    result = [0] * len(nums)

    for i in range(0, len(nums)):
        if nums[i] > 0:
            result[pos] = nums[i]
            pos+=2
        else:
            result[neg] = nums[i]
            neg+=2
            
    return result