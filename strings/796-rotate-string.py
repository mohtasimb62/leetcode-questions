'''
My approach:
    TC: O(n)
    SC: O(n)

    The trick here is to realize that if we concatenate a string with itself, then the resulted string
    will contain all the possible rotations.
'''
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s