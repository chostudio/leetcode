# Last updated: 8/6/2026, 7:27:59 AM
1class Solution:
2    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
3        adj = defaultdict(list)
4
5        for a, b in invocations:
6            adj[a].append(b)
7        # print(adj)
8
9        def firstdfs(node, visited):
10            if node in visited:
11                return
12            sus[node] = True
13            visited.add(node) # dont double path infinti it
14            for nei in adj[node]:
15                firstdfs(nei, visited)
16            return
17    
18        # first, mark all the sus nodes. basically do dfs from the point and add to set
19        sus = {}
20        for node in range(n):
21            sus[node] = False
22        s = set()
23        firstdfs(k, s)
24        print(sus)
25        
26
27        # if literally any node from outside the (SINGLE) sus method can reach any node in the sus method, then we just return everything. else we return everything but the sus nodes
28        
29        #global visited set so we dont rerun a path weve already visited
30        def dfs(node):
31            if node in visited:
32                # print(node, "return false")
33                return False # return false not none
34            
35            visited.add(node) # curr path
36            # print(node, "sus[node]", sus[node])
37            if sus[node] == True:
38                return True # we can add all the sus nodes
39
40            result = False
41            for nei in adj[node]:
42                # print(node, "->", nei, result)
43                # you have to put result AFTER the function call otherwise if resutl has something you'll never go deeper intothe chain first which we always want to do
44                result = dfs(nei) or result
45            
46            # bbubble up if at least one node in sus set is touched
47            return result
48
49       
50        visited = set()
51        for node in range(n):
52            if sus[node] == True:
53                continue # only start with nodes outside of sus
54            if dfs(node) == True:
55                # cannot just return list(adj.keys()) BECAUSE tere are unconnected nodes with NO edges # if one reach sus return all
56                ans = []
57                for node in range(n):
58                    ans.append(node)
59                return ans
60        # otherwise return everynode except for sus ones bc not all (theres only one set) so if one set cannot be reached then return everything but it. if there were multiple starting sus nodes, this would be a hard problem, would have to do 1 passthrough of check if component is sus to non sus. then another to actually mark entire component as non sus. then we would do our final check of if there is still sus or not sus and append as we go with an ans set
61        ans = []
62        for i in adj.keys():
63            if sus[i] == False: # note that all them exist in sus but its a hashmap so check the value
64                ans.append(i)
65        return ans