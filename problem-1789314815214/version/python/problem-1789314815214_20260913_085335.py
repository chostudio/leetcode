# Last updated: 9/13/2026, 8:53:35 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
9        
10        # how do you know if a leaf is a leaf node? Just check if there's children or not. You don't need to know the height.
11
12        # yes this is backtracking because you need to REMOVE the value of path val that doesnt work rather than needing to recompute down a chain again or leaving the old val inside, which we don't want
13        ans = []
14        def pathsum(node, path, amount):
15            if not node:
16                return 
17            
18            amount += node.val
19            path.append(node.val)
20            # print(height, maxheight, path)
21            # off by one for height error and remember that we dont want any root to leaf node, but specificaly path that reaches target sum
22            if not node.left and not node.right and amount == targetSum:
23                ans.append(path.copy())
24                # we dont return here bc we need to clean up this value and suma mount for each node (backtrck)
25
26            # otherwise, not a leaf node
27            if node.left:
28                pathsum(node.left, path, amount)
29            if node.right:
30                # typo where you copy pasted that forgot to change .left to .right
31                pathsum(node.right, path, amount)
32
33            amount -= node.val
34            path.pop() # we're going back up the chain
35            return
36
37        pathsum(root, [], 0)
38        return ans