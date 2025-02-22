'''
Approach 1:
    TC: O(n)
    SC: O(n) due to the split function

    Split the string to get each word in the given string into a list. We the reverse the list and join
    the words with a " " to get the final result.
'''

class Solution:
    def reverseWords(self, s: str) -> str:

        asList = s.split()

        for i in range(0, len(asList)//2):
            tmp = asList[i]
            asList[i] = asList[len(asList)-i-1]
            asList[len(asList)-i-1] = tmp

        resultStr = " ".join(asList)

        return resultStr