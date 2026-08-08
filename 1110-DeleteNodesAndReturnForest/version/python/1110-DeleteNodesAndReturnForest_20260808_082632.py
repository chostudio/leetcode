# Last updated: 8/8/2026, 8:26:32 AM
1class Solution:
2    def countHighestScoreNodes(self, parents: List[int]) -> int:
3        # post order dfs where we get the left and the right subtree but ALSO. if the node is a child, then we need the number of nodes the parent is connected to so i think at most bc binary tree it'll be 3 components that you need to calculate multiply. post order will get you the L and R subtrees back to the main node. but then you wouldn't get the top parent yet so we need to traverse this twice. first pass we count all the nodes. second pass we get all the L and R sections then minus the count of them from the total count - 1 (bc we count the node we're at) then multiply the three together. edge case is for the root node (which will always be 0), just make sure to not multiply by 0 bc there is no top section for it
4
5       
6        # def count(node):
7        #     if not node:
8        #         return 0
9        #     return count(node.left) + count(node.right) +1 # +1 stands for this node
10        
11        
12        def dfs(node):
13            #OOB
14            if node < 0 or node >= len(parents):
15                return 0
16            
17            print(node)
18            leftcount = dfs(adj[node][0]) if len(adj[node]) >= 1 else 0
19            rightcount = dfs(adj[node][1]) if len(adj[node]) == 2 else 0
20
21            # edge case where if we are at the top node, dont calc top count
22
23            # if node == -1:
24            #     res = max(leftcount, 1) * max(rightcount, 1)
25            #     maxscore[0] = max(maxscore[0], res)
26            #     score[res] += 1
27            # else: # not top node
28            top = totalnodes - (leftcount + rightcount) -1
29            res = max(top, 1) * max(leftcount, 1) * max(rightcount, 1)
30            print(top, res)
31            maxscore[0] = max(maxscore[0], res)
32            score[res] += 1
33
34            return leftcount + rightcount + 1 # + curr node
35
36        totalnodes = len(parents)
37        # change weird non binary tree array into typical navigatable adj list. yeah i thought the input was weird idk why
38        adj = defaultdict(list)
39
40        #how do you know which side the node goes on. does it technically not matter in this case since the nodes will always be at least on the right parent
41        for index, val in enumerate(parents):
42            # index is the node. val is what parent
43            adj[val].append(index) # we dont know which side per se
44        # print(adj)
45        score = defaultdict(int)
46        # score : num of nodes that have it
47        maxscore = [-1]
48        dfs(0)
49        return score[maxscore[0]]