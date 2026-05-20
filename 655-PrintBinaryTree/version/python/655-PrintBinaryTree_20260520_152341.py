# Last updated: 5/20/2026, 3:23:41 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
9        # first u gotta get width and height in order to format the 2d array and populate it full of "" values. 
10
11        # question gives u width as height, so u just need depth
12        
13
14        def dfs(node):
15            if not node: # NODEEEEEEE not root for everything here bruh double check to make sure you're referencing the correct node
16                return 0
17            return max(dfs(node.left), dfs(node.right)) + 1
18
19        
20        height = dfs(root) # bc root?
21        # you DONT put +1 for height
22
23        # you DONT put + 1 inside of the width equation
24        # The number of columns n should be equal to 2height+1 - 1.
25        width = 2**(height) - 1
26
27        arr = [[""] * width for i in range(height)]
28        print(width, height)
29        # secondly, you need to traverse the tree once more and keep track of the depth and leftness/rightness values we're at as we traverse. i would think dfs would be easier for this purpose, but it's possible to do bfs as well.
30        def place(node, r, c):
31            if not node:
32                return
33            # place it if we have one
34            # r, c
35            arr[r][c] = str(node.val)
36            if node.left:
37                # why is it -2 instead of -1 as specified in problem
38                place(node.left, r  + 1, c - 2**(height-r-2))
39            if node.right:
40                place(node.right, r + 1, c + 2**(height-r-2))
41        # start with root node
42        place(root, 0, (width-1)//2)
43        return arr
44
45        # is it possible to do in one pass? yes. how would you do that? build 2d thing layer by layer, most likely bfs. but u still need to get width ahead of time otherwise super hard string padding on both sides when u go back up the tree array
46