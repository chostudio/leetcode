# Last updated: 10/29/2025, 6:45:57 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two dummy nodes to make an odd and even linkedlist and then just join the two ones after
        # misread question, it's refering to indicies not value but now it's either or so that's good
        if not head:
            return # just in case if not exist

        curr = head
        evendummy = ListNode()
        evenstart = evendummy
        odddummy = ListNode()
        oddstart = odddummy

        amount = 1
        while curr:
            if amount % 2 == 0: # even
                evendummy.next = curr
                evendummy = evendummy.next
            else:
                odddummy.next = curr
                odddummy = odddummy.next
            amount += 1 # dont forget to increment
            curr = curr.next # dont forget to move the pointer up

        # once reg list pointer reach the end
        # concatenate the two together
        odddummy.next = evenstart.next # bc evenstart itself is 0
        evendummy.next = None # and set end to nothing
        return oddstart.next # start of new list
