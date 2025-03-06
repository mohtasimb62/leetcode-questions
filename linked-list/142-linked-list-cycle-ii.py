from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
Brute force approach:
    TC: O(n),
    SC: O(n)

    Just like leetcode 141, we are using a hashmap to store the nodes that we have visited. We 
    return the first node that we come across twice.
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = {}
        curr = head

        while curr is not None:
            if curr not in seen:
                seen[curr] = 1
            else:
                return curr

            curr = curr.next
            
        return None
    
