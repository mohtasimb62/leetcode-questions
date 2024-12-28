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