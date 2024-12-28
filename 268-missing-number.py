'''
Brute Force:
    TC: O(n^2)
    SC: O(1)

    Just check whether or not each element in nums exist between 0 - len(nums)+1 (+1 to account for the last number)
'''
def missingNumber(self, nums: List[int]) -> int:
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i


'''
Better approach:
    TC: O(n),
    SC: O(n)

    By hashing the appearance of each element in nums in a list, it is easy to tell which element is missing
'''

def missingNumber(self, nums: List[int]) -> int:
    hashArr = [0] * (len(nums)+1)

    for i in nums:
        hashArr[i] = 1

    for i in range(0, len(hashArr)):
        if hashArr[i] == 0:
            return i