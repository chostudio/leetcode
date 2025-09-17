# Last updated: 9/17/2025, 10:51:34 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        # either define this function inside the scope on the same level OR use self.whatever and you can move it under the return statement outside
        def merge(list1, list2):
            head = ListNode()
            dummy = head
            # vals inside list can be negative, meaning assigning a temp value won't work we actually should just .next to rest of whichever one is left once out of loop
            while list1 and list2:
                one = list1.val
                two = list2.val
                if one < two: # bruh always remeber that this is ascending sorting so direciton should be less than
                    dummy.next = list1
                    list1 = list1.next
                else:
                    dummy.next = list2
                    list2 = list2.next
                dummy = dummy.next # always remember to move forward otherwise infinite
            # possibility that one list still has more left / could be longer
            if list1:
                dummy.next = list1
            else: # if list2: # why else and not elif? what if both are same length
                dummy.next = list2
            return head.next # .next

        while len(lists) > 1: # more than one
            temp = []
            for i in range(0, len(lists), 2): # you need the 0 and len(lists) bc in order to make the for loop go by 2 each time it needs to have the prior arguements
                
                l1 = lists[i]
                l2 = None
                if i + 1 < len(lists): # checking if it's odd
                    l2 =  lists[i + 1]
                new_list = merge(l1, l2)
                temp.append(new_list)
            lists = temp # dont put this inside for loop

        return lists[0] # only one linked list left in the list

        