'''
    TC: O(n),
    SC: O(n)

    We use a Two Pointer approach for this problem. We only swap when we find two vowels and update
    the pointers accordingly. 
    SC is O(n) because we are converting the s to a list. 
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        left = 0
        right = len(s)-1
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']     # O(n) lookup as we are iterating the list to find the element

        while left <= right:
            if sList[left] not in vowels:
                left += 1
                continue
            
            if sList[right] not in vowels:
                right -= 1
                continue

            tmp = sList[left]
            sList[left] = s[right]
            sList[right] = tmp

            left += 1
            right -= 1

        return ''.join(sList)


'''
    Same approach but a bit faster because we are using a set which allows O(1) lookup.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        left = 0
        right = len(s)-1
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}     # O(1) lookup as we are using set

        while left <= right:
            if sList[left] not in vowels:
                left += 1
                continue
            
            if sList[right] not in vowels:
                right -= 1
                continue

            tmp = sList[left]
            sList[left] = s[right]
            sList[right] = tmp

            left += 1
            right -= 1

        return ''.join(sList)