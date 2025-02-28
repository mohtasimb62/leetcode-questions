from typing import List

'''
Brute Force approach:
    TC: O(n^2)
    SC: O(1)
    
    We set the result to the first string in the list. Then we iterate over the rest of the strings and
    compare the characters of the current string with the result string. If the characters don't match
    (meaning the prefix matches until this point), we update the result string to be the substring from 
    the start to the current index.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for i in range(1, len(strs)):
            currStr = strs[i]
            for j in range(0, min(len(result), len(currStr))):
                if result[j] != currStr[j]:
                    result = result[:j]
                    break
            
            result = result[:min(len(result), len(currStr))]

        return result
    

'''
Optimal approach:
    TC: O(nlogn)
    SC: O(1)
    
    We sort the strings in the list and then compare the first and last strings. The common prefix of the
    first and last strings will be the common prefix of all the strings in the list.

    What the sort does is that it brings the strings with the common prefix together. That way, if we 
    compare the first and last strings, we get the common prefix.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sortedList = sorted(strs)
        result = ""

        firstStr = sortedList[0]
        lastStr = sortedList[-1]

        for i in range(0, min(len(firstStr), len(lastStr))):
            if firstStr[i] != lastStr[i]:
                break
            result += firstStr[i]

        return result