# Last updated: 9/15/2025, 3:40:27 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node, base on which ever node is smaller/equal then point to that node
        dummy = ListNode() # init, nothing inside
        head = dummy
        # initialize pointesr for the list and not edit it in place or dont up to you
        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val < l2.val: # !!!!!!!! you swapped the greater than sign wrong logic that's why it was wrong
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next # always need to move head node forward
        if l2:
            head.next = l2
        elif l1:
            head.next = l1
        
        return dummy.next

