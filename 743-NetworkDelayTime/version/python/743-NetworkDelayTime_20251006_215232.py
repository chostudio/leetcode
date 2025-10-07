# Last updated: 10/6/2025, 9:52:32 PM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstras
        # min heap visited set bfs adj list
        adj = defaultdict(list)
        for curr, target_node, weight in times:
            adj[curr].append((weight, target_node))
        
        # weight, node
        minheap = [(0, k)]
        visited = set() # needs to have nothing in it at first bc we will pop out from minheap and do it anyways
        totaltime = 0
        while minheap:
            # since we dont care about level no need for another for loop to count length
            weight1, node1 = heapq.heappop(minheap)
            if node1 in visited:
                continue
            visited.add(node1)
            totaltime = weight1
            for weight2, node2 in adj[node1]:
                if node2 not in visited:
                    heapq.heappush(minheap, (weight1 + weight2, node2)) # remember syntax for heap. first argument is name of heap, then second if actual value. must be wrapped in tuple
        # equals NNNNNNN not k bc n is amount of nodes
        return totaltime if len(visited) == n else -1