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
'''
def search(self, nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        
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
    
    return -1