# brute force - TC: O(nlogn) + O(n), SC: O(n)
def removeDuplicates(self, nums: List[int]) -> int:
    numsSet = set()                 # to remove the duplicates from nums

    for num in nums:
        numsSet.add(num)

    numsSet = sorted(numsSet)       # to account for negative numbers

    i = 0
    for num in numsSet:
        nums[i] = num
        i+=1
    
    return len(numsSet)

# optimal -  TC: O(n), SC: O(1)
def removeDuplicates(self, nums: List[int]) -> int:
    left = 0
    right = 1                       # 2 pointer approach

    while right < len(nums):
        if nums[left] == nums[right]:
            right += 1
        else:
            left += 1
            nums[left] = nums[right]
            right += 1
            

    return left+1