'''
Brute force is to do a linear search which is a O(n) approach. Optimal solution is using binary search which
has O(logn) time complexity.
    TC: O(logn),
    SC: O(1)

    We need to know the concept of lower bound here. We are finding the smallest index where arr[mid] >= target.
    If we find that, that is a probable answer but we keep looking left for a smaller index else we look to the
    right. Return the smallest possible index.
'''

def searchInsert(self, nums: List[int], target: int) -> int:
    sizeOfNums = len(nums)
    low = 0 
    high = sizeOfNums - 1

    ans = len(nums)     # higest index possible to input elements

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans