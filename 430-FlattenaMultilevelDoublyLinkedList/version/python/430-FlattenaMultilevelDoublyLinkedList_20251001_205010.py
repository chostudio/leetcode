# Last updated: 10/1/2025, 8:50:10 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if there is a child, save the next pointer into the stack then hoist the child up from child to next and make sure the pointers are all updated then iterate
        node = head
        stack = []
        while node:
            if node.child:
                # NEED AN IF bc there could be no node.next
                if node.next:
                    stack.append(node.next)
                # save the old next into satck and hoist it up
                # temp save child to move into next
                nextnode = node.child
                node.child = None
                # point at each other
                node.next = nextnode
                nextnode.prev = node

            if node.next is None and len(stack) != 0:
                # whatever in stack will go be our next. append it and connect it
                newnode = stack.pop()
                node.next = newnode
                newnode.prev = node
            node = node.next
        return head