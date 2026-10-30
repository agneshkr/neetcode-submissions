# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iterative solution

        # curr = head
        # prev = None

        # while curr:
        #     next_one = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_one

        # return prev 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None # first entry which becomes the last node.
        return newHead




