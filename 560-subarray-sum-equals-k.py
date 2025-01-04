'''
Brute force approach:
    TC: O(n^3),
    SC: O(1)

    Generate all the subarrays and for each subarray, calculate the sum. If the sum is equal to k, increment 
    a count variable and return that at the end.
'''
def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            sum = 0

            for l in range(i, j+1):
                sum += nums[l]

            if sum == k:
                count += 1

    return count

'''
Better approach:
    TC: O(n^2),
    SC: O(1)

    Instead of calculating the sum every single time, keep track of the sum in a variable (The sum doesn't have 
    to be calculated every iteration. It's just the whatever the sum was plus the current element.)
'''
def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]

            if sum == k:
                count += 1

    return count
