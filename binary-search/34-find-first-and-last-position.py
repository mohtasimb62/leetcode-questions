'''
Brute force approach:
    TC: O(n),
    SC: O(1)

    Just do a linear search and find the first and last occurance of target in nums array.
'''

def searchRange(self, nums: List[int], target: int) -> List[int]:
    result = [-1, -1]

    for i in range(0, len(nums)):
        if nums[i] == target:
            if result[0] == -1:
                result[0] = i
            result[1] = i

    return result

'''
Optimal approach (using lower and upper bound):
    TC: O(logn),
    SC: O(1)

    The lower bound is the smallest index where nums[i] == target. This can be used to find the first
    position of an element. The upper bound is the smallest index where nums[i] != target. So the upper
    bound minus 1 can be used to find the last position of an element.
'''

class Solution:

    def lowerBound(self, arr, target):
        sizeOfArr = len(arr)
        lowerBoundIndex = sizeOfArr
        low = 0
        high = sizeOfArr - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= target:
                lowerBoundIndex = mid
                high = mid - 1
            else:
                low = mid + 1

        return lowerBoundIndex

    def upperBound(self, arr, target):
        sizeOfArr = len(arr)
        upperBoundIndex = sizeOfArr
        low = 0
        high = sizeOfArr - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > target:
                upperBoundIndex = mid
                high = mid - 1
            else:
                low = mid + 1

        return upperBoundIndex

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        lb = self.lowerBound(nums, target)
        ub = self.upperBound(nums, target)

        if lb >= len(nums) or nums[lb] != target:
            return result

        result[0] = lb
        result[1] = ub - 1

        return result


'''
Optimal approach (without lower and upper bound concept, i.e. raw binary search):
    TC: O(logn),
    SC: O(1)

    Just do binary search 2 times to find the first occurance and the last occurance.
'''

class Solution:
    def firstOccurance(self, nums, target):
        first = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return first
    
    def lastOccurance(self, nums, target):
        last = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        startingIndex = self.firstOccurance(nums, target)

        # you can check if startingIndex is -1 to avoid calling lastOccurance as if the startingIndex is -1 (
        # which means that that element is not even in the list), there's is no need to call lastOccurance which
        # saves a O(logn) operation.
        if startingIndex == -1:
            return result
            
        endingIndex = self.lastOccurance(nums, target)

        result[0] = startingIndex
        result[1] = endingIndex

        return result



