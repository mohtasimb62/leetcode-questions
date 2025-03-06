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
    
'''
Optimal approach:
    TC: O(n),
    SC: O(1)

    Again, just like leetcode 141, we are using the slow and fast pointer approach for the 
    optimal approach. We first find if a cycle exists. Then we find the first node of the cycle
    by resetting the slow pointer to the head and moving both the slow and fast pointers by one.
    The point where they meet is the first node of the cycle.
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        # if we reached the end of the linked list with the slow and fast pointers not being
        # the same, then we can conclude that there are no cycles and return None
        if fast is None or fast.next is None:
            return None

        # But if there is a cycle, the above if statement will not execute and we will then find
        # the first node of the cycle.
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow         # or fast, since they are the same