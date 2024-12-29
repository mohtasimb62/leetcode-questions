'''
Brute Force:
    TC: O(n^2) (this gives a time limit exceeded),
    SC: O(1)

    For every element, check if it appears again. Return the element that appears once.
'''
def singleNumber(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    for i in range(0, len(nums)):
        count = 0   # to track if an element appears more than once
        for j in range(0, len(nums)):
            if nums[i] == nums[j]:
                count += 1

        if count == 1:
            return nums[i]

'''
Using extra space (set):
    TC: O(n),
    SC: O(n)

    Add every element to the set and if that element appears again, remove it from the set. Return the element
    that remains in the set.
'''
def singleNumber(self, nums: List[int]) -> int:
    hashset = set()

    for num in nums:
        if num in hashset:
            hashset.remove(num)
        else:
            hashset.add(num)

    singleNumber = 0
    for item in hashset:
        singleNumber = item
        
    return singleNumber


'''
Optimal approach (using xor)
    TC: O(n),
    SC: O(1)

    Using xor
'''
def singleNumber(self, nums: List[int]) -> int:
    xor = 0

    for num in nums:
        xor ^= num

    return xor