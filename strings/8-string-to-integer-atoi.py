'''
My approach:
    TC: O(n),
    SC: O(1)

    Just following the steps as mentioned in the problem statement.
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""                         # to store the result which will be returned as int(result)
        withoutLeadingSpaces = s.strip()    # removing the leading and trailing spaces
        start = 0                           # to determine where the loop starts (mainly to handle the + and - cases)
        sign = 1                            # to determine if the number is positive or negative

        if withoutLeadingSpaces == "":
            return 0
  
        if withoutLeadingSpaces[0] == "-":
            sign = -1
            start = 1
        elif withoutLeadingSpaces[0] == "+":
            start = 1
        else: 
            start = 0
        
        for i in range(start, len(withoutLeadingSpaces)):
            if not (48 <= ord(withoutLeadingSpaces[i]) and ord(withoutLeadingSpaces[i]) <= 57):
                break
            result += withoutLeadingSpaces[i]

        if result == "":
            return 0

        num = sign * int(result)            # to get the signed number before comparing

        if num < -2**31:
            num = -2**31
        elif num > 2**31 - 1:
            num = 2**31 - 1

        return num
