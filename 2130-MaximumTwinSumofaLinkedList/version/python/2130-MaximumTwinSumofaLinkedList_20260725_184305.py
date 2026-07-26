# Last updated: 7/25/2026, 6:43:05 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def pairSum(self, head: Optional[ListNode]) -> int:
8        slow = ListNode()
9        slow.next = head
10        
11        fast = slow
12
13        while fast and fast.next:
14            slow = slow.next
15            fast  = fast.next.next
16            
17        # mid point slow, reverse second half
18
19        Prev = None
20
21        while slow:
22            temp = slow.next
23            slow.next = Prev
24            Prev = slow
25            slow = temp
26
27            
28        # second half start with prev
29        right = Prev
30        left = head
31        Ans = -inf # 5
32        while left and right:
33            Ans = max(Ans, left.val + right.val)
34            left = left.next
35            right = right.next
36
37        return Ans
38