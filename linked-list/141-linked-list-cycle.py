from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Brute force approach:
    TC: O(n),
    SC: O(n)

    We are using a hashmap (dictionary) to store the nodes that we have visited. If we come
    across any node that is already in the hashmap, we return True. Else, we add that node to
    the visited nodes hashmap. If we reach the end of the linked list, we just return False.
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        curr = head

        while curr is not None:
            if curr not in seen:
                seen[curr] = 1
            else:
                return True

            curr = curr.next

        return False


'''
Optimal approach:
    TC: O(n),
    SC: O(1)

    We are using the slow and fast pointer approach here. If there exists a cycle in the linked
    list, the slow and fast pointer is bound to meet at some point. And if they do, return True.
    Else, return False. 
    
    But how can we guarantee they will meet (proof)? Notice that the slow pointer moves by one
    step while the fast pointer moves by two steps. So, if the distance from the fast pointer to
    the slow pointer is d, after each iteration, the distance decrements by 1. So, no matter
    what d is, it will eventually reach 0 if there exists a cycle. If not, the loop will just
    exit early and return False. 
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast.next is not None and fast is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False