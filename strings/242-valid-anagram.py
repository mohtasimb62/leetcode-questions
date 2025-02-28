'''
Brute Force approach:
    TC: O(nlogn),
    SC: O(n) as the sorted function creates a new list

    Notice that sorting both the input strings will result in both of them having the same string, if
    they are anagrams. 
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = sorted(s)
        sortedT = sorted(t)

        return sortedS == sortedT