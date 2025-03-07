from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Brute force approach:
    TC: O(n),
    SC: O(n)

    We use a list to store the values of the odd nodes first and then the even nodes. We then
    traverse the linked list again and replace the values of the nodes with the values from the
    list. 
'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        oddEvenValues = []
        curr = head

        while curr is not None and curr.next is not None:
            oddEvenValues.append(curr.val)
            curr = curr.next.next

        # to account for the last node as the loop ends before it could be added
        if curr:
            oddEvenValues.append(curr.val)

        curr = head.next

        while curr is not None and curr.next is not None:
            oddEvenValues.append(curr.val)
            curr = curr.next.next

        # same reason as above
        if curr:
            oddEvenValues.append(curr.val)

        curr = head
        i = 0

        while curr is not None:
            curr.val = oddEvenValues[i]
            i += 1
            curr = curr.next

        return head
    

'''
Optimal approach:
    TC: O(n),
    SC: O(1)

    We use a 2 pointer approach here. The odd pointer points to the odd nodes and the even
    pointer points to the even nodes. We first connect the odd nodes, then the even nodes, and
    finally connect the last odd node to the starting even node.
'''
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next
        evenHead = odd.next     # to connect the last odd node to the starting even node

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenHead

        return head