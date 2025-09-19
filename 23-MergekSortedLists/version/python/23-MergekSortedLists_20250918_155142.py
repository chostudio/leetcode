# Last updated: 9/18/2025, 3:51:42 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        
        # 1, 1, 2, 3, 4, 4, 5, 6
        def merge(l1, l2):
            new_list = ListNode()
            dummy = new_list
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            # if somethign is still there
            if l1:
                dummy.next = l1
            if l2:
                dummy.next = l2
            return new_list.next # always .next
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None
                if i + 1 < len(lists): # in bounds so good
                    l2 = lists[i + 1]
                new_list = merge(l1, l2)
                temp.append(new_list) 
            lists = temp
        return lists[0]