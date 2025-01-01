'''
Brute Force approach:
    TC: O(n!)
    SC: O(n!)

    Calculate all the permutations, store them in a sorted order in a list, find the given permutation in the
    list and return the next permutation in the list.

    *Code not done as it will fail due to time complexity*
'''

'''
Optimal approach:
    TC: O(n),
    SC: O(1)

    3 steps:
    1. We find the index of the "break". This is to calculate the index of the longest possible prefix as we 
       need atleast 1 element which is greater  to the right of the element at the "break".
    2. Swap the element at the "break" with the next greatest in the right of the "break".
    3. Reverse the remaining to get the next permutation (This works because after the swapping (step 2), it
       doesn't matter what's in the remaining places as it's already greater. But since we need the next 
       immediate permutation, if we keep the remaining elements as small as possible (which is achieved by
       reversing the remaining), we have our next permutation.
'''
def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    indexOfBreak = -1
    sizeOfNums = len(nums)

    # finding the break
    for i in range(sizeOfNums-2, -1, -1):
        if nums[i] < nums[i+1]:
            indexOfBreak = i
            break

    if indexOfBreak == -1:
        nums.reverse()
        return nums

    # swapping with the next biggest element
    for i in range(sizeOfNums-1, indexOfBreak, -1):
        if nums[i] > nums[indexOfBreak]:
            tmp = nums[i]
            nums[i] = nums[indexOfBreak]
            nums[indexOfBreak] = tmp
            break

    # revering the remaining of the list
    nums[indexOfBreak+1:] = reversed(nums[indexOfBreak+1:])