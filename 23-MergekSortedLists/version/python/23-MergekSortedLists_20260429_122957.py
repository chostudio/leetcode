# Last updated: 4/29/2026, 12:29:57 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        # no need to do if len 0 return None early, but you could.
9
10        # put first into heap. WE ACTUALLY DONT GAF ABOUT THE LENGTH, index is only used to handle tie breakers
11        heap = []
12        for i in range(len(lists)):
13            node = lists[i]
14            if node == None:
15                continue
16            
17            # if two items vals in a heap are the same, python will continue moving down the chain, trying to compare more values until tiebreaker. two linkedlist object values cannot be compared with each other, thus we need a third value to be in the second place value to act as a necessary tiebreaker, ensuring python never gets to compare the node objects
18            # literally just the start values bc sorted alr
19            heapq.heappush(heap, (node.val, i, node))
20        
21        # you dont use the two pointer combine two lists technique with the heap. you pop ONE (the smallest) then put the next element into the heap (if there is a next value), move curr pointer by one everytime. only 1 while loop. this is actually the craziest thing ever bc it's so smart. why do 2 by 2 when it's already pop, push back, assign curr next, move curr to next
22
23        start = ListNode(0)
24        curr = start
25
26        while heap: # must not forget last value. don't do > than 1
27            val, i, node = heapq.heappop(heap)
28            if node.next:
29                # same index, alr gaurenteed to be unique
30                heapq.heappush(heap, (node.next.val, i, node.next))
31            curr.next = node
32            curr = curr.next
33        
34        # dont need to do return None if nothing bc it'll be fine. 
35        return start.next