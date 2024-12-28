def moveZeroes(self, nums: List[int]) -> None:
    '''
    Brute force: 
        TC: O(n) + O(k) + O(n-k) = O(2n) = O(n)
        
        SC: O(n) due to temp array

    Step 1: store the non-zero elements in a temp array
    Step 2: put the elements in the temp array (non-zero elements) in input array
    Step 3: put 0s in the remaining positions
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



def moveZeroes(self, nums: List[int]) -> None:
    '''
    Optimal (2 pointer approach): 
        TC: O(k) + O(n-k) = O(n),
        SC: O(1)

    Step 1: find the index of first 0
    Step 2: keep swapping as long as i is non-zero
    '''

    j = -1  # to find the first 0. If j stays -1 after iterating nums, there is no 0

    # step 1
    for i in range(0, len(nums)):
        if nums[i] == 0:
            j = i
            break

    # step 2
    if j != -1:
        for i in range(j+1, len(nums)):
            if nums[i] != 0:
                # swapping
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                j+=1

    print(nums)