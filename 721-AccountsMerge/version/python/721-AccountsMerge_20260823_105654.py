# Last updated: 8/23/2026, 10:56:54 AM
1class Solution:
2    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
3        
4        # from a purely dfs stnadpoint, i think this problem is completely doable actually once you know the trick
5
6        # you connect together using adj list/make a graph. then loop through it again to associate with name: emails. then put into final array by sorting hashmap into 2d arr. if you are deadset about using a particular approach to a problem, (only dfs, only dsu) you may be constraining yourself
7
8        # what if only one email at a time, then you're cooked in dfs. you can just assume if there's only one email available, then it's not connected to anything else
9
10        adj = defaultdict(list)
11        # connect emails together, must be bidirectional
12        for i in range(len(accounts)):
13            for j in range(1, len(accounts[i])-1):
14                # first one is email, rest is components
15                # every two basically. 
16                a = accounts[i][j]
17                b = accounts[i][j+1]
18                adj[a].append(b)
19                adj[b].append(a)
20
21        # connect name to email, put into final ans arr
22        ans = []
23        visited = set() # email names/components we've seen alr
24
25        def dfs(email, curr):
26            if email in visited:
27                return
28            
29            curr.append(email)
30            visited.add(email)
31
32            for nei in adj[email]:
33                if nei not in visited:
34                    dfs(nei, curr)
35        
36        # we look a the EMAIL if we've already visited it, then that means that component is good. otherwise, we want to append new component list with 
37        for i in range(len(accounts)):
38            name = accounts[i][0]
39            curr = []
40            # we shouldnt need to call it for every email since should be in same component anyways
41            # for j in range(1, len(accounts[i])):
42            if accounts[i][1] in visited:
43                continue
44            # else that means new component
45            dfs(accounts[i][1], curr)
46            
47            newcurr = [name] + sorted(curr)
48            ans.append(newcurr)
49
50        return ans
51
52
53