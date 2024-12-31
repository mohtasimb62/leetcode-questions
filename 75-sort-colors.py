'''
With extra space:
    TC: O(n),
    SC: O(n)

    Store the 0's, 1's, and 2's (in that order) to a new list and for every i, nums[i] = newArr[i]
'''
def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    newArr = []

    # finding 0s
    for num in nums:
        if num == 0:
            newArr.append(num)

    # finding 1s
    for num in nums:
        if num == 1:
            newArr.append(num)

    # finding 2s
    for num in nums:
        if num == 2:
            newArr.append(num)
    

    for i in range(0, len(nums)):
        nums[i] = newArr[i]