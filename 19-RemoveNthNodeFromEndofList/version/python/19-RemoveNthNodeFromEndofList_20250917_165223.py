# Last updated: 9/17/2025, 4:52:23 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        i = 0
        while i != n:
            fast = fast.next
            i += 1
        
        # if first node, then return second node
        if fast is None:
            return head.next

        # else iterate through
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        temp = slow.next.next
        slow.next = temp

        return head