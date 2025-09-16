# Last updated: 9/16/2025, 10:07:53 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        dummy = head
        carry = 0
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            amount = l1val + l2val + carry
            if amount >= 10:
                carry = 1
                amount -= 10
            else: # important to have carry 0 otherwise infinite. 
                carry = 0
            ans = ListNode(amount)
            dummy.next = ans
            dummy = dummy.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next