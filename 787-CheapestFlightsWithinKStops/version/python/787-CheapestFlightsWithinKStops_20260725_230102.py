# Last updated: 7/25/2026, 11:01:02 PM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        # is this not just dijstra or bfs approach with counter var?
4        # oh i see if we dijstra then we also have ot make sure that we dont requeue same thing? regardless for both def a visited set. wouldnt make sense to reloop bs no negative weights
5
6        adj = defaultdict(list)
7
8        for f, t, price in flights:
9            adj[f].append((t, price))
10
11        visited = [inf] * (n + 1) # guarenteed that first time we encounter node is cheapest option INSTEAD of just tracking 'hey did we visit this node' we need to track number of stops at a node to determine if we keep going bc smaller num of stops may help reach a further out end point that a cheaper cost but greater amount of stops path may NOT be able to reach the end
12        h = []
13        # order matters in heap sort remember
14        # cheapest cost, lowest k amount, node
15        heapq.heappush(h, (0, 0, src))
16        ans = inf
17        while h:
18            cost, kamount, node = heapq.heappop(h)
19            if visited[node] < kamount:
20                continue
21            # else les than or equal to
22            visited[node] = kamount # tracking num of stops
23            if node == dst:
24                ans = min(ans, cost)
25            # so if k == 1 then we get 1 stop so 0->1->3 is one stop, so it's more like 2 nodes away if 1 stop so it's k +1 really
26            if kamount > k: 
27                # if the path dies here then make sure not to mark the current node as visited, so we dont blcok another potential path
28                # visited.remove(node)
29                continue
30
31            for nei, addcost in adj[node]:
32                if visited[nei] >= kamount:
33                    heapq.heappush(h, (cost + addcost, kamount + 1, nei))
34
35        return ans if ans != inf else -1
36        # # on one hand, dijstra gets you cheapest, but i feel like bfs might be possible ehh dijstra for the win just add another thing for k
37        # # we'll do bfs level counter bc havent used it in a while
38        # q = deque()
39        # # visited = set()
40        # # mb no visited set bc there s a chance that longer route but cheaper route in bfs? so visited cost
41        # cost = [inf] * n
42
43        # q.append([src, 0])
44        # while k > 0 and q:
45        #     levellen = len(q)
46        #     for i in range(levellen):
47        #         node, currprice = q.popleft()
48        #         if cost[node] < currprice:
49        #             continue # why do a more expsneive option thats MORE stops than a prev one. if in same k steps then it'll be fine otherwise 
50
51                
52
53
54        #         if :
55        #             ans = min(ans, )
56
57        #     k -= 1
58
59
60        # return -1 if ans == inf else ans