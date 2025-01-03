# brute force - TC: O(n^2), SC: O(1)
# def linearSearch(self, num: int, nums: List[int]) -> bool:
# 	for i in nums:
# 	    if i == num:
# 			return True
# 	return False

# def longestConsecutive(self, nums: List[int]) -> int:
# 	if len(nums) == 0:
# 	    return 0

# 	longest = 1 	# to keep track of the longest in each iteration

# 	for i in range(len(nums)):
# 	    currNum = nums[i]	# to check if currNum + 1 is present (while loop)
# 	    count = 1			# to keep track of the currect longest

# 	    while self.linearSearch(currNum + 1, nums):
# 			count += 1
# 			currNum += 1
# 			longest = max(longest, count)

# 	return longest



# sorting - TC: O(nlogn) + O(n), SC: O(1)
def longestConsecutive(self, nums: List[int]) -> int:

	if len(nums) == 0:
		return 0

	sortedNums = sorted(nums)
	lastSmallest = float("-inf")		# to store the last smallest number to determine if this number is in the start of a sequence
	longest = 1
	count = 0

	for i in range(0, len(sortedNums)):
		if sortedNums[i] - 1 == lastSmallest:
			count += 1
			lastSmallest = sortedNums[i]
		if sortedNums[i] != lastSmallest:
			count = 1
			lastSmallest = sortedNums[i]

		longest = max(count, longest)

	return longest



# optimal (HashSet) - TC: O(n), SC: O(n)
def longestConsecutive(self, nums: List[int]) -> int:

	if len(nums) == 0:
		return 0

	longest = 1

	
	numsSet = set(nums)

	for num in numsSet:
		if num - 1 not in numsSet:
			currNum = num
			count = 1

			while currNum + 1 in numsSet:
				count += 1
				currNum += 1

			longest = max(longest, count)

	return longest