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