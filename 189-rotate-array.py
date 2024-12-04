def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Brute force -> TC: O(n), SC: O(n)
    tmpList = []
    n = len(nums)
    k %= n

    for i in range(n-k, n):
        tmpList.append(nums[i])

    for i in range(n-k-1, -1, -1):
        nums[i+k] = nums[i]

    for i in range(0, len(tmpList)):
        nums[i] = tmpList[i]



def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Without extra space -> TC: O(n), SC: O(1)
    n = len(nums)
    k %= n


    left = n - k
    right = n - 1

    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1

    left = 0
    right = n - k - 1

    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1

    left = 0
    right = n - 1

    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1