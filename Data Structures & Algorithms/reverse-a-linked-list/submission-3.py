# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # iterative solution

        curr = head
        prev = None

        while curr:
            next_one = curr.next
            curr.next = prev
            prev = curr
            curr = next_one

        return prev            
