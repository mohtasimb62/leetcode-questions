# A follow-up question to leetcode 33
'''
Brute force approach:
    TC: O(n),
    SC: O(1)

    Do a linear search and return the index of the element if found. If not, return -1.
'''

'''
Optimal approach:
    TC: O(logn),
    SC: O(1)

    This is a modified version of binary search. Use binary search (as the list is sorted) and eliminate the 
    areas where the target is guaranteed to be NOT found. Note that it is GUARANTEED that at each iteration,
    only ONE side (either the left or right) will be sorted.

    This would work if there are no duplicates (leetcode 33) but since there are duplicates in this question,
    test cases like `nums = [1,0,1,1,1]` fail as the duplicates make it impossible to figure out which portion
    is sorted. This is the ONLY edge case where the nums[low], nums[mid], and nums[high] all happen to be the
    same element because of the duplicates. Hence, handle this case by decrementing the low pointer and
    incrementing the high pointer. This handles this case because as low and high point to the same thing, they
    can just be eliminated. At this point, this is the same problem as leetcode 33.

    SO REMEMBER, in questions where there are duplicates, first solve the problem assuming there are no
    duplicates. Then, relax the assumption.
'''

from typing import List


def search(self, nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return True

        # to handle the edge case
        if nums[low] == nums[mid] and nums[mid] == nums[high]:
            low += 1
            high -= 1
        
        # this means the left side is sorted
        elif nums[low] <= nums[mid]:
            if target >= nums[low] and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1 

        # this means the right side is sorted
        else:
            if target >= nums[mid] and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return False