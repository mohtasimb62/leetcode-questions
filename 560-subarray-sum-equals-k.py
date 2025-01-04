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