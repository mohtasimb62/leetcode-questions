def moveZeroes(self, nums: List[int]) -> None:
    '''
    Brute force: 
        TC: O(n) + O(k) + O(n-k) = O(2n) = O(n)
        
        SC: O(n) due to temp array

    Step 1: store the non-zero elements in a temp array
    Step 2: Put the elements in the temp array (non-zero elements) in input array
    Step 3: Put 0s in the remaining positions
    '''

    tmpArr = []

    # step 1
    for num in nums:
        if num != 0:
            tmpArr.append(num)

    # step 2
    countOfNonZeroElements = len(tmpArr)
    for i in range(0, countOfNonZeroElements):
        nums[i] = tmpArr[i]

    # step 3
    for i in range(countOfNonZeroElements, len(nums)):
        nums[i] = 0

    print(nums)