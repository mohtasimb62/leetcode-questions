'''
Brute force approach:
    TC: O(n^2),
    SC: O(n) because we are storing all the substrings in a list

    Just simple brute force, we first generate all the substrings of the given string and then check 
    if the substring is odd or not. Note the use of slicing in the generateSubstrings() function.
'''
class Solution:
    def largestOddNumber(self, num: str) -> str:
        largestOddNumber = 0

        if int(num) % 2 != 0:
            largestOddNumber = num
            return largestOddNumber


        getSubstrings = self.generateSubstrings(num)
        
        for num in getSubstrings:
            if int(num) % 2 != 0:
                largestOddNumber = max(largestOddNumber, int(num))
        
        if largestOddNumber == 0:
            return ""
        else:
            return str(largestOddNumber)

    def generateSubstrings(self, num: str):
        result = []

        for i in range(0, len(num)):
            for j in range(i+1, len(num)+1):
                result.append(num[i:j])

        return result
    

'''
Optimal approach:
    TC: O(n)
    SC: O(1)

    Notice that the last digit of an odd number is always odd. So if we just iterate from the end of the 
    string and check if the current number is odd or not, we return the substring from the start to that 
    current index.
'''
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""
