# Last updated: 9/13/2026, 5:49:31 PM
1class Solution:
2    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
3        
4        # make the adj dag
5        adj = defaultdict(list) # a richer than [b, c, etc.]
6        for rich, less in richer:
7            adj[less].append(rich) # we want to know who is richer and louder
8        print(adj)
9        ans = [inf] * len(quiet) # unvisited at first
10        # given a person, check richer and bubble up quieter person or the current person and save it
11        def dfs(p):
12            if ans[p] != inf:
13                return ans[p] # alr visited and got richer, louder
14            
15            currloudest = p
16
17            for person in adj[p]:
18                maybeloudestperson = dfs(person)
19                # we want smallest quiet
20                if quiet[maybeloudestperson] < quiet[currloudest]:
21                    currloudest = maybeloudestperson
22            
23            ans[p] = currloudest
24            return currloudest
25
26        for person in range(len(quiet)):
27            # if ans[person] == inf:
28            dfs(person)
29        
30        return ans
31
32
33
34