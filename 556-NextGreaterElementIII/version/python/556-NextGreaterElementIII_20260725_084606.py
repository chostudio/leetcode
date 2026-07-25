# Last updated: 7/25/2026, 8:46:06 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        # wow a monotonic stack + linkedlist Q this is actually crazy lmao
9        stack = [] # put nodes in stack, if greater than pop you know the drill
10        node = head
11        while node:
12            # if not node.next:
13            #     stack.append(node) # always make ure to just grab the last value
14            while stack and stack[-1].val < node.val:
15                stack.pop()
16            stack.append(node)
17            node = node.next
18
19        # loop through stack and just chain together
20        for i in range(len(stack)-1):
21            stack[i].next = stack[i + 1]
22
23        return stack[0]