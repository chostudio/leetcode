# Last updated: 10/29/2025, 6:51:48 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # this is hilariously almost the same exact thought process as 308 odd even list that I just did?

        lesslist = ListNode()
        lessstart = lesslist
        morelist = ListNode()
        morestart = morelist

        if not head:
            return None
        curr = head
        while curr:
            if curr.val >= x:
                morelist.next = curr
                morelist = morelist.next
            else:
                lesslist.next = curr
                lesslist = lesslist.next
            curr = curr.next
        # join them together
        lesslist.next = morestart.next # bc morestart is a node itself for dummy so go to next one
        morelist.next = None # remove whatever last point at

        return lessstart.next
