from typing import List

def search(self, nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        # this is for the OVERFLOW case. If both low and high are INT_MAX, then adding them will cause them to 
        # overflow. Using the formula below will keep that in check. Or using something like "long long" in C++.
        # mid = low + ((high - low) // 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1