# Last updated: 2/17/2026, 9:33:27 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        # pre order
17        def dfs(node):
18            # IF NODE THEN DFS # ELSE SIGNAL END BY POUND SIGN
19            if node:
20                arr.append(str(node.val))
21                dfs(node.left)
22                dfs(node.right)
23            else:
24                arr.append("#")
25        arr = []
26        dfs(root)
27        return " ".join(arr)
28        
29
30    
31    def deserialize(self, data):
32        
33        """Decodes your encoded data to tree.
34        
35        :type data: str
36        :rtype: TreeNode
37        """
38        self.index = -1 # init inside of function
39
40        def dfs():
41            self.index += 1
42            if self.index >= len(arr): return
43            if arr[self.index] == "#":
44                return
45            node = TreeNode(int(arr[self.index]))
46            node.left = dfs()
47            node.right = dfs()
48            return node
49        arr = data.split()
50        return dfs()
51        
52
53# Your Codec object will be instantiated and called as such:
54# ser = Codec()
55# deser = Codec()
56# ans = deser.deserialize(ser.serialize(root))