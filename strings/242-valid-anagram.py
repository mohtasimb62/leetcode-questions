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
    
'''
Optimal approach:
    TC: O(n)
    SC: O(1)

    We could have used a hashmap (dictionary) to store the frequency of each character in the string, but
    since we know that the string will only have lowercase characters, we can just use a fixed size
    array (list) to store the frequency instead. Then we iterate over the first string and increment the
    frequency of each character and the second string to decrement the frequency of each character. We 
    then go over the frequency list and if there are any non-zero values, we return False because the 
    increment and decrement should result in a 0 if both the strings are anagrams. Else, we return
    True.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charFreq = [0]*26   # as string will only have the lowercase characters
        lowerS = s.lower()
        lowerT = t.lower()

        for i in range(0, len(lowerS)):
            charFreq[ord(lowerS[i]) - ord('a')] += 1
        
        for i in range(0, len(lowerT)):
            charFreq[ord(lowerT[i]) - ord('a')] -= 1

        for i in charFreq:
            if i != 0:
                return False

        return True
