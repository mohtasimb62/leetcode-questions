from typing import Optional

'''
Brute Force approach:
    TC: O(n + n/2) -> the n/2 is because we are traversing until the middle of the linked list,
    SC: O(1)

    Simply, calculate the size of the linked list first and then find the middle index. Return
    the linked list from that index.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0           # size of linked list
        temp = head     # temp variable to traverse the linked list

        # this loop calculates the size of the linked list
        while temp is not None:
            n += 1
            temp = temp.next

        mid = (n//2) + 1

        temp = head

        while temp is not None:
            mid -= 1

            if mid == 0:
                break
            
            temp = temp.next

        return temp
    

'''
Optimal approach:
    TC: O(n),
    SC: O(1)

    This is known as the slow and fast pointer approach. The slow pointer moves one step while 
    the fast pointer moves two steps. By the end of the algorithm, the slow pointer will be 
    pointing to the middle. Why? If there is a race with distance to cover "d" and there are 
    2 persons - person A with speed x and person B with speed 2x. Then by the time person B 
    finishes the distance, person A will be at the middle of the distance.
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow