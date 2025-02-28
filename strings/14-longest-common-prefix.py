from typing import List

'''
Approach 1:
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