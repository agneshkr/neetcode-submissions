# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_ptr, slow_ptr = head, head

        while fast_ptr and slow_ptr:
            if slow_ptr.next == None:
                return False
            slow_ptr = slow_ptr.next
            if fast_ptr.next == None or fast_ptr.next.next == None:
                return False
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False
        