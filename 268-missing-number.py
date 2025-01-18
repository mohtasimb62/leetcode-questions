'''
Brute Force:
    TC: O(n^2)
    SC: O(1)

    Just check whether or not each element in nums exist between 0 - len(nums)+1 (+1 to account for the 
    last number)
'''

from typing import List

def missingNumber(self, nums: List[int]) -> int:
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i


'''
Better approach:
    TC: O(n),
    SC: O(n)

    By hashing the appearance of each element in nums in a list, it is easy to tell which element is 
    missing
'''

def missingNumber(self, nums: List[int]) -> int:
    hashArr = [0] * (len(nums)+1)

    for i in nums:
        hashArr[i] = 1

    for i in range(0, len(hashArr)):
        if hashArr[i] == 0:
            return i


'''
Optimal approach:
    TC: O(n),
    SC: O(1)

    If you calculate the sum using Gauss Sum (n*(n+1)//2) and calculate the sum of all the elements in 
    nums, and get the difference, you will get the missing number
'''

def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    sumOfN = (n*(n+1)) // 2 # to get an integer instead of a floating point number
    sumOfNums = 0
    for num in nums:
        sumOfNums += num

    return sumOfN - sumOfNums