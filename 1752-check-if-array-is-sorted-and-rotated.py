# TC: O(n), SC: O(1)
def check(self, nums: List[int]) -> bool:
    count = 0

    for i in range(0, len(nums)-1):         # this loop iterates over each number and finds the INCREASE
        if nums[i] > nums[i+1]:
            count+=1

    if nums[len(nums)-1] > nums[0]:         # this checks for the INCREASE in the rotation
        count+=1
        
    return count<=1                         # there can be only ONE INCREASE