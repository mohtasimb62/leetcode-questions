'''
My solution:
    TC: O(n)
    SC: O(n)

    We create a dictionary to store the mapping of characters from s to t, but skipping the mapping if a
    mapping to a character in t already exists. Then, we can just replace the characters in s with the 
    mapping from the dictionary and check if the resulting string is equal to t.
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = {}                                # to store the mapping of characters from s to t
        sList = list(s)
        tList = list(t)

        for i in range(0, len(sList)):
            if tList[i] not in charMap.values():    # to check for duplicate values    
                charMap[sList[i]] = tList[i]
    
        for i in range(0, len(sList)):
            # the check for duplicate values might cause some keys to be left out and if they are, just
            # return False as the duplicate values mean that the strings are not isomorphic.
            if sList[i] not in charMap:
                return False
            sList[i] = charMap[sList[i]]

        return sList == tList
                