# Last updated: 8/2/2026, 5:09:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
9        
10        delete = set(to_delete)
11        ans = []
12        # if a nodes parent is deleted (and they are not going to be delteted) then that means that node is the top start of a new forest
13        def dfs(node, parentdelete):
14            if not node:
15                return
16            
17            # now we have a node
18            # do wehave its parent? and are we going to delete it?
19            # boolean
20            tobedeleted = node.val in delete
21            if parentdelete and tobedeleted == False:
22                ans.append(node)
23            
24            if node.left:
25                dfs(node.left, tobedeleted)
26                if node.left.val in delete:
27                    node.left = None
28            if node.right:
29                dfs(node.right, tobedeleted)
30                if node.right.val in delete:
31                    node.right = None
32            # note that we dont actually have to delete the forest in this case but if we did have to at the very end after the dfs recusion (aka post order). we would just set the left and right child to None and del the node. actually we do
33            return
34        # dont mark the "parent" of the root as tobedelted bc it doenst have a parent. we deal with root special case later
35        dfs(root, False)
36        # forgot the .val, u originally checked the root itself not the root.val. only val in set
37        if not root.val in delete:
38            ans.append(root)
39        return ans