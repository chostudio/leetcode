# Last updated: 6/28/2026, 8:32:24 PM
1class Solution:
2    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
3        adj = defaultdict(list)
4        for u, v, t in edges:
5            adj[u].append((v, t))
6        # the question is, is there a way to do only one algo and get both answers instead of doing two seprate ones
7        # dikstra (min time) but max remaining time is bfs checking every path. idk if two graph algos in same Q will TLE. "hey we found a path with dijstra, now bfs to see if we can get higher power than xyz we found"
8
9        # yes butit requires a 2d array of best power at node with specific time 2d memoization
10        heap = []
11        heapq.heappush(heap, (0, -power, source))
12        besttime = -1
13        bestpower = inf # inf bc no change. cant be 0 bc 0 is valid and we want to iknow if reachable or not
14        # maxpoweratnode[node][power] = min time at there
15        max_power_at_node = [[inf] * (power + 1) for _ in range(n)]
16        max_power_at_node[source][power] = 0 # we have to remember to set the best time for at the source node with starting power as 0 this is our basecase
17
18        while heap:
19            time, currpower, node = heapq.heappop(heap)
20            currpower = -currpower
21
22            # if max_power_at_node[node][currpower] == -inf:
23            #     # would be 0 again or assign greater val
24            #     max_power_at_node[node][currpower] = time # best time
25            if max_power_at_node[node][currpower] < time:
26                continue # break this path we dont need it, the time would be too long
27
28            if node == target:
29                # min heap we have the least time and biggest power bc min heap power negative
30                return [time, currpower]
31            
32            if currpower - cost[node] >= 0:
33                currpower = currpower - cost[node]
34                for nei, addtime in adj[node]:
35                    if max_power_at_node[nei][currpower] > time + addtime:
36                        # basically we wouldnt do it if it would be unoptimal e.g. greater time before we go to the node checking
37                        # if its less than then we also add the time here as we push to let the other nodes know
38                        max_power_at_node[nei][currpower] = time + addtime
39                        heapq.heappush(heap, (time + addtime, -currpower, nei))
40
41        # if nothing worked in the heap,
42        return [-1, -1]
43        # visited = set() # clear it
44        # okay now bfs to get better than targetreachpower
45
46        # we actually still have to care about time oof. needed to reread the question
47        # no visited set bc the 2d array removes possibilties for us. we want least time and visitng the same node with an equal time but greater power is ideal/2d arr has x power and we want lesser time