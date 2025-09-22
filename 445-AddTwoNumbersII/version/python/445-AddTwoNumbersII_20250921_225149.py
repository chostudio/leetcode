# Last updated: 9/21/2025, 10:51:49 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            temp = head
            prev = None
            while temp:
                next_node = temp.next
                temp.next = prev
                prev = temp
                temp = next_node
            return prev
        l11 = reverse(l1)
        l22 = reverse(l2)

        res = ListNode(0)
        temp = res
        val = 0
        while l11 or l22 or val:
            if l11:
                val += l11.val 
            if l22:
                val += l22.val 
            
            temp.next = ListNode(val%10)
            temp = temp.next
            val = val//10
            l11 = l11.next if l11 else None
            l22 = l22.next if l22 else None
        out = reverse(res.next)
        return out



        