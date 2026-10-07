# Last updated: 10/6/2026, 7:30:51 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: ListNode | None) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        if not head: return None
12        # get the halfway point
13        dummy = ListNode()
14        dummy.next = head
15
16        fast, slow = dummy.next, dummy.next
17        # does it start on head node? does it end when no more slow.next or no more slow. slow.next bc we need next.next
18        # we need to have it
19        while slow and slow.next and fast and fast.next:
20            fast = fast.next.next
21            slow = slow.next
22        print(slow.val)
23        # now slow is at the halfway point (right before it)
24        # reverse the second half of the list
25        prev = None
26        while slow:
27            temp = slow.next
28            slow.next = prev
29            prev = slow # move prev first b4 u move slow
30            slow = temp # og slow.next
31        
32        # iterate from both ends
33        left = dummy.next
34        right = prev # slow doenst exist but prev does
35        print(left.val, right.val)
36        isLeft = True
37        while left and left.next and right and right.next:
38            
39            # left, then right
40            if isLeft:
41                temp = left.next
42                left.next = right
43                left = temp
44            else: # right turn
45                temp = right.next
46                right.next = left
47                right = temp
48
49            isLeft = not isLeft
50        
51        # i dont think it would be lopsided it would be off by one at most on the right side. but since it's already on the thing it should work
52        return dummy.next