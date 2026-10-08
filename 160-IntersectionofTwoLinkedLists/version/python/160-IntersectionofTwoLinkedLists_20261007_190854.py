# Last updated: 10/7/2026, 7:08:54 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
9
10        # a + b + c = b + a + c
11        a, b = headA, headB # remember wher ethe heads are
12        while a is not None and b is not None:
13            if a == b:
14                return a # or b, same node
15            a = a.next
16            b = b.next
17            # bc if they are both none, then we wna tto break, not infinite loop
18            if a is None and b is not None:
19                a = headB
20            if b is None and a is not None:
21                b = headA
22        # either a ==b (same length, we hit it) or 
23        return None # both are none
24        