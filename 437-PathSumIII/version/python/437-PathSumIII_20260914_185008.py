# Last updated: 9/14/2026, 6:50:08 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
9        
10        # keyword is that it doesn't need to start at the root or a leaf. if it didnt then it would just be normal path sum, only count if at leaf node. leaf just means no children
11        total = 0
12        # this path sum seen : how many of it
13        seen = collections.defaultdict(int)
14        seen[0] = 1
15        def dfs(node, pathsum):
16            if not node:
17                return
18            
19            # update path sum
20
21            pathsum += node.val
22            nonlocal total
23            # if pathsum == targetSum: # or node.val == targetSum:
24            #     total += 1
25            # case wehre only one node and it literally just equals targetSum
26            # two sum like check. secondhalf - before correct path
27            # target = a - b e.g. 11 + -3 - (10)
28            # has to be bigger - smaller
29            if pathsum - targetSum in seen and seen[pathsum - targetSum] >= 1: # and node.val != targetSum: # edgecase where path - targetsum + currval is just path IF targetsum == node.val so we only want to count it once
30                total += seen[pathsum - targetSum]
31            
32            # note that we don't do a * b becuase not guarenteed that it's on same path. BACKTRACKING we need to remove from the hashmap if not same set
33        
34            # add before recursing, preorder
35            seen[pathsum] += 1
36            
37            if node.left:
38                dfs(node.left, pathsum)
39            
40            if node.right:
41                dfs(node.right, pathsum)
42            
43            # as we bubble back up the chain and go to the next other paths we need to remove the non accessible paths form the other side that a new side wouldnt be able to access
44            # note that we only remove the current path sum. we wouldnt need to remove (targetSum - pathsum) from seen bc that's a preior pasthsum and well eventually remove it if at every pathsum we just remove itself afterwards
45            if pathsum in seen and seen[pathsum] >= 1:
46                seen[pathsum] -= 1
47            # we don't need to pathsum -= node.val bc the value doesnt get perssited bubble back up anyways
48        
49        dfs(root, 0)
50        return total
51            