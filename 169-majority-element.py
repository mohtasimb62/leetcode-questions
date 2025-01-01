'''
Extra space approach:
    TC: O(n),
    SC: O(n)

    Store each element in a hashmap and store it's count. Return the element that appears 'len(nums) // 2' times
'''
def majorityElement(self, nums: List[int]) -> int:
    hashmap = {}

    for i in nums:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    majority = len(nums) // 2

    for key, value in hashmap.items():
        if value > majority:
            return key

    return 0


'''
Optimal approach (Moore's voting algorithm):
    TC: O(n),
    SC: O(1)
'''
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    element = 0

    for i in range(0, len(nums)):
        if count == 0:
            count = 1
            element = nums[i]
        elif nums[i] == element:
            count += 1
        else:
            count -= 1

    elementCounter = 0
    for i in range(0, len(nums)):
        if nums[i] == element:
            elementCounter += 1

    if elementCounter > (len(nums) // 2):
        return element

    return 0