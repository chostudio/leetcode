# Last updated: 6/23/2026, 7:55:01 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        #combining two worst enemies lowk
9        if not head:
10            return # case where no node
11        
12        dummy = ListNode()
13        dummy.next = head
14
15        start = head # first, count how many nodes
16        count = 1
17        while start and start.next:
18            count += 1
19            start = start.next
20        
21        if k % count == 0:
22            return dummy.next # no change
23
24        # we have start node exist, but no start.next
25        # now at last node, connect to make linked list a circle?
26        start.next = dummy.next
27
28
29        start = head
30        # Find the new tail by walking exactly count - (k % count) - 1 steps from the original head.
31        k = count - (k % count) - 1 # -1 bc the kth node would actually be the new start head 
32        while k:
33            k -= 1
34            # we are one behind
35            start = start.next
36        # now at k-1
37        ans = start.next
38        start.next = None
39        return ans