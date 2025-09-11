# Last updated: 9/11/2025, 12:32:12 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # halfway
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse
        backOne = None
        while slow:
            # remember the next node
            temp = slow.next 
            # make the reverse
            slow.next = backOne
            # then shift the two vars up one to next nodes
            backOne = slow
            slow = temp
        
        # once loop breaks, slow no longer exists but backOne is slow - 1 node so it's the last node
        # palindrome
        one, two = head, backOne
        while one and two:
            if one.val != two.val:
                return False
            one = one.next
            two = two.next
        return True