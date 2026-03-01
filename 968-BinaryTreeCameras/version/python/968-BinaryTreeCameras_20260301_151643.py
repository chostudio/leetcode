# Last updated: 3/1/2026, 3:16:43 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8
9# hard to memorize which goes where but i get it conceptually
10class Solution:
11    cameracount = 0
12    # the issue with dealing with Boolean instead of numbers is you have to account for the cases with one child, and it's a pain 
13    def minCameraCover(self, root: Optional[TreeNode]) -> int:
14        def dfs(node):
15            if not node:
16                return "none" # this is the nonexistant under the leaf
17            # work way up from covered not covered or vice versa
18            left, right = dfs(node.left), dfs(node.right)
19            if left == "none" and right == "none":
20                return "not covered"
21            if (left == "covered" and right == "covered") or (left == "covered" and right == "none") or (left == "none" and right == "covered"):
22                return "not covered" # if both are covered then we dont need to camera
23            
24            # if both children are cameras or if one is a camera and the other is covered then we're good
25            if (left == "camera" and right == "camera") or (left == "camera" and right == "covered") or (left == "covered" and right == "camera") or (left == "camera" and right == "none") or (left == "none" and right == "camera"):
26                return "covered" # but we do not have a camera
27
28            # if either is "not covered" EVEN if either child is a camera but the other one is
29            # if left == "not covered" or right == "not covered":
30            self.cameracount += 1
31            return "camera"
32            
33
34        result = dfs(root)
35        return self.cameracount if (result == "camera" or result == "covered") else self.cameracount + 1 # else it would be not covered or leaf which mans we adding one more camera for the root